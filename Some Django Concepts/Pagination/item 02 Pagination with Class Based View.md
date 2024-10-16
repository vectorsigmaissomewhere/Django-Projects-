
## Pagination

```text
Using pagination we can split data to serveral pages, with Previous/Next links. 

Django provides a few classes that help you manage paginated data:-
- Paginator Class 
- Page class 
```

Paginator Class
```text
class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True)
Where, 
object_list - It takes tuple, list, QuerySet or other sliceabel object with a count() or __len__() method.
It is required.
per_page - The maximum number of items to include on a page, not including orphans. It is required. 
orphans - Use this when you don't want to have a last page with very few items. If the last page 
would normally have a number of items less than or equal to orphans, then those items will be added 
to the previous page(which becomes the last page) instead of leaving the items on a page by 
themselves, orphans defaults to zero, which means pages are never combined and the last page may 
have one item. It is optional.

allow_empty_first_page - Whether or not the first page is allowed to be empty.If False and 
object_list is empty, then an EmptyPage error will be raised. It is optional.
```

Pagination Class Attributes
```text 
- count - The total number of objects, across all pages. 
- num_pages - The total number of pages. 
- page_range - A 1-based range iterator of page numbers, e.g. yielding[1,2,3,4].
```

Pagination Class Methods 
```text 
- get_page(number) - This method returns a Page object with the given 1-based index, while also 
handling out of range and invalid page numbers. 
If the page isn't a number, it returns the first page. 
If the page number is negative or greater than the number of pages, it returns the last page. 
Raises an EmptyPage exception only if you specify Paginator(..., allow_empty_first_page=False) and the 
object_list is empty. 

- page(number) - This method returns a Page object with the given 1-based index. 
Raises InvalidPage if the given page number doesn't exist.
```

Page Class 
```text 
class Page(object_list, number, paginator)
A page acts like a sequence of Page.object_list when using len() or iterating it directly.
```

Page Class Attributes
```text 
- object_list - The list of objects on this page. 
- number - The 1-based page number for this page. 
- paginator - The associated Paginator object.
```

Page Class Methods 
```text 
- has_next() - It returns True if there's a next page. 
- has_previous() - It returns True if there's a previous page. 
- has_other_pages() - It returns True if there's a next or previous page. 
- next_page_number() - It returns the next page number. Raises InvalidPage if next page doesn't exist. 
- previous_page_number() - It returns the previous page number. Raises InvalidPage if previous page doesn't exist. 
- start_index() - It returns the 1-based index of the first object on the page, relative to all of the 
objects in the paginator's list. For example, when paginating a list of 5 objects with 2 objects per page, 
the second page's start_index() would return 3. 
- end_index() - It returns the 1-based index of the last object on the page, relative to all of the objects in the 
paginator's list. For example, when paginating a list of 5 objects with 2 objects per page, the second page's end_index()
would return 4. 
```

Using Pagination 
```text 
- Pagination with Function Based View 
- Pagination with Class Based View 
```


## Coding Part 

classbasedpagination/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dhky#if!k6z!0(qyj@bgmi9(12xy$_f!^(ya*x@dk#)samtmdy'

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
]

ROOT_URLCONF = 'classbasedpagination.urls'

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

WSGI_APPLICATION = 'classbasedpagination.wsgi.application'


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

classbasedpagination/urls.py
```python
from django.contrib import admin
from django.urls import path
from blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
]
```

blog/templates/blog/home.html
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
    {% for post in page_obj%}
    <h2>{{post.title}}</h2>
    <p>{{post.desc|truncatewords:30}}<a href="{% url 'post' post.id%}">Read More</a></p>
    <small>{{post.publish_date}}</small>
    {% endfor %}
    <div>
        <span>
            {% if page_obj.has_previous %}
            <a href="?page={{page_obj.previous_page_number}}">Previous</a>
            {% endif %}
            <span>Page {{page_obj.number}} of {{page_obj.paginator.num_pages }}</span>
            {% if page_obj.has_next %}
            <a href="?page={{page_obj.next_page_number}}">Next</a>
            {% endif %}
        </span>
    </div>
</body>
</html>
```

blog/templates/blog/homesecond.html
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
    {% if is_paginated %}
    {% for post in page_obj%}
    <h2>{{post.title}}</h2>
    <p>{{post.desc}}</p>
    <small>{{post.publish_date}}</small>
    {% endfor %}
    <div>
        <span>
            {% if page_obj.has_previous %}
            <a href="?page={{page_obj.previous_page_number}}">Previous</a>
            {% endif %}
            <span>Page {{page_obj.number}} of {{page_obj.paginator.num_pages }}</span>
            {% if page_obj.has_next %}
            <a href="?page={{page_obj.next_page_number}}">Next</a>
            {% endif %}
        </span>
    </div>
    {% else %}
    {% for post in object_list %}
    <h2>{{post.title}}</h2>
    <p>{{post.desc}}</p>
    <small>{{post.publish_date}}</small>
    {% endfor %}
    {% endif %}
</body>
</html>
```

blog/templates/blog/post.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Post Page</h1>
    <h2>{{post.title}}</h2>
    <p>{{post.desc}}</p>
    <small>{{post.publish_date}}</small>
    <a href="{% url 'home' %}">Back to Home</a>
</body>
</html>
```

blog/admin.py
```python
from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'publish_date']
```

blog/models.py
```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    publish_date = models.DateTimeField()
```

blog/views.py
```python
from django.shortcuts import render
from .models import Post 
from django.views.generic import ListView, DetailView 
from django.http import Http404

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3 # page paginated or not check for homesecond.html 
    paginate_orphans = 1 # if there is one item only place that item to another page where there are max item 

    # if the page is not available take the page into page 1 
    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView, self).get_context_data(*args, **kwargs)    
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(*args, **kwargs)
    
    def paginate_queryset(self, queryset, page_size):
        try:
            return super(PostListView, self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).paginate_queryset(queryset, page_size)

class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post.html'
```

Where to find the full code 
```text
check classbasedpagination
```

What to learn here
```text
The overall thing is pagination
but here we have used class based pagination
```
