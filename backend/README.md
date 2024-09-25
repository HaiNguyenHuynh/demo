## Apply Migrations

```commandline
python manage.py makemigrations
python manage.py migrate
```

## Create group command

```commandline
python manage.py create_roles
```

## Create Superuser (Admin)

```commandline
python manage.py createsuperuser
```

## Run the Application

```commandline
python manage.py runserver
```

## User Registration and Authentication

User Registration: `POST /api/auth/registration/`
Login: POST `/api/auth/login/`
Social Login (SSO): POST `/api/auth/social/login/`