## Authentication Settings in Django 

Auth Settings
```text
Settings for django.contrib.auth 

AUTHENTICATION_BACKENDS
A list of authentication backend classes(as strings) to use when attempting to authenticate a user 
Default: ['django.contrib.auth.backends.ModelBackend']

AUTH_USER_MODEL 
The model to use to represent a USer. 
Default: 'auth.User'

LOGIN_REDIRECT_URL 
The URL or named URL pattern where requests are redirected after login when the LoginView
doesn't get a next GET parameter.

Default: '/accounts/profile/'


LOGIN_URL 
The URL or named URL pattern where requests are redirected for login when using the 
login_required() decorator, LoginRequiredMixin, or AccessMixin.

LOGOUT_REDIRECT_URL 
The URL or nameed URL pattern where requests are redirected after logout if LogoutView doresn't have
a next_page attribute.

If None, no redirect will be performed and the logout view will be rendered.
Default: None

PASSWORD_RESET_TIMEOUT_DAYS
The minimum number of days a password reset link is valid for. Depending on when the link is 
generated, it will be valid for up to a day longer.
Used by the PasswordResetConfirmView
Default: 3

PASSWORD_HASHERS
Default: [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS
The list of validators that are used to check the strength of user's passwords.
Default[] (Empty list)
```
