import functools


class combomethod(object):
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
        instances = tuple(map(id, args))
        if instances in to_wrap.__already_called:
            raise ValueError('Recursively called %s with %r' % (to_wrap, args))
        to_wrap.__already_called[instances] = True
        wrapped_val = to_wrap(*args)
        del to_wrap.__already_called[instances]
        return wrapped_val
    return wrapped
