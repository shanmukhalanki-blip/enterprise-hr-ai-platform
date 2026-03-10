from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)

    password = Column(String, nullable=False)

    role = Column(String, default="employee")

    created_at = Column(DateTime, default=datetime.utcnow)

    leaves = relationship("LeaveRequest", back_populates="employee")
    tokens = relationship("RefreshToken", back_populates="employee")


class LeaveRequest(Base):
    __tablename__ = "leave_requests"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    reason = Column(String, nullable=False)

    status = Column(String, default="PENDING")

    created_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="leaves")


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"))

    token = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="tokens")