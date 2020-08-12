## Basic Django Backend
Basic RESTful API using Django Rest Framework

### Tasks list
- [x] Users api CRUD endpoints
- [x] DRF JWT Authentication
- [x] Add docker configurations

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api/token` | Request jwt token
POST | `/api/token/verify` | Request jwt token
POST | `/api/token/refresh` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/user` | List users
GET | `/api/user/create` | Creates a user
GET | `/api/user/profile/{pk}` | Retrieve a user
PUT | `/api/user/update/{pk}` | Edit a user
DELETE | `/api/user/destroy/{pk}` | Delete a user


### Installation 
If you wish to run your own build, you two options
 1. Use Docker compose.
    
    `$ git clone https://github.com/p8ul/django-rest-framework-boilerplate`
    
    `$ cd django-rest-framework-boilerplate`    
    `$ docker-compose up`
 
 2. Without docker
 
First ensure you have python globally installed in your computer. If not, you can get python [here](python.org).

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    `$ pip install virtualenv`
Then, Git clone this repo to your PC

    `$ git clone https://github.com/p8ul/django-rest-framework-boilerplate`
    `$ cd django-rest-framework-boilerplate`
Create a virtual environment

    `$ virtualenv .venv`
    `$ source .venv/bin/activate`
Install dependancies

    `$ pip install -r requirements.txt`
Make migrations & migrate
    `$ python manage.py makemigrations`
    `$ python manage.py migrate`

Create Super user

    `$ python manage.py createsuperuser --email admin@admin.admin --username admin`

    When prompted password, enter 'adminadmin' for suitability with test case

### Launching the app
    $ python manage.py runserver

### Run Tests
    Test is currently available using Postman Collection Runner. Please head to https://documenter.getpostman.com/view/2425239/T1LMhmag for complete list of available endpoints for testing.



