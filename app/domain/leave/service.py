from datetime import date
from sqlalchemy.orm import Session

from app.db.models import LeaveRequest, Employee


def apply_leave(
    db: Session,
    employee: Employee,
    start_date: date,
    end_date: date,
):
    # Calculate leave days (inclusive)
    days = (end_date - start_date).days + 1

    if days <= 0:
        return None, "Invalid leave dates"

    if employee.leave_balance < days:
        return None, "Insufficient leave balance."

    leave_request = LeaveRequest(
        employee_id=employee.employee_id,
        start_date=start_date,
        end_date=end_date,
        days=days,
        status="PENDING",
    )

    db.add(leave_request)
    db.commit()

    return days, "PENDING"
