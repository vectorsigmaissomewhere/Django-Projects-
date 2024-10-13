## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```

DeleteView
```text
django.views.generic.edit.DeleteView

A view that displays a confirmation page and deletes an existing object. The given object 
will only be deleted if the request method is POST. If this view is fetched via GET, it 
will display a confirmation page that should contain a form that POSTs to the same URL.

This view inherits methods and attributes from the following views:
- django.views.generic.detail.SingleObjectTemplateResponseMixin
- django.views.generic.base.TemplateResponseMixin
- django.views.generic.edit.BaseDeleteView
- django.views.generic.edit.DeletionMixin
- django.views.generic.detail.BaseDetailView
- django.views.generic.detail.SingleObjectMixin 

Attribute:- 
template_name_suffix - The DeleteView page displayed to a GET request uses a 
template_name_suffixof'_confirm_delete'.

django.views.generic.edit.DeletionMixin
Enables handling of the DELETE http action.

Attributes:- 
success_url - The url to redirect to when the nominated object has been successfully 
deleted.
success_url may contain dictionary string formatting, which will be interpolated against
the object's filed attributes. For example, you could use success_url="/parent/{parent_id}/"
to redirect to a URL composed out of the parent_id field on a model.

Methods:- 
delete(request, *args, **kwargs) - Retireves the target object and calls its delete() 
method, then redirects to the success URL.

get_success_url() - Returns the url to redirect to when the nominated object has been 
successfully deleted. Returns success_url by default.
```

