Cache

What is Cache?
```text
A Cache, is an information technology for the termporary storage(caching) 
of Web documents, such as Web pages, images, and other types of Web 
multimedia, to reduce server lag.

Caching is one of those methods which a website implements to become 
faster. It is cost efficient and saves CPU processing time.

Django comes with a robust system that lets you save dynamic pages so 
they don't have to be calculated for each request.
```

What you can cache in Django?
```text
You can cache the output of specific views, you can cache only the pieces 
that are difficult to produce, or you can cache your entire site.
```

Following are the options of caching:-
```text
- Database Caching
- File System Caching
- Local Memory Caching
```

How Cache Works
```text
First condition, 
Imagine you have a single web page
WebPage -------------> Cache(Server checks if there is webpage in the cache)
If there is cache then it send the web page

Second condition,
Image you have a single web page
WebPage----------> Cache(Here there is no webpage in the cache)
In this case WebPage is generated and the generated page is saved in the cache 
So that next time it can response page faster 
```

How to implement Caching
```text
- The per-site cache- Once the cache is set up, the simplest way to use caching
is to cache your entire site.
- The per-view cache- A more ganular way to use the caching framework is by caching 
the output of individual views.
- Template fragement caching - This gives you more control what to cache.
```

The per-site cache
```text 
The per-site cache - Once the cache is set up, the simplest way to use caching is to 
cache your entire site.
For doing this, 
This middleware should be in order 
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    ]

CACHE_MIDDLEWARE_ALIAS - The cache alias to use for storage
CACHE_MIDDLEWARE_SECONDS - The number of seconds each page should be cached.
CACHE_MIDDLEWARE_KEY_PREFIX - If the cache is shared across multiple sites using the 
same Django installation, set this to the name of the site, or some other string that is 
unique to this Django instance, to prevent key collisions. Use an empty string if you 
don't care.
```

Database Caching
```text
Django can store its cached data in your database. This works best if you've got a fast, 
well-indexed database server.

CACHES = {
    'default': {
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table', # name of the database table
    }
}

Before using the database cache, you must create the cache table with this command:
python manage.py createcachetable

This creates a table in your database that is in the proper format that Django's 
database-cache system expects.
The name of the table is taken from LOCATION.

If you are using multiple database caches, createcachetable creates one table for 
each cache.
```

Cache Arguments
```text
Each cache backend can be given additional arguments to control caching behavior.

TIMEOUT: The default timeout, in seconds, to use for the cache. This argument
defaults to 300 seconds (5 minutes). You can set TIMEOUT to None so that, by 
default, cache keys never expire. A value of 0 causes keys to immediately
expire(effictively "don't cache").

OPTIONS: Any options that should be passed to the cache backend. The list of valid 
options will vary with each backend, and cache backends backed by a third-party
library will pass their options directly to the underlying cache library.

Cache backends that implement their own culling strategy(i.e., the locmen, filesystem 
and database backends) will honor the following options: 

MAX_ENTRIES: The maximum number of entries allowed in the cache before old values
are deleted. This argument defaults to 300.


CULL_FREQUENCY: The fraction of entries that are culled when MAX_ENTRIES is reached.
The actual ratio is 1/ CULL_FREQUENCY, so set CULL_FREQUENCY to 2 to cull half the entries 
when MAX_ENTRIES is reached. This argument should be an integer and defauls to 3.

A value of 0 for CULL_FREQUENCY means that the entire cache will be dumpled when 
MAX_ENTRIES is reached. On some bckends (database in particular) this makes culling 
much faster at the expenses of more cache misses.
```
Example of Cache Arguments
```text
CACHES = { 
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache'
       'LOCATION':'enroll_cache',
       'TIMEOUT':60,
       'OPTIONS':{
            'MAX_ENTRIES':1000
            }
       }
    }
```
