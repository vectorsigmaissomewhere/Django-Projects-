## Django Session Framework

```text
The session framework lets you store and retrieve arbitrary data on a per-site-visitor basics.
It stores data on the server side and abstracts the sending and receiving of cookies.
Cookies contain a session ID not the data itself.

By default, Django stores sessions in your database.
As it stores sessions in database so it is mandatory to run makemigrations and migrate
to use session. It will create required tables.

The Django sessions framework is entirely, and solely, cookie-based.
django.contrib.sessions.middleware.SessionMiddleware
django.contrib.sessions
```

What are the ways in which sessions can be stored?
```text
database-backend sessions- If you want to use a database-backend session, you need to add
'django.contrib.session' to you INSTALLED_APPS setting.

after configuration , hit python manage.py migrate to install the single database that 
stores session data.

file-based sessions - To use file-based sessions, set the SESSION_ENGINE setting to 
"django.contrib.sessions.backends.file".

You might also want to set the SESSION_FILE_PATH setting (which defaults to output from
tempfile.gettempdir(), most likely /tmp) to control where Django stores session files. Be 
sure to check that your Web server has permissions to read and write to this location.

cookie-based sessions - To use cookies -based sessions, set the SESSION_ENGINE setting to 
"django.contrib.sessions.backends.signed_cookies". The session data will be stores using
Django's tools for cryptographic signing and the SECRET_KEY setting.

cached sessions - For better performance, you may want to use a cache-based sesion
backend. To store session data using Django's cache system, you'll first need to make sure
you've configured your cache.
```

Using Sessions in views
```text
When SessionMiddleware is activated, each HttpRequest object, the first argument to any
Django view function will have a session attribute, which is a dictionary-like object.
You can read it and write to request.session at any point in your view. You can edit it
multiple times.

-Set Item 
request.session['key'] = 'value'

- Get Item
returned_value = request.session['key']
returned_value  = request.session['key']

- Delete Item
del request.session['key']
This raises KeyError if the given key isn't already in the sesssion.

- Contains
'key' in request.session
```
Program number 1 

Set, Get, Delete session in Django 

sessionframework/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@^236mkp)-7q(!w(ql)iaseo!f_ax--^a-^*ijo177t^^o72kv'

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
    'student',
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

ROOT_URLCONF = 'sessionframework.urls'

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

WSGI_APPLICATION = 'sessionframework.wsgi.application'


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

sessionframework/urls.py
```python
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('del/', views.delsession),
]
```

student/templates/student/delsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Session</title>
</head>
<body>
    <h1>You session has been deleted successfully</h1>
</body>
</html>
```

student/templates/student/getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}}
    {{lname}}
</body>
</html>
```

student/templates/student/setsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Session</title>
</head>
<body>
    <h1>Session setting up...........</h1>
</body>
</html>
```

student/views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'rathore'
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname', default='Guest')
    return render(request, 'student/getsession.html', {'name': name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request, 'student/delsession.html')
```

about this code
```text
This code set, get and delete session.
Where in session it stores name and lname
```

where to find the full code
```text
check sessionframework folder
```

 Session Methods
```text
keys() method returns a view object that displays a list of all the keys 
in the dictionary 
Syntax:- dict.keys()

items() method returns  the list with all dictionary keys with values.
Syntax:- dict.items()

clear() function is used to erase all the elements of list. After this operarion,
 list becomes empty.
Syntax:- dict.clear()

setdefault() method returns the value of a key(if the key is in dictionary). 
If not, it inserts key with a value to the dictionary.
Syntax: dict.setdefault(key, default_value)

flush()- It deletes the current session data from the session and delets the session cookie.
This is used if you want to ensure that the previous session data can't be accessed again 
from the user's browser(for example, the django.contrib.auth.logout() function calls it).
```

Program number 2 
```text
- Here we will only work on views.py and getsession.html
The rest of the program is similar to program number 1
The new thing about this program is we have used flush method and other dictionary methods
```
views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Ronaldo'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')
    return render(request, 'student/getsession.html', {'name': name,'lname': lname, 'keys': keys, 'items': items, 'age': age})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
        # you can use sesion.flush() to remove all the sessions can delete all the session in single line of code 
        # request.session.flush()
    return render(request, 'student/delsession.html')
```
getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}}
    {{lname}}<br><hr>
    <!--How to get session key-->
    {% for key in keys %}
    {{key}} 
    {% endfor %}<br><hr>
    {% for item in items %}
    {{item}}
    {% endfor %}<br><hr>
    {% for key, value in items %}
    {{key}} {{value}}
    {% endfor %}
</body>
</html>
```
where to find the full code 
``text
check sessionframework2 folder 
```
