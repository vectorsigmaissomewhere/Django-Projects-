## Field Lookups
```text
Field lookups are how you specify the meet of an SQL WHERE clause.
They're specified as keyword arguemnts to the QuerySet methods filter(), exclude() and get().
If you pass an invalid keyword argument, a lookup function will raise TypeError.
Syntax:- field__lookuptype=value
Example:- Student.objects.filter(marks__It='50')
SELECT * FROM myapp_student WHERE marks< '50';

The field specified in a lookup has to be the name of a model field.
In case of a ForeignKey you can specify the field name suffixed with
_id. In this case, the value parameter is expected to contain the raw 
value of the foreign model's primary key.
Example:- Student.objects.filter(stu_id=10)

exact - Exact match. If the value for comparison is None, it will be 
interpreted as an SQL NULL. This is case sensitive
Example:- Student.objects.get(name__exact='sonam')

iexact - Exact match. If the value provided for comparison is None, it 
will be interpreted as an SQL NULL. This is case insensitive.
Example:- Student.objects.get(name__iexact='sonam')

contains - Case-sensitive containment test.
Example:- Student.objects.get(name__contains='kumar')

icontains - Case-insensitive containment test.
Example:- Student.objects.get(name__contains='kumar')

in - In a given iterable; often a list, tuple, or queryset. 
It's not a common use case, but strings(being iterables) are accepted.
Example:- Student.objects.filter(id__in=[1,5,7])

gt - Greater than.
Example:- Student objects.filter(marks__gt=50)

gte - Greater than or equal to.
Example:- Student.objects.filter(marks__gte=50)

It - Less than.
Example:- Student.objects.filter(marks__It=50)

Ite - Less than or equal to.
Example:- Student.objects.filter(marks__Ite=50)

startswith - Case-sensitive starts-with
Example:- Student.objects.filter(name__startswith='r')

istartswith - Case-insensitive starts-with
Example:- Student.objects.filter(name__istartswith='r')

endswith - Case-sensitive ends-with.
Example:- Student.objects.filter(name__istartswith='r')

iendswith - Case-insensitive ends-with.
Example:- Student.objects.filter(name__iendswith='j')

range - Range test(inclusive).
Example:- Student.objects.filter(passdate_range=('2020-04-01','2020-05-05'))
SQL:- SELECT ... WHERE admission_date BETWEEN '2020-04-01' and '2020-05-05;
You can use range anywhere you can use BETWEEN in SQL --- for dates, numbers and even character.

date - For datetime fields, casts the value as data. Allows chaining additional field lookups. 
Take a data value.
Example:- 
Student.objects.filter(admdatetime__date = date(2020,6,5))
Student.objects.filter(admdatetime__date__gt = date(2020, 6, 5))

year - For date and datetime fields, and exact year match. Allows chaining additional field lookups.
Takes an integer year.
Example:-
Student.objects.filter(passdate__year=2020)
Student.objects.filter(passdate__year__gt=2019)

month - For date and datetime fields, an exact month match. Allows chaining additional field lookups.
Takes an integer 1 (January) through 12 (December).
Example:- 
Student.objects.filter(passdate__month=6)
Student.objects.filter(passdate__month__gt=5)

day - For date and datetime fields, an exact day match. Allows chaining additional field lookups. Takes
an integer day. 
Example:- 
Student.objects.filter(passdate__day=5)
Student.objects.filter(passdate__day__gt=3)
This will match any record with a pub_date on the third day of the month, such as January 3, July 3, 
etc.

week - For data and datetime fields, return the week number(1-52 or 53) according to ISO-8601, i.e.. 
weeks start on a Monday and the first week contains the year's first Thursday.
Example:-
Student.objects.filter(passdate__week=23)
Student.objects.filter(passdate__week__gt=22)

week_day - For date and datetime fields, a 'day of the week' match. Allows chaining additional field 
lookups. 
Takes an integer value representing the day of week from 1 (Sunday) to 7 (Saturday).
Example:- 
Student.objects.filter(passdate__week_day=6)
Student.objects.filter(passdate__week_day__gt=5)

This will match any record with a admission_date that falls on a Monday(day 2 of the week), regardless 
of the month or year in which it occurs. Week days are indexed with day 1 being Sunday and day 7 being 
Saturday.

quarter - For data and datetime fields, a 'quater of the year' match. Allows chaining additional field
lookups. Takes an integer value between 1 and 4 representing the quarter of the year.
Example to retrieve entries in the second quarter (April 1 to June 30):
Student.objects.filter(passdate__quarter=2)

time - For datetime fields, casts the value as time. Allows chaining additional field lookups. Takes a 
datetime.time value. 
Example:- Student.objects.filter(admdatetime__time__gt=time(6,00))

hour - For datetime and time fields, an exact hour match. Allows chaining additional field lookups. 
Takes an integer between 0 and 23.
Example:- Student.objects.filter(admdatetime__hour__gt=5)

minute - For datetime and time fields, an exact minute match. Allows chaining additional field lookups.
Takes an integer between 0 and 59.
Example:- Student.objects.filter(admdatetime__minute__gt=50)

second - For datetime and time fields, and exact second match. Allows chaining additional field lookups.
Takes an integer between 0 and 50.
Example:- Student.objects.filter(admdatetimer__second__gt=30)

isnull = Takes either True or False. which correspond to SQL queries of IS NULL or IS NOT NULL,  
repectively.
Example:- Student.objects.filter(roll_isnull=False)

regex
iregex
```
