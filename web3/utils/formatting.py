from .string import (
    force_bytes,
    force_text,
)
from .types import (
    is_bytes,
)


def pad_left(string, chars, filler="0"):
    """
    Should be called to pad string to expected length
    """
    numchars = chars - len(string)
    head = ""
    if numchars > 0:
        head = filler * numchars
    return head + string


def pad_right(string, chars, filler="0"):
    """
    Should be called to pad string to expected length
    """
    numchars = chars - len(string)
    tail = ""
    if numchars > 0:
        tail = filler * numchars
    return string + tail


def is_prefixed(value, prefix):
    return value.startswith(
        force_bytes(prefix) if is_bytes(value) else force_text(prefix)
    )


def is_0x_prefixed(value):
    return is_prefixed(value, '0x')


def remove_0x_prefix(value):
    if is_0x_prefixed(value):
        return value[2:]
    return value


def add_0x_prefix(value):
    if is_0x_prefixed(value):
        return value

    prefix = b'0x' if is_bytes(value) else '0x'
    return prefix + value
