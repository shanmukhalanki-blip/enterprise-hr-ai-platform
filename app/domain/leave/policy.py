class LeavePolicy:
    @staticmethod
    def can_apply(employee, days: int):
        if days <= 0:
            return False, "Invalid leave duration"

        if employee.leave_balance < days:
            return False, "Insufficient leave balance"

        return True, None
