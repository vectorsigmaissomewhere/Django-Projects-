## SearchFilter

about
```text
The SearchFilter class supports simple single query parameter based
searching, and is based on the Django admin's search functionality.

The SearchFilter class will only be applied if the view has a search_fields
attribute set. The search_fields attribute should be a list of names of text
type fields on the model, such as CharField or TextField.
```

How to use SearchFilter
```python
from rest_framework.filters import SearchFilter
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['city']
```

how to make request in browseable api
```text
http://127.0.0.1:8000/studentapi/?search=lisbon
hitting this url I will get all the Students who are from lisbon
```

where to find the fill code
```text
check gs35
```

## 1 Coding part in using SearchFilter

settings.py
```python
INSTALLED_APPS = [
    'rest_framework',
    'api',
    'django_filters',
]
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
]
```

admin.py
```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'passby']
```

models.py
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    passby = models.CharField(max_length=50) # teacher who checked result
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city', 'passby']
```

What to hit in browseable api
```text
This will give the data of all the user that belongs to the city lisbon
http://127.0.0.1:8000/studentapi/?search=lisbon
```

## More about search 
SearchFilter

```text
- '^' Starts-with search.
- '=' Exact matches.
- '@' Full-text search. (Currently only suported Django's PostgreSQL backend.)
- '$' Regex search.
```

Example:-
```text
search_fields = ['^name^',]

http://127.0.0.1:8000/studentapi/?search=r
```

views.py
```python
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    #search_fields = ['city'] # search data based on city
    #search_fields =['name','city'] # search based on name or city 
    #search_fields = ['^name'] # get that name that belong to a character 
    search_fields = ['=name'] # this should be equally match 
```


## Changing the url from search to q

url before
```text
http://127.0.0.1:8000/studentapi/?search=
```

url now 
```text
http://127.0.0.1:8000/studentapi/?q
```

To do this 
setting.py 
```text
REST_FRAMEWORK = {
    'SEARCH_PARAM': 'q'
}
```

To get the full code
```text
check gs35
```
