# Create FastAPI app instance
import json
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from faq_finder import FAQFinder, FAQItem
import requests

# Load FAQ datas
with open('faq.json', 'r') as f:
    raw_data = json.load(f)  
    faq_data2 = [FAQItem(**item) for item in raw_data]  


app = FastAPI(
    title="FAQ API",
    description="An API to answer known questions.",
    version="1.0.0"
)

faq_finder = FAQFinder(faq_data2)

# Endpoint to process FAQ queries
@app.post("/faq/similar", summary="Get the best similar FAQ item", tags=["FAQ"])
async def faq(question: str) -> Optional[FAQItem]:
    similar_faq_item = faq_finder.find_similar_faq_item_by_model(question)
    return similar_faq_item

@app.post("/faq/similars", summary="Get similar FAQ items ", tags=["FAQ"])
async def faq(question: str) -> List[FAQItem]:
    similar_faq_item = faq_finder.find_similar_faq_items_by_model(question)
    return similar_faq_item
    

# Automatic Swagger documentation is available at /docs
# OpenAPI schema can be accessed at /openapi.json