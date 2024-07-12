## Custom Authentication

about
```text
To implement a custom authentication scheme, subclass 
BaseAuthentication and override the authenticate(self, request) method.

The method should return a two-tuple of(user, auth) if authentication
succeeds, or None otherwise.
```

## Coding  Part Creating Custom authentication using browseable api

admin.py
```python
from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']    
```

customauth.py
```python
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

# return user or none if authenticated return user or return none
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No Such User')
        return (user, None) 
```

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

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customauth import CustomAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
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
To get all the data
go to the browser and give the username for authentiction

Why to give the username only
```text
That's how we have created our custom authentication 
```
url to hit
```text
http://127.0.0.1:8000/studentapi/?username=superuser
http://127.0.0.1:8000/studentapi/1/?username=superuser
```

Where to get the full code 
```text
CHeck gs29 for the full code
```

Conclusion
```text
Created custom authentication which lets you to access api only 
by the credentials provided you can make any kind of changes in the
code from customauth.py
```
