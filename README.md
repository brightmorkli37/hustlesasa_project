# HustleSasa Recommendation Engine

## Overview
A recommendation system for HustleSasa's e-commerce platform, demonstrating a content-based filtering technique for making recommendations for event tickets.

## Requirements
- **Python**: This project requires Python to be installed on your system. 
- Download and install the latest version of Python from [python.org/downloads](https://www.python.org/downloads/)
- Recommended Python version: 3.10 or higher
- Ensure Python is added to your system PATH during installation

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
```

### Step 5: running unit tests and the dev server
```bash
export DJANGO_SETTINGS_MODULE=root.settings
pytest
python manage.py runserver
```

## API Usage Documentation
The API provides detailed documentation for usage and testing. Access it via the following URLs when the server is running:

```bash
Swagger UI: http://127.0.0.1:8000/docs
ReDoc UI: http://127.0.0.1:8000/redoc
```