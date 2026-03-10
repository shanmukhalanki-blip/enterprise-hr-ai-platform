from app.db.database import engine, SessionLocal
from app.db.models import Base, Employee

# create tables first
Base.metadata.create_all(bind=engine)

db = SessionLocal()

employee = Employee(
    name="Test Employee",
    email="employee@test.com",
    password="123456",
    role="employee"
)

manager = Employee(
    name="Manager User",
    email="manager@test.com",
    password="123456",
    role="manager"
)

db.add(employee)
db.add(manager)

db.commit()

print("Test users created successfully")