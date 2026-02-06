# 1. Create project folder
mkdir PEPCLASS
cd PEPCLASS 
# python3 -m venv .venv create the venv
 For some Windows installations, you might need to use `python` instead of `python3`
# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install Django
pip install django

# 4. Create Django project
django-admin startproject myproject
cd myproject

# 5. Create polls app
python manage.py startapp polls

# 6. Make migrations and migrate database
python manage.py makemigrations
python manage.py migrate

# 7. Create superuser for admin panel
python manage.py createsuperuser

# 8. Run development server
python manage.py runserver

