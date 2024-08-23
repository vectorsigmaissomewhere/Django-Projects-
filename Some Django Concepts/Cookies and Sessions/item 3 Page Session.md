## Page Session

```text
In this section we have worked on
settings.py
In settings.py, we have added 20 seconds for page session
After 20 seconds the page session is expired
request.session.modified = True
What this is going to do is,


```

settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ezg4u80dyw!*7h)(^0s_v&ch=h5r(80r0=x0x%0rfxq_9(h@za'

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

ROOT_URLCONF = 'pagesession.urls'

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

WSGI_APPLICATION = 'pagesession.wsgi.application'


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

SESSION_COOKIE_AGE = 20 # 20 seconds
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
from django.shortcuts import render, HttpResponse

def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request, 'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True # every time your get session, your session will reset to 20 seconds 
        return render(request, 'student/getsession.html', {'name': name})
    else:
        return HttpResponse("Your session has Expired...")

def delsession(request):
    request.session.flush()
    request.session.clear_expired() # remove the session from the database
    return render(request, 'student/delsession.html')
```

