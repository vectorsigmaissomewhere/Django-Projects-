## Signals
```text
The signals are utilities that allow us to associate events with 
actions. 
Signals allow certain senders to notify a set of receivers that 
some action has taken place.
- Login and Logout Signals
- Model Signals
- Management Signals
- Request/Response Signals
- Test Signals
- Database Wrappers
```

Three major part of signals 
```text
Sender - Who will send Signal
Signal - Signal
Receiver - Who will receive Signal
```

Functions
```text
Receiver Function - This function takes a sender argument, along
with wildcard keyword arguments (**kwargs); all signal handlers
must take these arguments. A receiver can be any Python
function or method.
for Example:
def receiver_func(sender, request, user, **kwargs):
    pass

Connecting/Registering Receiver Function - There are two ways 
you can connect a receiver to a signal:-
- Manual Connect Route
- Decorator

Manual Connect Route - To receive a signal , register a receiver 
function using the Signal.connect() method. The receiver 
function is called when the signal is sent. All of the signal's 
receiver functions are called one at a time, in the order they
were registered.

Signal.connect(receiver_func, sender=None, weak=True, dispatch_uid=None)
Where, 
receiver_func - The callback function which will be connected
      to signal.
signal - Specifies a particular sender to receiver signals from.
weak - Django stores signal handlers as weak references by 
    default. This if your receiver is a local function, it may be 
    garbage collected. To prevent this, pass weak = False when 
    you call the signal's connect() method.
dispatch_uid - A unique identifier for a signal receiver in cases 
    where duplicate signals may be sent.
Decorator - @receiver(signal or list of signal, sender)
```

Built-in Signals
```text
Django provides a set of built-in signals that let user code get 
notified by Django itself of certain actions. 

Login and Logout Signals - The auth framework uses the following
    signals that can be used for notification when a user logs in or
    out.
django.contrib.auth.signals- 
    user_logged_in(sender, request, user) - Sent when a user logs
           in successfully.
    	sender - The class of the user that just logged in.
	request - The current HttpRequest instance.
	user - The user instance that just logged in.
     user_logged_out(sender, request, user) - Sent when the 
          logout method is called.
                  sender - The class of the user that just logged out or 
                     None if the user was not authenticated.
                   request - The current HttpRequest instance.
                   user - The user instance that just logged out or None
                         if the user was not authenticated.
     user_login_failed(sender, credentials, request) - 
                   Sent when the user failed to login successfully
                    sender - The name of the module used for authentication.
                    credentials - A dictionary of keyword arguments 
                         containing the user credentials that were passed
                         to authenticate() or your own custom 
                         authentication backend. Credentials matching a
                         set of 'sensitive' patterns, (including password) will
                         not be sent in the clear as part of signals.
                    request - The HttpRequest object, if one was 
                         provided to authenticate()
```

More about signals
Model Signals
```text
Model signals - A set of signals sent by the model system
django.db.models.signals
pre_init(sender, args, kwargs) - Whenever you instantiate a 
Django model, this signal is sent at the beginning of the model's
__init__() method.
sender - The model class that just had an instance created.
args - A list of positional arguments passed to __init__().
kwargs - A dictionary of keyword arguments passed to __init__().

post_init(sender, instance) - Like pre_init, but this one is sent 
when the __init__() method finishes.
sender - The model class that just had an instance created.
instance - The actual instance of the model that's just been 
created.

pre_save(sender, instance, raw, using, update_fields) - This is 
sent at the beginning of a model's save() method.
sender - The model class.
instance - The actual instance being saved.
raw - A boolean; True if the model is saved exactly  as presented
(i.e. when loading a fixture). One should not query/modify other
records in the database as the database might not be in a 
consistent state yet.
using - The database alias being used.
update_fields - The set of fields to update as passed to 
Model.save(), or None if update_fields wasn't passed to save().

post_save(sender, instance, created, raw, using, update_fields) - Like pre_save, but
sent at the end of the save() method.
sender - The model class.
instance - The actual instance being saved.
created - A boolean; True if a new record was created.
raw - A boolean; True if the model is saved exactly as presented(i.e. when loading 
a fixture). One should not query/modify other records in the database as the 
database might not be in a consistent state yet.
using  - The database alias being used.
update_fields - The set of fields to update as passed to Model.save(), one None if 
update_fields wasn't passed to save().
pre_delete(sender, instance, using) - Sent at the beginning of a model's delete() 
method and a queryset's delete() method.
sender - The model class
instance - The actual instance being deleted 
using - The database alias being used

post_delete(sender, instance, using) - Like pre_delete, but sent at the end of a
model's delete() method and a queryset's delete() method.
sender - The model class.
instance - The actual instance being deleted.
Note that the object will no longer be in the database, so be very careful what you 
do with this instance. 
using  - The database alias being used.

m2m_changed(sender, instance, action, reverse, model_pk_set, using) - Sent when
a ManyToManyField is changed on a model instance. Strictly speaking, this is not
a model signal since it is sent to the ManyToManyField, but since it complements 
the pre_save/post_save and pre_delete/post_delete when it comes to tracking 
changes to models, it is included here.

class_prepared(sender) - Sent whenever a model class has been "prepared" - that
is, once model has been defined and registered with Django's model system. 
Django uses this signal internally; it's not generally used in third-party applications.

Since this signal is sent during the app registry population process, and 
AppConfig.ready() runs after the app registry us fully populated, receivers cannot
be connected in that method. One possibility is to connect them
AppConfig.__init__() instead, taking care not to import models or trigger calls to 
the app registry.
sender - The model class which was just prepared.
```

Request/Response Signal
```text
Request/Response Signals - Signals sent by the core framework when processing a 
request.
django.core.signals
request_started(sender, environ) - Sent when Django begins processing an HTTP 
request.
sender - The handler class - e.g. django.core.handlers.wsgi.WsgiHandler - that 
handled the request
environ - The environ dictionary provided to the request

request_finished(sender) - Sent when Django finishes delivering an HTTP response 
to the client. 
sender - The handler class.
got_request_exception(sender, request) - This signal is sent whenever Django 
encounters an exception while processing an incoming HTTP request.
sender - Unused (always None).
request - The HttpRequest object.
```

Management Signals
```text
Management signals - Signals sent by Django-admin
django.db.models.signals
pre_migrate(sender, app_config, verbosity, interactive, using, plan, apps) - Sent by
the migrate command before it starts to install an application. It's not emitted
for applications that lacks a models module.
sender - An AppConfig instance for the application about to be migrated/synced.
app_config - Same as sender
verbosity - Indicates how much information manage.py is printing on screen.
Functions which listen for pre_migrate should adjust what they output to the 
screen based on the value of this argument.
interactive - If interactive is True, it's safe to prompt the user to input things on the
command line. If interactive is False, functions which listen for this signal should
not try to prompt for anything.
For example, the django.contrib.auth app only prompts to create a superuser 
when interactive is True.
using - The alias of database on which a command will operate.
plan - The migration plan that is going to be used for the migration run. While the 
plan is not public API, this allows for the rare cases when it is necessary to know the
plan. A plan is  a list of two-tuples with the first item being the instance of a 
migration class and the second item showing if the migration was rolled back(True)
or applied(False).
apps - An instance of Apps containing the state of the project before the migration
run. It should be used instead of the global apps registry to retrieve the models 
you want to perform operations on.

post_migrate(sender, app_config, verbosity, interactive, using, plan, apps) - Sent at 
the end of the migrate(even if no migrations are run) and flush command. It's not 
emitted for applications that lack a models module.

Handlers of this signal must not perform database scheme alternations as doing so
may cause the flush command to fail if it runs during the migrate command.

sender - An App Config instance for the application that was just installed.
app_config - Same as sender.
verbosity - Indicates how much information manage.py is printing on screen.
Functions which listen for post_migrate should adjust what they output to the 
screen based on the value of this argument.
interactive - If interactive is True, it's safe to prompt the user to input things on the
command line. If interactive is False, functions which listen for this signal should
not try to prompt for anything.

For example, the django.contrib.auth app only prompts to create a superuser
when interactive is True.

using - The database alias used for synchronization. Defaults to the default database.
plan - The migration plan that was used for the migration run. While the plan is not 
public API, this allows for the rare cases when it is necessary to know the plan. A 
plan is a list of two-tuples with the first item being the instance of  a  migration 
class and the second item showing if the migration was rolled back(True) or 
applied(False).
apps - An instance of Apps containing the state of the project after the migration 
run . It should be used instead of the global apps registry to retrieve the models
you want to perform operations on.
```

Test Signals
```text
Signals only sent when running tests.
django.test.signals
setting_changed(sender, setting, value, enter) - This signal is sent when the value of
a setting is changed through the django.test.TestCase.settings() context manager 
or the 
django.test.override_settings() decorator/context manager.

It's actually sent twice: when the new value is applied("setup") and when the 
original value is restored("teardown"). Use the enter argument to distinguish 
between the two.

You can also import this signal from django.core.signals to avoid importing from 
django.test in non-test situations

sender - The settings handler.
setting - The name of the setting.
value - The value of the setting after the change. For settings that initially don't 
exist, in the "teardown" phase, value is None.
enter - A boolean; True if the setting is applied, False if restored.
```

Database Wrappers
```text
Database Wrappers - Signals sent by the database wrapper when a database connection is initiated
django.db.backends.signals
connection_created - Sent when the database wrapper makes the initial
connection to the database. This is particularly useful if you'd like to send any post
connection commands to the SQL backend.
sender - The database wrapper class -
 i.e. django.db.backends.postgresql.DatabaseWrapper or 
django.db.backends.mysql.DatabaseWrapper, etc

connection - The database connection that was opened. This can be used in a 
multiple-database configuration to differentiate connection signals from 
different databases.
```

builtinsignals/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+-%*(0-#teox$jf*gakk75%me^&cr-1#fxg_15(+8v!ihkqc36'

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
    # blog.apps.BlogConfig, instead of writing blog you can write this 
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

ROOT_URLCONF = 'builtinsignals.urls'

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

WSGI_APPLICATION = 'builtinsignals.wsgi.application'


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

builtinsignals/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
]
```

blog/apps.py
```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        import blog.signals
```

blog/signals.py
```python
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# Without decorator login 
"""
def login_success(sender,request,user, **kwargs):
    print("------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print("User Password:", user.password) 
    print(f'Kwargs:, {kwargs}')

user_logged_in.connect(login_success, sender=User)
"""

# With decorator login
@receiver(user_logged_in, sender=User)
def login_success(sender,request,user, **kwargs):
    print("------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print("User Password:", user.password) 
    print(f'Kwargs:, {kwargs}')

user_logged_in.connect(login_success, sender=User)

# with decorator logged out
@receiver(user_logged_out, sender=User)
def log_out(sender,request,user, **kwargs):
    print("------------------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs:, {kwargs}')

# user_logged_out.connect(log_out, sender=User)

# User login failed
@receiver(user_login_failed)
def log_out(sender,credentials, request, **kwargs):
    print("------------------------")
    print("Login Failed Signal...")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f'Kwargs:, {kwargs}')

# user_logged_out.connect(log_out, sender=User)

# Pre Save
# trigger this method when user is save I guess

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("------------------------")
    print("Pre Save Signal...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs:, {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)

# post save
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("------------------------")
        print("Post Save Signal...")
        print("New Record")
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'Kwargs: {kwargs}')
    else:
        print("-------------------------")
        print("Post Save Signal...")
        print("Update")
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'kwargs: {kwargs}')
# post_save.connect(at_beginning_save, sender=User)

# pre delete
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("--------------------------")
    print("Pre Delete Signal....")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f"kwargs: {kwargs}")
# pre_delete.connect(at_beginning_delete, sender=User)

# post delete
@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("----------------------------------")
    print("Post Delete Signal.......")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f"kwargs: {kwargs}")
# post_delete.connect(at_ending_delete, sender=User)

# pre init
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("----------------------------------")
    print("Pre Init Signal.....")
    print("Sender:", sender)
    print(f"Args: {args}")
    print(f"kwargs: {kwargs}")
# pre_init.connect(at_beginning_init, sender=User)

# post init
@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("----------------------------")
    print("Post Init Signal.....")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')
# post_init.connect(at_beginning_init, sender=User)

# At beginning Request
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("-----------------------------------")
    print("At Beginning Request.....")
    print("Sender:", sender)
    print("Environ:", environ)
    print(f"kwargs: {kwargs}")
# request_started.connect(at_beginning_request)

# At Ending Request 
@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("-----------------------------")
    print("At Ending Request..........")
    print("Sender:", sender)
    print(f"kwargs: {kwargs}")
# request_finished.connect(at_ending_request)

# At exception
@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("------------------------------------")
    print("At Request Exception......")
    print("Sender: ", sender)
    print("Request:", request)
    print(f"Kwargs: {kwargs}")
# got_request_exception.connect(at_req_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("---------------------------------")
    print("before_install_app......")
    print("Sender:", sender)
    print("App_config:", app_config)
    print("Verbosity:", verbosity)
    print("Interactive:", interactive)
    print("Using:", using)
# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------")
    print("at_end_migrate_flush....")
    print("Sender:", sender)
    print("App_config:", app_config)
    print("Verbosity:", verbosity)
    print("Interactive:", interactive)
    print("Using:", using)
    print("Plan:", plan)
    print("App:", apps)
    print(f"Kwargs: {kwargs}")
# post_migrate.connect(at_end_migrate_flush)

# every database connection initiated(called)
@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("--------------------------")
    print("Initial connection to the database...")
    print("Sender:", sender)
    print("Connection:", connection)
    print(f"kwargs: {kwargs}")
# connection_created.connect(conn_db)
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse
# for generating exception
def home(request):
    a = 10/0
    return HttpResponse("Hello")
```

Where to find the full code
```text
check builtinsignals
```



