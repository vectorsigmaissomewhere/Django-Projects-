## Token Authentication in Django RESTC Framework

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
