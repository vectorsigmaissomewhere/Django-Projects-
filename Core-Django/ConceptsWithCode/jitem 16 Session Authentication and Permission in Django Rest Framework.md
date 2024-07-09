## Session Authentication
```text
in previous file we learned about Basic Authentication
in this file we are are learning about Session Authentication
```

about
```text
This authentication scheme uses Django's default session backend for 
authentication. Session authentication is appropriate for AJAX clients that 
are running in the same session content as your website.
If successfully authenticaed, Session Authentication provides the
following credentials.
request.user will be a Django User instance.
request.auth will be None.

Unauthenticated responses that are denied permission wil result in an 
HTTP 403 Forbidden response.

If you're using an AJAX style API with SessionAuthentication, you'll need 
to make sure you include a valid CSRF token for any "unsafe" HTTP
method calls, such as PUT, PATCH, POST or DELETE requests.
```

Permission
```text
check previous file to read about this
```

Permission
```
list of permission classes 
- AllowAny , read in previous file
- IsAuthenticated, read in previous file
- IsAdminUser, read in previous file
- IsAuthenticatedOrReadOnly , we will check in this file
- DjangoModelPermissions, we will check in this file
- DjangoObjectPermissions, we will check in this file
- Custom Permissions , we will check in this file
```

check full code in gs21

1 IsAuthenticatedOrReadOnly
```text
The IsAuthenticatedOrReadOnly will allow authenticated users to 
perform any request. Requests for unauthorised users will only be 
permitted if the request method is one of the "safe" method; GET, 
HEAD or OPTIONS.

Very Very Important Note ,
This permission is suitable if you want to your API to allow read
permissions to anonymous uers, and only allow write permissions to 
authenticated users.
```

Example 
```python
permission_classes = [IsAuthenticatedOrReadOnly] 
```

2 DjangoModelPermissions
```text
This permission class ties into Django's standard django.contrib.auth 
model permissions. This permission must only be applied to views that
have a queryset property set. Authorization will only be granted if the 
user is authenticated and has the relevant model permissions assigned.
- POST requests require the user to have the add permission on the
model.
- PUT and PATCH requires the user to have the delete permission on the 
model.
- The default behaviour can also be overridden to support custom model
permissions. For example, you might want to include a view model 
permission for GET requests.

The use custom model permissions, override DjangoModelPermissions 
and set the perms and map property.

note,
the superuser will give permission to a particular user from the admin
panel.
```
 Example
```python
permission_classes = [DjangoModelPermissions]
```

3 DjangoModelPermissionsOrAnonReadOnly
```text
Similar to DjangoModelPermissions, but also allows unauthenticated
users to have read-only access to the API, means anonymous user 
can read the data 
```

What to learn from here
```text
just being authenticated don't allow to do CRUD 
There must be given model permission to do CRUD
```

4 DjangoObjectPermissions
```text
This permission class ties into Django's standard object permissions 
framework that allows per-object permissions on models. In order to use
this permission class, you'll also need to add a permission backend that 
supports object-level permissions, such as django-guardian.

As with DjangoModelPermissions, this permission must only be applied 
to views that have a queryset property or get_queryset() method. 
Authorization will only be granted if the user is authenticated and has 
the relevant per-object permissions and relevant model permissions 
assigned.

- POST requess require the user to have the add permission on the model instance.
- PUT and PATCH and DELETE same thing goes like the POST
```

CODING PART TO KNOW MORE ABOUT PERMISSION Like Model object permission and how anonymous user can read even read

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

views.py
```python
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly # read only to anonymous user, and write permission to authenticated users
from rest_framework.permissions import DjangoModelPermissions # give permission to user from the admin panel
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly # even the anonymous user can read but can't write

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # the below code is to do authentication if it is not made in settings.py or you can mention it globally in settings.py
    authentication_classes = [SessionAuthentication] 
    # permission_classes = [IsAuthenticated] # basics operation permission, only logged in user can perform CRUD
    # permission_classes = [AllowAny] # anyone can allow a particular resource
    # permission_classes = [IsAdminUser] # now is_staff user can only access the resource # not by normal user
    # is_staff should be true to access the resource or make changes in the resource
    # permission_classes = [IsAuthenticatedOrReadOnly] # read only to anonymous user, and write permission to authenticated users
    # permission_classes = [DjangoModelPermissions] # give the permissions from the admin panel, and the user must be authenticated
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # even the anonymous user can read but cannot write
```

Find the full code in 
```text
gs21 
```
