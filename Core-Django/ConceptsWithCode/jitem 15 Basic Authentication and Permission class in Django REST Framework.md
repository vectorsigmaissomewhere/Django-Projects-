## Why use Authentication and Permission?
```text
Currently our API doesn't have any restrictions on who can edit or delete 
Data.
We'd like to have some more advanced behavior in order to make sure
that:
- Data is always associated with a creator. 
- Only authenticated users may create Data.
- Only the creator of a Data may update or delete it.
- Unauthenticated requests should have full read-only access.
```

Authentication
```text
identifying user credentials or the token that it was signed with.
The permission and throttling policies can then use those 
credentials to determine of the request should be permitted.

Authentication is always run at the very start of the view, 
before the permission and throttling checks occur, and before any 
other code is allowed to proceed.
```

Authentication in Django Rest Framework
```text
REST framework provides a number of authentication schemes out of
the box, and also allows you to implement custom schemes.
Some authentication list provided by DRF :-
- BasicAuthentication
- SessionAuthentication
- TokenAuthentication
- RemoteUserAuthentication
- CustomAuthentication
```

Basic Authentication
```
This authentication scheme uses HTTP Basic Authentication, signed 
against a user's username and password.
Basic authentication is generally only appropriate for testing.
If successfully authenticated, BasicAuthentication provides the following
credentials.
- request.user will be a Django User instance.
- request.auth will be None.

Unauthenticated response that are denied permissio will result in an
HTTP-401 Unauthorized response with an appropriate 
WWW-Authenticate Reader. For example:
```
