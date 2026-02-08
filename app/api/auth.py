from fastapi import APIRouter, HTTPException
from app.core.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

USERS = {
    "emp001": {"role": "employee"},
    "mgr001": {"role": "manager"},
}

@router.post("/login")
def login(username: str):
    user = USERS.get(username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": username,
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
