from datetime import date
from sqlalchemy.orm import Session

from app.db.models import LeaveRequest, Employee


def apply_leave(
    db: Session,
    employee: Employee,
    start_date: date,
    end_date: date
):
    days = (end_date - start_date).days + 1

    if employee.leave_balance < days:
        return None, "Insufficient leave balance."

    leave = LeaveRequest(
        employee_id=employee.employee_id,
        start_date=start_date,
        end_date=end_date,
        days=days,
        status="PENDING"
    )

    employee.leave_balance -= days

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return days, "Leave applied"
