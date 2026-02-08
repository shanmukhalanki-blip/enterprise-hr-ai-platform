from pydantic import BaseModel

class ChatRequest(BaseModel):
    employee_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
