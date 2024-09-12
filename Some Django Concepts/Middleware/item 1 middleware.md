## Middleware
```text
Middleware is a framework of hooks into Django's request/response
processing.
It's a light, low-level "plugin" system for globally altering Django's input
or output. Each middleware component is responsible for doing some
specific function.

- Built in Middleware , this is already present and we are using it
- Custom Middleware
```

How Middleware Works
```text
Middleware means something in between 
user sent a request middleware checks if it is valid or not 
if valid the request is sent to the required views 


There can be more than one middleware 
```

Function based Middleware
```text
A middleware factory is a callable that takes a get_response callable
and returns a middleware.
A middleware is a callable that takes a request and returns a response,
just like a view.

def my_middleware(get_response):
    # One-time configuration and initialization
    def my_function(request):
        # Code to be executed for each request before the view are called
        response = get_response(request)
        # Code to be executed for each request/response after the view is called
        return response
```

get_response()
```text
The get_response callable provided by Django might be the actual view
(if this is the last listed middleware) or it might be the next middleware
in the chain.
The current middleware doesn't need to know or care what exactly it is, just
that it represents whatever comes next.

The get_response callable for the last middleware in the chani won't be the actual
view but rather a wrapper method from the handle which takes care of applying
view middleware, calling the view with appropriate URL arguments, and applying
template-response and exception middleware.

Middleware can live anywhere on your Python path.
```

Activating Middleware
```text
To activate a middleware component, add it to the MIDDLEWARE list in your Django settings.
In MIDDLEWARE, each middleware component is represented by a string: the full Python path
to the middleware factory's class or function name. The order in MIDDLEWARE matters because a
middleware can depend on other middleware. For instance, AuthenticationMiddleware stores the
authenticated user in the session; therefore, it must run after SessionMiddleware.

Eg.-
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.middleware.SessionMiddleware',
    'blog.middlewares.my_middleware'
    ]

```
