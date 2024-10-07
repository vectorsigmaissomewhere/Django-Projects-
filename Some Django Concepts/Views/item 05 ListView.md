
Class Based View
```text
Class-based views provide an alternative way to implement views as Python objects instead of 
functions.
They do not replace function-based views.
- Base Class-Based Views/ Base View
- Generic Class-Based Views / Generic View
```

Base Class-Based View
```text
Base class-based views can be thought of as parent views, which can be used by themselves or 
inherited from. They may not provide all the capabilities required for projects, in which case 
there are Mixins which extend what base views can do. 
- View 
- TemplateView
- RedirectView
```

Generic Class Based View
```text
Django's generic views are built off of those base views, and were developed as a shortcut for common
usage patterns such as displaying the details of an object.
They take certain common idioms and patterns found in view development and abstract them so that 
you can quickly write common views of data without having to repeat yourself.

Most generic views require the queryset key, which is a QuerySet instance
- Display View - ListView, DetailView 
- Editing View - FormView, CreateView, UpdateView, DeleteView
- Date Views - ArchiveIndexView, YearArchiveView, MonthArchiveView, WeekArchiveView, 
DayArchiveView, TodayArchiveView, DateDetailView


The two following generic class-based views are designed to display data.
- ListView 
- DetailView 
```

ListView
```text
django.views.generic.list.ListView 
A page representing a list of objects.
While this view is executing, self.object_list will contain the list of objects(usually, but not
necessarily a queryset) that the view is operating upon.

This view inherits methods and attributes from the following views:
- django.views.generic.list.MultipleObjectTemplateResponseMixin  ##
- django.views.generic.base.TemplateResponseMixin 
- django.views.generic.list.BaseListView 
- django.views.generic.list.MultipleObjectMixin      ##
- django.views.generic.base.View 
```

MultipleObjectTemplateResponseMixin
```text
A mixin class that performs template-based response rendering for views that operate upon a list of 
object instances. Required that the view it is mixed with provides self.object_list, the list of 
object instances that the view is operating on. self.object_list may be, but is not required to be, 
a QuerySet. 
This inherits methods and attributes from the following views:
- django.views.generic.base.TemplateResponseMixin 
Attribute:- 
template_name_suffix - The suffix to append to the auto-generated candidate template name. Default 
suffix is _list.
Method:- 
get_template_names() - It returns a list of candidate template names. 
```

BaseListView 
```text
A base view for displaying a list of objects. It is not intended to be used directly, but rather 
as a parent class of the django.views.generic.list.ListView or other views representing lists of 
objects.
This view inherits methods and attributes from the following views:
- django.views.generic.list.MultipleObjectMixin 
- django.views.generic.base.View 

Methods:-
get(request, *agrs, **kwargs) - It adds object_list to the context. If allow_empty is True
then display an empty list. If allow_empty is False then raise a 404 error.
```

MultipleObjectMixin
```text 
django.view.generic.list.MultipleObjectMixin
A mixin that can be used to display a list of objects. 
If paginate_by is specified, Django will paginate the results returned by this. You can specify 
the page number in the URL in one of two ways:

Use the page parameter in the URL conf.
Page the page number via the page query-string parameter.
These values and list are 1-based, not 0-based, so the first page would be represented as page 1.
As a special case, you are also permitted to use last as a value for page.
This allows you to access the final page of results without first having to determine how many 
pages there are.
Note that page must be either a valid page number or the value last; any other value for page 
will result in a 404 error.
Attribute:- 
allow_empty - A boolean specifying whether to display the page if no objects are avaiable. If 
this is False and no objects are available, the view will raise a 404 instead of displaying an 
empty page. By default, this is True.

model - The model that this view will display data for. Specifying model = Student is effectively 
the same as specifying queryset = Student.objects.all(), where objects stands for Student's 
default manager.

queryset - A QuerySet that represents the objects. If provided, the value of queryset supersedes 
the value provided for model.

ordering - A string or list of strings specifying the ordering to apply to the queryset. Valid 
values are the same as those for order_by().

Attributes:- 
paginate_by - An integer specifying how many objects should be displayed per page. If this is 
given, the view will paginate objects with paginate_by objects per page. The view will expect 
either a page query string parameter(via request.GET) or a page variable specified in the 
URL conf.

paginate_orphans - An integer specifying the number of "overflow" objects the last page can 
contain. This extends the paginate_by limit on the last page by up to paginate_orphans, in  
order to keep the last page from having a very small number of objects. 

page_kwargs - A string specifying the name to use for the page parameter. The view will expect 
this parameter to be available either as a query string parameter (via request.GET) or as a 
kwarg variable specified in the URLconf. Defaults to page. 

paginator_class - The paginator class to be used for pagination. By default, 
django.core.paginator.Paginator is used. If the custom paginator class doesn't have the same 
constructor interface as django.core.paginator.Paginator, you will also need to provide an 
implementation for get_paginator(). 

context_object_name - Designates the name of the variable to use in the context. 
```

Methods:- 
```text
get_queryset() - Get the list of items for this view. This must be an iterable and may be a 
queryset(in which queryset-specific behavior will be enabled).

get_ordering() - Returns a string(or iterable of strings) that defines the ordering that will be 
applied to the queryset. 
Returns ordering by default.

paginate_queryset(queryset, page_size) - Returns a 4-tuple containing(paginator, page, object_list, 
is_paginated).

Constructed by paginating queryset into pages of size page_size. If the request contains a page 
argument, either as a captured URL argument or as a GET argument, object_list will correspond to 
the objects from that page. 

get_paginate_by(queryset) - Returns the number of items to paginate by, or None for no pagination.
By default this returns the value of paginate_by. 

get_paginator(queryset, per_page, orphans=0, allows_empty_first_page=True) - Returns an instance of 
the paginator to use for this view. By default, instantiates an instance of paginator_class.

get_paginate_orphans() - An integer specifying the number of "overflow" objects the last page can 
contain. By default this returns the value of paginate_orphans. 

get_allow_empty() - Returns a boolean specifying whether to display the page if no objects are 
available. If this method returns False and no objects are available, the view will raise a 
404 instead of displaying an empty page. By default, this is True.

get_context_object_name(object_list)- Returns the context variable name that will be used to 
contain the list of data that this view is manipulating. If object_list is a queryset of 
Django objects and context_object_name is not set, the context name will be the model_name of 
the model that the queryset is composed from, with postfix '_list'  appended. For example, 
the model Article would have a context object named article_list.

get_context_data(**kwargs) - Returns context data for displaying the list of object.
Context 
object_list: The list of objects that this view is displaying. If context_object_name is 
specified, that variable will also be set in the context, with the same value as object_list.
is_paginated: A boolean representing whether the results are paginated. Specifically, this is 
set to False if no page size has been specified, or if the available objects do not span 
multiple pages.

paginator: An instance of django.core.paginator.Paginator. If the page is not paginated, this 
context variable will be None. 
page_obj: An instance of django.core.paginator.Page. If the page is not paginated, this 
context_variable will be None. 
```

ListView with Default Template and Context 
```python
# views.py 
from django.views.generic.list import ListView 
from .models import Student 
class StudentListView(ListView):
    model = Student 

# urls.py
urlpatterns = [
    path('student/', views.StudentListView.as_view(), name='student'),
]

# Default Template 
# Syntax :- AppName/ModelClassName_list.html
# Example:- school/student_list.html 

# Default Context
# Syntax:- ModelClassName_list 
# Example:- student_list 
# We can also use object_list
```

List View with Custom Template and Context 
```python 
# views.py
from django.views.generic.list import ListView 
from .models import Student 
class StudentListView(ListView):
    model = Student 
    template_name = 'school/student.html' # Custom Template name 
    context_object_name = 'students' # Custom Context Name 

# urls.py
urlpatterns=[
    path('student/', views.StudentListView.as_view(), name='student'),
]

# Note - school/students.html, school/student_list.html These both will work.
```

