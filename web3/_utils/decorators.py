import functools
import threading
import warnings


class combomethod:
    def __init__(self, method):
        self.method = method

    def __get__(self, obj=None, objtype=None):
        @functools.wraps(self.method)
        def _wrapper(*args, **kwargs):
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            else:
                return self.method(objtype, *args, **kwargs)
        return _wrapper


def reject_recursive_repeats(to_wrap):
    '''
    Prevent simple cycles by returning None when called recursively with same instance
    '''
    to_wrap.__already_called = {}

    @functools.wraps(to_wrap)
    def wrapped(*args):
        arg_instances = tuple(map(id, args))
        thread_id = threading.get_ident()
        thread_local_args = (thread_id,) + arg_instances
        if thread_local_args in to_wrap.__already_called:
            raise ValueError('Recursively called %s with %r' % (to_wrap, args))
        to_wrap.__already_called[thread_local_args] = True
        try:
            wrapped_val = to_wrap(*args)
        finally:
            del to_wrap.__already_called[thread_local_args]
        return wrapped_val
    return wrapped


def deprecated_for(replace_message):
    '''
    Decorate a deprecated function, with info about what to use instead, like:

    @deprecated_for("toBytes()")
    def toAscii(arg):
        ...
    '''
    def decorator(to_wrap):
        @functools.wraps(to_wrap)
        def wrapper(*args, **kwargs):
            warnings.warn(
                "%s is deprecated in favor of %s" % (to_wrap.__name__, replace_message),
                category=DeprecationWarning,
                stacklevel=2)
            return to_wrap(*args, **kwargs)
        return wrapper
    return decorator
