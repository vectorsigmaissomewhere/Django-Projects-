QuerySet API
```text
A QuerySet can be defined as a list containing all those objects we have 
created using the Django model.
QuerySets allow you to read the data from the database, filter it and order it.

query property - This property is used to get sql query of query set.
Syntax - queryset.query
```

Methods that return new QuerySets
```text
1. Retrieving all objects
all() - This method is used to retrieve all objects. This returns a copy of 
current QuerySet.
Example: - Student.objects.all()

2. Retrieving specific objects
filter(**kwargs) - It returns a new QuerySet containing objects that match the
given lookup paramters. filter() will always give you a QuerySet, even if only
a single object matches the query.
Example: - Student.objects.filter(marks=70)

3. exclude(**kwargs) - It returns a new QuerySet containing objects that do not match
the given lookup parameters.
Example: Student.objects.exclude(marks=70)

4. order_by(*fields) - It orders the fields.
- 'field' - Asc order
- '-field' - Desc order
- '?' - Randomly

5. reverse() - This works only there is ordering in queryset

6. values(*fields, **expression) - It returns a QuerySet that returns dictionaries, rather than
model instances, when used as an iterable. Each of those dictionaries reprsents and object, with
the keys corresponding to the attribute names of model objects.

```
