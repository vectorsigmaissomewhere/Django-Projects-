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

