from sqlalchemy.orm import Session
from app.db.models import Employee, LeaveRequest


# ==============================
# Employee Queries
# ==============================

def get_employee_by_emp_id(db: Session, employee_id: str):
    return (
        db.query(Employee)
        .filter(Employee.employee_id == employee_id)
        .first()
    )


# ==============================
# Manager Queries
# ==============================

def get_pending_leave_requests(db: Session):
    return (
        db.query(LeaveRequest)
        .filter(LeaveRequest.status == "PENDING")
        .all()
    )


def approve_leave_request(db: Session, leave_id: int):
    leave = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.id == leave_id)
        .first()
    )

    if not leave:
        return None

    leave.status = "APPROVED"
    db.commit()
    db.refresh(leave)

    return leave
