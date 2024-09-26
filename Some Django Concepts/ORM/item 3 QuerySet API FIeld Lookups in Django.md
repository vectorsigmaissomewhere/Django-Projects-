## Field Lookups
```text
Field lookups are how you specify the meet of an SQL WHERE clause.
They're specified as keyword arguemnts to the QuerySet methods filter(), exclude() and get().
If you pass an invalid keyword argument, a lookup function will raise TypeError.
Syntax:- field__lookuptype=value
Example:- Student.objects.filter(marks__It='50')
SELECT * FROM myapp_student WHERE marks< '50';

The field specified in a lookup has to be the name of a model field.
In case of a ForeignKey you can specify the field name suffixed with
_id. In this case, the value parameter is expected to contain the raw 
value of the foreign model's primary key.
Example:- Student.objects.filter(stu_id=10)

exact - Exact match. If the value for comparison is None, it will be 
interpreted as an SQL NULL. This is case sensitive
Example:- Student.objects.get(name__exact='sonam')

iexact - Exact match. If the value provided for comparison is None, it 
will be interpreted as an SQL NULL. This is case insensitive.
Example:- Student.objects.get(name__iexact='sonam')

contains - Case-sensitive containment test.
Example:- Student.objects.get(name__contains='kumar')

icontains - Case-insensitive containment test.
Example:- Student.objects.get(name__contains='kumar')

in - In a given iterable; often a list, tuple, or queryset. 
It's not a common use case, but strings(being iterables) are accepted.
Example:- Student.objects.filter(id__in=[1,5,7])

gt - Greater than.
Example:- Student objects.filter(marks__gt=50)

gte - Greater than or equal to.
Example:- Student.objects.filter(marks__gte=50)

It - Less than.
Example:- Student.objects.filter(marks__It=50)

Ite - Less than or equal to.
Example:- Student.objects.filter(marks__Ite=50)

startswith - Case-sensitive starts-with
Example:- Student.objects.filter(name__startswith='r')

istartswith - Case-insensitive starts-with
Example:- Student.objects.filter(name__istartswith='r')

endswith - Case-sensitive ends-with.
Example:- Student.objects.filter(name__istartswith='r')

iendswith - Case-insensitive ends-with.
Example:- Student.objects.filter(name__iendswith='j')

range - Range test(inclusive).
Example:- Student.objects.filter(passdate_range=('2020-04-01','2020-05-05'))
SQL:- SELECT ... WHERE admission_date BETWEEN '2020-04-01' and '2020-05-05;
You can use range anywhere you can use BETWEEN in SQL --- for dates, numbers and even character.

date - For datetime fields, casts the value as data. Allows chaining additional field lookups. 
Take a data value.
Example:- 
Student.objects.filter(admdatetime__date = date(2020,6,5))
Student.objects.filter(admdatetime__date__gt = date(2020, 6, 5))

year - For date and datetime fields, and exact year match. Allows chaining additional field lookups.
Takes an integer year.
Example:-
Student.objects.filter(passdate__year=2020)
Student.objects.filter(passdate__year__gt=2019)

month - For date and datetime fields, an exact month match. Allows chaining additional field lookups.
Takes an integer 1 (January) through 12 (December).
Example:- 
Student.objects.filter(passdate__month=6)
Student.objects.filter(passdate__month__gt=5)

day - For date and datetime fields, an exact day match. Allows chaining additional field lookups. Takes
an integer day. 
Example:- 
Student.objects.filter(passdate__day=5)
Student.objects.filter(passdate__day__gt=3)
This will match any record with a pub_date on the third day of the month, such as January 3, July 3, 
etc.

week - For data and datetime fields, return the week number(1-52 or 53) according to ISO-8601, i.e.. 
weeks start on a Monday and the first week contains the year's first Thursday.
Example:-
Student.objects.filter(passdate__week=23)
Student.objects.filter(passdate__week__gt=22)

week_day - For date and datetime fields, a 'day of the week' match. Allows chaining additional field 
lookups. 
Takes an integer value representing the day of week from 1 (Sunday) to 7 (Saturday).
Example:- 
Student.objects.filter(passdate__week_day=6)
Student.objects.filter(passdate__week_day__gt=5)

This will match any record with a admission_date that falls on a Monday(day 2 of the week), regardless 
of the month or year in which it occurs. Week days are indexed with day 1 being Sunday and day 7 being 
Saturday.

quarter - For data and datetime fields, a 'quater of the year' match. Allows chaining additional field
lookups. Takes an integer value between 1 and 4 representing the quarter of the year.
Example to retrieve entries in the second quarter (April 1 to June 30):
Student.objects.filter(passdate__quarter=2)

time - For datetime fields, casts the value as time. Allows chaining additional field lookups. Takes a 
datetime.time value. 
Example:- Student.objects.filter(admdatetime__time__gt=time(6,00))

hour - For datetime and time fields, an exact hour match. Allows chaining additional field lookups. 
Takes an integer between 0 and 23.
Example:- Student.objects.filter(admdatetime__hour__gt=5)

minute - For datetime and time fields, an exact minute match. Allows chaining additional field lookups.
Takes an integer between 0 and 59.
Example:- Student.objects.filter(admdatetime__minute__gt=50)

second - For datetime and time fields, and exact second match. Allows chaining additional field lookups.
Takes an integer between 0 and 50.
Example:- Student.objects.filter(admdatetimer__second__gt=30)

isnull = Takes either True or False. which correspond to SQL queries of IS NULL or IS NOT NULL,  
repectively.
Example:- Student.objects.filter(roll_isnull=False)

regex
iregex
```

fieldlookups/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6k_g52azb7+im3f+bx@)m1!%@w)(r116n#@8)absfs6#^!0*z9'

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

ROOT_URLCONF = 'fieldlookups.urls'

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

WSGI_APPLICATION = 'fieldlookups.wsgi.application'


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

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_TZ = False


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
    path('exact', views.exact),
    path('iexact', views.iexact),
    path('contains', views.contains),
    path('icontains', views.icontains),
    path('inlookup', views.inlookup),
    path('greaterthan', views.greaterthan),
    path('greaterthanequal', views.greaterthanequal),
    path('lessthan', views.lessthan),
    path('lessthanequal', views.lessthanequal),
    path('startswith', views.startswith),
    path('istartswith', views.istartswith),
    path('endswith', views.endswith),
    path('iendswith', views.iendswith),
    path('range', views.range),
    path('datelookup', views.datelookup),
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
        table, th, tr, td{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <table>
        <h3>Student Information</h3>
        <th>ID</th>
        <th>Name</th>
        <th>Roll</th>
        <th>City</th>
        <th>Marks</th>
        <th>Passing Date</th>
        <th>Admission Date Time</th>
        {% for student in students %}
        <tr>
            <td>{{student.id}}</td>
            <td>{{student.name}}</td>
            <td>{{student.roll}}</td>
            <td>{{student.city}}</td>
            <td>{{student.marks}}</td>
            <td>{{student.passdate}}</td>
            <td>{{student.admdatetime}}</td>
        </tr>
        {% endfor %}
    </table>
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
from datetime import date, time
# Create your views here.

def home(request):
    student_data = Student.objects.all()
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# exact lookup
# getting all the data with name ali 
# it is case sensitive
def exact(request):
    student_data = Student.objects.filter(name__exact='Ali') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# iexact works same as exact but it is case insensitive
def iexact(request):
    student_data = Student.objects.filter(name__iexact='ali') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# contains lookup , is there any name that contain the given value
def contains(request):
    student_data = Student.objects.filter(city__contains='I') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# icontains lookup 
def icontains(request):
    student_data = Student.objects.filter(city__icontains='I') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# in lookup, filter the id where it is 1 , 2
def inlookup(request):
    student_data = Student.objects.filter(id__in=[1,2]) 
    # student_data = Student.objects.filter(marks__in=[60,70])
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# gt greater than lookup
def greaterthan(request):
    student_data = Student.objects.filter(marks__gt=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# gte greater than and equal lookup
def greaterthanequal(request):
    student_data = Student.objects.filter(marks__gte=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# lt less than lookup
def lessthan(request):
    student_data = Student.objects.filter(marks__lt=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# lte less than equal lookup, now you will even get 70
def lessthanequal(request):
    student_data = Student.objects.filter(marks__lte=70) 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# startswith # case sensitive
def startswith(request):
    student_data = Student.objects.filter(name__startswith='s') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})
    
# istartswith # case insensitive
def istartswith(request):
    student_data = Student.objects.filter(name__istartswith='S') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# endswith # case senstitive
def endswith(request):
    student_data = Student.objects.filter(name__endswith='l') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# iendswith # case sensitive
def iendswith(request):
    student_data = Student.objects.filter(name__iendswith='L') 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# range, from this range to that range
def range(request):
    student_data = Student.objects.filter(passdate__range=('2020-01-01', '2024-05-30'))
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})

# date lookup
def datelookup(request):
    student_data = Student.objects.filter(admdatetime__date=date(2024, 5, 8))
    # you can use anylookup like for example 
    # student_data = Student.objects.filter(admdatetime__date__gt=date(2024, 5, 8))
    # student_data = Student.objects.filter(passdate__year=2020)
    # student_data = Student.objects.filter(passdate__year__gt=2019) # greater than 
    # student_data = Student.objects.filter(passdate__year__gte=2020) # greater than and equal
    # student_data = Student.objects.filter(passdate__month=4) # get all april data
    # student_data = Student.objects.filter(passdate__month__gt=4) # month greater than 4
    # student_data = Student.objects.filter(passdate__month__gte=4) # month greater and equal to 4
    # student_data = Student.objects.filter(passdate__day=2) # day equal to 2
    # student_data = Student.objects.filter(passdate__day__gt=2)
    # student_data = Student.objects.filter(passdate__day__gte=2)
    # student_data = Student.objects.filter(passdate__week=23)
    # student_data = Student.objects.filter(passdate__week__gt=14) 
    # student_data = Student.objects.filter(passdate__weeek_day=1) # data where there is sunday 
    # student_data = Student.objects.filter(passdate__week_day__gt=5)
    # student_data = Student.objects.filter(passdate__quarter=2) # first quarter january, feburary, march , second quarter april, may, june
    # student_data = Student.objects.filter(admdatetime__time__gt=time(6,30)) # data after 6:30
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=26)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)
    # student_data = Student.objects.filter(roll__isnull=True) # model object where the roll column is null
    

    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students': student_data})
```

Where to find the full code
```text
check fieldlookups
```
