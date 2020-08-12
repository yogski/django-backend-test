## Basic Django Backend
Basic RESTful API using Django Rest Framework

### Tasks list
- [x] Users api CRUD endpoints
- [x] Orders api CRUD endpoints
- [x] DRF JWT Authentication
- [x] Add docker configurations

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api/token` | Request jwt token
POST | `/api/token/verify` | Verify jwt token
POST | `/api/token/refresh` | Refresh jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/users/` | List all users
POST | `/users/` | Create a user
GET | `/users/{pk}` | Retrieve a user
PUT | `/users/{pk}` | Edit a user
DELETE | `/users/{pk}` | Delete a user
GET | `/orders/` | List all orders
POST | `/orders/` | Create a order
GET | `/orders/{pk}` | Retrieve a order
PUT | `/orders/{pk}` | Edit a order
DELETE | `/orders/{pk}` | Delete a order


### Installation 
There are 2 options available: using Docker or manual.
 1. Use Docker compose.
    
    $ git clone https://github.com/yogski/django-backend-test.git
    
    $ cd django-backend-test    
    $ docker-compose up
 
 2. Manual (without Docker)
 
Ensure Python 3.5 or later is installed. Check using

    $ python --version
After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/yogski/django-backend-test.git
    $ cd django-backend-test
Create a virtual environment

    $ virtualenv .venv
    $ source .venv/bin/activate
Install dependancies

    $ pip install -r requirements.txt
Make migrations & migrate
    $ python manage.py makemigrations
    $ python manage.py migrate

Create Super user

    $ python manage.py createsuperuser --email admin@admin.admin --username admin

    When prompted password, enter 'adminadmin' for suitability with test case

### Launching the app
    $ python manage.py runserver

### Run Tests
    Test is currently available using Postman Collection Runner. Please head to https://documenter.getpostman.com/view/2425239/T1LMhmag for complete list of available endpoints for testing.

