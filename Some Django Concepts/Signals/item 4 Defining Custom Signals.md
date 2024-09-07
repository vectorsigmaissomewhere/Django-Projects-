Defining Custom Signals
```text
All signals are django.dispatch.Signal instances.
class Signal(providing_args=list)

The providing_args is a list of the names of arguments the signal will 
provide to listeners. This is purely documentational, however, as there 
is nothing that checks that the signal actually provides these 
arguments to its listeners.

You're allowed to change this list of arguments at any time.
```

Sending signals
```text
There are two ways to send signals in Django.
- Signal.send(sender, **kwargs) - This is used to send a signal, all built-in
signals use this to send signals. You must provide the sender argument
which is a class most of the time any may provide as many other
keyword arguments as you like. It returns a list of tuple pairs
[(receiver, response), ...], representing the list of called receiver 
functions and their response values.

- Signal.send_robust(sender, **kwargs) - This is used to send a signal. You must provide the sender argument which is a class
most of the time and may provide as many other keyword 
arguments as you like. It returns a list of tuple pairs 
[(receiver, response), ... ], representing the list of called receiver
functios and their response values.  
```

Difference between send() and send_robust()
```text
- send() does not catch any expections raised by receivers; it 
simply allows errors to propagate. Thus not all receivers may 
be notified of a signal in the face of an error.
- send_robust() caches all errors derived from Python's 
Exception class, and ensures all receivers are notified of the
signal. If error occurs, the error instance is returned in the tuple
pair for the receiver that raised the error.
```

Disconnecting Signals
```text
Signal.disconnect(receiver=None, sender=None, dispatch_uid=None) 
This is used to disconnect a receiver from a signal. The arguments
are as described in Signal.connect(). The method returns True if a
receiver was disconnected and False if not.
```

blog/signals.py
```python
from django.dispatch import Signal, receiver

# Creating Signals
notification = Signal()

# Receiver Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse
from blog import signals

def home(request):
    signals.notification.send(sender=None, request=request, user=['Albert', 'Einstein'])
    return HttpResponse("This is Home Page")
```

customsignal/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%ockw3wl)nbw)7e0dhm^y0k703t%tvx0nrz)t)x)m1rhr&g-!d'

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
    'blog',
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

ROOT_URLCONF = 'customsignal.urls'

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

WSGI_APPLICATION = 'customsignal.wsgi.application'


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

customsignal/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```
