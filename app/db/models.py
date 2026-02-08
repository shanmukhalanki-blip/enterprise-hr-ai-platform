from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)
    name = Column(String)
    department = Column(String)
    manager = Column(String)
    leave_balance = Column(Integer)


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    days = Column(Integer)
    status = Column(String, default="PENDING")  # PENDING / APPROVED / REJECTED
