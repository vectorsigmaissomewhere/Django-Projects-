Custom Permissions
```text
To implement a custom permission, override BasePermission and 
implement either, or both, of the following methods:
- has_permission(self, request, view)
- has_object_permission(self, request, view, obj)
The method should return True if the request object be granted access
and False otherwise.
```

How to make this done
```text
first create file name custompermissions.py
```
coding example
```python
class MyPermission(BasePermission):
    def has_permission(self, request, view)
```

Coding Example

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated # making IsAuthenticated ours in custompermissions.py
from .custompermissions import MyPermission 

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # the below code is to do authentication if it is not made in settings.py or you can mention it globally in settings.py
    authentication_classes = [SessionAuthentication] 
    permission_classes = [MyPermission] # custom permission
```

myapp/custompermission.py
```python
from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET': # if request is GET you get the permission to access the API
            return True # true means you are giving permission to access the api
        return False
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
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')), #browseable api url in drf for login logout, provides option to login and logout
]
```

Note
```text
Research more about Custom Permission in Django REST framework
```
