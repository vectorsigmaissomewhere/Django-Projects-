## Class Based View with login required and staff member required Decorators in Django 

login_required Decorator
```text
login_required(redirect_field='next', login_url=None)
If the user is logged in, execute the view normally. The view code is free to assume 
the user is logged in.
If the user isn't logged in, redirect to settings.LOGIN_URL, passing the current absolute 
path in the query string. Example: /accounts/login/?next=/accounts/profile/
django.contrib.auth.decorators.login_required

Where, 
redirect_field_name - If you would prefer to use  a different name for this parameter, 
login_required() takes an optional redirect_field_name parameter. If you provide a value
to redirect_field_name, you will most likely need to customize your login template as well, 
since the template context variable which stores the redirect path will use the value of 
redirect field_name as its key rather than "next" (the default).

login_url - If you don't specify the login_url parameter, you'll need to ensure that the 
settings.LOGIN_URL and your login view are properly associated.
```

staff_member_required decorator
```text
staff_member_required(redirect_field_name='next', login_url='admin:login')
This decorator is used on the admin views that require authorization. A view decorated 
with this function will having the following behavior.
- If the user is logged in, is a staff member(User.is_staff=True), and 
is active(User.is_active=True), execute the view normally.
- Otherwise, the request will be redirected to the URL specified by the login_url 
parameter, with the originally requested path in a query string variable specified by 
redirect_field_name.
For example: /admin/login/?next=/profile/
```

permission_required Decorator
```text
permission_required(perm, login_ur=None, raise_exception=False)

It's a relatively common task to check whether a user has a particular permission. For that 
reason, Django provides a shortcut for those case: the permission_requireed() decorator.

Just like the has_perm() method, permission names take the form 
"<app label>.<permission codename>"
```

Decorating Class-Based View
```text
Decorating in urls.py or URLconf
The simplest way of decorating class-based views is to decorate the result of the 
as_view() method. The easiest place to do this is in the URLconf where you deploy 
your view:
from django.urls import path
from django.views.generic import TemplateView 
from registration.views.import ProfileTemplateView 
from django.contrib.auth.decorators import login_required 
urlpatterns = [
    path('dashboard/', login_required(TemplateView.as_view(template_name='bash/dash.html')), name='dash'),
    path('profile/', login_required(ProfileTemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    path('blogpost/', permission_required('blog.can_add')(BlogPostView.as_view())),
]
```

method_decorator
```text
The method_decorator decorator transforms a function decorator into a method decorator so 
that is can be used on an instance method.

A methon on a class isn't quite the same as a standalone function, so you can't just apply 
a function decortaor to the method you need to transform it into a method decorator first.

@method_decorator(*args, **kwargs)
```

Decorating in the Class
```text
To decorate every instance of a class-based view, you need to decorate the class 
definition itself. To do this you apply the decorator to the dispatch() method of the 
class.

from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

You can decorate the class instead and pass the name of the method to be decorated as the 
keyword argument name:

@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

If you have a set of common decorators used in several places, you can define a list 
or tuple of decorators and use this instead of invoking method_decorator() multiple times.
@method_decorator(never_cache, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

decorators = [never_cache, login_required]
@method_decorator(decorators, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

The decorators will process a request in the order they are passed to the decorator.
In the example, never_cache() will process the request before login_required().
```


## Coding Part

classbasedviewlogindecorators/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+cds*hn*^osqpd_b6b1l$djf)^=50e*h1#3i)bg-c$%ckkur&e'

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
    'registration'
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

ROOT_URLCONF = 'classbasedviewlogindecorators.urls'

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

WSGI_APPLICATION = 'classbasedviewlogindecorators.wsgi.application'


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

classbasedviewlogindecorators/urls.py
```python
from django.contrib import admin
from django.urls import path, include 
from registration import views
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('about/', login_required(views.AboutTemplateView.as_view()), name='about'),
    # path('about/', staff_member_required(views.AboutTemplateView.as_view()), name='about'),
    # login_required in views
    path('classabout/', views.AboutClassTemplateView.as_view(), name='classabout'),
    # item 3 
    path('classdecabout/', views.AboutClassDecTemplateView.as_view(), name='classdecabout'),
]
```

registration/templates/registration/about.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>I am about Page</h1>
</body>
</html>
```

registration/templates/registration/login.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Login">
        <a href="{% url 'password_reset' %}">Reset Password</a>
    </form>
</body>
</html>
```

registration/templates/registration/profile.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is profile page</h1>
    <a href="{% url 'logout' %}">Logout Button</a>
    <a href="{% url 'password_change' %}">Change Password</a>
</body>
</html>
```

registration/urls.py
```python
from django.urls import path, include 
from registration import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # item 1
    path('profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
    # item 2
    path('classprofile/', views.ProfileClassTemplateView.as_view(), name='classprofile'),
    # item 3 
    path('classdecprofile/', views.ProfileClassDecTemplateView.as_view(), name='classdecprofile'),
]
```

registration/views.py
```python
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# for views 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

"""
item 1:
login required decorators in  urls 
"""
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

class AboutTemplateView(TemplateView):
    template_name = 'registration/about.html'

"""
item 2:
login required decorators not in urls 
"""


class ProfileClassTemplateView(TemplateView):
    template_name = 'registration/profile.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class AboutClassTemplateView(TemplateView):
    template_name = 'registration/about.html'
    @method_decorator(login_required)
    # @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

"""
item 3:
decorator in class 
"""
@method_decorator(login_required, name='dispatch')
class ProfileClassDecTemplateView(TemplateView):
    template_name = 'registration/profile.html'

@method_decorator(login_required, name='dispatch')
class AboutClassDecTemplateView(TemplateView):
    template_name = 'registration/about.html'
```

Where to find the full code
```text
check classbasedviewlogindecorators
```

What to learn here
```text
you can add authentication decorators in url and views both 
```
