import httpx
from pydantic import BaseModel, Field
from typing import List, Optional


class Message(BaseModel):
    role: str
    content: str


class Choice(BaseModel):
    index: int
    message: Message
    logprobs: Optional[dict] = None
    finish_reason: str


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage
    system_fingerprint: Optional[str] = None

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: int = -1
    stream: bool = False
    n: Optional[int] = 1 

class ChatAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_chat_completion(self, payload: ChatCompletionRequest) -> ChatCompletionResponse:
        client = httpx.AsyncClient()
        response = await client.post(
            f"{self.base_url}/v1/chat/completions",
            json=payload.dict(),
            timeout=10.0,
        )
        response.raise_for_status()  # Gestion des erreurs HTTP
        response = ChatCompletionResponse(**response.json())
        return response