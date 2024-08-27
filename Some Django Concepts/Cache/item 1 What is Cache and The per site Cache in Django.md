Cache

What is Cache?
```text
A Cache, is an information technology for the termporary storage(caching) 
of Web documents, such as Web pages, images, and other types of Web 
multimedia, to reduce server lag.

Caching is one of those methods which a website implements to become 
faster. It is cost efficient and saves CPU processing time.

Django comes with a robust system that lets you save dynamic pages so 
they don't have to be calculated for each request.
```

What you can cache in Django?
```text
You can cache the output of specific views, you can cache only the pieces 
that are difficult to produce, or you can cache your entire site.
```

Following are the options of caching:-
```text
- Database Caching
- File System Caching
- Local Memory Caching
```

How Cache Works
```text
First condition, 
Imagine you have a single web page
WebPage -------------> Cache(Server checks if there is webpage in the cache)
If there is cache then it send the web page

Second condition,
Image you have a single web page
WebPage----------> Cache(Here there is no webpage in the cache)
In this case WebPage is generated and the generated page is saved in the cache 
So that next time it can response page faster 
```

How to implement Caching
```text
- The per-site cache- Once the cache is set up, the simplest way to use caching
is to cache your entire site.
- The per-view cache- A more ganular way to use the caching framework is by caching 
the output of individual views.
- Template fragement caching - This gives you more control what to cache.
```

The per-site cache
```text 
The per-site cache - Once the cache is set up, the simplest way to use caching is to 
cache your entire site.
For doing this, 
This middleware should be in order 
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    ]

CACHE_MIDDLEWARE_ALIAS - The cache alias to use for storage
CACHE_MIDDLEWARE_SECONDS - The number of seconds each page should be cached.
CACHE_MIDDLEWARE_KEY_PREFIX - If the cache is shared across multiple sites using the 
same Django installation, set this to the name of the site, or some other string that is 
unique to this Django instance, to prevent key collisions. Use an empty string if you 
don't care.
```

Database Caching
```text
Django can store its cached data in your database. This works best if you've got a fast, 
well-indexed database server.

CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table', # name of the database table
    }
}

Before using the database cache, you must create the cache table with this command:
python manage.py createcachetable

This creates a table in your database that is in the proper format that Django's 
database-cache system expects.
The name of the table is taken from LOCATION.

If you are using multiple database caches, createcachetable creates one table for 
each cache.
```

Cache Arguments
```text
Each cache backend can be given additional arguments to control caching behavior.

TIMEOUT: The default timeout, in seconds, to use for the cache. This argument
defaults to 300 seconds (5 minutes). You can set TIMEOUT to None so that, by 
default, cache keys never expire. A value of 0 causes keys to immediately
expire(effictively "don't cache").

OPTIONS: Any options that should be passed to the cache backend. The list of valid 
options will vary with each backend, and cache backends backed by a third-party
library will pass their options directly to the underlying cache library.

Cache backends that implement their own culling strategy(i.e., the locmen, filesystem 
and database backends) will honor the following options: 

MAX_ENTRIES: The maximum number of entries allowed in the cache before old values
are deleted. This argument defaults to 300.


CULL_FREQUENCY: The fraction of entries that are culled when MAX_ENTRIES is reached.
The actual ratio is 1/ CULL_FREQUENCY, so set CULL_FREQUENCY to 2 to cull half the entries 
when MAX_ENTRIES is reached. This argument should be an integer and defauls to 3.

A value of 0 for CULL_FREQUENCY means that the entire cache will be dumpled when 
MAX_ENTRIES is reached. On some bckends (database in particular) this makes culling 
much faster at the expenses of more cache misses.
```
Example of Cache Arguments
```text
CACHES = { 
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache'
       'LOCATION':'enroll_cache',
       'TIMEOUT':60,
       'OPTIONS':{
            'MAX_ENTRIES':1000
            }
       }
    }
```


Program number 1
```text
After 30 seconds you will get new data 
for 30 seconds you will get the same data
```

persitecache/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2-hngc#)lc55(tmg+&i6ce%_*@pqnv73@xcqb6+d_ndrhxw(b8'

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
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'persitecache.urls'

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

WSGI_APPLICATION = 'persitecache.wsgi.application'


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
CACHE_MIDDLEWARE_SECONDS = 30
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'enroll_cache', # name of the database table
    }
}
```

persitecache/urls.py
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
</body>
</html>
```

enroll/views.py
```python
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/course.html')
```

File Based Cache 
```text
Rest of the code is same as program number 1
only make changes in settings.py and add a folder named cache where we will
store cache
```
```text
The file-based backend serializes and stores each cache value 
as a separate file
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/Users/ADMIN/Desktop/Med/persitecache',
        }
    }

Make sure the directory pointed-to by this setting exists and is 
readable and writable by the system user under which your 
Web server runs
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION":/var/tmp/django_cache',
        }
   }
```
persitecache/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2-hngc#)lc55(tmg+&i6ce%_*@pqnv73@xcqb6+d_ndrhxw(b8'

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
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'persitecache.urls'

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

WSGI_APPLICATION = 'persitecache.wsgi.application'


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
CACHE_MIDDLEWARE_SECONDS = 30
"""
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'enroll_cache', # name of the database table
    }
}
"""

# File based caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/Users/ADMIN/Desktop/Med/persitecache/cache',
    }
}
```


Where to find the full code 
```text
check persitecache folder to get the full code
```

Local Memory Caching

Program number 3
```text
This is the default cache if another is not specified in your 
settings file. This cache is per-process and thread-safe.

Each process will have its own private cache instance, which 
means no cross-process caching is possible. This obviously also
means the local memory cache isn't particularly 
memory-efficient.

It's probably not a good choice for production environments.
It's nice for development.
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.locmen.LocMemCache',
        'LOCATION':'unique-snowflake', # The cache Location is used to identify individual memory stores.
        }
    }
```

```text
You need to make changes in settings.py only rest of the code is similar to program number 1
```
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2-hngc#)lc55(tmg+&i6ce%_*@pqnv73@xcqb6+d_ndrhxw(b8'

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
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'persitecache.urls'

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

WSGI_APPLICATION = 'persitecache.wsgi.application'


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
CACHE_MIDDLEWARE_SECONDS = 30
# Per site Cache
"""
CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'enroll_cache', # name of the database table
    }
}
"""

# File based caching
"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/Users/ADMIN/Desktop/Med/persitecache/cache',
    }
}
"""

# Local Memory Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake', # The cache Location is used to identify individual memory stores.
    }
}

```



