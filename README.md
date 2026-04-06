# Django Blog System

A simple blog application built using Django.

## Features
- Create, edit, delete blog posts
- Admin panel
- Slug-based URLs
- Published/Draft system
- Author system

## Tech Stack
- Django
- SQLite
- HTML (Templates)

## Run Locally

```bash
git clone <repo-url>
cd project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver