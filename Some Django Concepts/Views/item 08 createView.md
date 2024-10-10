## Generic Editing View
```text
The following views are described on this page and provide a foundation for editing content:
- FormView
- CreateView
- UpdateView 
- DeleteView
```


CreateView
```text
django.views.generic.edit.CreateView

A view that displays a form for creating an object, redisplaying the form with validation errors(if
there are any) and saving the object.

This views inherits methods and attributes from the following  views:
django.views.generic.detail.SingleObjectTemplateResponseMixin
django.views.generic.base.TemplateResponseMixin 
django.views.generic.edit.BaseCreateView 
django.views.generic.edit.ModelFormMixin 
django.views.generic.edit.FormMixin 
django.views.generic.detail.SingleObjectMixin 
django.views.generic.edit.ProcessFormView 
django.views.generic.base.View 

Attributes:-  

model - A model class. Can be explicitly provided, otherwise will be determined by examining 
self.object or queryset. 

fields - A list of names of fields. This is interpreted the same way as the Meta.field attribute of 
ModelForm.
This is a required attribute if you are generating the form class automatically(e.g. using model).
Omitting this attribute will result in an ImproperlyConfigured exception.

success_url - The URL to redirect to when the form is successfully processed.
success_url may contain dictionary string formatting, which will be interpolated against the 
object's field attributes. For example, you could use success_url="polls/{slug}/" to redirect to 
a URL composed out of the slug field on a model.

Methods:- 

get_form_class() - Retrieve the form class to instantiate. If form_class is provided, that class 
will be used. Otherwise, a ModelForm will be instantiated using the model associated with the 
queryset, or with the model, depending on which attribute is provided.

get_form_kwargs() - Add the current instance(self.object) to the standard get_form_kwargs().

get_success_url() - Determine the URL to redirect to when the form is successfully validated. 
Returns django.views.generic.edit.ModelFormMixin.success_url if it is provided; otherwise, attempts
to use the get_absolute_url() of the object.

form_valid(form) - Saves the form instance, sets the current object for the view, and redirects to 
get_success_url().

form_invalid(form) - Renders a response, providing the invalid form as context.
```
