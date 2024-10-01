## Model Manager
```text
A Manager is the interface through which database query operations are provided to Django models.
At least one Manager exists for every model in a Django application.

Model manager is used to interact with database.
By default, Django adds a Manager with the name objects to every Django model class.

django.db.models.manager.Manager
```

Change Mangager Name
```text
By default, Django adds a Manager with the name objects to every Django model class.
However, if you want to use objects as a field name, or if you want to use a name other 
than objects for the Manager, you can rename it on a per-model basis.

To rename the Manager for a given class, define a class attribute of type models.Manager()
on that model.
from django.db import models
class Student(models.Model):
    name = models.CharField(max_length = 70)
    roll = models.IntegerField()
    students = models.Manager()

# get all model objects, a different approach
student_data = Student.students.all()
```

## Coding Part

settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_u5a9boyy^^h)llzf0c@r@*!b7_@z%4eg)q!vguvqe(1u1+-7l'

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

ROOT_URLCONF = 'modelmanagerchangemanager.urls'

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

WSGI_APPLICATION = 'modelmanagerchangemanager.wsgi.application'


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

urls.py
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
    <title>Document</title>
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
                <th>Name</th>
                <th>Roll</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.roll }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table><hr>
</body>
</html>
```

models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager() by default it was it
    students = models.Manager()
```

views.py
```python
from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    student_data = Student.students.all()
    return render(request, 'school/home.html', {'students': student_data})
```

Where to find the full code
```text
check modelmanagerchangemanager
```


## Custom Model Manager
```text
You can use a custom Manager in a particular model by extending the base Manager class and 
instantiating your custom Manager in your model.
A custom Manager model can return anything you want. It doesn't have to return a QuerySet.
- to modify the initial QuerySet the Manager returns
- to add extra Manager methods
```

## Modify the initial QuerySet
```text
A Manager's base QuerySet returns all objects in the system. You can override a Manager's 
base QuerySet by overriding the Manager.get_queryset() method. get_queryset() should return 
a QuerySet with the properties you require.

Write Model Manager
class CustomManager(models.Manager):
    def get_queryset(self):       # overriding Built-in method called when we call all()
        return super().get_queryset().order_by('name')

Associate Manager with Model
class Student(models.Model):
    objects = models.Manager()       # Default Manager  ---------]
                                                                 ] ---You can associate more than 
                                                                 ]      one manager in one Model
    students = CustomManager()       # Custom Manager   ---------]

views.py
Student_data = Student.objects.all()      # Work as per default Manager
Student_data = Student.students.all()      # Work as per Custom Manager
```

## Coding 

managers.py
```python
from django.db import models

# gettting name data by order
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
```

models.py
```python
from django.db import models
from .managers import CustomManager
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager() # default ModelManager be objects in views but CustomMangager will also work
    students = CustomManager() # now the name will come by order
```
views.py
```python
from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    student_data = Student.students.all()
    return render(request, 'school/home.html', {'students': student_data})
```

where to find the fulll code 
```text
check modifytheinitialqueryset
```


## Add extra Manager methods
```text
Adding extra Manager methods is the preferred way to add "table-level" functionality to your models.
-------Write Model Manager-----
class CustomManager(models.Manager):
    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1,r2))

------Associate Manager with Model--------
class Student(models.Model):
    objects = models.Manager()
    students = CustomManager()

-----views.py------------
Student_data = Student.objects.all()
Student_data = Student.students.get_stu_roll_range(101, 103)
```

## Coding Part

managers.py
```python
from django.db import models

class CustomManager(models.Manager):
    def get_stu_roll_range(self, r1, r2):
        return super().get_queryset().filter(roll__range=(r1, r2))
```

models.py
```python
from django.db import models
from .managers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    objects = models.Manager() # by default it was it
    students = CustomManager()
```

views.py
```python
from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    # get data from 1 to 9
    student_data = Student.students.get_stu_roll_range(1,9)
    return render(request, 'school/home.html', {'students': student_data})
```

Where to find the full code
```text
check addextramanagermethods
```

## Model Manager with Proxy Model

## Coding Part
