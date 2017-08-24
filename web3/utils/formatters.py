from __future__ import absolute_import

from cytoolz.functoolz import (
    curry,
)

from eth_utils import (
    to_list,
    to_dict,
)


def hex_to_integer(value):
    return int(value, 16)


@curry
@to_list
def apply_formatter_at_index(formatter, at_index, value):
    if at_index + 1 > len(value):
        raise IndexError(
            "Not enough values in iterable to apply formatter.  Got: {0}. "
            "Need: {1}".format(len(value), at_index)
        )
    for index, item in enumerate(value):
        if index == at_index:
            yield formatter(item)
        else:
            yield item


@curry
def apply_formatter_if(formatter, condition, value):
    if condition(value):
        return formatter(value)
    else:
        return value


@curry
@to_dict
def apply_formatters_to_dict(formatters, value):
    for key, item in value.items():
        if key in formatters:
            yield key, formatters[key](item)
        else:
            yield key, item


@curry
@to_list
def apply_formatter_to_array(formatter, value):
    for item in value:
        yield formatter(item)


@curry
def apply_one_of_formatters(formatter_condition_pairs, value):
    for formatter, condition in formatter_condition_pairs:
        if condition(value):
            return formatter(value)
    else:
        raise ValueError("The provided value did not satisfy any of the formatter conditions")
