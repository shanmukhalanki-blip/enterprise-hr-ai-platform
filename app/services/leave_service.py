from app.domain.leave.policy import (
    calculate_leave_days,
    validate_leave_balance
)

def apply_leave(db, employee, start_date, end_date, leave_type="CL"):
    holidays = set()  # later fetch from DB

    days = calculate_leave_days(
        start_date=start_date,
        end_date=end_date,
        holidays=holidays
    )

    validate_leave_balance(
        leave_type=leave_type,
        requested_days=days,
        balance=employee.leave_balance
    )

    employee.leave_balance -= days
    db.commit()

    return days

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
