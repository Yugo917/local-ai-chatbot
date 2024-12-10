from typing import List, Optional
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

# doc : https://sbert.net/docs/quickstart.html

class Contact(BaseModel):
    name: str
    channel: str
    channelType: str

class FAQItem(BaseModel):
    question: str
    answer: str
    contacts: List[Contact]

class FAQFinder:
    def __init__(self, faqItems: List[FAQItem]):  
        self.faqItems = faqItems;   
        # Load the semantic similarity model
        # This model is used to compute embeddings for questions
        self.sentence_transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

        # Prepare question embeddings for efficient similarity searches
        # These embeddings are precomputed for all FAQ questions
        faq_questions = [item.question for item in faqItems]
        self.faq_questions_embeddings = self.sentence_transformer_model.encode(faq_questions, convert_to_tensor=True)

    # Function to find the most similar question from the FAQ
    def find_similar_faq_item_by_model(self, query: str, threshold: float = 0.75) -> Optional[FAQItem]:
        # Compute embedding for the user's query
        query_embedding = self.sentence_transformer_model.encode(query, convert_to_tensor=True)
        # Compute cosine similarity between query and FAQ embeddings
        scores = util.cos_sim(query_embedding, self.faq_questions_embeddings)
        # Identify the highest similarity score and its index
        best_score, best_index = scores.max(), scores.argmax()
        # Return the matching FAQ entry if the score exceeds the threshold
        if best_score > threshold:
            return self.faqItems[best_index]
        return None
    
    # Function to find the most similar question from the FAQ
    def find_similar_faq_items_by_model(self, query: str, threshold: float = 0.2, max_results: int = 5) -> List[FAQItem]:
        # Compute embedding for the user's query
        query_embedding = self.sentence_transformer_model.encode(query, convert_to_tensor=True)        
        # Compute cosine similarity between query and FAQ embeddings
        scores = util.cos_sim(query_embedding, self.faq_questions_embeddings)        
        # Convert scores tensor to a list of scores with indices
        scores_with_indices = [(i, score) for i, score in enumerate(scores.squeeze().tolist())]        
        # Filter scores above the threshold
        filtered_scores = [(i, score) for i, score in scores_with_indices if score > threshold] 
        if not filtered_scores:
            return []       
        # Sort by score in descending order
        sorted_scores = sorted(filtered_scores, key=lambda x: x[1], reverse=True)        
        # Limit the results to the maximum number specified
        top_scores = sorted_scores[:max_results]        
        # Retrieve the corresponding FAQ items
        matching_faq_items = [self.faqItems[i].dict() for i, _ in top_scores]
        
        return matching_faq_items