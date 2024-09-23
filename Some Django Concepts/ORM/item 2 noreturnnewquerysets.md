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


update_or_create(defaults=None, **kwargs) - A convenience method for updating an object with the
given kwargs, creating a new one if necessary. The defaults is a dictionary of (field, value) pairs
used to update the object. The values in defaults can be callables.

It returns a tuple of (object, created), where object is the created or updated object and created is a
boolean specifying whether a new object was created.

The update_or_create method tries to fetch an object from database based on the given kwargs. If a 
match is found, it updates the fields passed in the defaults dictionary.

Example:-
student_data, created = Student.objects.update_or_create(id=14, name='Kohli', defaults={'name':'Sameer'})

bulk_create(objs, batch_size=None, ignore_conficts=False) - This method inserts the provided list 
of objects into the database in an efficient manner.
The method's save() method will not be called, and the pre_save and post_save signals will not be sent.
It does not work with child models in a multi-table inheritance scenario.
If the model's primary key is an AutoField it does not retrieve and set the primary key attribute, 
as save() does, unless the database backend supports it(currently PostgreSQL).
It does not work with many-to-many relationships.
It casts objs to a list, which fully evaluates objs if it's a generator. The cast allows inspecting 
all objects so that any objects with a manually set primary key can be inserted first.
The batch_size parameter controls how many objects are created in a single query. The default is to 
create all objects in one batch, except for SQLite where the default is such that at most 999 variables
per query are used.
On databases that support it (all but Oracle),setting the ignore_conflicts parameter to True tells the 
database to ignore failure to insert any rows that fail constraints such as duplicate unique values. 
Enabling this parameter disables setting, the primary key on each model instance.
Example:-
objs = [
    Student(name='Sonal', roll=120, city='Dhanbad', marks=40, pass_date='2020-5-4),
    Student(name='Kunal', roll=121, city='Dumka', marks=50, pass_date='2020-5-7'),
    Student(name='Anisa', roll=122, city='Giridih', marks=70, pass_date='2020-5-9')
]
Student_data = Student.objects.bulk_create(objs)

bulk_update(objs, fields, batch_size=None) - This method efficiently updates the given fields
on the provided model instances, generally with one query. QuerySet.update() is used to save 
the changes, so this is more efficient than iterating through the list of models and calling 
save() on each of them.

You cannot update the model's primary key.

Each model's save() method isn't called, and the pre_save and post_save signals aren't sent.

If updating a large number of columns in a large number of rows, the SQL generated can be very 
large. Avoid this by specifying a suitable batch_size.

Updating fields defined on multi-table inheritance ancestors will incur an extra query per ancestor.

If objs contains duplicates, only the first one is updated.

The batch_size parameter controls how many objects are saved in a single query. The default is to 
update all objects in one batch, except for SQLite and Oracle which have restrictions on the 
number of variables used in a query. 
Example :- 
all_student_data = Student.objects.all()
for stu in all_student_data:
    stu.city = 'Bhel'
    student_data =Student.objects.bulk_update(all_student_data, ['city'])



in_bulk(id_list=None, field_name='pk') - It takes a list of field values(id_list) and the field_name
for those values, and returns a dictionary mapping each value to an instance of the object wih the 
given field value. If id_list isn't provided, all objects in the queryset are returned. field_name 
must be a unique filed, and it defaults to the primary key.

Example:- 
student_data = Student.objects.in_bulk([1,2])
print(student_data[1].name)
print()
student_data1 = Student.objects.in_bulk([])
print(student_data1)
print()
student_data2 = Student.objects.in_bulk()
print(student_data2)


delete() - The delete method, conveniently, is named delete(). This method immediately delete the 
object and returns the number of objects deleted and a dictionary with the number of deletions per
object type.

Example:- 
Delete One Record
student_data = Student.objects.get(pk=22)
deleted = student_data.delete()

Delete in bulk
You can also delete objects in bulk. Every QuerySet has a delete() method, which deletes all members of 
that QuerySet.
Example:- student_data = Student.objects.filter(marks=50).delete()

Delete All Records
Example:- student_data = Student.objects.all().delete()



count() - It returns an integer representing the number of objects in the database matching the 
QuerySet. A count() call performs a SELECT COUNT(*) behind the scenes.
Example:-
student_data = Student.objects.all()
print(student_data.count())


explain(format=None, **options) - use to analyze query
Example:- print(Student.objects.all().explain)

aggregate(*args, **kwargs)
as_manager()
iterator(chunk_size=2000)
```
