import hashlib

from eth_utils import (
    is_boolean,
    is_null,
    is_dict,
    is_list_like,
    is_number,
    is_text,
    is_bytes,
    force_bytes,
)

from .six import (
    Generator,
)


def generate_cache_key(value):
    """
    Generates a cache key for the *args and **kwargs
    """
    if is_bytes(value):
        return hashlib.md5(value).hexdigest()
    elif is_text(value):
        return generate_cache_key(force_bytes(value))
    elif is_boolean(value) or is_null(value) or is_number(value):
        return generate_cache_key(repr(value))
    elif is_dict(value):
        return generate_cache_key((
            (key, value[key])
            for key
            in sorted(value.keys())
        ))
    elif is_list_like(value) or isinstance(value, Generator):
        return generate_cache_key("".join((
            generate_cache_key(item)
            for item
            in value
        )))
    else:
        raise TypeError("Cannot generate cache key for value {0} of type {1}".format(
            value,
            type(value),
        ))
