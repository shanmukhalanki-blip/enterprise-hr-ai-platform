from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import require_manager
from app.db.database import SessionLocal
from app.db.crud import get_pending_leave_requests, approve_leave_request

router = APIRouter(
    prefix="/manager",
    tags=["Manager"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/leaves")
def get_pending_leaves(
    db: Session = Depends(get_db),
    user=Depends(require_manager)
):
    return get_pending_leave_requests(db)


@router.post("/leaves/{leave_id}/approve")
def approve_leave(
    leave_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_manager)
):
    approve_leave_request(db, leave_id)
    return {"status": "Leave approved"}
