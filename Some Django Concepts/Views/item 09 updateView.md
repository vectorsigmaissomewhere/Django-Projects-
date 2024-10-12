## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```

Update View
```text
django.views.generic.edit.UpdateView 

A view that displays a form for editing an existing object, redisplaying the form with 
validation errors(if there are any) and saving changes to the object. This uses a form
automatically genereated from the object's model class (unless a form class is maually 
specified).

This view inherits methods and attributes from the following views:
- django.views.generic.detail.SingleObjectTemplateResponseMixin
- django.views.generic.base.TemplateResponseMixin 
- django.views.generic.edit.BaseUpdateView 
- django.views.generic.edit.ModelFormMixin
- django.views.generic.edit.FormMixin 
- django.views.generic.edit.SingleObjectMixin 
- django.views.generic.edit.ProcessFormView 
- django.views.generic.base.View 


Attributes:

template_name_suffix - The UpdateView page displayed to a GET request uses a 
template_name_suffix of'_form_'.
object - When using UpdateView you have access to self.object, which is the object 
being updated. 
```
