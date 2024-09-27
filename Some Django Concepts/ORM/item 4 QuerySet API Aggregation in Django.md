## Aggregation
```text
sometimes you will need to retrive values that are derived by summarizing or aggregating a 
collection of objects.

aggregate() - It is a terminal clause for a QuerySet that, when invoked, returns a 
dictionary of name-value pairs. The name is an identifier for the aggregate value; 
the value is the computed aggregate. The name is automatically generated from the name 
of the field and the agggregate function.

Syntax:- aggrgate(name=agg_function('field'), name=agg_function('field'),)
field - It describes the aggregate value that we want to compute.
name - If you want to manually specify a name for the aggregate value, you can 
do so by providing that name when you specify the aggregate clause.

annotate() - Per-object summaries can be generated using the annotate() clause.
When an annotate() clause is specified, each object in the QuerySet will be 
annotated with the specified values. The output of the annotate() clause is 
a QuerySet; this QuerySet can be modified using any other QuerySet operation, 
including filter(), order_by(), or even additional calls to annotate().
```

## Aggregation Function
```text
Django provides the following aggregation functions in the django.db.models module.

Avg(expression, output_field=None, distinct=False, filter=None, **extra) - It returns the 
mean value of the given expression, which must be numeric unless you specify a different 
output_filed.

Default alias:<field>__avg

Return type: float if input is int, otherwise same as input filed, or output_field if supplied

Has one optional argument:

distinct: If distince=True, Avg returns the mean value of unique values. This is the SQL 
equivalent of AVG(DISTINCT <field>). The default value is False.

Count(expression, distinct=False, filter=None, **extra) - It returns the number of objects
that are related through the provided expression.
Default alias: <field>__count
Return type: int
Has one optional argument:
distinct - If distince=True, the count will only include unique instance. This is the SQL
equivalent of COUNT(DISTINCT<field>). The default value is False.

Max(expression, output_field=None, filter, **extra) - It returns the maximum value of the 
given expression. 
Default alias: <field>__max
Return type: same as input field, or output_field if supplied

Min(expression, output_field=None, filter=None, **extra) - It returns the minimum value of 
the given expression. 
Default alias: <field>__min
Return type: same as input field, or output_field if suppplied

Sum(expression, output_field=None, distinct=False, filter=None, **extra) - It compute the sum 
of all values of the given expression. 
Default alias: <field>__sum
Return type: same as input field, or output_field if supplied
Has one optional argument:
distinct - If distinct=True. Sum returns the sum of unique values. This is the SQL equivalent
of SUM(DISTINCT <field>).
The default value is False.

StdDev(expression, output_field=None, sample=False, filter=None, **extra) - It returns the 
standard deviation of the data in the provided expression.
Default alias: <field>__stddev
Return type: float if input is int, otherwise same as input field, or output_field if supplied
Has one optional argument:
sample- By default, StdDev returns the population standard deviation. However, if sample=True, 
the return value will be the sample standard deviation. 

Variance(expression, output_field=None, sample=False, filter=None, **extra) - It return value will
be the sample standard deviation.

Variance(expression, output_field = None, sample=False, filter=None, **extra) - It return the 
variance of the data in the provided expression.
Default alias: <field>__variance
Return type: float if input is int, otherwise same as input field, or output_field is supplied
Has one optional argument:
sample - By default, Variance returns the population variance. However if sample=True, the return 
value will be the sample variance.
```

fieldlookups/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-phfqg*xa7w*653fue1ie4z^1#h*z0mk+fiu&9c!@a4n3q7q_1l'

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

ROOT_URLCONF = 'querysetaggregation.urls'

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

WSGI_APPLICATION = 'querysetaggregation.wsgi.application'


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
    </table>

    <hr>
    <h3>Statistics</h3>
    <ul>
        <li>Average Marks: {{ average.marks__avg }} {{average}}</li>
        <li>Sum of Marks: {{ summation.marks__sum }} {{summation}}</li>
        <li>Minimum Marks: {{ minimum.marks__min }} {{minimum}}</li>
        <li>Maximum Marks: {{ maximum.marks__max }} {{maximum}}</li>
        <li>Total Count of Students: {{ totalcount.marks__count }} {{totalcount}}</li>
    </ul>
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
from django.db.models import Avg, Sum, Min, Max, Count

def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    summation = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalcount = student_data.aggregate(Count('marks'))

    context = {
        'students': student_data,
        'average': average,
        'summation': summation,
        'minimum': minimum,
        'maximum': maximum,
        'totalcount': totalcount,
    }

    return render(request, 'school/home.html', context)
```

## output
```text
Student Information
ID	Name	Roll	City	Marks	Passing Date	Admission Date Time
1	Sonam	101	Ranchi	90	Sept. 13, 2024	Sept. 6, 2024, 6:25 a.m.
2	Rahul	102	Ranchi	70	Aug. 15, 2024	May 8, 2024, 9:17 a.m.
3	Raj	103	Ranchi	80	June 12, 2024	May 15, 2024, 6:25 a.m.
4	Ali	104	Bokaro	60	May 16, 2024	March 6, 2024, 6:20 p.m.


Statistics
Average Marks: 75.0 {'marks__avg': 75.0}
Sum of Marks: 300 {'marks__sum': 300}
Minimum Marks: 60 {'marks__min': 60}
Maximum Marks: 90 {'marks__max': 90}
``

Where to find the full code
```text
checkquerysetaggregation
```
