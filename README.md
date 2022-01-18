## Table of contents
* [General info](#Todo-app)
* [Images](#images)
* [How to Install and Run the Project](#How-to-Install-and-Run-the-Project)
* [Technologies](#technologies)

## General info


# Todo-app
This is my first project, thanks to which I learned CRUD and fullstack approach.
This application is developed using Django Rest Framework and Vue.js.
User can create a lists of todo list, edit and delete them.

## images
![Photo one](https://github.com/Dariusz95/Todo-app/blob/main/todos_frontend/public/Zdj1.jpg?raw=true)
![Photo two](https://github.com/Dariusz95/Todo-app/blob/main/todos_frontend/public/Zdj2.jpg?raw=true)
![Photo three](https://github.com/Dariusz95/Todo-app/blob/main/todos_frontend/public/Zdj3.jpg?raw=true)

## How to Install and Run the Project
### Backend
```
$ clone this repository - git clone https://github.com/Dariusz95/Todo-app
$ cd Todo-app\todos_backend
$ pip install virtualenv
$ virtualenv env
```
#### Activate the virtual environment
##### Mac OS / Linux
```
$ source env/bin/activate
```
##### Windows
```
$ env\Scripts\activate
```
```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
### Frontend
```
$ cd Todo-app\todos_frontend
$ npm install
$ npm run serve
```

# technologies
* Vue.js 2.6.11
* Django Rest Framework 3.12
