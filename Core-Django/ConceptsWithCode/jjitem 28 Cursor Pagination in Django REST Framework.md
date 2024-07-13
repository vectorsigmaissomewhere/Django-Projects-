## Cursor Pagination

about
```text
The cursor-based pagination presents an opaque "cursor" indicator that the 
client may use to page through the result set. This pagination style only
presents forward and reverse controls, and does not allow the client to 
navigate to arbitrary positions.

Cursor based pagination requires that there is a unique, unchanging ordering
of items in the result set. The ordering might typically be a creation 
timestamp on the records, as this presents a consistent ordering to paginate
against.

The default is to order by"-created". This assumes that there must be a 
'created' timestamp field on the model instances, and will presnet a 
"timestamp" style paginated view, with the most recently added items first.

The CursorPagination class includes a number of attributes that may be
overridden to modify the pagination style. 

To set these attributes you should override the CursorPagination class, and 
then enable your custom pagination class.

- page_size = A numeric value indicating the page size. If set, this overrides
the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings
key.
- cursor_query_param = A string value indicating the name of the "cursor"
query parameter. Defaults to 'cursor'.

- ordering  = This should be a string, or list of strings, indicating the field 
agsint which the cursor based pagination will be appplied. For example:
ordering = 'slug'. Defaults to -created. This value may also be overridden by
using OrderingFilter on the view.

template = The name of  a template to use when rendering pagination 
controls in the browsable API. May be overridden to modify the rendering
style, or set to None to disable HTML pagination controls completely.
Defaults to "rest_framework/pagination/previous_and_next.html".

This template is not used the most.
```

## Coding Part of Cursor Pagination

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
from rest_framework.pagination import CursorPagination

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu' # changed the link text
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
from .mypaginations import MyCursorPagination


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination
```

settings.py
```text
for installed apps add api and rest_framework
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentList.as_view()),
]
```

conclusion
```text
Now you can do pagination by clicking next and previous button
```
