## Create Registration Form using UserCreationForm in Django

What to expect in this file
```text
use UserCreationForm , extend UserCreationForm and make custom form
AuthenticationForm to register, login, logout
```

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
## Login

Function that you need to before doing login
authenticate() 
```text
authenticate(request = None, ** credentials) - verify credentials, 
It takes credentials as keywork arguments, username and password
 for the default case, checks them against each authentication 
backend, and returns a User object if the credentials are valid 
for a backend. 

If the credentials aren't valid for any backend or if a backend raises 
PermissionDenied, it returns None.

request is an optional HttpRequest which is passed on the authenticate()
method of the authentication backends.
Example:- 
user = authenticate(username ='ronaldo', password = 'lisbon')

After it is authenticated and we give them to login()
```

login()
```text
login(request, user, backend = None) - To log a user in, from a view, use login(). 
It takes an HttpRequest object and a User object login() saves the 
user's ID in the session, using Django's session framework.

When a user logs in, the user's ID and the backend that was used for 
authentication are saved in the user's session. This allows the same 
authentication backend to fetch the user's details on a future request.
```

We will use AuthenticationForm  in login form 

logout()
```text
logout(request) - To log out a user who has been logged in via 
django.contrib.auth.login(), use django.contrib.auth.logout() within your
view. It takes an HttpRequest object and has no return value.

When you call logout(), the session data for the current request is 
completely cleaned out. All existing data is removed. This is to prevent another
 person from using the same Web browser to log in and have access to the previous
 user's session data.
```

## 1 Using this program you can authenicate user, logout user and also change the password without old password or with old password

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
from django.shortcuts import render,redirect, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm # using UserCreationForm
# using my form with more fields
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm # pre-build form to change password with old password
from django.contrib.auth.forms import SetPasswordForm # password change form to change password without old password
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash # maintains session 


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

# use this function view if you want to use your forms.py to include more fields  
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


# making a login view function
def user_login(request):
    # if someone is already authenticated i don't need to login
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')
    

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# views to change password with old password 
def user_change_pass(request):
    # I don't want to see the change password template when user is logged out
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user) # session is not maintained and it is logging out so using this function
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')

# change password without old password
def user_change_pass1(request):
    # I don't want to see the change password template when user is logged out
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user) # session is not maintained and it is logging out so using this function
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')    
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
```

forms.py
```python
# why to create forms.py because we need other fields like first name last name and email

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm # use to display all the info of user 
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

    
# using UserChangeForm and show only the data that we need to show
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User # all the data coming from User model so using User here
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'} # changing the label name of email
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
        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p class="er">{{ error }}</p>
        {% endfor %}
        {% endif %}
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
    <a href="{% url 'login' %}">Login</a>
</body>
</html>
```

userlogin.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        .er{
            color: red;
        }
    </style>
</head>
<body>
    <form action="" method="POST" novalidate>
        {% csrf_token %}
        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p class="er">{{ error }}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }} <br><br>
        {% endfor %}
        <input type="submit" value="submit"> 
    </form>
    <a href="{% url 'signup' %}">Signup</a>
</body>
</html>
```
profile.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is Profile Page</h1>
    <h2>Welcome, {{ user.username }}</h2>
    {% if messages %}
    {% for message in messages %}
    <small {% if message.tags %} class="{{ message.tags }}" {% endif %}>{{ message }}</small>
    {% endfor %}
    {% endif %
    <a href="{% url 'changepass' %}">Change Password with old password</a><br> <!--Change password with old password-->
    <a href="{% url 'changepass1' %}">Change Password without old password</a> <!--Change password without old password-->
    <a href="{% url 'logout' %}">Logout</a>
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
    path('signup/', views.sign_up,name='signup'), # the third url means when other url wants to open the signup it need signup
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile, name='profile'),
    path('logout/',views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'), # link to change password with old password
    path('changepass1/', views.user_change_pass1, name='changepass1') # link to change password without old password
]
```

changepass.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
</head>
<body>
    <h1>Change Password with old password</h1>
    <!--novalidate lauda tyo khali jada fill garr vnne message dekhaudaina-->
    <form action="" method="POST" novalidate>
        {% csrf_token %}
        {% csrf_token %}
        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p class="er">{{ error }}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }}<br><br>
        {% endfor %}
        <input type="submit" value="Save">
    </form>
    <a href="{% url 'profile' %}">Profile</a>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

changepass1.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Password</title>
</head>
<body>
    <h1>Change password without old password</h1>
    <!--novalidate lauda tyo khali jada fill garr vnne message dekhaudaina-->
    <form action="" method="POST" novalidate>
        {% csrf_token %}
        {% csrf_token %}
        {% if form.non_field_errors %}
        {% for error in form.non_field_errors %}
        <p class="er">{{ error }}</p>
        {% endfor %}
        {% endif %}
        {% for fm in form %}
        {{ fm.label_tag }} {{ fm }} {{ fm.errors|striptags }}<br><br>
        {% endfor %}
        <input type="submit" value="Save">
    </form>
    <a href="{% url 'profile' %}">Profile</a>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

