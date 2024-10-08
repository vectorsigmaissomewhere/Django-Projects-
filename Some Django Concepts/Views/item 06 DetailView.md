
DetailView
```text
django.views.generic.detail.DetailView
While this view is executing, self.object will contain the object that the view is operatin g
upon.
This view inherits methods and attributes from the following views:
- django.views.generic.SingleObjectTemplateResponseMixin
- django.views.generic.base.TemplateResponseMixin
- django.views.generic.detail.BaseDetailView
- django.views.generic.detail.SingleObjectMixin
- django.views.generic.base.View
```

SingleObjectTemplateResponseMixin
```text
django.views.generic.detail.SingleObjectTemplateResponseMixin

A mixin class that performs template-based response rendering for views that operate upon a single
object instance. Requires that the view it is mixed with provides self.object, the object instance
that the view is operating on. self.object will usually be, but is not required to be, an instance 
of a Django model. It may be None if the view is in the process of constructing a new instance.

This view inherits methods and attributes from the following views:
- django.views.generic.base.TemplateResponseMixin 

Attribute:- 
template_name_field - The field on the current object instance that can be used to determine the 
name of a candidate template. If either template_name_field itself or the value of the 
template_name_field on the current object instance is None, the object will not be used for a 
candidate template name.

template_name_suffix - The suffix to append to the auto-generated candidate template name. Default
suffix is_detail.

Method:- 
get_template_names() - Returns a list of candidate template names. Returns the following list:
the value of template_name on the view(if provided)
the contents of the template_name_field field on the object instance that the view is operating upon
(if available)
<app_label>/<model_name><template_name_suffix>.html
```

SingleObjectMixin
```text
django.views.generic.detail.SingleObjectMixin
Provides a mechanism for looking up an object associated with the current HTTP request.
Attribute:- 
model - The model that this view will display data for. Specifying model = Student is effectively
the same as specifying queryset = Student.objects.all(), where objects stands for Student's 
default manager. 

queryset - A QuerySet that represents the objects. If provided, the value of queryset supersedes the 
value provided for model.

slug_field - The name of the filed on the model that contains the slug. By default, slug_field is 
'slug'.

slug_url_kwarg - The name of the URLConf Keyword argument that contains the slugs. By default, 
slug_url_kwarg is 'slug'.

Attribute:- 

pk_url_kwarg - The name of the URLConf keyword arguement that contains the primary key. By 
default, pk_url_kwarg is 'pk'.
context_object_name - Designates the name of the variable to use in the context.
query-pk_and_slug - If True, causes get_object() to perform its lookup using both the primary key 
and the slug. Defaults to False.

Methods:- 
get_object(queryset=None) - Returns the single object that this view will display. If queryset is 
provided, that queryset will be used as the source of objects; otherwise, get_queryset() will be 
used. get_object() looks for a pk_url_kwarg argument in the arguments to the view; if this 
argument is found, this method performs a primary-key based lookup using that value. If this 
argument is not found, it looks for a slug_url_kwarg argument, and performs a slug lookup using the 
slug_field.

When query_pk_and_slug is True, get_object() will perform its lookup using both the primary key and 
the slug.

get_queryset() - Returns the queryset that will used to retrieve the object that this view will 
display. By default, get_queryset() returns the value of the queryset attriute if it is set, 
otherwise it constructs a QuerySet by calling the all() method on the model attribute's default 
manager. 

get_slug_field() - Returns the name of a slug field to be used to look up by slug. By default this 
returns the value of slug_field.

get_context_object_name(obj) - Returns the context variable name that will be used to contain the 
data that this view is manipulating. If context_object_name is not set, the context name will be 
constructed from the model_name of the model that the queryset is composed from. For example, the 
model Article would have context object name 'article'

get_context_data(**kwargs) - Returns context data for displaying the object.
The base implementation of this method required that the self.object attribute be set by the view 
(even if None). Be sure to do this if you are using the mixin without one of the built-in views that 
does so.

It returns a dictionary with these contents:
object: The object that this view is displaying(self.object).
```

DetailView with Default Template & Context 
```python
# views.py
from django.views.generic.detail import DetailView
from .models import Student 
class StudentDetailView(DetailView):
    model = Student 

# urls.py
urlpatterns = [
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student'),
]

# Default Template
Syntax:- AppName/ModelClassName_detail.html 
Example:- school/student_detail.html 

# Default Context
Syntax:- ModelClassName 
Example:= student 
```

DefaultView with Custom Template & Context 
```python 
# views.py
from django.views.generic.detail import DetailView 
from .models import Student 
class StudentDetailView(DetailView):
    model = Student 
    template_object_name = 'student/student.html' # custom template name 
    context_object_name = 'student' # custom context name 

# urls.py
urlpatterns = [
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student'),
] 
```
