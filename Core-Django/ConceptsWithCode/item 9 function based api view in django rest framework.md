# Function Based api_view
about
```text
This wrapper provides a few bits of functionality such as making sure you receive Request
instances in your view, and adding context to Response objects so that content negotiation can be 
performed.
The wrapper also provides behaviour such as returning 405 Method Not Allowed reponses when appropriate, and handling and ParseError expections that occur when accessing request.data with malformed input.

By default only GET methods will be accepted. Other methods will respond with "405 Method
Not Allowed".

@api_view() then get is already present
but if you want get, post, put, delete what you can do to mention this is by 
@api_view(['GET','POST','PUT','DELETE'])
def function_name(request)
```

How to do this api_view
```text
- for get request
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        stu  = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)

- for post request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status # what are the status code we receive from response like 200 , 300 , 400, 100, 404
@api_view(['POST'])
def student_create(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.error.status = status.HTTP_400_BAD_REQUEST)
```

What is request?
```text
REST framework's Request objects provide flexible request parsing that allows you to 
treat requests with JSON data or other media types in the same way that you would 
normally deal with form data.

first 
request.data : request.data returns the parsed content of the request body. This is 
similar to the standard request.POST and request.FILES atrributes excpet that:
- It includes all parsed content, including file and non-file inputs.
- It supports parsing the content of HTTP methods other than POST, meaning that you 
can access the content of PUT or PATCH requests.
- It supports REST framework's flexible request parsing, rather than just supporting 
form data. for example you can handle incoming JSON data in the same way that 
you handle incoming form data.
second
request.method : request.method returns the uppercased string representation of the 
request's HTTP method.
Brower-based PUT, PATCH and DELETE forms are transparently supported.

third 
request.query_params : request.query_params is a more correctly named synonum for
request.GET.
For clarity inside your code, we recommend using request.query_params instead of the 
Django's standard request.GET. Doing so will help keep your codebase more correct
and obvious - any HTTP method type may include query parameters, not just GET 
requests.
```

Response()
```text
REST framework supports HTTP content negotiation by providing  a Response class which allows you to return 
content that can be rendered into multiple content types, depending on the client request.

Response objects are initialized with data, which should consist of native Python primitives. REST framework
then uses standard HTTP content negotition to determine how it should render the final reposne content.

Response class simply provides a nicer interface for returning content-negotiated Web API responses, that can 
be rendered to multiple formats.

Syntax: - Response(data, status = None, template_name = None, headers = None, content_type = None)
- data: The unrendered, serialized data for the response. 
- status: A status code for the reponse. Defaults to 200.
- template_name: A template name to use only if HTMLRenderer or some other custom template renderer is the 
accepted renderer for the response.
- headers: A dictionary of HTTP headers to use in the response.
- content_type: The content type of the response. Typically, this will be set automatically by the renderer as 
determined by content  negotiation, but there may be some cases where you need to specity the content type 
explicitly. 
```
# CODING PART

1 Test your api using browseable api

views.py
```python
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
"""
# Create your views here.
@api_view() # if nothing is present here get is present like (['GET'])
def hello_world(request):
    return Response({'msg','Hello World'})
"""
"""
# for post
@api_view(['POST'])
def hello_world(request):
    if request.method == "POST":
        print(request.data)
        return Response({'msg':'This is POST Request'})
"""
# depends upon the request made
@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':'This is GET Request'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'This is POST Request','data':request.data})
```

settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)-^qfjl11l-)m(ned*blopn-6hhk^08$_+3yf@)x!e^loflkla'

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

ROOT_URLCONF = 'gs9.urls'

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

WSGI_APPLICATION = 'gs9.wsgi.application'


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

myapp.py
```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# this function will give you the data according to the id 
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers, json=data)
    try:
        r.raise_for_status() 
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Response content is not valid JSON")

get_data()

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Rchecking1',
        'roll':120,
        'city':'Dhanchad'
    }
    headers = {'content-Type':'application/json'}
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers,data = json_data)
    data = r.json()
    print(data)

post_data()


# this function will update the data with id
# this is a partial updates as only required data is updated 
def update_date():
    data = {
        'id': 9,
        'name': 'Ramos',
        'roll': 111,
        'city': 'banchi'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':6}

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
#delete_data()
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.hello_world)
]
```

hit the below url in browser
```text
http://127.0.0.1:8000/studentapi/
```

2 Crud Using Function Based api_view

impovement in the number of number of lines we used to write in gs7 has becomed less

```text
for get request
when get_data(2)
{'id': 2, 'name': 'Rahul', 'roll': 102, 'city': 'Ranchi'}

when get_data()
[{'id': 1, 'name': 'Sonam', 'roll': 101, 'city': 'Ranchi'}, {'id': 2, 'name': 'Rahul', 'roll': 102, 'city': 'Ranchi'}, {'id': 3, 'name': 'Raj', 'roll': 103, 'city': 'Bokaro'}]
```

function based api_view
models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
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

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
```
views.py
```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id') # getting directly parsed data
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,  partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api),
]
```
myapp.py
```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# this function will give you the data according to the id 
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers, json=data)
    try:
        r.raise_for_status() 
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Response content is not valid JSON")

# get_data()

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Sumit',
        'roll':120,
        'city':'Ranchi'
    }
    headers = {'content-Type':'application/json'}
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers,data = json_data)
    data = r.json()
    print(data)

# post_data()


# this function will update the data with id
# this is a partial updates as only required data is updated 
def update_date():
    data = {
        'id': 4,
        'name': 'Ranchi',
        'roll': 112,
        'city': 'Hunchi'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':4}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
delete_data()
```

3 Crud using browseable api with proper status code

models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
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

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api),
    path('studentapi/<int:pk>',views.student_api)
]
```

myapp.py
```python
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

# this function will give you the data according to the id 
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers, json=data)
    try:
        r.raise_for_status() 
        data = r.json()
        print(data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("Response content is not valid JSON")

# get_data()

# this function will send data to the server and save it into table 
# this is in dictionary form 
def post_data():
    data = {
        'name':'Sumit',
        'roll':120,
        'city':'Ranchi'
    }
    headers = {'content-Type':'application/json'}
    # converting this into json form 
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers,data = json_data)
    data = r.json()
    print(data)

# post_data()


# this function will update the data with id
# this is a partial updates as only required data is updated 
def update_date():
    data = {
        'id': 4,
        'name': 'Ranchi',
        'roll': 112,
        'city': 'Hunchi'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# update_date()

# this function will delete the data based on id 
def delete_data():
    data = {'id':4}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers=headers, data = json_data)
    data = r.json()
    print(data)
delete_data()
```

views.py
```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk 
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED) # when ever it shows 201 when created
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # when ever we get error we get this error status code
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,  partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
```

Conclusion
```text
Learned change the data using third party api
Learned about browseable api and status code
```
