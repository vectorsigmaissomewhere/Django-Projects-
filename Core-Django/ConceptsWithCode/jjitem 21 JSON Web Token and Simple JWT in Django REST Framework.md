## JSON Web Token(JWT)

We have already studied about
```text
- BasicAuthentication
- SessionAuthentication
- TokenAuthentication
- CustomAuthentication
```

Important Authentication
```text
Third party packages
- Django OAuth Toolkit
- JSON Web Token Authentication-> This is famous one and we will use this
- Hawk HTTP Authentication
- HTTP Signature Authentication
- Djoser
- django-rest-auth/ dj-rest-auth
- django-rest-framework-social-oauth2
- django-rest-knox
- drfpasswordless
```


about json web token(jwt)
```text
JSON Web Token is a fairly new standard which can be used for token-
based authentication. Unliked the build-in TokenAuthentication scheme, 
JWT Authentication doesn't need to use a database to validate a token.

for more info about jwt check: https://jwt.io/
```

Simple JWT
```text
Simple JWT provides a JSON Web Token authentication backend for 
the Django REST Framework. It aims to cover the most common use
cases of JWTs by offering a conservative set of default features. It also
aims to be easily extensible in case a desired feature is not present.

check the below link for more detail:
https://django-rest-framewrok-simplejwt.readthedocs.io/en/latest/
```

How to Install Simple JWT
```text
pip install djangorestframework-simplejwt
```

To use Simple JWT You have to do some configurations
```text
for putting jwt authentication globally 
settings.py
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTCATION_CLASSES':(
	    'rest_framework_simplejwt.authentication.JWTAuthentication',
)}

you can even configure is locally from views.py

urls.py 
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
urlspatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

Verify Jwt Token
```text
You can also include a route for Simple JWT's TokenVerifyView if you wish to 
allow API users to verify HMAC-signed tokens without having access to your 
signing key.

urls.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
urlspatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'), # this is optional , use this when user is sending request and generating token
]
```

JWT Default Settings
```text
from datetime import timedelta
SIMPLE_JWT={
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5), # this means you token will expire in 5 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1), # extra token with expiry date of 1 day
    'ROTATE_REFRESH_TOKENS': False, # setting false you will get only access token, setting it true will give you access token and refresh token
    'BLACKLIST_AFTER_ROTATION': True,
}
```

Some of the important properties 
```text
ACCESS_TOKEN_LIFETIME': A datetime.timedelta object which specifies how 
long access tokens are valid.

REFESH_TOKEN_LIFETIME- A datetime.timedelta object which specifies how 
long refresh tokens are valid.
```

Use JWT
```text
GET Token
http POST http://127.0.0.1:8000/gettoken/ username="user1" password="yourpassword" 


Verify Token
http POST http://127.0.0.1:8000/verifytoken/
token=""
```

Refresh Token
```text
http POST http://127.0.0.1:8000/refreshtoken/
refresh="yourrefreshtoken"
and when you enter you will get access get token


When to use GET Token
when I am registered in the api
but to access the api i need get the token for authentication 

and the server will give the user access token and refresh token
but he forgets or access token gets exipred in that case he will get a 
refresh token 
```

Permission Classes be the same

we will only use IsAuthenticated

check gs30 to get the whole code
## Coding Part 

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
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Router Object
router = DefaultRouter() 

# Register StudentViewSet With Router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # generate token
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'), # gives a new token
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'), 
]
```

what to expect to get token in the command line
```text

Getting the token 
http POST http://127.0.0.1:8000/gettoken/ username="user1" password="#beta123"
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 483
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 12 Jul 2024 20:24:14 GMT    
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4  
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE2MTU0LCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6ImRmYzNkOWIzODIzZTQxZGJiMjEyMzZhNjUxYzc2ZTczIiwidXNlcl9pZCI6Mn0.xgfQOXDOxNyNMyOLKzcrYWJulvZiCIbmJ0bIGuLVWXo",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDkwMjI1NCwiaWF0IjoxNzIwODE1ODU0LCJqdGkiOiJmMzI0ZDFlMWNjZjA0NzlmYTQ4ZmNkOTliNDkyNTQ2MiIsInVzZXJfaWQiOjJ9.tTEc6zYuQoejUoShMhRsewZ40v59Q69_9u5LSNGFVdo"
}

Verifying the token within 5 minute if you have created your token within
5 minutes then you will get ok response

http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE2MTU0LCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6ImRmYzNkOWIzODIzZTQxZGJiMjEyMzZhNjUxYzc2ZTczIiwidXNlcl9pZCI6Mn0.xgfQOXDOxNyNMyOLKzcrYWJulvZiCIbmJ0bIGuLVWXo"
NMyOLKzcrYWJulvZiCIbmJ0bIGuLVWXo";f0b50805-a3f9-416c-82a7-dd65371cd04bHTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 2
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 12 Jul 2024 20:27:24 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{}

Verifying token after 5 minutes

 http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE2MTU0LCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6ImRmYzNkOWIzODIzZTQxZGJiMjEyMzZhNjUxYzc2ZTczIiwidXNlcl9pZCI6Mn0.xgfQOXDOxNyNMyOLKzcrYWJulvZiCIbmJ0bIGuLVWXo"
HTTP/1.1 401 UnauthorizedJ0bIGuLVWXo";f0b50805-a3f9-416c-82a7-dd65371cd04b
Allow: POST, OPTIONS
Content-Length: 65
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 12 Jul 2024 20:32:12 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Accept
WWW-Authenticate: Bearer realm="api"
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "code": "token_not_valid",
    "detail": "Token is invalid or expired"
}

Now , user cannot use the token and access the api
Now, use have two options
- first create a new token i.e gettoken
- second use the refresh token i.e refreshtoken and generate a new access token

Use are using a refresh token

http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMDkwMjI1NCwiaWF0IjoxNzIwODE1ODU0LCJqdGkiOiJmMzI0ZDFlMWNjZjA0NzlmYTQ4ZmNkOTliNDkyNTQ2MiIsInVzZXJfaWQiOjJ9.tTEc6zYuQoejUoShMhRsewZ40v59Q69_9u5LSNGFVdo"
HTTP/1.1 200 OKShMhRsewZ40v59Q69_9u5LSNGFVdo";f0b50805-a3f9-416c-82a7-dd65371cd04b
Allow: POST, OPTIONS
Content-Length: 241
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 12 Jul 2024 20:35:54 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE2ODU0LCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6IjMxZWZiNGVlODcwNjQ5NTc5MmFhYTk2Njc5MGEzMWI2IiwidXNlcl9pZCI6Mn0.vwKF2pfNLw7p1ZJ79FUA3OsREjiIIJHlCR1p6bPnGuw"

If it is again expired he will use the refresh token
```

Get the data using the authentication token
```text
http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE3NTYxLCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6IjdmZDhlMjg4OGE3OTQzNTNiODY0OWU0YzY5ZDVkOTE5IiwidXNlcl9pZCI6Mn0.4LZopBI9hoOfJ4CROa70SMsy9Eb0ErO_snnn2j0vpUQ'
HTTP/1.1 200 OKpBI9hoOfJ4CROa70SMsy9Eb0ErO_snnn2j0vpUQ' ;f0b50805-a3f9-416c-82a7-dd65371cd04b
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 108
Content-Type: application/json
Cross-Origin-Opener-Policy: same-origin
Date: Fri, 12 Jul 2024 20:50:34 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.11.4
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

[
    {
        "city": "Lisbon",
        "id": 1,
        "name": "ronaldo",
        "roll": 101
    },
    {
        "city": "argentina",
        "id": 2,
        "name": "messi",
        "roll": 102
    }
]
```

Insert date
```text
http -f POST http://127.0.0.1:8000/studentapi/ name=rahul roll=102 city=Bokaro 'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwODE3OTExLCJpYXQiOjE3MjA4MTU4NTQsImp0aSI6ImI5ZDA2ZTJkZGI5MzQxNjRiN2QxMGFjMDQzNmY4NDA3IiwidXNlcl9pZCI6Mn0.BAOM6hLll4aEW3XFfVnQXu_Vy-vZ1GEDf8lsxlNBjK0'
```

Conclusion
```text
Here we learned about how JWT Token works
```
