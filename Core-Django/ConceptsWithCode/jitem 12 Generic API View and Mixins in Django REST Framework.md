# Generic API View and Mixins in Django REST Framework 

about
```text
we will use whatever that is made in rest_framework

This class extends REST framework's APIView class, adding commonly
required behavior for standard list and detail views.

Attributes:
queryset - The queryset that should be used for returning objects from this view.
 Typically, you must either set this attribute, or override the get_queryset() method.
If you are overriding a view method, It is important that you can get_queryset() instead of
accessing this property directly, as queryset will get evaluated once, those results will be
cached for all subsequent requests.
means use this attribute and set objects or use the methods to set the object

serializer_class - The serializer class that should be used for validating and
deserializing input, and for serializing output. Typically, you must either set this attribute,
or override the get_serializer_class() method.

lookup_field - The model field that should be used to for performing object lookup of
individual model instances. Defaults to 'pk'.

lookup_url_kwarg - The URL keyword argument that should be used for object lookup.
 The URL conf should include a keyword argument corresponding to this value.
If unset this defaults to using the same value as lookup_field.

pagination_class  - The pagination class that should be used when paginating list results.
Defaults to the same value as the DEFAULT_PAGINATION_CLASS setting, which is 'rest_framework.pagination.
PageNumberPagination'.Setting pagination_class = None will disable pagination on this view.

filter backends  - A list of filter backend classes that should be used for filtering the queryset.
Defaults to the same value as the DEFAULT FILTER BACKENDS setting.
```

Methods
```text
get_queryset(self) - It returns the queryset that should be used for list views,
and that should be used as the base for lookups in detail views. Defaults to returning the queryset
specified by the queryset attribute.

This method should always be used rather than accessing self.queryset directly,
as self.queryset gets evaluated only once, and those results are cached for all subsequent requests.

get_objects(self) - It returns an object instance that should be used for detail views.
 Defaults to using the lookup_field parameter to filter the base queryset. 

get_serializer_class(self) - It returns the class that should be used for the serializer.
 Defaults to returning the serializer_class attribute.

get_serializer_context(self) - It returns a dictionary containing any extra context
 that should be supplied to the serializer. Defaults to including 'request'.'view' and 'format' keys.

get_serializer(self, instance = None, data = None, many = False, partial = False) -
It returns a serializer instance.

get_paginated_response(self, data) - It returns a paginated style Response object.

paginated_queryset(self, queryset) - Paginate a queryset if required, either returning a page object,
 or None if pagination is not configured for this view.

filter_queryset(self, queryset) - Given a queryset, filter it with whichever filter backends are in use,
returning a new queryset.
```

about method
```text
most of the methods are automatically generated and implemented
but if you need some modification you make chnage in get_queryset().
```

what is queryset()
```text
returing all data of a table at a time
```

Mixins
