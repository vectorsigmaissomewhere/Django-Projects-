QuerySet API
```text
A QuerySet can be defined as a list containing all those objects we have 
created using the Django model.
QuerySets allow you to read the data from the database, filter it and order it.

query property - This property is used to get sql query of query set.
Syntax - queryset.query
```

Methods that return new QuerySets
```text
1. Retrieving all objects
all() - This method is used to retrieve all objects. This returns a copy of 
current QuerySet.
Example: - Student.objects.all()

2. Retrieving specific objects
filter(**kwargs) - It returns a new QuerySet containing objects that match the
given lookup paramters. filter() will always give you a QuerySet, even if only
a single object matches the query.
Example: - Student.objects.filter(marks=70)

3. exclude(**kwargs) - It returns a new QuerySet containing objects that do not match
the given lookup parameters.
Example: Student.objects.exclude(marks=70)

4. order_by(*fields) - It orders the fields.
- 'field' - Asc order
- '-field' - Desc order
- '?' - Randomly

5. reverse() - This works only there is ordering in queryset

6. values(*fields, **expression) - It returns a QuerySet that returns dictionaries, rather than
model instances, when used as an iterable. Each of those dictionaries reprsents and object, with
the keys corresponding to the attribute names of model objects.

7. distinct(*fields) - This eliminates duplicate rows from the query results.

8. values_list(*fields, flat=False, named=False) - This is similar to values() except that instead of
returning dictionaries, it returns tuples when iterated over.
- If you don't pass any values to values_list(), it will return all the fields in the model, in the
order they were declared.
- If you only pass in a single field, you can also pass in the flat parameter. If True, this will mean
the returned results are single values, rather than one-tuples.
- You can pass named=True to get results as a namedtuple

9. using(alias) - This method is for controlling which database the QuerySet will be evaluated against if
you are using more than one database. The only argument this method takes is the alias of a database,
as defined in DATABASES.
Example:- student_data = Student.objects.using('default') # 'default' is the database name

10. dates(field, kind, order='ASC') - It returns a QuerySet that evaluates to a list of datetime date objects
representing all available dates of a particular kind within the contents of the QuerySet.
Where,
field - It should be the name of a DateField of your model.
kind - It should be either "year", "month", "week", or "day".
"year" returns a list of all distinct year values for the field.
"month" returns a lit of all distinct year/month values for the field.
"week" returns a list of all distinct year/month values for the field. All dates will be on Monday.
"day" returns a list of all distinct year/month/day values for the field.
order - It should be either 'ASC' or 'DESC'. This specifies how to order the results. defaults to 'ASC'
Each datetime date object in the result list is "truncated" to the given type.

11. datetimes(field_name, kind, order='ASC', tzinfo=None) - It returns a QuerySet that evaluates to
a list of datetime.datetime objects representing all available dates of a particular kind within the contents
of the QuerySet.
Where,
field - It should be the name of a DateField of your model.
kind - It should be either "year", "month", "week", or "day".
"year" returns a list of all distinct year values for the field.
"month" returns a lit of all distinct year/month values for the field.
"week" returns a list of all distinct year/month values for the field. All dates will be on Monday.
"day" returns a list of all distinct year/month/day values for the field.
order - It should be either 'ASC' or 'DESC'. This specifies how to order the results. defaults to 'ASC'
tzinfo - It defines the time zone to which datetimes are converted prior to truncation. This parameter
must be a datetime.tzinfo object. If it's None, Django uses the current time zone. It has no effect
when USE_TZ is False.
Each datetime date object in the result list is "truncated" to the given type.

12. none() - Calling none() will create a queryset that never returns any objects and no query will
be executed when accessing the results. A qs.none() queryset is an instance of EmptyQuerySet.
Example :- student_data = Student.objects.none()

13. union(*other_qs, all=False) - Uses SQL's UNION operator to combine the results of two or more QuerySets.
The UNION operator selects only distinct values by default. To allow duplicate values, use the all=True
argument.

14. intersection(*other_qs) - Uses SQL's INTERSECT operator to return the shared elements of two or more
QuerySets.
Example :- student_data = qs1.intersection(qs2)

15. difference(*other_qs) - Uses SQL's EXCEPT operator to keep only elements present in the QuerySet but
not in some other QuerySets.
Example :- student_data = qs1.difference(qs2)

Less used query methods

16. select_related(*fields)
17. defer(*fields)
18. only(*fields)
19. prefetch_related(*lookups)
20. extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
21. select_for_update(nowait=False, skip_located=False, of=())
22. raw(raw_query, params=None, translations=None)
23. annotate(*args, **kwargs)
```

Operators that return new QuerySets
```text
AND(&) - Combines two QuerySets using the SQL AND operator.
Example:-
student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
student_data = Student.objects.filter(id=6, roll=106)
student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

OR(|) - Combines two QuerySets using the SQL OR operator.
Example:-
Student.objects.filter(id=11) | Student.objects.filter(roll=106)
Student.objects.filter(Q(id=11) | Q(roll=106))
```

## Program part

querysetapi/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6ltt!3et3d#3se24h9*sjc455!_&#9e09h^-h2+m99iejz#ro-'

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

ROOT_URLCONF = 'querysetapi.urls'

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

WSGI_APPLICATION = 'querysetapi.wsgi.application'


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

querysetapi/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.queryall),
    path('queryfilter/', views.queryfilter),
    path('queryexclude/', views.queryexclude),
    path('queryorderby/', views.queryascendingorderby),
    path('queryorderbyneg/', views.querydescendingorderby),
    path('queryrandom/', views.queryrandom),
    path('queryreverse/', views.queryreverse),
    path('queryvalues/', views.queryvalues),
    path('queryvalueslist/', views.queryvalueslist),
    path('usingmethod/', views.using),
    path('querydates/', views.querydates),
    path('queryunion/', views.queryunion),
    path('queryintersection/', views.queryintersection),
    path('querydifference/', views.querydifference),
    path('andoperator/', views.andoperator),
    path('oroperator/', views.oroperator),
]
```

school/templates/school/home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Queryset Api</title>
    <style>
        table, th, tr, td{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <table>
    <h1>Student Information</h1>
    <th>ID</th>
    <th>Name</th>
    <th>Roll</th>
    <th>City</th>
    <th>Marks</th>
    <th>Passing Year</th>
    {% for student in students %}
    <tr>
    <td>{{ student.id }}</td>
    <td>{{ student.name }}</td>
    <td>{{ student.roll }}</td>
    <td>{{ student.city }}</td>
    <td>{{ student.marks }}</td>
    <td>{{ student.pass_date }}</td>
    </tr>
    {% endfor %}
    </table>
</body>
</html>
```

school/admin.py
```python
from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Student)
admin.site.register(Teacher)
```

school/models.py
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    pass_date = models.DateField()

class Teacher(models.Model):
    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()
    
```


school/views.py
```python
from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# get all models objects
def queryall(request):
    student_data = Student.objects.all()
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# filter model object attribute
def queryfilter(request):
    student_data = Student.objects.filter(marks=90)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# filter model object attribute 
def queryexclude(request):
    student_data = Student.objects.exclude(marks=90)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# queryset in ascending order by looking unicode means 
# if there are three city Akabare, Biratnagar, akabare
# when you run the query you will be getting the model object in 
# "Akabare, Biratnagr, akabare " order instead it should be 
# "AKabare, akabare, Biratnagar"
def queryascendingorderby(request):
    student_data = Student.objects.order_by('city')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# queryset in descending order
def querydescendingorderby(request):
    student_data = Student.objects.order_by('-city')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# random queryset, each time you call this method you get the different order query object
def queryrandom(request):
    student_data = Student.objects.order_by('?')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# reverse(), model objects in reverse order
def queryreverse(request):
    student_data = Student.objects.order_by('id').reverse()
    #student_data = Student.objects.order_by('id').reverse()[:2] # get last 3 model objects
    #student_data = Student.objects.order_by('id').reverse()[0:2] # get last 3 model objects
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# values() , get model objects in list of dictionaries 
def queryvalues(request):
    # student_data = Student.objects.values()
    student_data = Student.objects.values('name', 'city') # if I need only name and city
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# values_list() no values is associated with id, so you won't be able to see the data this way
def queryvalueslist(request):
    # student_data = Student.objects.values_list() # make named=True to see data
    student_data = Student.objects.values_list('id', 'name', named=True) # if i need only id and names 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# using() method
def using(request):
    student_data = Student.objects.using('default')
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# dates() method
def querydates(request):
    # by default in ascending order
    student_data = Student.objects.dates('pass_date', 'month') # values in tuple so we are unable to see, make named = True to view data
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})


# union() method
def queryunion(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.union(qs1)
    # student_data = qs2.union(qs1, all=True) # if you want duplicates
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# intersection() method
def queryintersection(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.intersection(qs1)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

# difference() method
def querydifference(request):
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.difference(qs1)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

def andoperator(request):
    student_data = Student.objects.filter(id=4) & Student.objects.filter(roll=104)
    # student_data = Student.objects.filter(id=4, roll=104) # second way 
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106)) # third way 
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})

def oroperator(request):
    student_data = Student.objects.filter(id=4) | Student.objects.filter(roll=103)
    # student_data = Student.objects.filter(Q(id=4) | Q(roll=103)) # second way  
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query) # generate sql query
    return render(request, 'school/home.html', {'students': student_data})
```

Where to find the full code
```text
check querysetapi
```

