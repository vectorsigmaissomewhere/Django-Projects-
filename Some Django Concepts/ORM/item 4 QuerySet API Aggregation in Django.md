## Aggregation
```text
sometimes you will need to retrive values that are derived by summarizing or aggregating a 
collection of objects.

aggregate() - It is a terminal clause for a QuerySet that, when invoked, returns a 
dictionary of name-value pairs. The name is an identifier for the aggregate value; 
the value is the computed aggregate. The name is automatically generated from the name 
of the field and the agggregate function.

Syntax:- aggrgate(name=agg_function('field'), name=agg_function('field'),)
field - It describes the aggregate value that we want to compute.
name - If you want to manually specify a name for the aggregate value, you can 
do so by providing that name when you specify the aggregate clause.

annotate() - Per-object summaries can be generated using the annotate() clause.
When an annotate() clause is specified, each object in the QuerySet will be 
annotated with the specified values. The output of the annotate() clause is 
a QuerySet; this QuerySet can be modified using any other QuerySet operation, 
including filter(), order_by(), or even additional calls to annotate().
```

## Aggregation Function
```text
Django provides the following aggregation functions in the django.db.models module.

Avg(expression, output_field=None, distinct=False, filter=None, **extra) - It returns the 
mean value of the given expression, which must be numeric unless you specify a different 
output_filed.

Default alias:<field>__avg

Return type: float if input is int, otherwise same as input filed, or output_field if supplied

Has one optional argument:

distinct: If distince=True, Avg returns the mean value of unique values. This is the SQL 
equivalent of AVG(DISTINCT <field>). The default value is False.

Count(expression, distinct=False, filter=None, **extra) - It returns the number of objects
that are related through the provided expression.
Default alias: <field>__count
Return type: int
Has one optional argument:
distinct - If distince=True, the count will only include unique instance. This is the SQL
equivalent of COUNT(DISTINCT<field>). The default value is False.

Max(expression, output_field=None, filter, **extra) - It returns the maximum value of the 
given expression. 
Default alias: <field>__max
Return type: same as input field, or output_field if supplied

Min(expression, output_field=None, filter=None, **extra) - It returns the minimum value of 
the given expression. 
Default alias: <field>__min
Return type: same as input field, or output_field if suppplied

Sum(expression, output_field=None, distinct=False, filter=None, **extra) - It compute the sum 
of all values of the given expression. 
Default alias: <field>__sum
Return type: same as input field, or output_field if supplied
Has one optional argument:
distinct - If distinct=True. Sum returns the sum of unique values. This is the SQL equivalent
of SUM(DISTINCT <field>).
The default value is False.

StdDev(expression, output_field=None, sample=False, filter=None, **extra) - It returns the 
standard deviation of the data in the provided expression.
Default alias: <field>__stddev
Return type: float if input is int, otherwise same as input field, or output_field if supplied
Has one optional argument:
sample- By default, StdDev returns the population standard deviation. However, if sample=True, 
the return value will be the sample standard deviation. 

Variance(expression, output_field=None, sample=False, filter=None, **extra) - It return value will
be the sample standard deviation.

Variance(expression, output_field = None, sample=False, filter=None, **extra) - It return the 
variance of the data in the provided expression.
Default alias: <field>__variance
Return type: float if input is int, otherwise same as input field, or output_field is supplied
Has one optional argument:
sample - By default, Variance returns the population variance. However if sample=True, the return 
value will be the sample variance.
```
