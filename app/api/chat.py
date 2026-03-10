from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.db.crud import get_employee_by_emp_id
from app.core.auth import require_employee

router = APIRouter()


# -------------------------
# Request / Response Models
# -------------------------

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# -------------------------
# Chat Endpoint
# -------------------------

@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user=Depends(require_employee)
):
    # Extract employee ID from JWT
    employee_id = user["sub"]

    # Fetch employee from DB
    employee = get_employee_by_emp_id(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    message = request.message.lower()

    # Simple leave query logic
    if "leave" in message:
        return ChatResponse(
            reply=f"You have {employee.leave_balance} leave days remaining."
        )

    return ChatResponse(
        reply="I can help you with leave information."
    )
