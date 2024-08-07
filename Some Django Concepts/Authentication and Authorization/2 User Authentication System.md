## User Authentication System

```text
Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions.

Django authentication provides both authentication and authorization 
together and is generally referred to as the authentication system.

By default, the required configuration is already included in the setting.py
generated by djnago-admin startproject, these consist of two items listed
in your INSTALLED_APPS setting:
'django.contrib.auth' contains the core of the authentication framework, and its default models;.
'django.contrib.contenttypes' is the Django content type system, which allows permissions to be associated with models you create.

and these items in your MIDDLEWARE setting:
SessionMiddleware manages sessions across requests.
AuthenticationMiddleware associates users with request using sessions.
```

## django.contrib.auth
```
in venv
lib\site-packages\django\contrib\auth
models.py
class User
User object - User objects are the core of the authentication system.
Only one class of user exists in Django's authentication framework, i.e.,
'superusers' or admin 'staff users are just user objects with special 
attributes set, not different classes of user objects.
```

What to aspect from this file
```text
- Creating Super Users
- Changing Password
- Authenticating User
- Creating User
- Permissions and Authorization
- Groups
- How to log a user in
- How to log a user out
```

What we learned from here
```text
We can give permission to a certain user by giving certain permission can be given by superuser.

You can add group and give permission to group throught superuser in admin panel
also you can add the user to the group to give permission to other users.
```

Conclusion
```text
Authentication from coding 
Authorization from admin panel mostly
```
 
