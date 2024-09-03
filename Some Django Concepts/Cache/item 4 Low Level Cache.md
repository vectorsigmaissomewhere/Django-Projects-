## Low Level Cache API
```text
Sometimes, caching an entire rendered page doesn't gain you 
very much and is, in fact, inconvenient overkill.
Perhaps, for instance, your site includes a view whose results 
depend on several expensive queries, the results of which 
change at different intervals. In this case, it would not be ideal
to use the full-page caching that the per-site or per-view cache
strategies offer, because you wouldn't want to cache the entire
result(since some of the data changes often), but you'd still
want to cache the results that rarely change.

For cases like this, Django exposes a low-level cache API. You can 
use this API to store objects in the cache with any level of 
granularity you like. You can cache any Python object that can be 
picked safely: strings, dictionaries, lists of model objects, and so
forth

django.core.cache.cache
```

How to use to Low Level Cache API 
```text
from django.core.cache import cache

cache.set(key, value, timeout=DEFAULT_TIMEOUT, version=None) - This method is used to set cache,
Where,
key - It should be str.
value - It can be any pickelable Python object
timeout - It is number of seconds the value should be stored in
the cache. Timeout of None will cache the value forever. A 
timeout of 0 won't cache the value.
version - It is an int. You can set cache with same key but 
different version.

cache.get(key, default=None, version=None) - This method is 
used to get cache. If the key doesn't exists in the cache, it 
returns None.
Where, 
default - This specifies which value to return if the object doesn't
exist in the cache.


cache.add(key, value, timeout=DEFAULT_TIMEOUT, version=None) 
- This method is used to add a key only if it doesn't already exist.
It takes the same parameters as set(), but it will not attempt to 
update the cache if the key specified is already present. If you
need to know whether add() stored a value in the cache, you
can check the return value. It will return True if the value was
stored, False otherwise.

cache.get_or_set(key, default, timeout=DEFAULT_TIMEOUT, version=None) 
- This method is used to get a key's value or set a value if the key
isn't in the cache. It takes the same parameters as get() but
the default is set as the new cache for the key, rather than
returned. You can also pass any callable as default value.

cache.set_many(dict, timeout) - This method is used to set multiple values more efficiently, use set_many() to pass a 
dictionary of key-value pairs.

cache.get_many(keys, version=None) - There's also a 
get_many() interface that only hits the cache once. get_many() 
returns a dictionary with all the keys you asked for that actually
exist in the cache (and haven't expired).

cache.delete(key, version=None) - This method is used to delete
keys explicitly to clear the cache for a particular object.

cache.delete_many(keys, version=None) - This method is used to
clear a bunch of keys at once. It can take a list of keys to be 
cleared.

cache.clear() - This method is used to delete all the keys in the
cache. Be careful with this; clear() will remove everything from 
the cache, not just the keys set by your application.

cache.touch(key, timeout=DEFAULT_TIMEOUT, version=None)
- This method is used to set a new expiration for a key. touch()
returns True if the key was successfully touched, False 
otherwise.

cache.incr(key, delta=1, version=None)
cache.decr(key, delta=1, version=None)

cache.close() - You can close the connection to your cache with
close() if implemented by the cache backend.
```

lowlevelcacheapi/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@h7o@^*$5&r@1ksk$n2ymuz@6f$t$hzo8^^$wryq_v^($k@1*e'

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

ROOT_URLCONF = 'lowlevelcacheapi.urls'

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

WSGI_APPLICATION = 'lowlevelcacheapi.wsgi.application'


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

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'enroll_cache',
    }
}
```

lowlevelcacheapi/urls.py
```python
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
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
    <h2>{{fm}}</h2>
    <h2>{{stu.name}}</h2>
    <h2>{{stu.roll}}</h2>
</body>
</html>
```

enroll/views.py
```python
from django.shortcuts import render
from django.core.cache import cache

# Long code
"""
def home(request):
    mv = cache.get('movie','has_expired') # if there is any value in movie then returns movie value else returns has_expired
    if mv == 'has_expired':
        cache.set('movie','The Manjhi', 30)
        mv = cache.get('movie')
    return render(request, 'enroll/course.html', {'fm':mv})
"""

# Short code
"""
def home(request):
    mv = cache.get_or_set('movie',2000,30, version=2)
    return render(request, 'enroll/course.html',{'fm':mv})
"""

# Set key
"""
def home(request):
    data = {'name':'Sonam', 'roll':101}
    cache.set_many(data,30)
    sv = cache.get_many(data)
    print(sv)
    return render(request, 'enroll/course.html', {'stu':sv})
"""
    
# Delete Key
"""
def home(request):
    cache.delete('roll') # check the database to see the key
    cache.delete('fees', version=2) 
    return render(request, 'enroll/course.html')
"""

# incrementing decrementing keys
def home(request):
    #cache.set('roll', 101, 600)
    #rv = cache.get('roll')
    #print(rv)
    dv = cache.decr('roll',delta=1)
    # dv = cache.incr('roll', delta = 3)
    print(dv)
    return render(request, 'enroll/course.html')

# delete all the keys
"""
def home(request):
    cache.clear()
    return render(request, 'enroll/course.html')
"""
```

Where to find the full code
```text
check lowlevelcacheapi
```

