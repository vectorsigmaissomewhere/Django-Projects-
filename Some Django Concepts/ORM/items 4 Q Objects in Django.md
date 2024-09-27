## Q Objects
```text
Q objects is an object used to encapsulate a collection of keyword arguments. These 
keyword arguments are specified as in "Field lookups".
If you need to execute more complex queries, you can use Q objects.
Q objects can be combined using the & and | operators. When an operator is used on 
two Q objects, it yields a new Q object.

from django.db.models import Q

& (AND) Operator
Example:- Student.objects.filter(Q(id=6) & Q(roll=106))

| (OR) Operator
Example:- Student.objects.filter(Q(id=6) | Q(roll=108))

~ Negation Operator
Example:- Student.objects.filter(~Q(id=6))
```
