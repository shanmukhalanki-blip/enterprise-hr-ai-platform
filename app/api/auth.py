from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.database import get_db
from app.db.models import Employee
from app.core.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login endpoint using OAuth2 form
    """

    email = form_data.username
    password = form_data.password

    user = db.query(Employee).filter(Employee.email == email).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")

    access_token = create_access_token(user)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }