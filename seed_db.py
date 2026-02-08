from app.db.database import SessionLocal
from app.db.models import Employee

db = SessionLocal()

employees = [
    Employee(
        employee_id="EMP001",
        name="Ravi Kumar",
        department="Engineering",
        manager="Suresh Rao",
        leave_balance=12
    ),
    Employee(
        employee_id="EMP002",
        name="Anita Sharma",
        department="HR",
        manager="Meena Iyer",
        leave_balance=18
    )
]

for emp in employees:
    exists = db.query(Employee).filter(Employee.employee_id == emp.employee_id).first()
    if not exists:
        db.add(emp)

db.commit()
db.close()

print("✅ Database seeded successfully")
