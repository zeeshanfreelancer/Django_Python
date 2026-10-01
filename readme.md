python -m venv venv
venv\Scripts\Activate.ps1
pip install requests
pip list
pip freeze > requirements.txt
pip install -r requirements.txt
deactivate

python --version

1: Create a virtual environment
python -m venv venv

2: Activate it:
venv\Scripts\Activate.ps1

3: Install Django
pip install django
django-admin --version

4: Create your Django project
django-admin startproject config .

5: Start the Django server
python manage.py runserver

6: Create your first Django app
Create a users app:
python manage.py startapp users

7: Register the app
config/settings.py
Find:

INSTALLED_APPS = 

Add:

"users",