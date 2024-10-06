
RedirectView in Django
```text
django.views.generic.base.RedirectView
It redirects to a given URL.

The given URL may contain dictionary-style string formatting, which will be interpolated against the 
parameters captured in the URL. Because keyword interpolation is always done(even if no
arguments are passed in), any "%" characters in the URL must be written as "%%" so that Python 
will convert them to a single percent sign on output.

If the gievn URL is None, Django will return an HttpResponseGone (410).

This view inherits methods and attributes from the following view:
- django.views.generic.base.View

Attributes:- 
url - The URL to redirect to,as a string. Or None to raise a 410(Gone) HTTP error.

pattern_name - The name of the URL pattern to redirect to. Reversing will be done using 
the same args and kwargs as are passed in for this view.

permanent - Whether the redirect should be permanent. The only difference here is the HTTP 
status code returned. If True, then the redirect will use status code 301. If False, then 
the redirect will use status code 302. By default, permanent is False.

query_string - Whether to pass along the GET query string to the new location. If True, then 
the query string is appended to the URL. If False, then the query string is discarded. By 
default, query_string is False.

Methods:- 
get_redirect_url(*args, **kwargs) - It constructs the target URL for redirection. 

The args and kwargs arguments are positional and/or keyword argument captured from the URL 
pattern, respectively.

The default implementation uses url as a starting string and performs expansion of % named
parameters in that string using the named groups captured in the URL.

If url is not set, get_redirect_url() tries to reverse the pattern_name using what was captured 
in the URL(both named and unamed groups are used).

If requested by query_string, it will also append the query string to the generated URL. Subclasses 
may implement any behavior they wish, as long as the method returns a redirect-ready URL string.
```

## Coding Part

redirect/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#&s7owhknalws@vzi_b+)q#w82w3*1mvj7i_qkzm(na_m51fy#'

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

ROOT_URLCONF = 'redirectview.urls'

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

WSGI_APPLICATION = 'redirectview.wsgi.application'


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
    <h1>Home Page {{pk}}</h1>
    <h2>{{post}}</h2>
</body>
</html>
```

redirectview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    # when I hit home url it should get rediect to / url 
    path('home/', views.RedirectView.as_view(url='/'), name='home'), 
    # when I hit the pattern url it should get redirect to home pattern_name should be same as name 
    path('pattern/', views.RedirectView.as_view(pattern_name='home'), name='pattern'),
    # if some one goes to ronaldo url it will get redirected to google.com
    path('ronaldo/', views.RedirectView.as_view(url='https://www.google.com'), name='ronaldo'),
    # this is related to views.py
    path('ronaldosecond/', views.RonaldoRedirectView.as_view(), name='ronaldosecond'),
    
    #  working with MbappeRedirectView, when i hit mbappe/11 what happens
    path('mbappe/<int:pk>', views.MbappeRedirectView.as_view(),name='mbappe'),
    # when I hit mbappe/number it takes me to home but it doesn't hit the ''/number url but ''
    path('<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),


    # sending string instead of number 
    path('balatoli/<slug:post>/', views.MbappeRedirectView.as_view(), name='balatoli'),
    path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
```

school/views.py
```python
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.

class RonaldoRedirectView(RedirectView):
    url = 'https://www.google.com'

class MbappeRedirectView(RedirectView):
    # when the url is hit, it should find the pattern_name and hit the url with this pattern name
    pattern_name = 'mindex' 
    permanent = True # status code changed from 302 to 301
    query_string = True  # when this is done the query will remain on the url for example url 127.0.0.1:8000/roll/12/?isdcjhdshfckh
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['pk'] = 16
        return super().get_redirect_url(self, *args, **kwargs)
```

Where to find the full code
```text
check redirectview
```

Conclusion
```text
Hitting one url takes me to another url
```
