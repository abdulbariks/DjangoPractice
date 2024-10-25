Create Virtual Environment
py -m venv env
env\Scripts\activate.bat run by cmd for activate the environment

Install Django
py -m pip install Django
py --version check python version
django-admin --version Check Django Version

Create Django Project
django-admin startproject DjangoPractice
py manage.py runserver Run the Django Project

Create Django App
py manage.py startapp machineLearning

Django Views
Django URLs

Django Templates:
Create a templates folder inside the templates folder, and create a HTML file named deepLearning.html & machineLearning.html.

Change Settings:
settings.py file in the DjangoPractice folder update TEMPLATE_DIR & INSTALLED_APPS

Create Static files (CSS, JavaScript, Images)

Display Data: Prepare Template, Add Link, Add Main Index Page, 404 page not found

Bootstrap added HTML file

Install Bootstrap 5 in Django project: pip install django-bootstrap-v5

Template inheritance dynamic url create

Django Models: Create Table (Model), Insert Data, Update Data, Delete Data, Update Model

Django Admin: Create User, Include DeepLearning, Set Fields to Display, Update DeepLearning, Add Members, Delete DeepLearning

Django form:
