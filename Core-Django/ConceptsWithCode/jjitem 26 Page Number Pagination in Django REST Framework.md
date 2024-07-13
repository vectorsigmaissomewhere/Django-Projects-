## Pagination

```text
REST framework includes support for customizable pagination styles. This 
allows you to modify how large result sets are split into individual pages of 
data.  
```	

Classes in DRF for pagination
```text
- PageNumberPagination
- LimitOffsetPagination
- CursorPagination
```	

Pagination Global Setting
```text
The pagination style may be set globally, using the 
DEFAULT_PAGINATION_CLASS and PAGE_SIZE setting keys.
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE':5
}
```

Pagination Locally i.e Per View 
```text
You can set the pagination class on an individual view by using the
pagination_class attribute.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
```

1 PageNumberPagination
```text
This pagination style accepts a single number page number in the request 
query parameters. 
To enable the PageNumberPagination  style globally, use the following 
configuration, and set the PAGE_SIZE as desired:
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASSES': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE':5
}

http://127.0.0.1:8000/studentapi/?page=3

The PageNumberPagination class includes a number of attributes that may
be overridden to modify the pagination style.
To set these attributes you should override the PageNumberPagination class,
and then enable your custom pagination class.

- django_paginator_class - The Django Paginator class to use. Default is 
django.core.paginator.Paginator, which should be fine for most use cases.
- page_size - A numeric value indicating the page size. If set, this override the 
Defaults to the same value as the PAGE_SIZE settings key.
- page_query_param- A string value indicating the name of the query 
parameter to use for the pagination control.
- page_size_query_param - If set, this is a string value indicating the name of 
a query parameter that allows the client to set the page size on per-request 
basis. Defaults to None, indicating that the client may not control the 
requested page size.
- max_page_size - If set, this is a numeric value indicating the maximum 
allowable requested page size. This attribute is only valid if page_size_query_param 
is also set.
- last_page_strings - A list or tuple of string values indicating values that may 
be used with the page_query_param to request the final page in the set . 
Defaults to ('last')
- template - The name of a template to use when rendering pagination 
controls in the browsable API. May be overridden to modify the rendering
style, or set to None to disable HTML pagination controls completely. 
Defaults to "rest_framework/pagination/numbers.html".
```

PageNumberPagination Example
```python
# inherited because we want to modify the attribute
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'records'
    max_page_size = 7

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
```

Coding Part 
```text
check gs37 for full code
```

## Coding Part Pagination 

admin.py
```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']
```

models.py
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
```

mypaginations.py
```python
from rest_framework.pagination import PageNumberPagination
class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p' # change page to p text for url 
    page_size_query_param = 'records' # change per page records to 10 # http://127.0.0.1:8000/studentapi/?p=1&records=10
    max_page_size = 7 # doing this user cannot change the records more than 7
    # http://127.0.0.1:8000/studentapi/?p=last # this takes me to that last page
    last_page_strings = 'end' # change that last to end
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll']
```

views.py
```python
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .mypaginations import MyPageNumberPagination


class StduentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumberPagination
```

settings.py
```text
No changes in settings.py
only make changes in settings.py
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StduentList.as_view()),
]
```

Where to get the whole code
```text
chedk gs38 to get the whole code
```
conclusion
```text
From here we learned about how to do pagination
for that check the browsable api
```
