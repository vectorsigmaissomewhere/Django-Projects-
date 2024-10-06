
TemplateView
```text
django.views.generic.base.TemplateView

It renders a given template, with the context containing parameters captured in the URL.
This views inherits methods and attributes from the following view:
- django.views.generic.base.TemplateResponseMixin
- django.views.generic.base.ContextMixin
- django.views.generic.base.View

class TemplateView(TemplateResponseMixin, ContextMixin, View):
```

TemplateResponseMixin
```text
It provides a mechanism to construct a TemplateResponse, given suitable context, The template to 
use is configurable and can be further customized by subclass.

Attributes:- 
template_name - The full name of a template to use as defined by a string. Not defining a 
template_name will raise a django.core.exceptions.ImproperlyConfigured exception.

template_engine - The NAME of a template engine to use for loading the template. 
template_engine is passed as the using keyword argument to response_class. Default is None, 
which tell Django to search for the template in all configured engines.

response_class - The response class to be returned by render_to_response method. Default is 
TemplateResponse. The template and context of TemplateResponse instances can be altered later
(e.g. in template response middleware).
If you need custom template loading or custom context object instantiation, create a 
TemplateResponse subclass and assign it to response_class.

content_type - The content type to use for the response.content_type is passed as a keyword
argument to response_class. Default is None - meaning that Django uses 'text/html'.

Methods:- 
render_to_response(context, **response_kwargs) - It returns a self.response_class instance.
If any keyword arguments are provided, they will be passed to the constructor of the response
class.

Calls get_template_names() to obtain the list of template names that will be searched looking
for an existent template.

get_template_names() - It returns a list of template names to search for when rendering the template The first template that is found will be used.
If template_name is specified, the default implementation will return a list containing 
template_name(if it is specified).

A default context mixin that passes the keyword arguments received by get_context_data() as the 
template context.
Attribute:- 
extra_context - A dictionary to include in the context. This is a convenient way of specifying 
some context in as_view().

Method:- 
get_context_data(**kwargs) - It returns a dictionary representing the template context. The 
keyword arguments provided will make up the returned context.
```

Example
```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

# urls.py
from school import views
urlpatterns = [
  path('home/', views.HomeView.as_view(), name='home'),
]
```

TemplateView With Context
```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context(**kwargs)
    context['name'] = 'Sonam'
    context['roll'] = 101
    return context

# urls.py
urlpatterns = [
  path('home/', views.HomeView.as_view(), name='home'),
]
```

TemplateView With Extra Context

```python
# views.py
from django.views.generic.base import TemplateView
class HomeView(TemplateView):
  template_name = 'school/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context(**kwargs)
    context['name'] = 'Sonam'
    context['roll'] = 101
    return context

#urls.py
urlpatterns = [
  path('home/', views.HomeView.as_view(extra_context={'course':'python'}), name='home'),
]
```


## Coding Part 

templateview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m6ip8zhu$sn)=(j$x-+pj^c^p--wi#5jd)8vaf&mbpfhp)q#o4'

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
    'school',
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

ROOT_URLCONF = 'templateview.urls'

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

WSGI_APPLICATION = 'templateview.wsgi.application'


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

templateview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='home'),
    path('index/', views.TemplateView.as_view(template_name='school/home.html'), name='index'),
    path('home/', views.HomeTemplateView.as_view(), name='home'),
    path('home2/', views.HomeTemplateViewTwo.as_view(), name='home2'),
    path('home3/', views.HomeTemplateViewTwo.as_view(extra_context={'course':'Python'}), name='home3'),
    path('home4/<int:cl>', views.HomeTemplateViewTwo.as_view(), name='about'),
]
```

school/templates/school/home.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Home Page</h1>
    <h2>{{name}}</h2>
    <h2>{{roll}}</h2>
    <h3>{{course}}</h3>
    <h3>{{cl}}</h3>
</body>
</html>
```

school/views.py
```python
from django.shortcuts import render
from django.views.generic.base import TemplateView 
# Create your views here.

class  HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

class HomeTemplateViewTwo(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sonam'
        context['roll'] = 101
        print(kwargs) 
        return context 
```

where to find the full code
```text
check templateview
```
