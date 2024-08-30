The Per View Caching in Django
```text
The per-view cache - A more granular way to use the caching 
framework is by caching the output of individual views. 
django.views.decorators.cache defines a cache-page decorator
that will automatically cache the view's response. If multiple
URLs point at the same view, each URL will be cached seperately.


from django.views.decorators.cache import cache_page
@cache_page(timeout, cache, key_prefix)
def my_view(request):
    

timeout - The cache timeout, in seconds.
cache - This directs the decorator to use a specific cache( from 
your CACHES settings when caching view results. By default, the
default cache will be used.
key_prefix - You can also override the cache prefix on a per-view
basis. It works in the same way as the 
CACHE_MIDDLEWARE_KEY_PREFIX setting for the middleware.
```

Specifying per-view cache in the URL cont
```python
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('route/', cache_page(timeout, cache, key_prefix)(view_function)),
]

urlpatterns = [
    path('home/', cache_page(60)(views.home),name="home"),
]
````

Database Caching
```text
Django can store its cached data in your database. This works best if you've
got a fast, well-indexed database server.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table', # the name of the database table
        }
     }

Before using the database cache, you must create the cache table with this command:
python manage.py createcachetable

This creates a table in your database that is in the proper format that Django's
database-cache system expects.
This name of the table is taken from LOCATION.

If you are using multiple database caches, createcachetable creates one table for
each cache.
```
