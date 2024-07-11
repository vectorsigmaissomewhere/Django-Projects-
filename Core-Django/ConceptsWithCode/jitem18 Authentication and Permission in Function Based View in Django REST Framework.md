Motive of this example
```text
To show how to implement authentication and permission in function based view in django rest framework
you need to work in models.py , serializers.py , views.py , urls.py and oviously in settings.py
we are not working in each of these files

Here you need to add decorators class to apply authentication and permissions
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.student_api),
    path('studentapi/<int:pk>',views.student_api)
]
```

views.py
```python
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk 
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED) # when ever it shows 201 when created
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # when ever we get error we get this error status code
    
    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data,  partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
```

Get the full code
```text
check gs23 project directory
``


