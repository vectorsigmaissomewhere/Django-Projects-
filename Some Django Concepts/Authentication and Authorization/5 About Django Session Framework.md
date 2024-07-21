## Django Session Framework

```text
The session framework lets you store and retrieve arbitrary data on a per-site-visitor basics.
It stores data on the server side and abstracts the sending and receiving of cookies.
Cookies contain a session ID not the data itself.

By default, Django stores sessions in your database.
As it stores sessions in database so it is mandatory to run makemigrations and migrate
to use session. It will create required tables.

The Django sessions framework is entirely, and solely, cookie-based.
django.contrib.sessions.middleware.SessionMiddleware
django.contrib.sessions
```

What are the ways in which sessions can be stored?
```text
database-backend sessions- If you want to use a database-backend session, you need to add
'django.contrib.session' to you INSTALLED_APPS setting.

after configuration , hit python manage.py migrate to install the single database that 
stores session data.

file-based sessions - To use file-based sessions, set the SESSION_ENGINE setting to 
"django.contrib.sessions.backends.file".

You might also want to set the SESSION_FILE_PATH setting (which defaults to output from
tempfile.gettempdir(), most likely /tmp) to control where Django stores session files. Be 
sure to check that your Web server has permissions to read and write to this location.

cookie-based sessions - To use cookies -based sessions, set the SESSION_ENGINE setting to 
"django.contrib.sessions.backends.signed_cookies". The session data will be stores using
Django's tools for cryptographic signing and the SECRET_KEY setting.

cached sessions - For better performance, you may want to use a cache-based sesion
backend. To store session data using Django's cache system, you'll first need to make sure
you've configured your cache.
```

Using Sessions in views
```text
When SessionMiddleware is activated, each HttpRequest object, the first argument to any
Django view function will have a session attribute, which is a dictionary-like object.
You can read it and write to request.session at any point in your view. You can edit it
multiple times.

-Set Item 
request.session['key'] = 'value'

- Get Item
returned_value = request.session['key']
returned_value  = request.session['key']

- Delete Item
del request.session['key']
This raises KeyError if the given key isn't already in the sesssion.

- Contains
'key' in request.session
```
