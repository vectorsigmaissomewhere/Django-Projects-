## Token Authentication in Django REST Framework

we have studied 
```text
-  BasicAuthentication
- SessionAuthentication
- TokenAuthentication [Today]
```

about TokenAuthentication
```text
This authentication scheme uses  a simple token-based HTTP Authentication
scheme. Token authentication is appropriate for client-server setups, such as
native desktop and mobile clients

To use the Token Authentication scheme you'll need to configure the 
authentication classes to include TokenAuthentication, and additionally 
include rest_framework.authtoken in your INSTALLED_APPS setting:

INSTALLED_APPS = [
..
'rest_framework.authtoken',
]
```

Note
```text
Make sure to run manage.py migrate after changing your settings. The 
rest_framework.authtoken app provides Django database migrations.
```

What happens when Token Authentication successfully works
```text
If successfully authenticated, Token Authentication provides the following 
credentials.
request.user will be a Django User instance.
request.auth will be a rest_framework.authtoken.models. Token instance.

Unauthenticated responses that are denied permission will result in an
HTTP 401 Unauthorized response with an appropriate WWW-Authenticate
header. For example:
WWW-Authenticate: Token

The http command line tool may be useful for testing token authenticated
APIs. For example:

http http://127.0.0.1:8000/studentapi/'Authorization: Token
9944b09199c62bcf9418ad846dd0e4bbfc6ee4b'
if token is valid or not for authorization
```

Note
```text
If you use TokenAuthentication in production you must ensure that your API
is only available over https.
```

How to Generate Token
```text
- Using Admin Application
- Using Django manage.py command 
i.e python manage.py drf_create_token<username> - This command will
return API Token for the given user of Creates a Token if token doesn't exist
for user.
- By exposing an API endpoint
- Using Signals
```

the rest of the code came from gs21

1 Generate Token of a user from admin panel
```text
as you add 'rest_framework.authtoken' in your settings file 
you need to migrate the database 
after migrating go to the admin panel 
Now, you better know what to be done 
```

2 Generate Token using Django manage.py command
How to do it from terminal
```text
python manage.py drf_create_token username 
``

How Client can Ask/Create Token
```text
When using TokenAuthentication, you may want to provide a mechanism for
clients to obtain a token given the username and password.

REST framework provides a built-in view to provide this behavior. To use it, 
add the obtain_auth_token view to your URLconf:

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
	path('gettoken/',obtain_auth_token)
]

The obtain_auth_token view will return a JSON reponse when valid 
username and password fields are POSTED to the view using form data
or JSON:

http POST http://127.0.0.1:8000/gettoken/ username='name' password='pass'
{'token':'503b87b454e6fa35059ddeb01170b5ed0ad98be5'}

It also generates token if the token is not generated for the provided user.
```

3 Generate Token by exposing an API Endpoint
```text
pip install httpie
type in terminal
http POST http://127.0.0.1:8000/gettoken/ username="user1" password="#beta123"
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 52
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 11 Jul 2024 23:33:35 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "token": "fe4f9d672816e98886c345ccbd520f729bf210e6"
}

```
summary till now 
```text
Check the above code in gs25 
make changes in urls.py, views.py and settings.py and hit the above command 
```
Where to find the code till now
```text
Check the file gs24 , gs25 and gs26 to get the full code till code
```

Coding Part Generate Token by exposing an API Endpoint

admin.py
```python
from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
```

auth.py
```python
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # the below code is to do authentication if it is not made in settings.py or you can mention it globally in settings.py
    # authentication_classes = [SessionAuthentication] 
    # permission_classes = [IsAuthenticated] # basics operation permission, only logged in user can perform CRUD
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
    'rest_framework.authtoken',
    'api',
]
```

urls.py
```python
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken

# Creating Router Object
router = DefaultRouter() 

# Register StudentViewSet With Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')), #browseable api url in drf for login logout, provides option to login and logout
    path('gettoken/',CustomAuthToken.as_view())
]
```

what to hit in command line
```text
http POST http://127.0.0.1:8000/gettoken/ username="superuser" password="superuser"
HTTP/1.1 200 OK     
Allow: POST, OPTIONS
Content-Length: 91  
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Thu, 11 Jul 2024 23:58:46 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Vary: Cookie
X-Content-Type-Options: nosniff
Vary: Cookie
Vary: Cookie
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "email": "ambani@gmail.com",
    "token": "aa437336c22e121cde6444f6120307b8916aacf7",
    "user_id": 1
}
```
