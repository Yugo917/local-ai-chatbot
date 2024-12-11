# Create FastAPI app instance
import json
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chat_api_client import ChatAPIClient, ChatCompletionRequest, Message
from faq_finder import FAQFinder, FAQItem
import requests

from prompter import Prompter

# Load FAQ datas
with open('dataset/faq.json', 'r') as f:
    faq_dataset_raw_json = json.load(f)  
    faq_dataset = [FAQItem(**item) for item in faq_dataset_raw_json]  

with open('dataset/faq.json', 'r', encoding='utf-8') as f2:
    faq_dataset_raw_txt = f2.read()


with open('dataset/support_preprompt_v4.md', 'r', encoding='utf-8') as f3:
    support_preprompt_raw_txt = f3.read()

app = FastAPI(
    title="FAQ API",
    description="An API to answer known questions.",
    version="1.0.0"
)

origins = [
    "null", 
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://myfrontendapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser uniquement les origines spécifiées
    allow_credentials=True,  # Autoriser les cookies
    allow_methods=["*"],  # Autoriser toutes les méthodes : GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Autoriser tous les headers
)

faq_finder = FAQFinder(faq_dataset)

chat_api_client = ChatAPIClient("http://127.0.0.1:1234")

prompter = Prompter()



# Endpoint to process FAQ queries
@app.post("/faq/similar", summary="Get the best similar FAQ item", tags=["FAQ"])
async def faq_similar(question: str) -> Optional[FAQItem]:
    similar_faq_item = faq_finder.find_similar_faq_item_by_model(question)
    return similar_faq_item

@app.post("/faq/similars", summary="Get similar FAQ items ", tags=["FAQ"])
async def faq_similars(question: str) -> List[FAQItem]:
    similar_faq_item = faq_finder.find_similar_faq_items_by_model(question)
    return similar_faq_item

@app.post("/llm/chat", summary="Chat with the generative ai", tags=["AI"])
async def llm_chat(prompt: str) -> str:
    payload = ChatCompletionRequest(
        model="llama-3.2-3b-instruct",
        messages=[Message(role="user", content=prompt)],
        temperature=0.7,
        max_tokens=-1,
        stream=False
    )
    chat_result = await chat_api_client.get_chat_completion(payload)
    str_response = chat_result.choices[0].message.content
    return str_response

@app.post("/faq-chatbot/with-full-dataset-preprompt/chat", summary="Chat with your FAQ ChatBot", tags=["AI"])
async def faq_chatbot_chat(prompt: str) -> str:
    patterns = [
        ("MY_FAQ_JSON_DATASET", faq_dataset_raw_txt),
        ("MY_QUESTION", prompt),
    ]
    enhanced_prompt = prompter.replace_patterns(support_preprompt_raw_txt, patterns)
    result = await llm_chat(enhanced_prompt)
    return result

@app.post("/faq-chatbot/with-optimized-dataset-preprompt/chat", summary="Chat with your optimized FAQ ChatBot", tags=["AI"])
async def faq_optimized_chatbot_chat(prompt: str ) -> str:
    faq_similars_dataset = await faq_similars(prompt)
    faq_similars_dataset_json = json.dumps(faq_similars_dataset, indent=4)
    patterns = [
        ("MY_FAQ_JSON_DATASET", faq_similars_dataset_json),
        ("MY_QUESTION", prompt),
    ]
    enhanced_prompt = prompter.replace_patterns(support_preprompt_raw_txt, patterns)
    result = await llm_chat(enhanced_prompt)
    return result

@app.post("/faq-chatbot/faq-finder/chat", summary="Chat with your optimized FAQ ChatBot", tags=["AI"])
async def faq_finder_chat(prompt: str ) -> str:
    similar_faq_item = faq_finder.find_similar_faq_items_by_model(prompt,0.2,1)
    faq_similars_dataset_json = json.dumps(similar_faq_item, indent=4)
    return faq_similars_dataset_json


# Automatic Swagger documentation is available at /docs
# OpenAPI schema can be accessed at /openapi.json