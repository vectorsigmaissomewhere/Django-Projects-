## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```


CreateView
```text
django.views.generic.edit.CreateView

A view that displays a form for creating an object, redisplaying the form with validation errors(if
there are any) and saving the object.

This views inherits methods and attributes from the following  views:
django.views.generic.detail.SingleObjectTemplateResponseMixin
django.views.generic.base.TemplateResponseMixin 
django.views.generic.edit.BaseCreateView 
django.views.generic.edit.ModelFormMixin 
django.views.generic.edit.FormMixin 
django.views.generic.detail.SingleObjectMixin 
django.views.generic.edit.ProcessFormView 
django.views.generic.base.View 

Attributes:-  

model - A model class. Can be explicitly provided, otherwise will be determined by examining 
self.object or queryset. 

fields - A list of names of fields. This is interpreted the same way as the Meta.field attribute of 
ModelForm.
This is a required attribute if you are generating the form class automatically(e.g. using model).
Omitting this attribute will result in an ImproperlyConfigured exception.

success_url - The URL to redirect to when the form is successfully processed.
success_url may contain dictionary string formatting, which will be interpolated against the 
object's field attributes. For example, you could use success_url="polls/{slug}/" to redirect to 
a URL composed out of the slug field on a model.

Methods:- 

get_form_class() - Retrieve the form class to instantiate. If form_class is provided, that class 
will be used. Otherwise, a ModelForm will be instantiated using the model associated with the 
queryset, or with the model, depending on which attribute is provided.

get_form_kwargs() - Add the current instance(self.object) to the standard get_form_kwargs().

get_success_url() - Determine the URL to redirect to when the form is successfully validated. 
Returns django.views.generic.edit.ModelFormMixin.success_url if it is provided; otherwise, attempts
to use the get_absolute_url() of the object.

form_valid(form) - Saves the form instance, sets the current object for the view, and redirects to 
get_success_url().

form_invalid(form) - Renders a response, providing the invalid form as context.
```

## Coding Part


createview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-st7op34-pz@%d+r9)o+hka)d7d#w+m4h3x*3ovv3+(bktvpby#'

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

ROOT_URLCONF = 'createview.urls'

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

WSGI_APPLICATION = 'createview.wsgi.application'


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

createview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name='stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('studetail/<int:pk>', views.StudentDetailView.as_view(), name='detail'),
    path('create2/', views.StudentTwoCreateView.as_view(), name='stu2create'),
]
```

school/templates/school/sform.html
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
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

school/templates/school/student_detail.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>
    {{student.name}}
    {{student.email}}
    {{student.password}}
    </h1>
</body>
</html>
```

school/templates/school/student_form.html
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
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

school/templates/school/thanks.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Your Form has Submitted</h1>
</body>
</html>
```

student/forms.py
```python
from django import forms 
from .models import Student 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'email', 'password']
        widgets = {'name':forms.TextInput(attrs={'class':'myclass'}), 'password':forms.PasswordInput(attrs={'class':'mypass'})}
```

school/models.py
```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    """
    def get_absolute_url(self):
        return reverse("thankyou")
    """
    # return to the same data as when the form being submitted
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
```

school/views.py
```python
from django.shortcuts import render
from django.views.generic.edit import CreateView 
from .models import Student 
from django.views.generic.base import TemplateView 
from django.views.generic.detail import DetailView 
from django import forms 

from .forms import StudentForm

# data will get saved 
class StudentCreateView(CreateView):
    model = Student 
    fields = ['name', 'email', 'password']
    # success_url = '/create/' # after the data is saved go to this url 
    success_url = '/thanks/'
    # template_name = 'school/sform.html' # custom form 

    # adding class to the form template html 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentDetailView(DetailView):
    model = Student 


# This is send model create view that is related with forms.py
class StudentTwoCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'
```

Where to find the full code
```text
check createview
```

What to learn here 
```text
- Create form using createview class
- redirect to specific template after submitting form
- change attribute of the forms for example changing attribute type of form
- default type of password is text change it into password 
```
