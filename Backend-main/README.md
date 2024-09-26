# Django Backend Project

This project is a Django-based backend application. Below are the steps to set up the project, including creating a virtual environment, installing dependencies, and running the application. First, navigate to your preferred directory and create a folder for the project. For example, go to the Documents folder using `cd %USERPROFILE%\Documents`, and then create a folder named Backend with `mkdir Backend`. Enter the Backend folder with `cd Backend`. Now, create a virtual environment inside this folder by running `python -m venv venv`. Once the virtual environment is created, activate it. If you're on Windows, run `venv\Scripts\activate`, or if you're on macOS/Linux, use `source venv/bin/activate`.

With the virtual environment activated, install Django by running `pip install django`. Once Django is installed, create a new Django project inside the Backend folder by running `django-admin startproject Backend .`. Make sure to include the dot (`.`) at the end to create the project in the current folder. Now, create a new Django app inside the project by running `python manage.py startapp ProyBackEndApp`. 

Once the app is created, you need to register it in the project’s settings. Open the `settings.py` file located in the project folder (e.g., `Backend/settings.py`) and add `ProyBackEndApp` to the `INSTALLED_APPS` list. Your `INSTALLED_APPS` should look like this:

`INSTALLED_APPS = [ 'django.contrib.admin', 'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions', 'django.contrib.messages', 'django.contrib.staticfiles', 'ProyBackEndApp', ]`

After registering the app, define your models in `ProyBackEndApp/models.py`. For example, here is a simple model for a blog post:

`from django.db import models class Post(models.Model): title = models.CharField(max_length=200) content = models.TextField() created_at = models.DateTimeField(auto_now_add=True) def __str__(self): return self.title`

Once your model is defined, register it in the Django admin panel by going to `ProyBackEndApp/admin.py` and adding the following lines:

`from django.contrib import admin from .models import Post admin.site.register(Post)`

Next, you need to apply database migrations to create the corresponding database tables for your models. First, run `python manage.py makemigrations` to prepare the migrations, and then apply them by running `python manage.py migrate`. After running migrations, you’ll want to create a superuser to access the Django admin panel. To create a superuser, run `python manage.py createsuperuser` and follow the prompts to provide a username, email, and password.

Now that everything is set up, you can start the Django development server by running `python manage.py runserver`. The server will be accessible at `http://127.0.0.1:8000/`. To access the Django admin interface, go to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created. You can now manage your models and data through the admin interface.

This completes the basic setup for your Django project, including creating a virtual environment, setting up a Django project and app, defining models, applying migrations, and creating a superuser to manage the admin panel.
