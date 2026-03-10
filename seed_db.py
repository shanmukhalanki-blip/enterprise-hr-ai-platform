from app.db.database import engine, SessionLocal
from app.db.models import Base, Employee

# 🔥 Force table creation
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear old data (optional safety)
db.query(Employee).delete()
db.commit()

# Seed employee
employee = Employee(
    employee_id="EMP001",
    name="Shanmukh",
    department="Engineering",
    manager="Manager A",
    leave_balance=12
)

db.add(employee)
db.commit()

db.close()

print("Database seeded successfully.")