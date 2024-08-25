File Based Session
```text
In this section the session will get saved in a file
```

settings.py
```python
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4e%*gq-g=+#nfz7oy6o+j54^)%+b+cazj8%y(x2l1ll@ix7*px'

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

ROOT_URLCONF = 'fileBassedSession.urls'

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

WSGI_APPLICATION = 'fileBassedSession.wsgi.application'


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


SESSION_ENGINE = 'django.contrib.sessions.backends.file' # now file will save in file
SESSION_FILE_PATH = os.path.join(BASE_DIR, 'session') # path where session will get saved
```

urls.py
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

You have to create a folder name session

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
    {{name}} <br>
    {{ request.session.get_session_cookie_age }} seconds <br>
    {{ request.session.get_expiry_age }} seconds <br>
    {{ request.session.get_expiry_date }} <br>
    {{ request.session.get_expiry_at_browser_close }} <br>
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

views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600) # expiry date set for 30 seconds
    # request.session.set_expiry(0) # expires when the browser is closed 
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() # remove the session from the database
    return render(request, 'student/delsession.html')
```

Where to find the full code
```text
check fileBassedSession folder 
```



