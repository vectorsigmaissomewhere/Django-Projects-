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
