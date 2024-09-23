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

earliest(*fields) - It returns the earliest object in the table based on the 
given field(s).
Example:- student_data = Student.objects.earliest('pass_date')

exists() - It returns True if the QuerySet contains any result, and False if not.
This tries to perform the query in the simplest and fastes way possible, but it does
execute nearly the same query as a normal QuerySet query.
Example:- 
student_data = Student.objects.all()
print(student_data.exists()) 

create(**kwargs) - A convenience method for creating an object and saving it all one step.
Example:- 
To save data 
first way - 
s = Student(name='Sameer', roll=112, city='Bokaro' marks=60, pass_date='2020-5-4')
s.save(force_insert=True)
second way - 
s = Student.objects.create(name='Sameer', roll=112, city='Bokaro', marks=60, pass_date='2020-5-4')

get_or_create(defaults=None, **kwargs) - A convenience method for looking up an object with the
given kwargs (may be empty if your model has defaults for all fields), creating one if necessary.
It returns a tuple of (object, created), where object is the retrieved or created object and 
created is a boolean specifying whether a new object was created.
Example:-
student_data, created = Student.objects.get_or_create(name='Sameer', roll=112, city='Bokaro', marks=60, pass_date = '2020-5-4')
print(student_date, created)

update(**kwargs) - Performs an SQL update query for the specified fields, and returns the number of 
rows matched(which may not be equal to the number of rows updated if some rows already have the 
new value)
Example:-
student_data = Student.objects.filter(id=12).update(name='Kabir', marks=80)

# Update student's city Pass who has marks 60
student_data = Student.objects.filter(marks=60).update(city='Pass')

student_data = Student.objects.get(id=12).update(name='Kabir', marks=80)
```
