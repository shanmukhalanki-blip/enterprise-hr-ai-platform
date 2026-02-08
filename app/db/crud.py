from sqlalchemy.orm import Session
from app.db.models import Employee

def get_employee_by_emp_id(db: Session, employee_id: str):
    return db.query(Employee).filter(Employee.employee_id == employee_id).first()
from datetime import date

from app.db.models import LeaveRequest

def apply_leave(db, employee, start_date, end_date):
    days = (end_date - start_date).days + 1

    if employee.leave_balance < days:
        return None, "Insufficient leave balance."

    leave_request = LeaveRequest(
        employee_id=employee.employee_id,
        start_date=start_date,
        end_date=end_date,
        days=days,
        status="PENDING"
    )

    db.add(leave_request)
    db.commit()

    return days, "Leave request submitted for approval."
def approve_leave(db, leave_id):
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if not leave:
        return "Leave request not found."

    employee = db.query(Employee).filter(Employee.employee_id == leave.employee_id).first()

    if employee.leave_balance < leave.days:
        return "Insufficient leave balance at approval time."

    employee.leave_balance -= leave.days
    leave.status = "APPROVED"
    db.commit()

    return "Leave approved."

def reject_leave(db, leave_id):
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()
    if not leave:
        return "Leave request not found."

    leave.status = "REJECTED"
    db.commit()

    return "Leave rejected."

from app.db.models import LeaveRequest


def get_pending_leave_requests(db):
    return (
        db.query(LeaveRequest)
        .filter(LeaveRequest.status == "PENDING")
        .all()
    )


def approve_leave_request(db, leave_id: int):
    leave = (
        db.query(LeaveRequest)
        .filter(LeaveRequest.id == leave_id)
        .first()
    )

    if not leave:
        return None

    leave.status = "APPROVED"
    db.commit()
    return leave
