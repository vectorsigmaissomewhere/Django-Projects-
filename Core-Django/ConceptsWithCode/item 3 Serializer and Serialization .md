## SERIALIZER AND SERIALIZATION IN DJANGO REST FRAMEWORK

Python JSON
```text
Python has a build in package called json,
 which is used to work with json data

methods
dumps(data)  This is used to convert python object into json string.
Example
To use json package First we have to import it.
import json
python_data = {'name':'Anish','roll':101}
json_data = json.dumps(python_data)
python(json_data)
{"name":"Anish","roll":101} // json data in double quotation

loads(data)  This is used to parse json string
Example: - 
import json
json_data = {"name":"Anish","roll":101}
parsed_data = json.loads(json_data)
print(parsed_data)
{'name':'Anish','roll':101}
```

What we learned
```text
Convert python data to json , dumps() method
convert json data to python , loads() method
```

## Serializers

```text
serializers does serialization and deserialization
```
About serializers
```text
In django REST Framework, serializers are reponsible for converting complex data
such as querysets and model instances to native Python datatypes (called serialization)
that can then be easily rendered into JSON, XML or other content types which is 
understandable to Front End.
```

Deserialization done by serializers
```text
allows parsed data to be converted back into complex types 
after first validating the incoming data.
```

Ways to do Serializer Class
```text
A serializer class is very similar to a Django Form and ModelForm class, and includes
similar validation flags on the various fields, sich as required, max_length and default.

Django Rest Framework provides a Serializer class which gives you a powerful, 
generic way to control the output of your responses, as well as ModelSerializer class
which provides a useful shortcut for creating serializers that deal with model instances 
and querysets.
```


How to create serializer class
```text
- Create a seperate serializers.py file to write all serializers
```

```python
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length = 100)
	roll  = serializers.IntegerField()
	city  = serializers.CharField(max_length = 100)
```

models.py
```python
from django.db import models
class Student(models.Model):
	name = models.CharField(max_length = 100)
	roll = models.IntegerField()
	city = models.CharField(max_length = 100)
// then migrate the database
```

Process
```text
Convert python data to json data to client 
Convert client json data to python 
```

For example
```text
We have a table 
in this table 
one row data means one model object data
row1 is model object 1
row2 is model object 2
row3 is model object 3

model object means model instance
model instance means complex data type
```

Complex Data Type  ----convert-->Python Native DataType  ----convert--------->Json Data
		 serialization			render into json


## Serialization 
```text
The process of converting complex data such as querysets and model instances to 
native Python datatypes are called as Serialization in DRF.
```

Model data set object

Serializing model data

```text
Creating model instance stu
stu = Student.objects.get(id = 1)

Converting model instance stu to Python Dict/ Serializing Object
serializer = StudentSerializer(stu)
```

Serializing Querydata set

```text
Creating Query Set
stu  = Student.objects.all()

Creating Query Set stu to List of Python Dict/Serializing Query Set
serializer = StudentSerializer(stu, many = True)
// many before that are lots of data
```

To see data in serializer
```text
This is serialized data
serializer.data
```

JSONRenderer
```text
This is used to render Serialized data into JSON
which is understandable by Front End.

Why to do this because front only understand json
To use this you need to import JSONRenderer
from rest_framework.renderers import JSONRenderer

After this render the data into json
json_data = JSONRenderer().render(serializer.data)
```


Revision
```text
3 steps
convert the model object to python dict and convert into json data
model object
stu = Student.object.get(id=1)
serializer = StudentSerializer(stu)
json_data = JSONRenderer().render(serializer.data)
```

JSONResponse() method 
```text
syntax
JsonResponse (data,encorder = DjangoJSONEncoder, safe = True, json_dumps_params = None,**kwargs)

An HttpResponse subclass that helps to create a JSON-encoded response.
It inherits most behavior from its superclass with a couple differences:
- Its default Content-Type header is set to application/json.
 - The first paramter, data should be a dict instance.
If the safe parameter is set to False it can be any JSON-serializable to object.
- The encoder, which defaults to django.core.serializers.json.DjangoJSONEncoder, will be used 
to serializer the data.
- default value of safe is True. If safe is false any object can be passed for serialization(otherwise
only dict instances are allowed). If safe is True and a non-dict object is passed as the first argument, 
a TypeError will be raised.
- The json_dumps_params parameter is a dictonary of keyword arguments to pass to the 
json.dumps() call used to generate the response.
```



## Conclusion of the theory is to remember the below infomation
Revision
```text
3 steps
convert the model object to python dict and convert into json data
model object
stu = Student.object.get(id=1)  
serializer = StudentSerializer(stu)
json_data = JSONRenderer().render(serializer.data)
---------------------------------------------------------------------------------
| id | Name      | Roll | City             |  
| 1  | Anish       | 101 | Itahari 	      |  <-----------Model object 1
| 2  | Ronaldo  | 102 | Portugal    |   <-----------Model object 2
| 3  | Messi      |  103 | Argentina |   <-----------Model object 3

Model Object 1 converted to Python Dict  converted to Json Data
and the above are the statement to convert 
```





## Coding part

1. serialization of one model object

file structure
```text
api
- admin.py
- models.py
- serializers.py
- views.py

gs1
- settings.py
- urls.py
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
    city  = models.CharField(max_length=100)
```

serializers.py
```python
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
```

views.py
```python
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
# Model Object - Single Student Data

def student_detail(request):
    stu = Student.objects.get(id=2)  # select the model objecgt
    serializer = StudentSerializer(stu)  # serialize stu model object which is converted into python data
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    return HttpResponse(json_data, content_type='application/json')  # sending data of type json
```


```settings.py
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k8xn5=8f2s98nx0*(yb@_1m)(_dxye^!!m_6(!6^^ut!orx!wm'

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
    'api',
    'rest_framework',
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

ROOT_URLCONF = 'gs1.urls'

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

WSGI_APPLICATION = 'gs1.wsgi.application'


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
    path('stuinfo/',views.student_detail),
]
```

Output
```text
model object in django  format
in stuinfo/ url
for example, output
{"name":"Messi","roll":10,"city":"Argentina"}
```


2. Anatomy of model object
   
views.py
```python
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
# Model Object - Single Student Data

def student_detail(request):
    stu = Student.objects.get(id=2)  # select the model objecgt
    print(stu)
    serializer = StudentSerializer(stu)  # serialize stu model object which is converted into python data
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')  # sending data of type json
```

Output
```text
Student object (2)
StudentSerializer(<Student: Student object (2)>):
    name = CharField(max_length=100)
    roll = IntegerField()
    city = CharField(max_length=100)
{'name': 'Messi', 'roll': 10, 'city': 'Argentina'}
b'{"name":"Messi","roll":10,"city":"Argentina"}'
[08/Jun/2024 07:22:10] "GET /stuinfo/ HTTP/1.1" 200 45
```

3. Get json data according to the url
   
urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.student_detail),
]
```

views.py
```python
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
# Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)  # select the model objecgt
    serializer = StudentSerializer(stu)  # serialize stu model object which is converted into python data
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    return HttpResponse(json_data, content_type='application/json')  # sending data of type json
```

output
```text
http://127.0.0.1:8000/stuinfo/1
output : {"name":"Ronaldo","roll":7,"city":"Lisbon"}

http://127.0.0.1:8000/stuinfo/2
output : {"name":"Messi","roll":10,"city":"Argentina"}
```

3 QuerySet get all students data

views.py
```python
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
# Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)  # select the model objecgt
    serializer = StudentSerializer(stu)  # serialize stu model object which is converted into python data
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    return HttpResponse(json_data, content_type='application/json')  # sending data of type json

# QuerySet - All student data
def student_list(request):
    stu = Student.objects.all() # select the model objecgt
    serializer = StudentSerializer(stu , many=True)  # serialize stu model object which is converted into python data
    json_data = JSONRenderer().render(serializer.data)  # converted into json data
    return HttpResponse(json_data, content_type='application/json')  # sending data of type json
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_list)
]
```

Output
```text
url: http://127.0.0.1:8000/stuinfo/
output : [{"name":"Ronaldo","roll":7,"city":"Lisbon"},{"name":"Messi","roll":10,"city":"Argentina"},{"name":"Mbappe","roll":1,"city":"Paris"}]
```

4 Access our API with python code

create app.py inside project folder 

app.py
```python
import requests
URL = "http://127.0.0.1:8000/stuinfo/"

r = requests.get(url = URL)

data = r.json()
print(data)
```
output
```text
[{'name': 'Ronaldo', 'roll': 7, 'city': 'Lisbon'}, {'name': 'Messi', 'roll': 10, 'city': 'Argentina'}, {'name': 'Mbappe', 'roll': 1, 'city': 'Paris'}]


5 Convert and send json data in one line


views.py
```python
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse


# Create your views here.
# Model Object - Single Student Data

def student_detail(request,pk):
    stu = Student.objects.get(id=pk)  # select the model objecgt
    serializer = StudentSerializer(stu)  # serialize stu model object which is converted into python data
    # json_data = JSONRenderer().render(serializer.data)  # converted into json data
    # return HttpResponse(json_data, content_type='application/json')  # sending data of type json
    return JsonResponse(serializer.data) # this is dict 

# QuerySet - All student data
def student_list(request):
    stu = Student.objects.all() # select the model objecgt
    serializer = StudentSerializer(stu , many=True)  # serialize stu model object which is converted into python data
    # son_data = JSONRenderer().render(serializer.data)  # converted into json data
    # return HttpResponse(json_data, content_type='application/json')  # sending data of type json
    return JsonResponse(serializer.data,safe=False) # non dict data so using safe = False 
```

output
```text
url : http://127.0.0.1:8000/stuinfo/1
output : {"name": "Ronaldo", "roll": 7, "city": "Lisbon"}

url : http://127.0.0.1:8000/stuinfo/
output : [{"name": "Ronaldo", "roll": 7, "city": "Lisbon"}, {"name": "Messi", "roll": 10, "city": "Argentina"}, {"name": "Mbappe", "roll": 1, "city": "Paris"}]
```


