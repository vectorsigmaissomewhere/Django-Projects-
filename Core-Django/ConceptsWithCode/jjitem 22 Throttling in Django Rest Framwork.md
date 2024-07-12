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


