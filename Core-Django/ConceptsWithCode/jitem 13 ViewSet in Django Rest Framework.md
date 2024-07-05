## ViewSet

about
```text
Django REST Framework allows you to combine the logic for a set
of related views in a single class, called a ViewSet.

There are two main advantages of using a ViewSet over using a View class.
- Repeated logic can be combined into a single class.
- By using routers, we no longer need to deal woth wiring up the URL conf ourselves.
means router gives url
```

## Some classes

ViewSet Class

about
```text
A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as get() or post(), and instead provides actions such as list() and create().
- list() -> Get All Records
- retrieve() -> Get Single Record
- create() -> Create/Insert Record
- update() -> Update Record Completely
- partial_update() -> Update Record Partially
- destroy() -> Delete Record
```

How to make ViewSet class
```python
from rest_framework import viewsets
class StudentViewSet(viewsets.ViewSet):
    def list(self, request): ................
    def create(self, request): .....................
    def retrieve(self, request, pk = None): ........................
    def update(self, request, pk = None): ..............
    def partial_update(self, request, pk = None): ................
    def destroy(self, request, pk = None): ....................
```

ViewSet CLass
```text
During dispatch, the following attributes are available on the ViewSet: -
- basename - the base to use for the URL names that are created.
- action - the name of the current action(e.g., list, create).
- detial - boolean indicating if the current action is configures for a list or detail
- suffix - the display suffix for the viewset type - mirrors the detail attribute
- name - the display name for the viewset. This argument is mutually exclusive to suffix.
- description - the display description for the individual view of a viewset.
```

ViewSet - URL Config
```python 
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # creating default router object
router.register('studentapi', views.StudentViewSet, basename = 'student') # register StudentViewSet with Router
urlpatterns = [
    path('', include(router.urls)), # The API URLS are now determined automatically by the router
]
```

## CODING PART
views.py
```python
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        id = pk 
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updateed'})
        return Response(serializer.errors)
    
    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
```

urls.py
```python
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter() 

# Register StudentViewSet With Router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
```
Also, If you want to get more information of the view request use the below code in every method
```python
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("*********Retrieve************")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)
```
## What is different here
```text
Use of routers
Why routers?
Before we had jungles of urls, means lots of urls
what router does is, it help us to create less urls
In this code we only have one url that is ''
Also you don't have to create a seperate paramter in url for other methods
```

Conlusion
```text
the code in this section is same as jitem12
and here we made changes in views.py and urls .py only
Used routers as it made the url less in compared to jitem 12
```
