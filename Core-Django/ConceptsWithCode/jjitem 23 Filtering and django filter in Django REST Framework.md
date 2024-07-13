## Filtering

about
```text
The simplest way to filter the queryset of any view that subclasses 
GenericAPIView is to override the .get_queryset() method.
```

## Coding Part where there are students where their marks been checked by certain user that is user1 and user2
```text
what the program is
if user1 logs in only the user1 will see the data of students that he have checked likewise,
if user2 logs in only the user2 will see the data of students that he have checked
We are using browsable api for it
```

settings.py
```text
register rest_framework and api
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

views.py
```python
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user # current user goes to user
        return Student.objects.filter(passby=user) # getting data of only the current user that is logged in
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

where to find the full code
```text
gs33
```


## Coding get the data of user who lives in a certain city, we are setting it globally

settings.py
```python
INSTALLED_APPS = [
'api',
'django_filters',
'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS':['django_filters.rest_framework.DjangoFilterBackend'],
}
```

views.py
```python
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['city']
```

## Coding set filter in view only 

views.py
```python
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend] # mentioning filter locallly 
    filterset_fields = ['city']
    # filterset_fields  = ['name','city'] # for multiple fields
```
