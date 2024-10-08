

## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```

FormView
```text
django.views.generic.edit.FormView

A view that displays a form. On error, redisplays the form with validation errors; on success, 
redirects to a new URL. 
This view inherits methods and attributes from the following views:
- django.views.generic.base.TemplateResponse.Mixin
- django.views.generic.edit.BaseFormView
- django.views.generic.edit.FormMixin
- django.views.generic.edit.ProcessFormView
- django.views.generic.base.View
```

FormMixin
```text
django.views.generic.edit.FormMixin
A mixin class that provides facilities for creating and displaying forms. 
This view inherits methods and attributes from the following views:
    - django.views.generic.base.ContextMixin 

Attributes:- 
initial - A dictionary containing initial data for the form.
form_class - The form class to instantiate.
success_url - The URL to redirect to when the form is successfully processed.
prefix - The prefix for the generated form.

Methods:- 
get_initial() - Retrieve initial data for the form. By default, returns a copy of initial.

get_form_class() - Retrieve the form class to instantiate. By default form_class.

get_form(form_class=None) - Instantiate an instance of form_class using get_form_kwargs(). 
If form_class isn't provided get_form_class() will be used.

get_form_kwargs() - Build the keyword arguments required to instantiate the form.
The initial argument is set to get_initial(). If the request is a POST or PUT, the request 
data(request.POST and request.FILES) will also be provided.

get_prefix() - Determine the prefix for the generated form. Returns prefix by default.

get_success_url() - Determine the URL to redirect to when the form is successfully validated.
Returns success_url by default.

form_valid(form) - Redirects to get_success_url().

form_invalid(form) - Renders a response, providing the invalid form as context.

get_context_data(**kwargs) - Calls get_form() and adds the result to the context data with the 
name 'form'.
```

ProcessFormView
```text
django.views.generic.edit.ProcessFormView
A mixin that provides basic HTTP GET and POST workflow.
Extends
django.views.generic.base.View

Methods:- 
get(request, *args, **kwargs) - Renders a response using a context created with get_context_data().

post(request, *args, **kwargs) - Constructs a form, checks the form for validity and handles it 
accordingly.

put(*args, **kwargs) - The PUT action is also handled and passes all parameters through to post().
```

Example of FormView
```python
# forms.py
from django import forms 
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)

# views.py
from django.views.generic.edit import FormView
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm 
    success_url = '/thankyou/'
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        return HttpResponse('Msg Sent')

class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'

# urls.py
from school import views
urlpatterns = [
    path('contact/', views.ContactForm.as_view(), name='contact'),
    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),
]
```


## Coding Part 

formview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6k7fl0)*&ky9%+r%bu%z8jhm--9s9p_4e+eu_42)lsvpl9ui0+'

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

ROOT_URLCONF = 'formview.urls'

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

WSGI_APPLICATION = 'formview.wsgi.application'


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

formview.urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),
]
```

school/templates/school/contact.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form </title>
</head>
<body>
    <form action="" method="post" novalidate>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Send">
    </form>
</body>
</html>
```

school/templates/school/thankyou.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Thank you </h1>
</body>
</html>
```

school/forms.py
```python
from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)

class FeedbackForm(forms.Form):
    your_name = forms.CharField()
    your_email = forms.EmailField()
    msg = forms.CharField(widget=forms.Textarea)
```

school/views.py
```python
from django.shortcuts import render, HttpResponse
from .forms import ContactForm 
from django.views.generic.edit import FormView 
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm 
    success_url = '/thankyou/' # if the user hits the submit button take him to thankyou page
    # set the initial form data
    initial = {'name':'Ronaldo'}
    # capture form data 
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        # return super().form_valid(form)
        return HttpResponse('<h1>Message Sent</h1>')

class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'
```

Where to find the full code
```text
check formview
```

What to get in this file
```text
Learn about form view
as you can create a form using form view class
custom template can be made
```
