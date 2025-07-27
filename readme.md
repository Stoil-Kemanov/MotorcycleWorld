# Motorcycle World - Django Web Application

## Setup Instructions
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`

## Project Description
Django web application for motorcycle enthusiasts featuring user profiles, motorcycle catalog, and gear recommendations.

## Current Features
- Email-based user registration and authentication
- User profiles with physical characteristics and riding preferences
- Personal motorcycle inventory management
- Bootstrap-responsive UI design
- Django admin interface for content management
- 