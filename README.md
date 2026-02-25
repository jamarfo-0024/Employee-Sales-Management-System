# Employee Sales & Commission Management System (ESCMS)

## Overview

The Employee Sales & Commission Management System (ESCMS) is a secure REST API built using Django and Django REST Framework. The system helps organizations manage employees, track sales, calculate commissions automatically, monitor payments, and view employee performance through dashboard endpoints.

This project was developed as a capstone backend system focusing on real-world business logic, secure API design, and scalable architecture.

---

## Features

- JWT Authentication (Secure API access)
- Role-based permissions (Admin / Employee)
- Employee management system
- Customer assignment to employees
- Secure sales tracking
- Commission calculation
- Payment tracking (salary + commission status)
- Employee dashboard summary endpoint
- Activity tracking and activity feed
- Optimized database queries using `select_related` and `prefetch_related`
- RESTful API structure

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (Development Database)

---

## Project Structure

Employee-Sales-Management-System/
│
├── accounts/
├── employees/
├── customers/
├── sales/
├── payments/
├── activity/
│
├── core/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore


---

## Installation

### Clone Repository
https://github.com/jamarfo-0024/Employee-Sales-Management-System.git


Navigate into project:
cd Employee-Sales-Management-System


---

### Create Virtual Environment
python -m venv venv


Activate virtual environment:

Windows:
venv\Scripts\activate


Mac/Linux:
source venv/bin/activate


---

### Install Dependencies
pip install -r requirements.txt


---

### Run Migrations
python manage.py migrate


---

### Create Superuser
python manage.py createsuperuser


---

### Run Development Server
python manage.py runserver


Open: http://127.0.0.1:8000/


---

## Authentication

This API uses JWT Authentication.

### Login Endpoint
POST /api/token/


Example Body:


{
"username": "your_username",
"password": "your_password"
}


Response:


{
"access": "ACCESS_TOKEN",
"refresh": "REFRESH_TOKEN"
}


---

### Authorization Header

For protected endpoints:


Authorization: Bearer ACCESS_TOKEN


---

## API Endpoints

### Employees

- GET `/api/employees/`
- POST `/api/employees/`

### Employee Dashboard

- GET `/api/dashboard/summary/`

Returns:

- Total sales
- Total revenue
- Total commission
- Unpaid payments

---

### Customers

- GET `/api/customers/`
- POST `/api/customers/`

---

### Sales

- GET `/api/sales/`
- POST `/api/sales/`

Security:

- Employees can only create sales for their assigned customers.
- Admin users have full access.

---

### Payments

- GET `/api/payments/`
- POST `/api/payments/`

Tracks:

- Salary payments
- Commission payments
- Payment status

---

### Activity Feed

Tracks user actions such as:

- Sale creation
- Customer assignment
- Payment updates

---

## Security Features

- JWT authentication
- Role-based access control
- Queryset filtering by logged-in user
- Protected business logic validation
- Secure sales creation checks

---

## Testing API

Recommended tools:

- Thunder Client (VS Code Extension)
- Postman

Steps:

1. Login using `/api/token/`
2. Copy access token
3. Add header:


Authorization: Bearer ACCESS_TOKEN


4. Test endpoints.

---

## Author

Dr Marfo

---

## Capstone Project

This project was developed as part of a backend capstone program focusing on:

- API design
- Secure backend architecture
- Real-world business workflow implementation
