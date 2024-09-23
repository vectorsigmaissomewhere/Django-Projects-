## Method that do not return new QuerySets

Retrieving a single object
```text
get() - It returns one single object. If There is no result match it will raise 
DoesNotExist exception. If more than one item matches the get() query. It will 
raise MultipleObjectsReturned.
Example :- Student.objects.get(pk=1)

first() - It returns the first object matched by the queryset, or None if there
is no matching object. If the QuerySet has no ordering defined, then the queryset 
is automatically ordered by the primary key.
Example :- Studdent.objects.order_by('name').first()

last() - It returns the last object matched by the queryset, or None if there is
no matching object. If the QuerySet has no ordering defined, then the queryset is
automatically ordered by the primary key.

latest(*fields) - It returns the latest object in the table based on the given field(s).
Example:- student_data = Student.objects.latest('pass_date')

```
