Class Based APIView

about
```text
Rest framework provides and APIView class, which subclasses Django's View class.
Difference Between APIView classes and regular View classes:
- Requests passed to the handler method will be REST framework's Request instances, not Django's HttpRequest instances.
- Handler methods may return REST framework's Response, instead of Django's HttpResponse. The view will manage content negotiation and setting the correct renderer on the response.
- Any APIException exceptions will be caught and mediated into apprpriate responses.
- Incoming request will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.
```

About the code
```python
from rest_framework.views import APIView
class StudentAPI(APIView):
    def get(self,request, format = None):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
```

## CODING PART

class based apiview in django rest framework example with browseable api

models.py
```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
```

serializers.py
```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']        
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentAPI.as_view()), # as it is class based api views
    path('studentapi/<int:pk>',views.StudentAPI.as_view()),
]
```

settings.py
```python
...
INSTALLED_APPS = [
    ....
    'rest_framework',
    'api',
]
```

admin.py
```python
from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
```

views.py
```python
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
class StudentAPI(APIView):
    def get(self, request, pk = None, format=None):
        id = pk 
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED) # when ever it shows 201 when created
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # when ever we get error we get this error status code
    
    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,  partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self, request, pk, format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
```

urls to hit in browser
```text
http://127.0.0.1:8000/studentapi/

program flow
urls.py  - views.py  - serializers.py - returns responed in browser
```

