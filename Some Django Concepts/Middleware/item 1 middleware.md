## Middleware
```text
Middleware is a framework of hooks into Django's request/response
processing.
It's a light, low-level "plugin" system for globally altering Django's input
or output. Each middleware component is responsible for doing some
specific function.

- Built in Middleware , this is already present and we are using it
- Custom Middleware
```

How Middleware Works
```text
Middleware means something in between 
user sent a request middleware checks if it is valid or not 
if valid the request is sent to the required views 


There can be more than one middleware 
```

Function based Middleware
```text
A middleware factory is a callable that takes a get_response callable
and returns a middleware.
A middleware is a callable that takes a request and returns a response,
just like a view.

def my_middleware(get_response):
    # One-time configuration and initialization
    def my_function(request):
        # Code to be executed for each request before the view are called
        response = get_response(request)
        # Code to be executed for each request/response after the view is called
        return response
```

get_response()
```text
The get_response callable provided by Django might be the actual view
(if this is the last listed middleware) or it might be the next middleware
in the chain.
The current middleware doesn't need to know or care what exactly it is, just
that it represents whatever comes next.

The get_response callable for the last middleware in the chani won't be the actual
view but rather a wrapper method from the handle which takes care of applying
view middleware, calling the view with appropriate URL arguments, and applying
template-response and exception middleware.

Middleware can live anywhere on your Python path.
```

Activating Middleware
```text
To activate a middleware component, add it to the MIDDLEWARE list in your Django settings.
In MIDDLEWARE, each middleware component is represented by a string: the full Python path
to the middleware factory's class or function name. The order in MIDDLEWARE matters because a
middleware can depend on other middleware. For instance, AuthenticationMiddleware stores the
authenticated user in the session; therefore, it must run after SessionMiddleware.

Eg.-
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.middleware.SessionMiddleware',
    'blog.middlewares.my_middleware'
    ]

```

Program number 1

## Function Based Middleware

blog/middlewares.py
```python
def my_middleware(get_response): # middleware name # paramter pass next middleware
    print("One TIme Initialization")
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse

def home(request):
    print("I am View")
    return HttpResponse("This is Home Page")
```

middleware/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*dd8dw3pt-+k(^)ukd5kbt@uw34wxp#qfz)%x33l&rpuobh0^^'

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
    'blog.middlewares.my_middleware', # app.filename.middlewarename
]

ROOT_URLCONF = 'middleware.urls'

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

WSGI_APPLICATION = 'middleware.wsgi.application'


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

middleware/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

terminal response
```text
This is before view
I am View
This is after view
[12/Sep/2024 17:05:53] "GET / HTTP/1.1" 200 17
This is before view
This is after view
Not Found: /favicon.ico
```


Class Based Middleware
```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization
    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called
        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called
        return response
```

__init__(get_response)
```text
__init__(get_response) - Middleware factories must accept a get_response argument. You can also
initialize some global state for the middleware. Keep in mind a couple of caveats:
- Django initializes your middleware with only the get_response argument, so you can't define
__init__() as requiring any other arguments.
- Unlike the __call__() method which is called once per request, __init__() is called only once, when
the Web server starts.
```

Activating Middleware
```text
To activate a middleware component, add it to the MIDDLEWARE list in your Django settings.

In MIDDLEWARE, each middleware component is represented by a string: the full Python path to
the middleware factory's class or function name. The order in MIDDLEWARE matters because a
middleware can depend on other middleware. For instance, AuthenticationMiddleware stores the
authenticated user in the sesion; therefore, it must run after SessionMiddlewarse.

Eg. -
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'blog.middlewares.MyMiddleware'
    ]

```

blog/middlewares.py
```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response 
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse

def home(request):
    print("I am View")
    return HttpResponse("This is Home Page")
```

classbasedmiddleware/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2@vs0e6--5kz2u9t$569bfr&-4)o&7vw!ssxd+rsh@ldbl=fmi'

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
    'blog.middlewares.MyMiddleware',
]

ROOT_URLCONF = 'classbasedmiddleware.urls'

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

WSGI_APPLICATION = 'classbasedmiddleware.wsgi.application'


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

classbasedmiddleware/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

output
```text
This is before view
I am View
This is after view
```

## Multiple Middleware 

blog/middlewares.py
```python
class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Brother Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Brother before view")
        response = self.get_response(request)
        print("This is Brother after view")
        return response 
    
class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Father before view")
        response = self.get_response(request)
        print("This is Father after view")
        return response 
    
class MommyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mommy Initialization")
    
    def __call__(self, request):
        # code that runs before calling view 
        print("This is Mommy before view")
        response = self.get_response(request)
        print("This is Mommy after view")
        return response 
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse

def home(request):
    print("I am View")
    return HttpResponse("This is Home Page")
```

blog/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-52q%k5of9%lvvvyxsog#t95xgqj1c-b2g^hmn-#%89&u3l5wby'

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
    'blog.middlewares.BrotherMiddleware',
    'blog.middlewares.FatherMiddleware',
    'blog.middlewares.MommyMiddleware',
]

ROOT_URLCONF = 'multiplemiddleware.urls'

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

WSGI_APPLICATION = 'multiplemiddleware.wsgi.application'


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

multiplemiddleware/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

output
```text
Before going to the url

One Time Mommy Initialization
One Time Father Initialization
One Time Brother Initialization

After hitting the url

This is Brother before view
This is Father before view
This is Mommy before view
I am View
This is Mommy after view
This is Father after view
This is Brother after view
[16/Sep/2024 14:16:41] "GET / HTTP/1.1" 200 17
This is Brother before view
This is Father before view
This is Mommy before view
This is Mommy after view
This is Father after view
This is Brother after view
```


## Middleware Hooks
```text
Following are special methods to class-based middleware:
process_view(request, view_func, view_args, view_kwargs) - It is called
just before Django calls the view.
It should return either None or an HttpResponse object.
If it returns None, Django will continue processing this request, 
executing any other process_view() middleware and, then, the 
appropriate view.
It is returns an HttpResponse object, Django won't bother calling the 
appropriate view; it'll apply response middleware to that HttpResponse
and return the result.
```

Middleware Hooks parameters

process_view
```text
process_view(request, view_func, view_args, view_kwargs)
Where, 
Request - It is an HttpRequest object.
view_func - It is the Python function that Django is about to use. (It's 
the actual function object, not the name of the function as a string.)
view_args - It is a list of positional arguments that will be passed to the 
view.
view_kwargs - It is a dictionary of keyword arguments that will be 
passed to the view.
Neither view_args nor view_kwargs include the first view argument
(request).
```

process_exception
```text
process_exception(request, exception) - Django calls process_exception() when
a view raises an exception.
It should return either None or an HttpResponse object.
If it returns an HttpResponse object, the template response and response middleware
will be applied and the resulting response returned to the browser. Otherwise, default
exception handling kicks in.
Where,
Request - It is an HttpRequest object.
Exception - It is an Exception object raised by the view function.
Note - Middleware are run in reverse order during the response phase, which includes
process_exception. If an exception middleware returns a response, the process_exception
methods of the middleware classes above that middleware won't be called at all.
```

process_template_response
```text
process_template_response(request, response) - This method is called just after the view
has finished executing, if the response instance has a render() method, indicating that it
is a TemplateResponse or equivalent.

It must return a response object that implements a render method.

It could alter the given response by changing response.template_name and response.context_data,
or it could create and return a brand-new TemplateResponse or equivalent.

You don't need to explicitly render responses, responses will be automatically rendered once
all template response middleware has been called.
Where,
request - It is an HttpRequest object.
response - It is the TemplateResponse object(or equivalent) returned by a Django view or by a
middleware.
```

Template Response
```text
TemplateResponse - TemplateResponse is a subclass of SimpleTemplateResponse that knows about 
the current HttpRequest.

A TemplateResponse object can be used anywhere that a normal django.http.HttpResponse can be 
used. It can also be used as an alternative to calling render().

Method

__init__(request, template, context=None, context_type=None, status=None, charset=None,using = None)
- It instantiates a TemplateResponse object with the given request, template, context, 
content type, HTTP status, and charset.
Where, 

request - An HttpRequest instance.
template - A backend-dependent template object(such as those returned by get_template()), the name
of a template, or a list of template names.

context - A dict of values to add to the template context. By default, this is an empty dictionary.
context_type - The value included in the HTTP Content-Type header, including the MIME type 
specification and the character set encoding. If content_type is specified, then its value is used.

status - The HTTP status code for the response.

charset - The charset in which the response will be encoded. If not given it will be extracted from 
content_type, and if that is unsuccessful, the DEFAULT_CHARSET setting will be used.

using  - The NAME of a template engine to use for loading the template.


There are three circumstances under which a TemplateResponse will be rendered:
When the TemplateResponse instance is explicitly rendered, using the 
SimpleTemplateResponse.render() method.
When the content of the response is explicitly set by assigning response.content.
After passing through template response middleware, but before passing through
response middleware.

Note - 
A TemplateResponse can only be rendered once.
```


## Middleware Hooks

blog/templates/blog/user.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {{ name }}
</body>
</html>
```

blog/templates/middlewares.py
```python
from django.shortcuts import HttpResponse
class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print("This is Process View - Before View")
        return HttpResponse("This is before view")
    
    # process view 
    """
    def process_view(request, *args, **kwargs):
        print("This is Process View - Before View")
        return None
    """

class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        print("Exception Occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)

class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print("Process Template Response From Middleware")
        response.context_data['name'] = 'Sonam'
        return response
```

blog/views.py
```python
from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse 

def home(request):
    print("I am Home View")
    return HttpResponse("This is Home Page")

def excp(request):
    print("I am Excp View")
    a = 10 / 0
    return HttpResponse("This is Excp Page")

def user_info(request):
    print("I am User Info View")
    context = {'name':'Rahul'}
    return TemplateResponse(request, 'blog/user.html', context)
```

middlewareHooks/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y@(ms(tgtbq#8823zqlfh_$=-gse-*39g=5ejjt!3!7=dmyp@h'

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
    'blog.middlewares.MyProcessMiddleware',
    'blog.middlewares.MyExceptionMiddleware',
    'blog.middlewares.MyTemplateResponseMiddleware',
]

ROOT_URLCONF = 'middlewareHooks.urls'

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

WSGI_APPLICATION = 'middlewareHooks.wsgi.application'


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

middlewareHooks/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('excp/', views.excp),
    path('user/', views.user_info),
]
```

output
```text
There is a url for each
so each url goes to the middleware
```
