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
Program number 1 

Set, Get, Delete session in Django 

sessionframework/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@^236mkp)-7q(!w(ql)iaseo!f_ax--^a-^*ijo177t^^o72kv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sessionframework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sessionframework.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

sessionframework/urls.py
```python
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('del/', views.delsession),
]
```

student/templates/student/delsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Session</title>
</head>
<body>
    <h1>You session has been deleted successfully</h1>
</body>
</html>
```

student/templates/student/getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}}
    {{lname}}
</body>
</html>
```

student/templates/student/setsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Session</title>
</head>
<body>
    <h1>Session setting up...........</h1>
</body>
</html>
```

student/views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'rathore'
    return render(request, 'student/setsession.html')

def getsession(request):
    # name = request.session['name']
    name = request.session.get('name', default='Guest')
    lname = request.session.get('lname', default='Guest')
    return render(request, 'student/getsession.html', {'name': name, 'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request, 'student/delsession.html')
```

about this code
```text
This code set, get and delete session.
Where in session it stores name and lname
```

where to find the full code
```text
check sessionframework folder
```

 Session Methods
```text
keys() method returns a view object that displays a list of all the keys 
in the dictionary 
Syntax:- dict.keys()

items() method returns  the list with all dictionary keys with values.
Syntax:- dict.items()

clear() function is used to erase all the elements of list. After this operarion,
 list becomes empty.
Syntax:- dict.clear()

setdefault() method returns the value of a key(if the key is in dictionary). 
If not, it inserts key with a value to the dictionary.
Syntax: dict.setdefault(key, default_value)

flush()- It deletes the current session data from the session and delets the session cookie.
This is used if you want to ensure that the previous session data can't be accessed again 
from the user's browser(for example, the django.contrib.auth.logout() function calls it).
```

Program number 2 
```text
- Here we will only work on views.py and getsession.html
The rest of the program is similar to program number 1
The new thing about this program is we have used flush method and other dictionary methods
```
views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session['lname'] = 'Ronaldo'
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')
    return render(request, 'student/getsession.html', {'name': name,'lname': lname, 'keys': keys, 'items': items, 'age': age})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
        # you can use sesion.flush() to remove all the sessions can delete all the session in single line of code 
        # request.session.flush()
    return render(request, 'student/delsession.html')
```
getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}}
    {{lname}}<br><hr>
    <!--How to get session key-->
    {% for key in keys %}
    {{key}} 
    {% endfor %}<br><hr>
    {% for item in items %}
    {{item}}
    {% endfor %}<br><hr>
    {% for key, value in items %}
    {{key}} {{value}}
    {% endfor %}
</body>
</html>
```
where to find the full code 
```text
check sessionframework2 folder 
```

Session Methods
```text
- get_session_cookie_age() - It returns the age of session 
cookies, in seconds. Defaults to SESSION_COOKIE_AGE.
- set_expiry(value) - It sets the expiration time for the sesion.
You can pass a number of different values:
  If value is an integer, the session will expire after that many 
   seconds of inactivity. For example, calling 
   request.session.set_expiry(300) would make the session 
   expire in 5 minutes.

  If value is a datetime or timedelta object, the session will expire
  at the specific date/time. Note that datetime and timedelta 
   values are only serializable if you are using the PickleSerializer.

  If value is 0, the user's session cookie will expire when the 
   user's Web browser is closed.
  If value is None, the session reverts to using the global session 
   expiry policy.
  Reading a session is not considered activity for expiration  
  purposes. Session expiration is computed from the last time 
  the session was modified.

- get_expiry_age() - It returns the number of seconds until this 
  session expires. For sessions with no custom expiration
   (or those set to expire at browser close), this will equal
   SESSION_COOKIE_AGE.
   This function accepts two optional keyword argumets:
    modification: last modification of the session, as a datetime
        object. Defaults to the current time
    expiry: expiry information of the session, as a datetime object,
       an int (in seconds), or None. Defaults to the value stored in 
       the session by set_expiry(), if there is one, or None.

- get_expiry_date() - It returns the date this session will expire.
    For sessions with no custom expiration(or those set to expire
     at browser close), this will equal the date 
     SESSION_COOKIE_AGE seconds from now.
 
     This function accepts the same keyword arguments as 
       get_expiry_age()

- get_expire_at_browser_close()- It returns either True or False, 
    depending on whether the user's session cookie will expire 
     when the user's Web browser is closed.

- clear_expired()- It removes expired sessions from the session 
     store. This class method is called by clearsessions.
```


Program number 3
```text
Learn about session timeout
Every single code is similar to program number 1 only changed part will be placed here
```
sessionframework3/student/templates/student/delsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Session</title>
</head>
<body>
    <h1>You session has been deleted successfully</h1>
</body>
</html>
```
sessionframework3/student/templates/student/getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}} <br>
    {{ request.session.get_session_cookie_age }} seconds <br>
    {{ request.session.get_expiry_age }} seconds <br>
    {{ request.session.get_expiry_date }} <br>
    {{ request.session.get_expiry_at_browser_close }} <br>
</body>
</html>
```
sessionframework3/student/templates/student/setsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Session</title>
</head>
<body>
    <h1>Session setting up...........</h1>
</body>
</html>
```

views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600) # expiry date set for 30 seconds
    # request.session.set_expiry(0) # expires when the browser is closed 
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() # remove the session from the database
    return render(request, 'student/delsession.html')
```

where to find the full code
```text
check sessionframework3
``

Program number 4
```text
The rest of the code will be similar to program number 3
Here we learned about cookies
```
Session Methods
```text
set_test_cookie() - It sets a test cookie to determine whether the user's browser
supports cookies. Due to the way cookie work, you won't be able to test this until
the user's next page request.

test_cookie_worked() - It returns either True or False, depending on whether the 
user's browser accepted the test cookie. Due to the way cookies work, you'll have
to call set_test_cookie() on a previous, seperate page request.

delete_test_cookie() - It deletes the test cookie. Use this to clean up after yourself.
```
sessionframework4/urls.py
```python
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.settestcookie),
    path('check/', views.checktestcookie),
    path('del/', views.deltestcookie),
]
```
student/templates/student/checktestcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Check Test Cookie</title>
</head>
<body>
    <p>Check Test Cookie</p>
    {{request.session.test_cookie_worked}}
</body>
</html>
```
student/templates/student/deltestcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Cookie</title>
</head>
<body>
    <h1>Your cookie has been deleted successfully</h1>
</body>
</html>
```
student/templates/student/settestcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Test Cookie</title>
</head>
<body>
    <h1>Set Test Cookie..........</h1>
</body>
</html>
```

views.py
```python
from django.shortcuts import render

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')
```

Where to find the full code
```text
check sessionframework4
```

Program number 5
```text
Here we will work on session settings
```

Session Settings
```text
SESSION_CACHE_ALIAS - If you're using cache-based session storage, this selects the 
cache to use. Default: 'default'

SESSION_COOKIE_AGE - The age of session cookie, in seconds. Defaults: 1208600 
(2 weeks, in seconds)

SESSION_COOKIE_DOMAIN - The domain to use for session cookies. Set this to a 
string such as "example.com". for cross-domain cookies, or use None for 
standard domain cookie.

Be cautious when updating this setting on a production site. If you update this
setting to enable cross-domain cookies on a site that previously used standard 
domain cookies, existing user cookies will be set to the old domain. This may 
result in them being unable to log in as long as these cookies persist.
Default: None

SESSION_COOKIE_HTTPONLY - Whether to use HttpOnly flag on the session cookie. 
If this is set to True, client-side JavaScript will not be able to access the session
cookie. 

HttpOnly is a flag included in a Set-Cookie HTTP response header. It's part of the 
RFC 6265 standard for cookies and can be a useful way to mitigate the risk of a 
client-site script accessing the protected cookie data.

This makes it less trival for an attacker to escalate a cross-site scripting 
vulnerablity into full hijacking of a user's session. There aren't many good 
reasons for turing this off. Your code shouldn't read session cookie from 
Javascript Default: True

SESSION_COOKIE_NAME - The name of the cookie to use for sessions. This can
be whatever you want(shouldn't be same as other cookie in your application). 
Default: 'sessionid'

SESSION_COOKIE_PATH - The path set on the session cookie. This should either
match the URL path of your Django installation or be parent of that path.

This is useful if you have multiple Django instances running under the same 
hostname. They can use different cookie path, each instance will only see its 
own session cookie. Default '/'

SESSION_COOKIE_SAMESITE - The value of the SameSite flag on the session 
cookie. This flag prevents the cookie from being sent in cross-site requests 
thus preventing CSRF attacks and making some methods of stelaing session
cookie impossible.
Possible values for the setting are:
'Strict' : prevents the cookie from being sent by the browser to the target 
site in all cross-site browsing context, even when following a regular link.

For example, for a GitHub-like website this would mean that if a 
logged-in-user follows a link to  a private Github project posted on a 
corporate discussion forum or email, GitHub will not receive the session
cookie and the user won't be able to access the project. A blank website, 
however, most likely doesn't want to allow any transactional page to be 
linked from external sites so the 'Strict' flag would be appropriate.

'Lax' (default): provides a balance between security and usability for 
websites that want to maintain user's logged-in session after the user
arrives from an external link.

In the Github scenario, the session cookie would be allowed when 
following a regular link from an external website and be blocked 
in CSRF-prone request methods(e.g. POST).

None: disables the flag.


SESSION_COOKIE_SECURE - Whether to use a secure cookie for the 
session cookie. If this is set to True, the cookie will be marked as 
"secure", which means browsers may ensure that the cookie is only sent 
under an HTTPS connection.

Leaving this setting off isn't a good idea because and attacker could capture
an unencrypted session cookie with a packet sniffer and use the cookie 
to hijack the user's session. Default: False


SESSION_ENGINE - Controls where Django stores session data. 
Included engines are: 
'django.contrib.sessions.backends.db'
'django.contrib.sessions.backends.file'
'django.contrib.sessions.backends.cache'
'django.contrib.sessions.backends.cached_db'
'django.contrib.sessions.backends.signed_cookies'
'Default: 'django.contrib.sessions.backends.db'


SESSION_EXPIRE_AT_BROWSER_CLOSE - Whether to expire the sesion when 
the user closes their browser. Default: False

SESSION_FILE_PATH - If you're using file-based session storage, this sets the 
directory in which Django will store session data. When the default value(None)
is used, Django will use the standard temporary directory for the system. 
Default: None

SESSION_SAVE_EVERY_REQUEST - Whether to save the session data on every request.
If this is False(default), then the session data will only be saved if it has been modified
that is, if any of its dictionary values have been assigned or deleted. Empty sessions
won't be created, even if this setting is active. Default: False

SESSION_SERIALIZER - Full import path of a serializer class to use for serializing session data. 
Included serializers are:
'django.contrib.sessions.serializers.PickleSerializer'
'django.contrib.sessions.serializers.JSONSerializer'
Default: 'django.contrib.sessions.serializers.JSONSerializer'
```
sessionframework5/settings.py
```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+s5seozzxdz@44k2rcjk22u0enzi=suq+@(yw(yop(2t$)o&#1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sessionframework5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sessionframework5.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_COOKIE_AGE = 400 # session created for 400 seconds
SESSION_COOKIE_NAME = 'sessionname' # sessionid name changed
SESSION_COOKIE_PATH = '/home' # change session path, default is root
SESSION_COOKIE_HTTPONLY = True # you can't access cookie from client side using javscript
SESSION_COOKIE_SECURE = True # cookie is secured, session hijacking, session sniffing can't be done
# SESSION_ENGINE = 'django.contrib.sessions.backends.file' # file based 
SESSION_EXPIRE_AT_BROWSER_CLOSE = True # even if the browser closes the session is expired
# SESSION_SAVE_EVERY_REQUEST
# SESSION_SERIALIZER that is json serializer
```

student/templates/student/delsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Session</title>
</head>
<body>
    <h1>You session has been deleted successfully</h1>
</body>
</html>
```

student/templates/student/getsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <p>Your name from the session</p>
    {{name}} <br>
    {{ request.session.get_session_cookie_age }} seconds <br>
    {{ request.session.get_expiry_age }} seconds <br>
    {{ request.session.get_expiry_date }} <br>
    {{ request.session.get_expiry_at_browser_close }} <br>
</body>
</html>
```

student/templates/student/setsession.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Session</title>
</head>
<body>
    <h1>Session setting up...........</h1>
</body>
</html>
```

views.py
```python
from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    request.session.set_expiry(600) # expiry date set for 30 seconds
    # request.session.set_expiry(0) # expires when the browser is closed 
    return render(request, 'student/setsession.html')

def getsession(request):
    name = request.session['name']
    return render(request, 'student/getsession.html', {'name': name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() # remove the session from the database
    return render(request, 'student/delsession.html')
```


