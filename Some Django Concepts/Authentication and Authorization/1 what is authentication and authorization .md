Types of Authentication Classes

```text
rest_framework.authentication.BaseAuthentication is the super class of all authentication module
These super class authentication have four different type classes:
- BasicAuthentication - validating username and password
- SessionAuthentication - validating session whether logged in
- TokenAuthentication- Remote Auth
- RemoteUserAuthentication - Auth by padding token key
```

Setting Authentication
```text
- Globally for all view at settings.py
- Specific View at Class based View 
- Specific View at Function based View - Decoratorn 
```


## Authentication and Authorization
```text
Authentication - Authentication is about validating your credentials
like Username and password to verify your identity.
Authorization - Authorization is the process to determine whether 
the authenticated user has access to particular resources.
It checks your rights to grant you access to resources such as information, databases, files, etc.

For example we have an application which have a, b, c,d resources
and a user is authenticated to use the application but he is authorized to use a and b resources only means he can only use the authorized resources.
```
