## Throttling

about
```text
Throttling is similar to permissions, in that it determines if a request should 
be authorized. Throttles indicate a temporary state and are used to control
the rate of requests that clients can make to an API.

Your API might have a restrictive throttle for unauthentictaed requests, and 
as less restrictive throttle for authenticated requests.
```

configuration for throttling
```text
The default throtling policy mat be set globally using the 
DEFAULT_THROTTLE_CLASSES and DEFAULT_THROTTLE_RATES settings. For 
example.
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
         ' rest_framework.throttling.UserRateThrottle',
      ],
      'DEFAULT_THROTTLE_RATES':{
            'anon':'100/day',
            'user':'1000/day'
}
```

Some of the classes of throttling
```text
- AnonRateThrottle
- UserRateThrottle
- ScopedRateThrottle
```

AnonRateThrottle
```text
The AnonRateThrottle will only ever throttle unauthenticated users. The IP
address of the incoming request is used to generate a unique key to throttle
against.
The allowed request rate is determined from one of the following (in order 
of preference).
The rate property on the class, which may be provided by overriding 
AnonRateThrottle and setting the property.
The DEFAULT_THROTTLE_RATES['anon'] setting.
AnonRateThrottle is suitable if you want to restrict the rate of requests from
unknown sources.
```

UserRateThrottle
```text
The UserRateThrottle will throtlle users to a given rate of requests across
the API. The user id is used to generate a unique key to throttle against.
Unauthenticated requests will fall back to using the IP address of the 
incoming request to generate a unique key to throttle against.

The allowed request rate is determined from one of the following (in order
of preference).

The rate property on the class, which may be provied by overriding 
UserRateThrottle and setting the property.
```

ScopedRateThrottle
```text
The ScopedRateThrottle class can be used to restrict access to specific parts
of the API. This throttle will only be applied if the view that is being accessed
includes a throttle_scope property. The unique throttle key will then be 
formed by concatenating the "scope" of the request with the unique used id 
or IP address.
```


## 1 Coding part to show how AnonRateThrottle and UserRateThrottle works

about the program 
```
This program will let anonymous user to make only 2 request in a day
and an authenticate user to make 5 request in an hour

Here you need to take care of views.py ,setttings.py and urls.py cause the rest
of the program is similar to other program 
```

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
```

settings.py
```python
REST_FRAMEWORK= {
    'DEFAULT_THROTTLE_RATES':{
        'anon': '2/day', # for anonymous user
        'user': '5/hour',
    }
}
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

admin.py
```python
from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
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

## Coding to Set Throtttling for each of the user here for user can make 3 request per minute

settings.py
```python
REST_FRAMEWORK= {
    'DEFAULT_THROTTLE_RATES':{
        'anon': '2/day', # for anonymous user
        'user': '5/hour',
        'jack': '3/minute',
    }
}
```

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from api.throttling import JackRateThrottle

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]    
```

throttling.py
```python
from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle):
    scope = 'jack'
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

Where to find code till now

```text
Check the above code in gs31
```

## Coding throttling in each of the view sets 
```text
This program shows how many times a user can use a particular function in a day , hour or minute
we are using browseable api for this
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
from rest_framework.generics import ListAPIView # used for getting data
from rest_framework.generics import CreateAPIView # used for creating post
from rest_framework.generics import RetrieveAPIView # used for getting data according to id
from rest_framework.generics import UpdateAPIView # used to updating data according to id 
from rest_framework.generics import DestroyAPIView # used to delete data according to id 
from rest_framework.throttling import ScopedRateThrottle # used to throttle in each view 

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu' # only 5 request per hour for this view

class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu' # only 5 request per hour for this view

class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'
```

settings.py
```python

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'viewstu': '5/hour',
        'modifystu': '2/day',
    }
}
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from api import views

from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('studentapi/', views.StudentList.as_view()), # url for views 
    path('studentapi/', views.StudentCreate.as_view()), # url to make post
    #path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()), # url for getting data
    #path('studentapi/<int:pk>/', views.StudentUpdate.as_view()), # used for updating data
    #path('studentapi/<int:pk>/',views.StudentDestroy.as_view()), # used to deleting data
]
```

Conclusion 
```text
Get the full code from gs31 and gs32
We learned about how we can reduce the request made by user in our api using throttling
```
