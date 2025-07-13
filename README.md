This is a Django-based REST API project that allows creating and retrieving KPA (Key Performance Assessment) form data using PostgreSQL. It is built using Django REST Framework.

Setup Instructions

1 - Clone the Repo
```bash
git clone https://github.com/Deepakch17/kpa-django-api-new.git
cd kpa-django-api-new

2 - Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate  # On Linux/macOS

3 - Install Dependencies
pip install -r requirements.txt

4 - Set Up PostgreSQL
Make sure PostgreSQL is installed and running.
Create a database named kpa_db.
Add the database credentials in .env file (create one if not present):

  DB_NAME=kpa_db
  DB_USER=postgres
  DB_PASSWORD=your_password
  DB_HOST=localhost
  DB_PORT=5432

5 - Run Migrations & Start Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Tech Stack Used

Python 3
Django 5
Django REST Framework
PostgreSQL
python-decouple (for .env variables)
Postman (for API testing)

Implemented APIs

**| Endpoint                   | Method | Description             |
| -------------------------- | ------ | ----------------------- |
| `/api/form-data/`          | POST   | Submit a new KPA form   |
| `/api/form-data/<int:id>/` | GET    | Retrieve KPA form by ID |
**

Folder Structure


kpa-django-api-new/
│
├── kpa_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── kpa_project/
│   └── settings.py
│
├── manage.py
├── .env
└── requirements.txt

Limitations / Assumptions

No authentication implemented (for simplicity).
No update/delete endpoints (only create and retrieve).
Assumes local PostgreSQL setup with access credentials.
Basic validation (handled by DRF serializers).
