1. Install dependencies
pip install django djangorestframework djangorestframework-simplejwt
2. Apply migrations
python manage.py makemigrations
python manage.py migrate
3. Run the server
python manage.py runserver

Authentication

Register a new user

POST /api/register/

Login and receive JWT token

POST /api/login/

Products

Get all products

GET /api/products/

Create a product (Admin only)

POST /api/products/

Orders

Create a new order

POST /api/orders/

View orders

Admin: view all orders
Customer: view their own orders
GET /api/orders/list/

Update an order (Admin only)

PUT /api/orders/{id}/
