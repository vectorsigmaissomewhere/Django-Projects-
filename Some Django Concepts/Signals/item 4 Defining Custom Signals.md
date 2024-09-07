Defining Custom Signals
```text
All signals are django.dispatch.Signal instances.
class Signal(providing_args=list)

The providing_args is a list of the names of arguments the signal will 
provide to listeners. This is purely documentational, however, as there 
is nothing that checks that the signal actually provides these 
arguments to its listeners.

You're allowed to change this list of arguments at any time.
```

Sending signals
```text
There are two ways to send signals in Django.
- Signal.send(sender, **kwargs) - This is used to send a signal, all built-in
signals use this to send signals. You must provide the sender argument
which is a class most of the time any may provide as many other
keyword arguments as you like. It returns a list of tuple pairs
[(receiver, response), ...], representing the list of called receiver 
functions and their response values.

- Signal.send_robust(sender, **kwargs) - This is used to send a signal. You must provide the sender argument which is a class
most of the time and may provide as many other keyword 
arguments as you like. It returns a list of tuple pairs 
[(receiver, response), ... ], representing the list of called receiver
functios and their response values.  
```

Difference between send() and send_robust()
```text
- send() does not catch any expections raised by receivers; it 
simply allows errors to propagate. Thus not all receivers may 
be notified of a signal in the face of an error.
- send_robust() caches all errors derived from Python's 
Exception class, and ensures all receivers are notified of the
signal. If error occurs, the error instance is returned in the tuple
pair for the receiver that raised the error.
```

Disconnecting Signals
```text
Signal.disconnect(receiver=None, sender=None, dispatch_uid=None) 
This is used to disconnect a receiver from a signal. The arguments
are as described in Signal.connect(). The method returns True if a
receiver was disconnected and False if not.
```
