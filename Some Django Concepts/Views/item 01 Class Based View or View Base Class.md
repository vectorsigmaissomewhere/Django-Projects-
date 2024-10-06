
Type of Views
```text
- Function Based View
- Class Based View
```

Class Based View
```text
Class-based views provide an alternative way to implement views as Python objects instead of 
functions.
They do not replace function-based views.

Two types of class based view
- Base Class-Based Views/ Base View
- Generic Class-Based Views/ Generic View

Advantages:- 
- Organization of code related to specific HTTP methods(GET, POST, etc, ) can be addressed by
  seperate methods instead of conditional branching
- Object oriented techniques such as mixins (multiple inheritance) can be used to factor code 
  into resuable components. 
```

Base Class-Based View
```text
Base class-based views can be thought of as parent views, which can be used by themselves or 
inherited from. They may not provide all the capabilities required for projects, in which case 
there are Mixins which extend what base views can do.
- View
- Template View
- RedirectView
```

View
```text
django.views.generic.base.View
The master class-based base view. All other class-based views inherit from this base. It isn't 
strictly a generic view and thus can also be imported from django.views.

generic is in 
Lib\site-packages\django\views\generic in Python

Attribute:- 
http_method_names = ['get', 'post', 'put, 'patch', 'delete', 'head', 'options', 'trace']
The list of HTTP method names that this view will accept.

Methods:- 
setup(self, request, *args, **kwargs) - It initializes view instance attribute: self.request, 
self.args, and self.kwargs prior to dispatch()

dispatch(self, request, *args, **kwargs) - The view part of the view - the method that accepts
a request argument plus arguments, and returns a HTTP response

The default implementation will inspect the HTTP method and attempt to delegate to a method that
matches the HTTP method; a GET will be delegated to get(), a POST to post(), and so on.

Be default, a HEAD request will be delegated to get(). If you need to handle HEAD requests in a 
different way than GET, you can override the head() method.

http_method_not_allowed(self, request, *args, **kwargs) - If the view was called with a HTTP 
method it doesn't support, this method is called instead.
The default implementation returns HttpResponseNotAllowed with a list of allowed methods in   
plain text. 

options(self, request, *args, **kwargs) - If handles responding to requests for the OPTIONS 
HTTP verb. Returns a response with the Allow header containing a list of the view's allowed 
HTTP method names.

as_view(cls, **initkwargs) - It returns a callable view that takes a request and returns a 
response.

_allowed_methods(self)
```

## Difference between function based view and class based view 

```text
in function based view you don't have to define get method
but in class based view you have to define get method
```
function based view

views.py
```python
from django.html import HttpResponse
def myview(request):
  return HttpResponse('<h1>Function Based View</h1>')
```
urls.py
```python
from django.urls import path 
from school import views 
urlpatterns = [path('func/', views.myview, name='func')]
```

class based view

views.py
```python  
from django.views import View 
class MyView(View):
  def get(self, request):
    return HttpResponse('<h1>Class Based View</h1>')
```
urls.py
```python 
from django.urls import path 
from school import views 
urlpatterns = [
  path('cl/', views.MyView.as_view(), name='cl'),
]
```

how urls.py in class based view works
```text
MyView.as_view() is called when request is called 
and this function creates an instance and calls 
setup function to initialize attribute
and then dispatch method is called
this checks which method is this 
if the requested http method is present in the views 
it returns http response if not it returns http response 
not allowed 
```

## CODING PART

classbasedview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c+b&h0b9-dica6jub-+kpg63sr7-i$^(ajp343_%nay#!a6#d^'

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

ROOT_URLCONF = 'classbasedview.urls'

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

WSGI_APPLICATION = 'classbasedview.wsgi.application'


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

school/templates/school/contact.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>
</body>
</html>
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
    {{msg}}
    <h1>This is home page</h1>
</body>
</html>
```

school/templates/school/news.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Page</title>
</head>
<body>
    {{info}}
</body>
</html>
```

classbasedview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', views.myview, name='func'), # url for function based view
    path('cl/', views.MyView.as_view(), name='cl'), # url for class based view
    # path('cl/', views.MyView.as_view(name='Ronaldo'), name='cl') # pass value in views  
    path('subcl/', views.MyViewChild.as_view(), name='subcl'),
    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.ContactClassView.as_view(), name='contactcl'),
    path('newsfun/', views.newsfun, name='newsfun'),
    #path('newscl/', views.NewsClassView.as_view(), name='newscl'), # don't send the template
    path('newscl/', views.NewsClassView.as_view(template_name='school/news.html'), name='newcl'), # send the template from views
]
```

school/forms.py
```python
from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=7)
```

school/views.py
```python
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Function Based View
def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')

# Class Based View
class MyView(View):
    name = 'Ronaldo'
    def get(self, request):
        return HttpResponse(self.name)

# inheriting MyView class 
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse("This is sub class "+self.name)
    
# function based view 
def homefun(request):
    return render(request, 'school/home.html')

# class based view 
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html')

# write context in function based view
def aboutfun(request):
    context = {'msg':'Welcome to Function based about view'}
    return render(request, 'school/home.html', context)

# write context in class based view 
class AboutClassView(View):
    def get(self, request):
        context = {'msg':'Welcome to Class Based about view'}
        return render(request, 'school/home.html', context)

## with form in case of function based view 
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})    

## with form in case of class based view
class ContactClassView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')

## function based views for  
def newsfun(request):
    context = {'info':'Ronaldo is the GOAT.'}
    return render(request, 'school/news.html', context)

""""
second way of doing this this 
views.py
def newsfun(request, template_name):
    template_name = template_name
    context = {'info':'RONALDO is the GOAT'}
    return render(request, template_name, context)

urls.py
path('newsfun/', views.newsfun, {'template_name':'school/news.html'}, name='newsfun')
"""

# news class based view
class NewsClassView(View):
    template_name = ''
    def get(self, request):
        context = {'info': 'Ronaldo is the GOAT'}
        return render(request, self.template_name , context)
```

Where to find the full code
```text
check classbasedview
```

## Conclusion
```text
Learned about function based view and class based view
also the ways to pass templates in view class and functions view  
```
