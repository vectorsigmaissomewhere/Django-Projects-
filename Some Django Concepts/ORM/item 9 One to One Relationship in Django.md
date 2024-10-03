## Model Relationship and One to One Relationship in Django

Model Relationship
```text
Django offers way to define the three most common types of database relationships
- One to One Relationship
- Many to One Relationship
- Many to Many Relationships
```

One to One Relationships
```text
When one row of table A can be linked to one row of table B.

To define a one-to-one relationship, use OneToOneField. You can it just
like any other Field type by including it as a class attribute of your model.   

OneToOneField requies a positional argument, the class to which the model is related

Syntax:- OneToOneField(to, on_delete, parent_link=False, **options)
Where, 
to - The class to which the model is related, 
on_delete - When an object referenced by a ForeignKey is deleted, Django will emulate the 
behavior of the SQL constraint specified by the on_delete arguement on_delete doesn't 
create an SQL constraint in the database.
parent_link - When True and used in a model which inherits from another concrete model, 
indicates that this field should be used as the link back to the parent class, rather 
than the extra OneToOneField which would normally be implicitly created by subclassing.

limit_choices_to - Sets a limit to the available choices for this field when this field
is rendered using a ModelForm or the admin (by default, all objects in the queryset ar
available to choose). Either a dictionary, a Q object, or a callable returning or Q 
object can be used.

related_name - The name to use for the relation from the related back to this one. It's also the 
default value for related_query_name(the name to use for the reverse filter name from the target model.)
If you'd prefer Django not to create a backwards relation, set related_name to '+' or end it with
'+'.

related_query_name - The name to use for the reverse filter name from the target model. If defaults
to value of related_name or default_related_name if set, otherwise it defaults to the name of the
model.

to_fiel - The field on the related object that the relation is to. By default, Django uses the primary
key of the related object. If you reference a difference field, that field must have unique=True.

swappable - Controls the migration framework's reaction if the ForeignKey is pointing at a 
swappable model. If it is True - the default - then if the ForeignKey is pointing at a model which
matches the current value of settings.AUTH_USER_MODEL(or another swappable model setting)
the relationship will be stored in the migration using a reference to the setting, not to the model
directly.

db_constraint - Controls whether or not a constraint should be created in the database for this 
foreign key. The default is True, and that's almost certainly what you want; setting this to False
can be very bad for data integrity. That said, here are some scenarios where you might want to do 
this:
You have legacy data that is not valid.
You're sharding your database.
If this is set to False, accessing a related object that doesn't exist will raise its DoesNotExist
exception.

on_delete - When an object referenced by a ForeignKey is deleted, Django will emulated the 
behavior of the SQL constraint specified by the on_delete argument, on_delete doesn't create 
an SQL constraint in the database.
The possible values for on_delete are found in django.db.models"
- CASCADE - Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CONSTRAINT
also deletes the object containing the ForeignKey.
- PROTECT - Prevent deletion of the referenced object by raising ProtectedError, a subclass of 
django.db.IntegrityError.
- SET_NULL - Set the ForeignKey null; this is only possible if null is True.
- SET_DEFAULT - Set the ForeignKey to its default value; a default for the ForeignKey must be set.
- SET() - Set the ForeignKey to the value passed to SET(), or if a callable is passed in, the result 
of calling it.
- DO_NOTHING - Take no action. If you database backend enforces referential integrity, this will cause
an IntegrityError unless you manually add an SQL ON DELETE constraint to the database field.
```

Example:- One to One Relation 
```python
class User(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    page_name = models.CharField(max_length-70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
```

onetoonerelationship/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8bipp66yatgwywa7o7x1=ng6nx@o&8t#ljwr&jd+cgl2f-j8su'

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
    'myapp',
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

ROOT_URLCONF = 'onetoonerelationship.urls'

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

WSGI_APPLICATION = 'onetoonerelationship.wsgi.application'


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

why init is because we have made added signals in app.py

myapp/init.py
```python
default_app_config = 'myapp.apps.MyappConfig'
```

myapp/admin.py
```python
from django.contrib import admin
from .models import Page, Like
# Register your models here.
admin.site.register(Page)
admin.site.register(Like)
```

myapp/apps.py
```python
from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals 
```

myapp/models.py
```python
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True) you can't delete user as it is protecting page
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to ={'is_staff':True}) # now no-one can add pages 
    """Till now who we delete user pages will also get deleted, but now 
    deleting user will delete the user too, Reverse Relation for that we are using signal"""
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


# example of model inheritance
class Like(Page):
    panna = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    likes = models.IntegerField()
```

myapp/signals.py
```python
from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

# when you delete page, user will get delete
# inorder to do this import signals in app.py
@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print("Page Post_Delete")
    instance.user.delete()
```




