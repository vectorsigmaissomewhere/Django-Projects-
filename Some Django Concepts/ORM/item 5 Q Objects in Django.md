## Q Objects
```text
Q objects is an object used to encapsulate a collection of keyword arguments. These 
keyword arguments are specified as in "Field lookups".
If you need to execute more complex queries, you can use Q objects.
Q objects can be combined using the & and | operators. When an operator is used on 
two Q objects, it yields a new Q object.

from django.db.models import Q

& (AND) Operator
Example:- Student.objects.filter(Q(id=6) & Q(roll=106))

| (OR) Operator
Example:- Student.objects.filter(Q(id=6) | Q(roll=108))

~ Negation Operator
Example:- Student.objects.filter(~Q(id=6))
```


fieldlookups/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n5m_b(y*9je$f%_vfji3(a*(rs#1vjtxb25269wqs52lgl=#gw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'school',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'QObjects.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'QObjects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

fieldlookups/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

school/templates/school/home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Information</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
            padding: 8px;
            text-align: left;
        }
        h3 {
            margin: 20px 0 10px;
        }
    </style>
</head>
<body>
    <h3>Student Information</h3>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Roll</th>
                <th>City</th>
                <th>Marks</th>
                <th>Passing Date</th>
                <th>Admission Date Time</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.roll }}</td>
                <td>{{ student.city }}</td>
                <td>{{ student.marks }}</td>
                <td>{{ student.passdate }}</td>
                <td>{{ student.admdatetime }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table><hr>
</body>
</html>
```

school/models.py
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    passdate = models.DateField()
    admdatetime = models.DateTimeField()
```

school/views.py
```python
from django.shortcuts import render
from .models import Student
from django.db.models import Q

def home(request):
    # student_data = Student.objects.filter(Q(id=4) & Q(roll=104)) # filter whose id is 4 or roll is 104
    # student_data = Student.objects.filter(Q(id=4) | Q(roll=103)) # filter whose id is 4 or roll is 103
    student_data = Student.objects.filter(~Q(id=6)) # student data whose id is not 6 
    print("Return: ", student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request, 'school/home.html',{'students':student_data})
```

Where to find the full code
```text
QObjects
```

