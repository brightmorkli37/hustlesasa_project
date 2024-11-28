# HustleSasa Recommendation Engine

## Overview
A recommendation system for HustleSasa's e-commerce platform, demonstrating a content-based technique.

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/brightmorkli37/hustlesasa_project.git
cd hustlesasa_project
```

### Step 2: Create Virtual environment and install dependencies
Linux or Mac OS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Setup Database
create the file ".env" in the project directory and add your postgres database details;
```bash
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=db_user_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### Step 4: Apply migrations and runserver
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

API Usage Documentation
The API provides detailed documentation for usage and testing. Access it via the following URLs when the server is running:

```bash
Swagger UI: http://127.0.0.1:8000/docs
ReDoc UI: http://127.0.0.1:8000/redoc
```