## Cookies

about
```text
A cookie is a small piece of text data set by Web server that resided on the client's machine.
Once it's been set, the client automatically retuns the cookie to the web servce with each 
request that is makes.
This allows the server to place value it wishes to 'remember' in the cookie, and have 
access to them when creating a response. 
```

How Cookie works
```text
hotel example
client goes to a hotel
hotel doesn't know about the client information
client gives his information to the hotel
hotel saves the information and gives the client an id
so when ever the user goes to the hotel , it recognizes the id
and the hotel gives all the services.

even the theme is stored in the computer
the web server checks the cookie and give the theme to the user compuer
```

Django Cookies
```text
HttpRequest.COOKIES - A dictionary containing all cookies. Keys and values are strings.
set_cookie() - set_cookie is used to set/create/sent cookies.
Syntax: - HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
domain = None, secure=False, samesite=None)
Example:- set_cookie("name","sonam")
key - This is the name of the cookie.
value- This sets the value of cookie. This value is stored on the clients computer.
name and value are requried to set cookie. 

if you value is given to optional paramters: default value is given 
```

Creating Cookies
```text
max_age- It should be a number of seconds, or None(default) if the cookie should last
only as long as the client's browser session. If expires is not specified, it will be calculated.
Example:- set_cookie("name","sonam", max_age=60*60*24*10) // 10 days

expires - It describes the time when cookie will be expire. It should either be a string in 
the format "Wdy, DD-Mon-YY HH:MM:SS GMT" or a datetime.datatime object in UTC. If
expires is a datetime object, the max_age will be calculated.

Example: - set_cookie("name","sonam", expires=datetime.utcnow() + timedelta(days=2))

path - Path can be / (root) or /mydir(directory).
Example:- set_cookie("name", "sonam","/")
Example:- set_cookie("name","sonam","/home")
```

About domain
```text
domain - Use domain if you want to set a cross-domain cookie. For example, 
domain="example.com" will set a cookie that is readable by the domains 
www.example.com, blog.example.com, etc. Otherwise, a cookie will only be readable by 
the domain that set it.

Example:- set_cookie("name","sonam", domain="geekyshows.com")

cookie in subdomain
Example:- set_cookie("name","sonam","code.geekyshows.com")


secure - Cookie to only be transmitted over secure protocol as https. When set to True, 
the cookie will only be set if a secure connection exists.
Example: - set_cookie("name", "sonam",max_age=60*60*24*10, path="/", 
domain="geekyshows.com", secure=True)

httponly - Use httponly=True if you want to prevent client-side JavaScript from having 
access to the cookie.

HttpOnly is a flag included in a Set-Cookie HTTP response header. It's part of the RFC 6265
standard for cookie and can be a useful way to mitigate the risk of a client-side script
accessing the protected cookie data.
Example:- set_cookie("name","sonam", max_age=60*60*24*10, httponly=True)

samesite - Use samesite='Strict' or samesite='Lax' to tell browser not to send this cookie
when performing a cross-origin request. Samesite isn't supported by all browsers, so it's
not a replacement for Django's CSRF protection, but rather a defense in depth measure.

RFC 6265 states that user agents should support cookies of at least 4096 bytes. For many 
browsers this is also the maximum size. Django will not raise an exception if there's an 
attempt to store a cookie of more than 4096 bytes, but many browsers will not set the 
cookie correctly.

Example: -set_cookie("name","sonam",samesite='Strict')
```

Reading /Accessing Cookie
```text
HttpRequest.COOKIES - A dictionary containing all cookies. Keys and values are strings.
Syntax:- request.COOKIES['key'];
Example:- request.COOKIES['name'];

Syntax:- request.COOKIES.get('key',default)
Example:- request.COOKIES.get('name')
Example:- request.COOKIES.get('name',"Guest")
```

Replace/AppendCookies
```text
When we assign a new value to cookie, the current cookie are not replaced. The new 
cookie is parsed and its name-value is appended to the list. The expection is when you 
assign a new cookie with the same name(and same domain and path, if they exist) as a 
cookie that already exists. In this case the old value is replaced with the new.

Examples:- 

- set_cookie("name", "sonam") --------
			              ---------------------Replace
   set_cookie("name","rahul")----------

- set_cookie("name", "sonam") ---------
			               ---------------------Append
   set_cookie("lnam","jha")---------------
```

Deleting Cookies
```text
HttpResponse.delete_cookie(key, path='/', domain=None) - This method is used to delete
the cookie based on given key with same domain and path, if they were set, otherwise
the cookie may not be deleted.

Example:- delete_cookie('name')
``


## Creating Signed Cookies
```text
HttpResponse.set_signed_cookie(key, value, salt=", max_age=None, expires = None, 
path='/', domain=None, secure =False, httponly=False, samesite=None)

It is similar to set_cookie(), but cryptographic signing the cookie before setting it. Use in
conjunction with HttpRequest.get_signed_cookie().

You can use the optional salt argument for added key strength, but you will need to 
remember to pass it to the corresponding HttpRequest.get_signed_cookie() call.
```


Getting Signed Cookies
```text
HttpRequest.get_signed_cookie(key, default=RAISE_ERROR, salt=", max_age=None)
It returns a cookie value for a signed cookie, or raises a django.core.signing.BadSignature
exception if the signature is no longer valid.

If you provide the default argument the exception will be suppressed and that default 
value will be returned instead.

The optional salt argument can be used to provide extra protection against brute force 
attacks on your secret key. If supplied, the max_age argument will be checked against 
the signed timestamp attached to the cookie value to ensure the cookie is not older
 than max_age seconds.
```

## Coding Part 

settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'student',
]
```

urls.py
```python
from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.setcookie),
    path('get/',views.getcookie),
    path('del/', views.delcookie),
]
```

templates\student\delcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete Cookie</title>
</head>
<body>
    <h4>Delete Cookie........</h4>
</body>
</html>
```
templates\student\getcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GET COOKIE</title>
</head>
<body>
    <h4>Get Cookie</h4>
    {{name}}
</body>
</html>
```

templates\student\setcookie.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Cookie</title>
</head>
<body>
    <h4>Cookie Set.........</h4>
</body>
</html>
```

views.py
```python
from django.shortcuts import render
from datetime import datetime, timedelta

# this the code to set cookies
def setcookie(request):
    response = render(request, 'student/setcookie.html') # renders setcookie.html when cookie is set
    """set cookies"""
    #response.set_cookie('name', 'sonam')
    # response.set_cookie('name', 'sonam', max_age=120) # after 120 second the cookie will expire
    # response.set_cookie('name', 'sonam', expires=datetime.utcnow()+timedelta(days=2)) # the cookie will expire after 2 days 
    """set signed cookies"""
    response.set_signed_cookie('name', 'sonam',salt='nm', expires=datetime.utcnow()+timedelta(days=2)) 
    return response

# get the cookie value
def getcookie(request):
    """get cookies """
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', "Guest") # if name key is not available it will show guest
    """get signed cookies"""
    name = request.get_signed_cookie('name',default="Guest", salt='nm')
    return render(request, 'student/getcookie.html', {'name':name}) #sending name to the getcookie.html 

# delete the cookie value
def delcookie(request):
    response = render(request, 'student/delcookie.html') # render delcookie to delete cookie
    response.delete_cookie('name') 
    return response
```

Cookies Security Issues
```text
- Can misuse client details
- Can track User
- Client Can Delete Cookies
- Client can Manipulate Cookie
```
Cookies Limitation
```text
- Each cookie can contain 4096 bytes Data
- Cookies can be stores in Browser and server
- It is sent with each request
```
