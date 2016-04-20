# General string formatting and utility functions
import json
import six


def padLeft(string, chars, sign="0"):
    """
    Should be called to pad string to expected length
    """
    numchars = chars - len(string)
    prefix = ""
    if numchars > 0:
        prefix = sign * numchars
    return prefix + string


def padRight(string, chars, sign="0"):
    """
    Should be called to pad string to expected length
    """
    numchars = chars - len(string)
    postfix = ""
    if numchars > 0:
        postfix = sign * numchars
    return string + postfix


def isNumber(obj):
    """
    Returns true if object is an integer/long/float, otherwise false
    """
    return isinstance(obj, six.integer_types) or isinstance(obj, six.integer_types)


def isInteger(obj):
    """
    Returns true if object is an integer/long, otherwise false
    """
    return isinstance(obj, six.integer_types)


def isString(obj):
    """
    Returns true if object is string, otherwise false
    """
    return isinstance(obj, six.string_types)


def isFunction(obj):
    """
    Returns true if object is function, otherwise false
    """
    return callable(obj)


def isObject(obj):
    """
    Returns true if object is Objet, otherwise false
    """
    return isinstance(obj, dict)


def isBoolean(obj):
    """
    Returns true if object is boolean, otherwise false
    """
    return isinstance(obj, bool)


def isArray(obj):
    """
    Returns true if object is array, otherwise false
    """
    return isinstance(obj, list)


def isJson(string):
    """
    Returns true if given string is valid json object
    """
    try:
        decoded = json.loads(string)
        if decoded or decoded == {}:
            return True
    except:
        pass
    return False
