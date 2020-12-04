# Test django GCP

This repo is create to demoded the beheavior of Django files and GCP storage

## Install

### Requirements

- [Python3](https://www.python.org/download/releases/3.0/)
- [PIP](https://pypi.org/project/pip/)
- [virtualenv](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3)
  (optional)

### Use virtual enviroment (optional)

Create virtual env

```bash
virtualenv  django_gcp -p python3
```

Activate environment, **You should activate each time when the terminal is open**

### Install dependencies

```bash
pip install -r requirements.txt
```

### Initialize database

The project use sqlite3 so you don't need configure any external database,
to execute all migration use:

```bash
python manage.py migrate
```

Now you need create a user to login as a admin

```bash
python manage.py createsuperuser
```

## Run

Start server

```bash
python manage.py runserver
```

Go to [http://127.0.0.1:8000/admin/contacts/contact/](http://127.0.0.1:8000/admin/contacts/contact/), then login and create a new Contact with 1 file
