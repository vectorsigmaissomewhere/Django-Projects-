## DeSerialization

definition
```text
Serializers are also responsible for deserialization 
which means it allows parsed data to be converted 
back into complex types, after validating the incoming data
```

process
```text
jsondata ----->Python Native Datatype---------->ComplexDataType

first parse data then do de-serialization
```
Things to learn before doing de-serialization

1)  BytesIO()
```text
A stream implementation using an in-memory bytes buffer.
It inherits BufferedIOBase. The buffer is discarded when the 
close() method is called.

How to implement
import io
stream = io.BytesIO(json_data)
```

2) JSONParser()
```text
This is used to parse json data to python native data type

How to implement
from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)
```

3) De-serialization
```text
De-serialization allows parsed data to be converted back
into complex types, after first validating the incoming data.

How to implement
Creating Serializer Object
serializer = StudentSerializer(data  = parsed_data)

Validated Data
serializer.is_valid()

serializer.validated_data
serializer.errors
```

4) serializer.validated_data
```text
This is the Valid data
serializer.validated_data
```

That's the end


## Create Data/Insert Data
```python
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
	name  = serializers.CharField(max_length = 100)
	roll = serializers.IntegerField()
	city  = serializers.CharField(max_length = 100)

	def create(self, validate_data):
		return Student.objects.create(**validate_data)
```

## Coding part 

## main objective : other company application sending data into our application
sending data from frontend
```text
myapp.py is sending post request to views.py
and the data is coming to views.py
```

project directory
```text
gs2 is out main project folder
- myapp.py

api
- admin.py
- models.py
- serializers.py
- views.py

gs2
- settings.py
- urls.py
```

myapp.py
```python
# this is different application
import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"


data = {
    'name' : 'Ronaldo',
    'roll' : 7,
    'city' : 'Lisbon'
}

json_data = json.dumps(data)
r = requests.post(url=URL,data = json_data)
data = r.json()
print(data)
```

admin.py
```python
from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
```

models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)
```

views.py
```python
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt  # bypass csrf token
def student_create(request):
    if request.method == 'POST': # checking if the request is POST
        json_data = request.body # converting request data into json data
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream) # converting stream data into python data
        serializer = StudentSerializer(data=pythondata) # converting python data into complex data
        if serializer.is_valid(): # is complex data ready to be saved in database
            serializer.save()
            res = {'msg':'Data Created'}  
            json_data = JSONRenderer().render(res) # sending response to the applicaton from where the data is coming 
            return HttpResponse(json_data,content_type='application/json') # sending the json data
        
        # if it is not validated
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json') # sending the json data
```

settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(vkd^7$b3uq@!#ya49vkw1y6w&b5-=#ae1p2pbj45n8s&ol7m$'

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
    'rest_framework',
    'api',
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

ROOT_URLCONF = 'gs2.urls'

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

WSGI_APPLICATION = 'gs2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stucreate/',views.student_create),
]
```

in terminal
```text
python myapp.py
output: {'msg': 'Data Created'}
```
