
Class Based View
```text
Class-based views provide an alternative way to implement views as Python objects instead of 
functions.
They do not replace function-based views.
- Base Class-Based Views/ Base View
- Generic Class-Based Views / Generic View
```

Base Class-Based View
```text
Base class-based views can be thought of as parent views, which can be used by themselves or 
inherited from. They may not provide all the capabilities required for projects, in which case 
there are Mixins which extend what base views can do. 
- View 
- TemplateView
- RedirectView
```

Generic Class Based View
```text
Django's generic views are built off of those base views, and were developed as a shortcut for common
usage patterns such as displaying the details of an object.
They take certain common idioms and patterns found in view development and abstract them so that 
you can quickly write common views of data without having to repeat yourself.

Most generic views require the queryset key, which is a QuerySet instance
- Display View - ListView, DetailView 
- Editing View - FormView, CreateView, UpdateView, DeleteView
- Date Views - ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, 
DayArchiveView, TodayArchiveView, DateDetailView


The two following generic class-based views are designed to display data.
- ListView 
- DetailView 
```

ListView
```text
django.views.generic.list.ListView 
A page representing a list of objects.
While this view is executing, self.object_list will contain the list of objects(usually, but not
necessarily a queryset) that the view is operating upon.

This view inherits methods and attributes from the following views:
- django.views.generic.list.MultipleObjectTemplateResponseMixin  ##
- django.views.generic.base.TemplateResponseMixin 
- django.views.generic.list.BaseListView 
- django.views.generic.list.MultipleObjectMixin      ##
- django.views.generic.base.View 
```

MultipleObjectTemplateResponseMixin
```text
A mixin class that performs template-based response rendering for views that operate upon a list of 
object instances. Required that the view it is mixed with provides self.object_list, the list of 
object instances that the view is operating on. self.object_list may be, but is not required to be, 
a QuerySet. 
This inherits methods and attributes from the following views:
- django.views.generic.base.TemplateResponseMixin 
Attribute:- 
template_name_suffix - The suffix to append to the auto-generated candidate template name. Default 
suffix is _list.
Method:- 
get_template_names() - It returns a list of candidate template names. 
```

BaseListView 
```text
A base view for displaying a list of objects. It is not intended to be used directly, but rather 
as a parent class of the django.views.generic.list.ListView or other views representing lists of 
objects.
This view inherits methods and attributes from the following views:
- django.views.generic.list.MultipleObjectMixin 
- django.views.generic.base.View 

Methods:-
get(request, *agrs, **kwargs) - It adds object_list to the context. If allow_empty is True
then display an empty list. If allow_empty is False then raise a 404 error.
```

MultipleObjectMixin
```text 
django.view.generic.list.MultipleObjectMixin
A mixin that can be used to display a list of objects. 
If paginate_by is specified, Django will paginate the results returned by this. You can specify 
the page number in the URL in one of two ways:

Use the page parameter in the URL conf.
Page the page number via the page query-string parameter.
These values and list are 1-based, not 0-based, so the first page would be represented as page 1.
As a special case, you are also permitted to use last as a value for page.
This allows you to access the final page of results without first having to determine how many 
pages there are.
Note that page must be either a valid page number or the value last; any other value for page 
will result in a 404 error.
Attribute:- 
allow_empty - A boolean specifying whether to display the page if no objects are avaiable. If 
this is False and no objects are available, the view will raise a 404 instead of displaying an 
empty page. By default, this is True.

model - The model that this view will display data for. Specifying model = Student is effectively 
the same as specifying queryset = Student.objects.all(), where objects stands for Student's 
default manager.

queryset - A QuerySet that represents the objects. If provided, the value of queryset supersedes 
the value provided for model.

ordering - A string or list of strings specifying the ordering to apply to the queryset. Valid 
values are the same as those for order_by().

Attributes:- 
paginate_by - An integer specifying how many objects should be displayed per page. If this is 
given, the view will paginate objects with paginate_by objects per page. The view will expect 
either a page query string parameter(via request.GET) or a page variable specified in the 
URL conf.

paginate_orphans - An integer specifying the number of "overflow" objects the last page can 
contain. This extends the paginate_by limit on the last page by up to paginate_orphans, in  
order to keep the last page from having a very small number of objects. 

page_kwargs - A string specifying the name to use for the page parameter. The view will expect 
this parameter to be available either as a query string parameter (via request.GET) or as a 
kwarg variable specified in the URLconf. Defaults to page. 

paginator_class - The paginator class to be used for pagination. By default, 
django.core.paginator.Paginator is used. If the custom paginator class doesn't have the same 
constructor interface as django.core.paginator.Paginator, you will also need to provide an 
implementation for get_paginator(). 

context_object_name - Designates the name of the variable to use in the context. 
```

Methods:- 
```text
get_queryset() - Get the list of items for this view. This must be an iterable and may be a 
queryset(in which queryset-specific behavior will be enabled).

get_ordering() - Returns a string(or iterable of strings) that defines the ordering that will be 
applied to the queryset. 
Returns ordering by default.

paginate_queryset(queryset, page_size) - Returns a 4-tuple containing(paginator, page, object_list, 
is_paginated).

Constructed by paginating queryset into pages of size page_size. If the request contains a page 
argument, either as a captured URL argument or as a GET argument, object_list will correspond to 
the objects from that page. 

get_paginate_by(queryset) - Returns the number of items to paginate by, or None for no pagination.
By default this returns the value of paginate_by. 

get_paginator(queryset, per_page, orphans=0, allows_empty_first_page=True) - Returns an instance of 
the paginator to use for this view. By default, instantiates an instance of paginator_class.

get_paginate_orphans() - An integer specifying the number of "overflow" objects the last page can 
contain. By default this returns the value of paginate_orphans. 

get_allow_empty() - Returns a boolean specifying whether to display the page if no objects are 
available. If this method returns False and no objects are available, the view will raise a 
404 instead of displaying an empty page. By default, this is True.

get_context_object_name(object_list)- Returns the context variable name that will be used to 
contain the list of data that this view is manipulating. If object_list is a queryset of 
Django objects and context_object_name is not set, the context name will be the model_name of 
the model that the queryset is composed from, with postfix '_list'  appended. For example, 
the model Article would have a context object named article_list.

get_context_data(**kwargs) - Returns context data for displaying the list of object.
Context 
object_list: The list of objects that this view is displaying. If context_object_name is 
specified, that variable will also be set in the context, with the same value as object_list.
is_paginated: A boolean representing whether the results are paginated. Specifically, this is 
set to False if no page size has been specified, or if the available objects do not span 
multiple pages.

paginator: An instance of django.core.paginator.Paginator. If the page is not paginated, this 
context variable will be None. 
page_obj: An instance of django.core.paginator.Page. If the page is not paginated, this 
context_variable will be None. 
```

ListView with Default Template and Context 
```python
# views.py 
from django.views.generic.list import ListView 
from .models import Student 
class StudentListView(ListView):
    model = Student 

# urls.py
urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='student'),
]

# Default Template 
# Syntax :- AppName/ModelClassName_list.html
# Example:- school/student_list.html 

# Default Context
# Syntax:- ModelClassName_list 
# Example:- student_list 
# We can also use object_list
```

List View with Custom Template and Context 
```python 
# views.py
from django.views.generic.list import ListView 
from .models import Student 
class StudentListView(ListView):
    model = Student 
    template_name = 'school/student.html' # Custom Template name 
    context_object_name = 'students' # Custom Context Name 

# urls.py
urlpatterns=[
    path('student/', views.StudentListView.as_view(), name='student'),
]

# Note - school/students.html, school/student_list.html These both will work.
```

## Coding Part

listview/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7_3+sx%#h0$-j&qb3x6jy7fao$%)dfhsf#+q3(nqt8uznb!2$o'

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

ROOT_URLCONF = 'listview.urls'

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

WSGI_APPLICATION = 'listview.wsgi.application'


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

listview/urls.py
```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # this url shows listview
    path('student/', views.StudentListView.as_view(), name='student'),
    path('studentsecond/', views.StudentSecondListView.as_view(), name='studentsecond'),
    path('studentthird/', views.StudentThirdListView.as_view(), name='studentthird'),
    path('studentfourth/', views.StudentFourthListView.as_view(), name='studentfourth'),
    path('studentfifth/', views.StudentFifthListView.as_view(), name='studentfifth'),
]
```

school/templates/school/student_get.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is student_get.html template</h1>
    {% for student in student_list %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
</body>
</html>
```

school/templates/school/student_list.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    {% for student in student_list %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
</body>
</html>
```

school/templates/school/studentthird.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is student third page</h1>
    {% for student in student_list %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
</body>
</html>
```

school/templates/school/studentfourth.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is Student fourth html page as we have changed the context from student_list to students</h1>
    {% for student in students %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
</body>
</html>
```

school/templates/school/studentfifth.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is StudentFifthListView</h1>
    {% for student in students %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
    <br>
    {% for student in freshers %}
    {{student.name}}
    {{student.roll}}
    {{student.course}} <br>
    {% endfor %}
</body>
</html>
```

school/admin.py
```python
from django.contrib import admin
from .models import Student 
# Register your models here.

admin.site.register(Student)
```

student/models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    course = models.CharField(max_length=70)
```

school/views.py
```python
from django.shortcuts import render
from django.views.generic.list import ListView 
from .models import Student 


# this view shows listview 
class StudentListView(ListView):
    model = Student 

    # Use of ListView is I don't need to write the below lines of code
    """
    stud = Student.object.all()
    context = {'student_list':stud}
    return render(request, 'school/student_list.html', context)
    """

# custom listview 
class StudentSecondListView(ListView):
    model = Student 
    # the above search for student_list.html while this view search for student_get.htmk
    template_name_suffix = '_get'
    # orders by name 
    ordering = ['name']

# in previous view we must have student_list.html or student_get.html as template name 
# custom listview where we gonna change the template name 
class StudentThirdListView(ListView):
    model = Student
    template_name = 'school/studentthird.html'

# change context name 
# that is our default context name is student_list in template page
# but we are change it into students
class StudentFourthListView(ListView):
    model = Student 
    template_name = 'school/studentfourth.html'
    context_object_name = 'students'

# filter data 
# get only data whose course is Python from get_queryset method
# get data with order of name but with context name freshers 
class StudentFifthListView(ListView):
    model = Student 
    template_name = 'school/studentfifth.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course='Python')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context
```

where to find the whole code 
```text
check listview
```

What we learned here
```text
we learned about listview
using this you don't have to write lots of code for making get request
also if you want any configuration like filtering models, changing template file and changing context name
can be done 
```
