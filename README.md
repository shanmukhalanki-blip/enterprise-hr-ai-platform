# 🏢 Internal HR Chatbot (AI-Powered)

An internal HR chatbot system that allows employees to:
- Check leave balance
- Apply for leave via chat  
And allows managers to:
- View pending leave requests
- Approve leave requests via dashboard

Built as a **full-stack application** with role-based access control.

---

## 🚀 Features

### 👩‍💼 Employee
- Login using employee ID
- Chat with HR bot
- View leave balance
- Apply for leave using natural language
- Get updates after manager approval

### 🧑‍💼 Manager
- Login using manager ID
- View all pending leave requests
- Approve leave requests
- Leave balance auto-updated

---

## 🧱 Tech Stack

### Backend
- **Python**
- **FastAPI**
- **JWT Authentication**
- **SQLAlchemy**
- **SQLite**
- Role-based access control (Employee / Manager)

### Frontend
- **React (Vite)**
- **Fetch API**
- Conditional UI rendering by role

---

## 🔐 Authentication

- JWT-based authentication
- Tokens stored in browser localStorage
- Backend enforces role permissions
- Frontend adapts UI based on role

---

## 📂 Project Structure

