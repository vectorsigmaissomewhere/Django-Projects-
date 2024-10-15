## Customize Authentication Views
```text
This is a list with all the views django.contrib.auth provides.
- LoginView
- LogoutView 
- PasswordChangeView
- PasswordChangeDoneView
- PasswordResetView 
- PasswordResetDoneView 
- PasswordResetConfirmView 
- PasswordResetCompleteView 
```

LoginView
```text
django.contrib.auth.views.LoginView 
template_name = 'registration/login.html'
path('login/', views.LoginView.as_view(), name='login')
It's your responsibility to provide the html for the login template, called 
registration/login.html by default. 
- If called via GET, it displays a login form that POSTs to the same URL.
- It called via POST with user submitted credentials, it tries to log the user in. 
- If login is successful, the view redirects to the URL specified in next. 
- If next isn't provided, it redirects to settings.LOGIN_REDIRECT_URL (which defaults to
/accounts/profile/).
- If login isn't successful, it redisplays the login form.

Default Template:- 
registration/login.html 
This template gets passed four template context variables:
- form: A Form object representing the AuthenticationForm.
- next: The URL to redirect to after successful login. This may contain a query string, 
too.
- site: The current Site, accoring to the SITE_ID setting. If you don't have the site 
framework installed, this will be set to an instance of RequestSite, which derives the 
site name and domain from the current HttpRequest.
- site_name: An alias for site site.name. If you don't have the site framework installed, 
this will be set to the value of request.META['SERVER_NAME'].

Custom Template:-
path('login/', views.LoginView.as_view(template_name='myapp/login.html'), name='login')

Attributes:- 
template_name: The name of a template to display for the view used to log the user in. 
Defaults to registation/login.html 
redirect_field_name: The name of a GET field containing the URL to redirect to after 
login. Defaults to next. 
authentication_form: A callable(typically a form class) to use for authentication. 
Defaults to AuthenticationForm. 
extra_context: A dictionary of context data that will be added to the default context data
passed to the template. 
redirect_authenticated_user: A boolean that controls whether or not authenticted users 
accessing the login page will be redirected as if they had just successfully logged in. 
Defaults to False. 
success_url_allowed_hosts: A set of hosts, in addition to request.get_host(), that are 
safe for redirecting after login. Defaults to an empty set.
```

LogoutView 
```text 
django.contrib.auth.views.LogoutView 
template_name = 'registration/logged_out.html' 
path('logout/', views.LogoutView.as_view(), name='logout')
logged_out.html template is already available and used by admin logout template file. 
You can create your onw custom logout template by defining template_name attribute. 

Default Template:-
registration/logged_out.html 
This template gets passed three template context variables:
- title: The string "Logged out", localized 
- site: The current Site, according to the SITE_ID setting. If you don't have the site
framework installed, this will be set to an instance of RequestSite, which derives the 
site name and domain from the current HttpRequest.
- site_name: An alias for site.name. If you don't have the site framework installed, this 
will be set to the value of request.META['SERVER_NAME'].

Custom Template:- 
path('logout/', views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout')

Attributes:- 
next_page: The URL to redirect to after logout. Defaults to settings.LOGOUT_REDIRECT_URL.
template_name: The full name of a template to display after logging the user out. Defaults
to registration/logged_out.html.
redirect_field_name: The name of a GET field containing the URL to redirect to after log 
out. Defaults to next. Overrides the next_page URL if the given GET parameter is passed.
extra_context: A dictionary of context data that will be added to the defalt context data
passed to the template.
success_url_allowed_hosts: A set of hosts, in addition to request.get_host(), that are 
safe for redirecting after logout. Default to an empty set.
```

PasswordChangeView 
```text 
django.contrib.auth.views.PasswordChangeView
template_name = 'registration/password_change_form.html'
path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
registration/password_change_form.html template is already available and used by admin
change password template file.
You can create your own custom change password template by defining template_name 
attribute.

Default Template:- 
registration/password_change_form.html 
This template gets passed following template context variables:
- form: The password change form 

Custom Template
path('password_change/', views.PasswordChangeView.as_view(template_name='myapp/changepass.html'), name='password_change').

Attributes:- 
template_name: The full name of a template to use for displaying the password change form.
Decfaults to registration/password_change.form.html if not supplied.
success_url: The URL to redirect to after a successful password change. Defaults to 
'password_change_done'.
form_class: A custom "change password" form which must accept a user keyword argument. The 
form is responsible for actually changing the user's password. Defaults to 
PasswordChangeForm.
extra_context: A dictionary of context data that will be added to the default context data
passed to the template.
```

PasswordChangeDoneView 
```text 
django.contrib.auth.views.PasswordChangeDoneView 
template_name = 'registration/password_change_done.html'
path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
registration/password_change_done.html.html template is already available and used by 
admin password change done template file.
You can create your own custom password change done template by defining template_name 
attribute.

Default Template:- 
registration/password_change_done.html 

Custom Template:- 
path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name='myapp/changepassdone.html'), name='password_change_done'),

Attributes:- 
template_name: The full name of a template to use. Defaults to 
registration/password_change_done.html if not supplied.
extra_context: A dicionary of context data that will be added to the default context data
passed to the template.
```

PasswordResetView
```text 
django.contrib.auth.views.PasswordRestView 
template_name = 'registration/password_reset_form.html'
path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
registration/password_reset_form.html template is already available and used by admin 
password reset template file. 
You can create your own custom password reset template by defining template_name attribute.

Default Template:- 
registration/password_reset_form.html 
This template gets passed following template context variable:
- form: The forms for resetting the user's password. 

Custom Template:- 
path('password_reset/', views.PasswordResetView.as_view(template_name='myapp/resetpass.html'), name='password_reset'),

The Email template gets passed following email template context variables:
- email: An alias for user.email 
- user - The current User, according to the email from field. Only active users are able 
to reset their passwords(User.is_active is True).
- site_name: An alias for site.name. If you don't have this site framework installed, 
this will be set to the value of request.META['SERVER_NAME']. For more on sites, see The 
"sites" framework.
- domain: An alias for site.domain. If you don't have the site framework installed, this 
will be set to the value of request.get_host().
- protocol: http or https 
- uid: The user's primary key encoded in base 64.
- token: Token to check that the reset link is valid.

Attributes:-
template_name: The full name of a template to use for displaying the password reset form.
Defaults to registration/password_reset_form.html if not supplied.
form_class: Form that will be used to get the email of the user to reset the password for.
Defaults to PasswordResetForm. 
email_template_name: The full name of a template to use for generating the email with 
the reset password link. Defaults to registation/password_reset_email.html if not 
supplied.
subject_template_name: The full name of a template to use for the subject of the email with 
the reset password link. Defaults to registation/password_reset_subject.txt if not 
supplied.
token_generator: Instance of the class to check the one time link. This will default to 
default_token_generator, it's an instance of 
django.contrib.auth.tokens.PasswordResetTokenGenerator.
success_url: The URL to redirect to after a successful password reset request. Defaults to 
'password_reset_done'.


Attributes:- 
from_email: A valid email address. By default Django uses the DEFAULT_FROM_EMAIL.
extra_context: A dictionary of context data that will be added to the default context 
data passed to the template.
html_email_template_name: The full name of a template to use for generating a text/html 
multipart email with the password reset link. By default, HTML email is not sent.
extra_email_context: A dicionary of a context data that will be available in the email 
template. It can be used to override default template context values listed below 
e.g. domain.
```

PasswordResetDoneView 
```text
django.contrib.auth.views.PasswordResetDoneView 
The page shown after a user has been emailed a link to reset their password. This view is 
called by default if the PasswordResetView doesn't have an explicit success_url URL set. 

If the email address provided does not exist in the system, the user is inactive, or  
has an unsuable password, the user will still be redirected to this view but no 
email will be sent. 

template_name = 'registration/password_reset_done.html'
path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
registration/password_reset_done.html template is already available and used by admin 
password reset template file. 
You can create your own custom password reset done template by defining template_name 
attribute. 

Default Template:-
registration/password_reset_done.html 

Custom Template:-
path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name='myapp/resetpassdone.html'), name='password_reset_done'),

Attribute:
template_name: The full name of a template to use. Defaults to 
registration/password_reset_done.html if not supplied. 
extra_context: A dictionary of context data that will be added to the default context 
data passed to template.
```

PasswordResetConfirmView 
```text
django.contrib.auth.views.PasswordResetConfirmView 
It presents a form for entering a new password.
Keyword arguments from the URL:
- uidb64: The user's id encoded in base64. 
- token: Token to check that the password is valid. 
template_name = 'registration/password_reset_confirm.html' 
path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
registration/password_reset_confirm.html template is already available and used by admin 
password reset confirm template file.

You can create your own custom password reset confirm template by defining template_name 
attribute. 

Default Template:- 
registration/password_reset_confirm.html 
This template gets passed following template context variables:
- form: The form for setting the new user's password. 
- validlink: Boolean, True if the link(combination of uidb64 and token) is valid or unused yet.

Custom Template:- 
path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name='myapp/resetpassconfirm.html'), name='password_reset_confirm'),

Attributes:-
template_name: The full name of a template to display the confirm password view. Default 
value is registration/password_reset_confirm.html 

token_generator: Instance of the class to check the password. This will default to 
default_token_generator, it's an instance of 
django.contrib.auth.tokens.PasswordResetTokenGenerator.

post_reset_login: A boolean indicating if the user should be automatically authenticatd 
after a successful password reset. Defaults to False. 

post_reset_login_backend: A dotted path to the authentication backend to use when 
authenticating a user if post_reset_login is True. Required only if you have multiple 
AUTHENTICATION_BACKENDS configured. Defaults to None.

form_class: Form that will be used to set the password. Defaults to SetPasswordForm.

success_url: URL to redirect after the password reset done. Defaults to 
'password_reset_complete'.

extra_context: A dictionary of context data that will be added to the default context 
data passed to the template. 

reset_url_token: Token parameter displayed as a component of password reset URLs. Defaults 
to 'set-password'.
```

PasswordResetCompleteView 
```text 
django.contrib.auth.views.PasswordResetCompleteView 
It presents a view which informs the user that the password has been successfully changed. 
template_name = 'registration/password_reset_complete.html'
path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

registration/password_reset_complete.html template is already available and used as admin 
password reset complete template file. 

You can create your custom password reset complete template by defining template_name 
attribute. 

Default Template:- 
registration/password_reset_complete.html 

Custom Template:-
path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='myapp/resetpasscomp.html'), name='password_reset_complete'),

Attributes:- 
template_name: The full name of a template to display the view. Defaults to 
registration/password_reset_complete.html 

extra_context: A dicionary of context data that will be added to the default context data 
passed to the template.
```

Built-in Forms 
```text 
- AdminPasswordChangeForm - A form used in the admin interface to change a user's password. 
It takes the user as the first positional argument. 
- AuthenticationForm - A form for logging a user in. It takes request as its first 
positional arguemnt, which is stored on the form instance for use by sub-classes. 
- PasswordChangeForm - A form for allowing a user to change their password. 
- PasswordResetForm - A form for generating and emailing a one-time use link to reset a 
user's password. 
- SetPasswordForm - A form that lets a user change their password without entering the 
old password. 
- UserChangeForm - A form used in the admin interface to change a user's information and 
permissions. 
- UserCreationForm - A ModelForm for creating a new user. 
```

