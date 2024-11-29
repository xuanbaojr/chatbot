from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_controller import DefaultLLM

app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'], 
    allow_headers=['*'], 
)

class Conversation(BaseModel):
    system: str | None = None
    human: str

@app.get("/")
async def hellow_world():
    return {"text":"chatbot_v1"}

@app.post("/default_llm/single_forward/{user_id}")
async def single_forward(user_id: int, conversation: Conversation):
    default_llm = DefaultLLM()
    res = default_llm.single_forward(conversation.human)
    return {"answer": res}
