from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.database import get_db
from app.db.models import LeaveRequest
from app.core.auth import require_employee

router = APIRouter(
    prefix="/leave",
    tags=["Leave"]
)


@router.post("/request")
def request_leave(
    start_date: str,
    end_date: str,
    reason: str,
    db: Session = Depends(get_db),
    current_user = Depends(require_employee)
):
    """
    Employee creates leave request
    """

    # Convert string → Python date
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

    leave = LeaveRequest(
        employee_id=current_user.id,
        start_date=start_date_obj,
        end_date=end_date_obj,
        reason=reason,
        status="PENDING"
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return leave