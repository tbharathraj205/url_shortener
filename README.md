
# URL Shortener

I made this URL shortener from scratch using Django.

## How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
````

### 2. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Then open:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Features

* Create short URLs
* Redirect short URLs to the original URL
* Store shortened URLs in SQLite
* View created URLs
* Django admin support