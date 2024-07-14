## Hyperlinked Model Serializer

about
```text
Provides a hyper link for each of the model object
```

admin.py
```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
```

models.py
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','roll','city']
```

views.py
```python
from django.shortcuts import render
from .serilalizers import StudentSerializer
from .models import Student
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```

urls.py
```python
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
```

to see the internal structure of Hyperlinked Model Serializer
```text
in your commandline type
python manage.py shell

from api.serializers import StudentSerializer
serializer = StudentSerializer()
print(repr(serializer))
```

To find  the full code
```
check gs42
```
