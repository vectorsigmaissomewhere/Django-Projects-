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

7. distinct(*fields) - This eliminates duplicate rows from the query results.

8. values_list(*fields, flat=False, named=False) - This is similar to values() except that instead of
returning dictionaries, it returns tuples when iterated over.
- If you don't pass any values to values_list(), it will return all the fields in the model, in the
order they were declared.
- If you only pass in a single field, you can also pass in the flat parameter. If True, this will mean
the returned results are single values, rather than one-tuples.
- You can pass named=True to get results as a namedtuple

9. using(alias) - This method is for controlling which database the QuerySet will be evaluated against if
you are using more than one database. The only argument this method takes is the alias of a database,
as defined in DATABASES.
Example:- student_data = Student.objects.using('default') # 'default' is the database name

10. dates(field, kind, order='ASC') - It returns a QuerySet that evaluates to a list of datetime date objects
representing all available dates of a particular kind within the contents of the QuerySet.
Where,
field - It should be the name of a DateField of your model.
kind - It should be either "year", "month", "week", or "day".
"year" returns a list of all distinct year values for the field.
"month" returns a lit of all distinct year/month values for the field.
"week" returns a list of all distinct year/month values for the field. All dates will be on Monday.
"day" returns a list of all distinct year/month/day values for the field.
order - It should be either 'ASC' or 'DESC'. This specifies how to order the results. defaults to 'ASC'
Each datetime date object in the result list is "truncated" to the given type.

11. datetimes(field_name, kind, order='ASC', tzinfo=None) - It returns a QuerySet that evaluates to
a list of datetime.datetime objects representing all available dates of a particular kind within the contents
of the QuerySet.
Where,
field - It should be the name of a DateField of your model.
kind - It should be either "year", "month", "week", or "day".
"year" returns a list of all distinct year values for the field.
"month" returns a lit of all distinct year/month values for the field.
"week" returns a list of all distinct year/month values for the field. All dates will be on Monday.
"day" returns a list of all distinct year/month/day values for the field.
order - It should be either 'ASC' or 'DESC'. This specifies how to order the results. defaults to 'ASC'
tzinfo - It defines the time zone to which datetimes are converted prior to truncation. This parameter
must be a datetime.tzinfo object. If it's None, Django uses the current time zone. It has no effect
when USE_TZ is False.
Each datetime date object in the result list is "truncated" to the given type.

12. none() - Calling none() will create a queryset that never returns any objects and no query will
be executed when accessing the results. A qs.none() queryset is an instance of EmptyQuerySet.
Example :- student_data = Student.objects.none()

13. union(*other_qs, all=False) - Uses SQL's UNION operator to combine the results of two or more QuerySets.
The UNION operator selects only distinct values by default. To allow duplicate values, use the all=True
argument.

14. intersection(*other_qs) - Uses SQL's INTERSECT operator to return the shared elements of two or more
QuerySets.
Example :- student_data = qs1.intersection(qs2)

15. difference(*other_qs) - Uses SQL's EXCEPT operator to keep only elements present in the QuerySet but
not in some other QuerySets.
Example :- student_data = qs1.difference(qs2)

Less used query methods

16. select_related(*fields)
17. defer(*fields)
18. only(*fields)
19. prefetch_related(*lookups)
20. extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)
21. select_for_update(nowait=False, skip_located=False, of=())
22. raw(raw_query, params=None, translations=None)
23. annotate(*args, **kwargs)
```

Operators that return new QuerySets
```text
AND(&) - Combines two QuerySets using the SQL AND operator.
Example:-
student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
student_data = Student.objects.filter(id=6, roll=106)
student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

OR(|) - Combines two QuerySets using the SQL OR operator.
Example:-
Student.objects.filter(id=11) | Student.objects.filter(roll=106)
Student.objects.filter(Q(id=11) | Q(roll=106))
```
