from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.auth import decode_access_token, security
from app.schemas import ChatRequest, ChatResponse
from app.db.database import SessionLocal
from app.db.crud import get_employee_by_emp_id, apply_leave
from app.core.date_parser import extract_dates

# ✅ Router MUST be defined before usage
router = APIRouter()


# 🔐 Auth dependency (employee or manager)
def require_employee(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    payload = decode_access_token(token)

    if not payload or payload.get("role") not in ["employee", "manager"]:
        raise HTTPException(status_code=403, detail="Employee access required")

    return payload


# 🗄️ DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 💬 Chat endpoint
@router.post("/", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user=Depends(require_employee)
):
    # 1️⃣ Get employee identity from JWT
    emp_id = user["sub"].upper()

    # 2️⃣ Load employee from DB
    employee = get_employee_by_emp_id(db, emp_id)
    if not employee:
        return ChatResponse(reply="Employee not found.")

    # 3️⃣ Process message
    message = request.message.lower()

    if "apply leave" in message:
        start_date, end_date = extract_dates(message)

        if not start_date or not end_date:
            reply = "Please use format: Apply leave from YYYY-MM-DD to YYYY-MM-DD"
        else:
            days, status = apply_leave(db, employee, start_date, end_date)
            if not days:
                reply = status
            else:
                reply = (
                    f"Your leave request from {start_date} to {end_date} "
                    f"for {days} days has been submitted for approval."
                )

    elif "leave" in message:
        reply = f"You have {employee.leave_balance} leave days remaining."

    elif "manager" in message:
        reply = f"Your manager is {employee.manager}."

    elif "department" in message:
        reply = f"You work in the {employee.department} department."

    else:
        reply = (
            "I can help with leave balance, leave application, "
            "manager info, or department details."
        )

    return ChatResponse(reply=reply)
