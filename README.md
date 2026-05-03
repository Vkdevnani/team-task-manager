# 🚀 Team Task Manager (Full-Stack)

A production-ready full-stack web application for managing team projects and tasks with **role-based access control (Admin/Member)**. Built using FastAPI, React, and PostgreSQL, and deployed on Railway.

---

## 🔗 Live Demo

* Backend API: `https://your-backend-url.up.railway.app`
* API Docs (Swagger): `https://your-backend-url.up.railway.app/docs`

---

## 📦 Features

### 🔐 Authentication

* User Signup & Login
* JWT-based authentication
* Secure password hashing (bcrypt)

### 👥 Role-Based Access Control

* **Admin**

  * Create projects
  * Assign tasks
* **Member**

  * View assigned tasks
  * Update task status

### 📁 Project Management

* Create and manage projects
* Add team members to projects

### ✅ Task Management

* Create tasks
* Assign tasks to users
* Update task status (`TODO`, `IN_PROGRESS`, `DONE`)
* Due date tracking

### 📊 Dashboard

* View assigned tasks
* Track progress by status
* Identify overdue tasks

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* PostgreSQL (Railway)
* SQLAlchemy
* JWT (python-jose)
* Passlib + Bcrypt

### Frontend

* React (Vite)
* Tailwind CSS (optional)

### Deployment

* Railway (Backend + Database)
* GitHub (Version Control)

---

## 🧠 Architecture

* RESTful API design
* Modular backend structure:

  * `models` → Database schema
  * `schemas` → Validation (Pydantic)
  * `api` → Routes
  * `core` → Config & security
  * `db` → Database connection
  * `utils` → Helpers

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/team-task-manager.git
cd team-task-manager/backend
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

```env
DATABASE_URL=your_postgres_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Run Backend

```bash
uvicorn main:app --reload
```

### 5. Access API

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

1. Signup → Create user
2. Login → Get JWT token
3. Use token in Swagger:

```
Authorize → Bearer <token>
```

---

## 📁 Folder Structure

```
team-task-manager/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
├── docs/
└── README.md
```

---

## 📌 API Endpoints (Current)

### Auth

* `POST /auth/signup`
* `POST /auth/login`
* `GET /auth/me`

---

## 🎯 Future Enhancements

* Project APIs (Admin only)
* Task assignment APIs
* Kanban board UI
* Email notifications
* Activity logs

---

## 📹 Demo Video

*(Add your video link here)*

---

## 👨‍💻 Author

Vinay Kumar Devnani
Computer Science Engineering Student

---

## 📄 License

This project is for academic and evaluation purposes.
