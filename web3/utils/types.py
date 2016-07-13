import sys


if sys.version_info.major == 2:
    integer_types = (int, long)  # NOQA
    bytes_types = (bytes, bytearray)
    text_types = (unicode,)  # NOQA
    string_types = (basestring, bytearray)  # NOQA
else:
    integer_types = (int,)
    bytes_types = (bytes, bytearray)
    text_types = (str,)
    string_types = (bytes, str, bytearray)


def is_integer(value):
    return isinstance(value, integer_types)


def is_bytes(value):
    return isinstance(value, bytes_types)


def is_text(value):
    return isinstance(value, text_types)


def is_string(value):
    return isinstance(value, string_types)


def is_boolean(value):
    return isinstance(value, bool)


def is_Object(obj):
    """
    Returns true if object is Objet, otherwise false
    """
    return isinstance(obj, dict)


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
