import sys


if sys.version_info.major == 2:
    integer_types = (int, long)  # noqa: F821
    bytes_types = (bytes, bytearray)
    text_types = (unicode,)  # noqa: F821
    string_types = (basestring, bytearray)  # noqa: F821
else:
    integer_types = (int,)
    bytes_types = (bytes, bytearray)
    text_types = (str,)
    string_types = (bytes, str, bytearray)


def is_integer(value):
    return isinstance(value, integer_types) and not isinstance(value, bool)


def is_bytes(value):
    return isinstance(value, bytes_types)


def is_text(value):
    return isinstance(value, text_types)


def is_string(value):
    return isinstance(value, string_types)


def is_boolean(value):
    return isinstance(value, bool)


def is_object(obj):
    return isinstance(obj, dict)


def is_array(obj):
    return isinstance(obj, list)


def is_null(obj):
    return obj is None
