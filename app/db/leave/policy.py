from datetime import date, timedelta

WEEKENDS = {5, 6}  # Saturday, Sunday

LEAVE_TYPES = {
    "CL": {"annual": 12, "carry_forward": False},
    "SL": {"annual": 12, "carry_forward": False},
    "EL": {"annual": 18, "carry_forward": True, "max_carry": 30},
}


def is_working_day(day: date, holidays: set[date]) -> bool:
    return day.weekday() not in WEEKENDS and day not in holidays


def calculate_leave_days(
    start_date: date,
    end_date: date,
    holidays: set[date]
) -> int:
    days = 0
    current = start_date

    while current <= end_date:
        if is_working_day(current, holidays):
            days += 1
        current += timedelta(days=1)

    return days


def validate_leave_balance(
    leave_type: str,
    requested_days: int,
    balance: int
) -> None:
    if requested_days <= 0:
        raise ValueError("Invalid leave duration")

    if requested_days > balance:
        raise ValueError("Insufficient leave balance")

    if leave_type not in LEAVE_TYPES:
        raise ValueError("Invalid leave type")
