# order_management
# order_management
# Order Management API

This project implements a simple Order Management REST API using Django REST Framework.

Features
- JWT Authentication
- Role-based access control
- Nested order creation
- Admin and Customer roles
- Order total calculation

Setup Instructions

1. Clone repository
2. Install dependencies

pip install django djangorestframework djangorestframework-simplejwt

3. Run migrations

python manage.py migrate

4. Run server

python manage.py runserver

API Endpoints

Register
POST /api/register/

Login
POST /api/login/

Products
GET /api/products/
POST /api/products/

Orders
GET /api/orders/
POST /api/orders/create/

Update Order
PUT /api/orders/{id}/

Authentication

JWT Token must be added in header

Authorization: Bearer <token>
