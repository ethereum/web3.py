import functools
import codecs

from .types import (
    is_bytes,
    is_text,
    is_string,
)


def force_bytes(value):
    if is_bytes(value):
        return bytes(value)
    elif is_text(value):
        return codecs.encode(value, "iso-8859-1")
    else:
        raise TypeError("Unsupported type: {0}".format(type(value)))


def force_text(value):
    if is_text(value):
        return value
    elif is_bytes(value):
        return codecs.decode(value, "iso-8859-1")
    else:
        raise TypeError("Unsupported type: {0}".format(type(value)))


def force_obj_to_bytes(obj):
    if is_string(obj):
        return force_bytes(obj)
    elif isinstance(obj, dict):
        return {
            k: force_obj_to_bytes(v) for k, v in obj.items()
        }
    elif isinstance(obj, (list, tuple)):
        return type(obj)(force_obj_to_bytes(v) for v in obj)
    else:
        return obj


def force_obj_to_text(obj):
    if is_string(obj):
        return force_text(obj)
    elif isinstance(obj, dict):
        return {
            k: force_obj_to_text(v) for k, v in obj.items()
        }
    elif isinstance(obj, (list, tuple)):
        return type(obj)(force_obj_to_text(v) for v in obj)
    else:
        return obj


def coerce_args_to_bytes(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        bytes_args = force_obj_to_bytes(args)
        bytes_kwargs = force_obj_to_bytes(kwargs)
        return fn(*bytes_args, **bytes_kwargs)
    return inner


def coerce_args_to_text(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        text_args = force_obj_to_text(args)
        text_kwargs = force_obj_to_text(kwargs)
        return fn(*text_args, **text_kwargs)
    return inner


def coerce_return_to_bytes(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        return force_obj_to_bytes(fn(*args, **kwargs))
    return inner


def coerce_return_to_text(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        return force_obj_to_text(fn(*args, **kwargs))
    return inner
