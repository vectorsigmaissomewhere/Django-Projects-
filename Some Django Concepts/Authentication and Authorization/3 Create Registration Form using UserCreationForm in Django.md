## Create Registration Form using UserCreationForm in Django

User Authentication System
```text
Django comes with a user authentication system.
It handles user accounts, groups, permissions and 
cookie-based user sessions.

Django authentication provides both authentication and authorization together is generally 
referred to as the authentication system.

all configuration is included in settings.py by django-admin startproject
these consists of two items listed in your INSTALLED_APPS setting:
'django.contrib.auth' contains the core of the authentication framework and its default models
'django.contrib.contentypes' is the Django content type system, which allows permissions to be 
associated with models you create

MIDDLEWARE settings: we use these two middleware
SessionMiddleware manages sessions across requests.
AuthenticationMiddleware associated users with requests using sessions
```

django.contrib.auth models.py
```text
we know were django.contrib.auth is present 
models.py

class User:
User object is the core of authentication system
```

django.contrib.auth.forms.py
```text
we will use UserCreationForm to create forms which is present in forms.py present in auth 
also there is UserChangeForm to change the profile
check other class too
SetPasswordForm , a feature from which a user change the password, no need to enter the old password
PasswordChangeForm, enter your old password to change password
AdminPasswordChangeForm, admin change other user password
```

django.contrib.auth.admin.py
```text
GroupAdmin
UserAdmin
```

django.contrib.auth.urls.py
```text
hehe
```

django.contrib.auth.views.py
```text
hehe
```

User object Fields
```text
username - Usernames may contain alphanumeric,_,@, +,.and - characters. 
Its required and length is 150 characters or fewer

first_name  - This is optional (blank = True) and length is 30 characters of fewer
last_name - This is optional (blank = True) and length is 150 character or fewer
email - This is optional (blank = True)
password - Password is always stored in hashed.
group - Many-to-many relationship to Group
user_permissions - Many-to-many relationship to Permission
is_staff - Defines if the user can access the admin panel or not 
is_active - Always make this is_active to False or True and do not delete accounts , doing this 
helps not to break the foreign keys.
is_superuser - have all the permissions
last_login: A datetime of the user last login
date_joined: datetime of when the account was first created

is_authenticated - checks if the user is authenticated or not. always true, read_only
is_anonymous: way of differentiating User and Anonymous User objects. always false, read_only
get_username: returns the username for the user
get_full_name()
set_short_name(): returns the first name
set_password(raw_password) : hash the password.
check_password(raw_password) : check if the given password is correct or not for the user
set_unusable_password(): can be useful when authentication is made by external source such as an LDAP directory
has_usable_password(): 
get_user_permissions(obj=None) retunes the set of permissions
get_group_permissions(obj=None) returns the set of permissions
get_all_permissions(obj = None)
has_perm(perm, obj = None)
has_perm(perm_list, obj = None)
has_module_perms(package_name)
email_user(subject, message, form=None, **kwargs) : sends email to the user 
```

UserManager Methods
```text
The User model has a custom manager that has the following helper method
create_user(username, email = None, password = None, **extra_fields) - It creates, 
saves and returns an User.
The username and password are set as given. email is converted into lowercase adn 
the returned User object will have is_active set to True.

If no password is provided, set_unusable_password() will be called.
create_superuser(username, email = None, password=None, **extra_fields): creates superuser
with_perm(perm, i_active = True, superusers = True, backend = None, obj = None)
```

Group Object Fields
```text
name: 150 character or less
permissions - Many to many field to permissions
```

Permission Object FIleds
```text
name - It is required and length is 255 characters or fewer, Example: Can vote
content_type: 
codename: 100 characters or fewer, Example, can_vote
```

## Coding Part

settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!e4!u719+_($u7(gxt9o&2z5$b+#6^mb*n2(!p@51sj@=hz8xu'

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

ROOT_URLCONF = 'authenticationusercreationform.urls'

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

WSGI_APPLICATION = 'authenticationusercreationform.wsgi.application'


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

views.py
```python
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm # using UserCreationForm
# using my form withh more fields
from .forms import SignUpForm
from django.contrib import messages

# use this function view if you need only username and password
"""
def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm() # a blank form object
    return render(request, 'enroll/signup.html',{'form':fm}) # rendering the fm template in signup.html
"""

# use this function view if you want to use your forms 
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,"Account created successfully !!")
            fm.save()
            redirect('/signup/')
    else:
        fm = SignUpForm() # a blank form object
    return render(request, 'enroll/signup.html',{'form':fm}) # rendering the fm template in signup.html
```

forms.py
```python
# why to create forms.py because we need other fields like first name last name and email

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# extending the form 
class SignUpForm(UserCreationForm):
    # customize UserCreationForm label in this place
    # there are password1 and password2 in UserCreationForm 
    # Changing label of password2 
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'} # changing the label name 
```

signup.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<style>
    .success{
        color: red;
    }
</style>
<body>
    <form action="" method="POST" novalidate>
        {% csrf_token %}
        {% for fm in form %}
        {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }}<br><br>
        {% endfor %}
        <input type="submit" value="submit">
    </form>
    {% if messages %}
    {% for message in messages %}
    <small {% if message.tags %} class="{{ message.tags }}" {% endif %}>{{ message }}</small>
    {% endfor %}
    {% endif %}
</body>
</html>
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up),
]
```


