# 🚀 Employee Management System

An Employee Management System developed using **Python, FastAPI, SQLite, HTML, and CSS** to manage employee records efficiently. This application allows users to add, view, update, delete, and filter employee information through a user-friendly web interface.

## 📌 Project Overview

The Employee Management System is a web-based application designed to simplify employee record management. It provides an interface to manage employee details, view individual employee profiles, and organize employee information based on departments.

## ✨ Key Features

- **Add Employees:** Register new employees with details such as name, gender, image, salary, department, experience, and attendance.
- **View Employees:** Display employee records using profile cards.
- **Employee Details:** View detailed information about individual employees.
- **Update Employees:** Modify existing employee information.
- **Delete Employees:** Remove employee records from the database.
- **Department Filtering:** Filter employees based on their departments.
- **Dynamic HTML Rendering:** Display backend data dynamically using Jinja2 templates.
- **Database Management:** Store and manage employee information using SQLite.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML | Structure of web pages |
| CSS | Styling and user interface |
| Python | Backend programming |
| FastAPI | Backend framework and routing |
| SQLite | Database management |
| Jinja2 | Dynamic HTML templating |
| Uvicorn | ASGI server |
| Pydantic | Data validation |
| RedirectResponse | Handling page redirections |

## 📂 Project Structure

```text
EMPLOYEE_MANAGEMENT_SYSTEM/
│
├── main.py
├── employees.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── add_employee.html
│   ├── update_employee.html
│   └── employee_details.html
│
├── static/
│   ├── css/
│   └── images/
│
└── README.md
```

*Note: Adjust the template and static filenames according to your actual project structure.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd EMPLOYEE_MANAGEMENT_SYSTEM
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## 💡 What I Learned

Through this project, I gained practical experience in:

- Python backend development.
- Building web applications using FastAPI.
- Implementing CRUD operations.
- Connecting Python applications with SQLite databases.
- Rendering dynamic HTML pages using Jinja2.
- Handling HTTP requests and responses.
- Running applications using Uvicorn.
- Integrating frontend and backend components.

## 🚀 Future Enhancements

- Implement employee login and authentication.
- Add search functionality.
- Generate employee reports.
- Improve employee data analytics.
- Deploy the application to a cloud hosting platform.

## 👨‍💻 Author

**Ajay Kumar**

GitHub: [Your GitHub Profile](https://github.com/)

---

⭐ If you find this project useful, consider giving it a star!
