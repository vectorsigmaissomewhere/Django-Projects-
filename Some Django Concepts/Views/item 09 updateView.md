## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```

Update View
```text
django.views.generic.edit.UpdateView 

A view that displays a form for editing an existing object, redisplaying the form with 
validation errors(if there are any) and saving changes to the object. This uses a form
automatically genereated from the object's model class (unless a form class is maually 
specified).

This view inherits methods and attributes from the following views:
- django.views.generic.detail.SingleObjectTemplateResponseMixin
- django.views.generic.base.TemplateResponseMixin 
- django.views.generic.edit.BaseUpdateView 
- django.views.generic.edit.ModelFormMixin
- django.views.generic.edit.FormMixin 
- django.views.generic.edit.SingleObjectMixin 
- django.views.generic.edit.ProcessFormView 
- django.views.generic.base.View 


Attributes:

template_name_suffix - The UpdateView page displayed to a GET request uses a 
template_name_suffix of'_form_'.
object - When using UpdateView you have access to self.object, which is the object 
being updated. 
```

## Coding Part

updateview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&*t3^i2_$skz^!dg+3)xiz7y-nb_vj77=we_8dady&%clv$=1('

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

ROOT_URLCONF = 'updateview.urls'

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

WSGI_APPLICATION = 'updateview.wsgi.application'


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

updateview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.StudentCreateView.as_view(), name='stucreate'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='stuupdate'),
    path('thanksupdate/', views.ThanksUpdateView.as_view(), name='thanksupdate'),
    path('create2/', views.StudentCreateView2.as_view(), name='stucreate2'),
    path('update2/<int:pk>', views.StudentUpdateView2.as_view(), name='stuupdate2'),
]
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
        <input type="submit" value="Submit">
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
    <h1>Form Submitted !!</h1>
</body>
</html>
```

school/tempates/school/thanksupdate.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Form Update!!</h1>
</body>
</html>
```

school/admin.py
```python
from django.contrib import admin
from .models import Student 
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']
```

school/forms.py
```python
from django import forms 
from .models import Student 


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name', 'email', 'password']
        # adding classes
        widgets = {'name':forms.TextInput(attrs={'class':'myclass'}), 'password':forms.PasswordInput(render_value=True, attrs={'class':'mypass'})}
```

school/models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)
```

school/views.py
```python
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student 
from django.views.generic.base import TemplateView 
from django import forms

from .forms import StudentForm

"""Not working with forms.py"""
# Create your views here.
class StudentCreateView(CreateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'
    template_name = 'school/student_form.html'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 


class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student 
    fields = ['name', 'email', 'password']
    success_url = '/thanksupdate/'

    # adding classes in form 
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'mypass'})
        return form 

class ThanksUpdateView(TemplateView):
    template_name = 'school/thanksupdate.html'



"""Now working with forms.py"""
class StudentCreateView2(CreateView):
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView2(UpdateView):
    model = Student
    form_class = StudentForm 
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'
```


where to find the full code
```text
check updateview
```

What to learn here
```text
use of CreateView and UpdateView
for creating view and updating view
use of templateview for creating template
and returning to that particular template as success_url

Here forms are created by two way of by using just template and
next by creating a file name forms.py
```
