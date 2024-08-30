The Per View Caching in Django
```text
The per-view cache - A more granular way to use the caching 
framework is by caching the output of individual views. 
django.views.decorators.cache defines a cache-page decorator
that will automatically cache the view's response. If multiple
URLs point at the same view, each URL will be cached seperately.


from django.views.decorators.cache import cache_page
@cache_page(timeout, cache, key_prefix)
def my_view(request):
    

timeout - The cache timeout, in seconds.
cache - This directs the decorator to use a specific cache( from 
your CACHES settings when caching view results. By default, the
default cache will be used.
key_prefix - You can also override the cache prefix on a per-view
basis. It works in the same way as the 
CACHE_MIDDLEWARE_KEY_PREFIX setting for the middleware.
```

Specifying per-view cache in the URL cont
```python
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('route/', cache_page(timeout, cache, key_prefix)(view_function)),
]

urlpatterns = [
    path('home/', cache_page(60)(views.home),name="home"),
]
````

Database Caching
```text
Django can store its cached data in your database. This works best if you've
got a fast, well-indexed database server.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table', # the name of the database table
        }
     }

Before using the database cache, you must create the cache table with this command:
python manage.py createcachetable

This creates a table in your database that is in the proper format that Django's
database-cache system expects.
This name of the table is taken from LOCATION.

If you are using multiple database caches, createcachetable creates one table for
each cache.
```
## The most important line
```text
python manage.py createcachetable
```

Program number 1 
```text
adding decorator in views
stores the cache in database
```

perviewcache/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j!&y2xa7#4a_bu*lmczi7njv5n^o5@-7r%la$5_n+k-x(*gkl1'

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
    'enroll',
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

ROOT_URLCONF = 'perviewcache.urls'

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

WSGI_APPLICATION = 'perviewcache.wsgi.application'


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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
```

perviewcache/urls.py
```python
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact/', views.contact),
]
```
enroll/templates/enroll/course.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Course 1</h1>
    <h1>Course 2</h1>
    <h1>Course 3</h1>
    <h1>Course 4</h1>
</body>
</html>
```

enroll/templates/enroll/contact.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Contact 1</h1>
    <h1>Contact 2</h1>
    <h1>Contact 3</h1>
    <h1>Contact 4</h1>
</body>
</html>
```

enroll/templates/enroll/views.py
```python
from django.shortcuts import render
from django.views.decorators.cache import cache_page # used to cache a view

# Create your views here.
@cache_page(60) # helps to cache this view within one minute you will get the same data fro 1 minute
def home(request):
    return render(request, 'enroll/course.html')

def contact(request):
    return render(request, 'enroll/contact.html')
```


Program number 2
```text
Rest of the code is similar to program number 1
you have to work only in views.py and urls.py
```

perviewcache/urls.py
```python
from django.contrib import admin
from django.urls import path
from enroll import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home),
    path('',cache_page(120)(views.home)),
    path('home/',views.home),
    path('contact/', views.contact),
]
```

enroll/templates/enroll/views.py
```python
from django.contrib import admin
from django.urls import path
from enroll import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home),
    path('',cache_page(120)(views.home)),
    path('home/',views.home),
    path('contact/', views.contact),
]
```
Where to find the full code
```text
check perviewcache
```


