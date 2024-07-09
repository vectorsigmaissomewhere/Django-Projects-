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
