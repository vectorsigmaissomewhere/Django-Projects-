## ModelViewSet Class

ModelViewSet & ReadOnlyModelViewSet

CRUD API only in 3 lines

about
```text
The ModelViewSet class inherits from GenericAPIView and includes
implementations for various actions, by mixing in the behavior of the 
various mixin classes.
The actions provided by the ModelViewSet class are list(), retrieve(),
create(), update(), partial_update(), and destroy. You can use any of the 
standard attributes or method overrides provied by GenericAPIView
```

How to use ModelViewSet 
```python
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

here too we are using routers for url
only work with view


## ModelViewSet Class Coding 
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
]
```

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```


## ReadOnlyModelViewSet Class

about
```text
The ReadOnlyModelViewSet class also inherits from GenericAPIView. As
with ModelViewSet it also includes implementations for various actions,
but unlike ModelViewSet only provides the 'read-only' actions, list() and
retrieve(). You can use any of the standard attributes and method overrides available to GenericAPIView.

Means you can write list and retrieve the model 
you cannot post, update and delete.
```

How to use
```python 
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

## ReadOnlyModelSet Coding

urls.py
```python
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter() 

# Register StudentViewSet With Router
router.register('studentapi', views.StudentReadOnlyModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
```

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

Conclusion
```text
You have to make changes in urls.py and views.py only in both of the examples and everything is similar to jitem13

check full code from gs18 or gs19
```
