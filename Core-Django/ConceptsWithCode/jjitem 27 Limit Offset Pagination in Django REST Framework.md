## LimitOffsetPagination

```text
This pagination style mirrors the syntax used when looking up multiple 
database records. The client includes both a "limit" and an "offset" query
paramter. The limit indicates the maximum number of itmes to return, and
is equivalent to the page_size in other styles. The offset indicates the 
starting position of the query in relation to the complete set of paginated 
items. 

To enable the LimitOffsetPagination style globally, use the following 
configuration:
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.LimitOffsetPagination'
}

client sending request 
http://127.0.0.1:8000/studentapi/?limit=4&offset=6

The LimitOffset Pagination class includes a number of attribubtes that may 
be overridden to modfiy the pagination style.

To set these attributes you should override the LimitOffsetPagination class, 
and then enable your custom pagination class.

- default_limit :- A numeric value indicating the limit to use if one is not 
provided by the client in a query parameter. Defaults to the same value
as the PAGE_SIZE settings key.
- limit_query_param - A string value indicating the name of the "limit"
query paramter. Defaults to 'limit'
- offset_query_param- A string value indicating the name of the "offset"
query parameter. Defaults to 'offset'.
- max_limit - If set this is a numeric value indicating the maximum allowable
limit that may be requested to the client. Defaults to None.
- template - The name of a template to use when rendering pagination
controls in the browsabel API. May be overridden to modify the rendering 
style, or set to None to disable HTML pagination controls completely. 
Defaults to "rest_framework/pagination/numbers.html".
```

The url
```text
http://127.0.0.1:8000/studentapi/?limit=7&offset=9
```

## Coding part

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
from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5 # doing this in one page there you can see 5 items
    limit_query_param = 'mylimit'# offset means from that item you want to start
    offset_query_param = 'myoffset'
    max_limit = 6 # maximum item will be only 6 and you can get more items from using the url
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
from .mypaginations import MyLimitOffsetPagination


class StduentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination
```

settings.py
```text
only add in the installed apps
api and rest_framework
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

Conclusion
```text
Control the pagination using LimitOffsetPagination
```
