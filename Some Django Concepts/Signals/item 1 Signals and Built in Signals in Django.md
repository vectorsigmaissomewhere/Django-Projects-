## Signals
```text
The signals are utilities that allow us to associate events with 
actions. 
Signals allow certain senders to notify a set of receivers that 
some action has taken place.
- Login and Logout Signals
- Model Signals
- Management Signals
- Request/Response Signals
- Test Signals
- Database Wrappers
```

Three major part of signals 
```text
Sender - Who will send Signal
Signal - Signal
Receiver - Who will receive Signal
```

Functions
```text
Receiver Function - This function takes a sender argument, along
with wildcard keyword arguments (**kwargs); all signal handlers
must take these arguments. A receiver can be any Python
function or method.
for Example:
def receiver_func(sender, request, user, **kwargs):
    pass

Connecting/Registering Receiver Function - There are two ways 
you can connect a receiver to a signal:-
- Manual Connect Route
- Decorator

Manual Connect Route - To receive a signal , register a receiver 
function using the Signal.connect() method. The receiver 
function is called when the signal is sent. All of the signal's 
receiver functions are called one at a time, in the order they
were registered.

Signal.connect(receiver_func, sender=None, weak=True, dispatch_uid=None)
Where, 
receiver_func - The callback function which will be connected
      to signal.
signal - Specifies a particular sender to receiver signals from.
weak - Django stores signal handlers as weak references by 
    default. This if your receiver is a local function, it may be 
    garbage collected. To prevent this, pass weak = False when 
    you call the signal's connect() method.
dispatch_uid - A unique identifier for a signal receiver in cases 
    where duplicate signals may be sent.
Decorator - @receiver(signal or list of signal, sender)
```

Built-in Signals
```text
Django provides a set of built-in signals that let user code get 
notified by Django itself of certain actions. 

Login and Logout Signals - The auth framework uses the following
    signals that can be used for notification when a user logs in or
    out.
django.contrib.auth.signals- 
    user_logged_in(sender, request, user) - Sent when a user logs
           in successfully.
    	sender - The class of the user that just logged in.
	request - The current HttpRequest instance.
	user - The user instance that just logged in.
     user_logged_out(sender, request, user) - Sent when the 
          logout method is called.
                  sender - The class of the user that just logged out or 
                     None if the user was not authenticated.
                   request - The current HttpRequest instance.
                   user - The user instance that just logged out or None
                         if the user was not authenticated.
     user_login_failed(sender, credentials, request) - 
                   Sent when the user failed to login successfully
                    sender - The name of the module used for authentication.
                    credentials - A dictionary of keyword arguments 
                         containing the user credentials that were passed
                         to authenticate() or your own custom 
                         authentication backend. Credentials matching a
                         set of 'sensitive' patterns, (including password) will
                         not be sent in the clear as part of signals.
                    request - The HttpRequest object, if one was 
                         provided to authenticate()
```
