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

```
