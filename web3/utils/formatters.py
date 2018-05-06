from collections import (
    Iterable,
    Mapping,
)

from eth_utils import (
    is_dict,
    is_list_like,
    is_string,
    to_dict,
    to_list,
)

from web3.utils.decorators import (
    reject_recursive_repeats,
)
from web3.utils.toolz import (
    compose,
    curry,
    dissoc,
)


def hex_to_integer(value):
    return int(value, 16)


integer_to_hex = hex


@curry
@to_list
def apply_formatter_at_index(formatter, at_index, value):
    if at_index + 1 > len(value):
        raise IndexError(
            "Not enough values in iterable to apply formatter.  Got: {0}. "
            "Need: {1}".format(len(value), at_index + 1)
        )
    for index, item in enumerate(value):
        if index == at_index:
            yield formatter(item)
        else:
            yield item


def apply_formatters_to_args(*formatters):
    return compose(*(
        apply_formatter_at_index(formatter, index)
        for index, formatter
        in enumerate(formatters)
    ))


@curry
def apply_formatter_if(condition, formatter, value):
    if condition(value):
        return formatter(value)
    else:
        return value


@curry
@to_dict
def apply_formatters_to_dict(formatters, value):
    for key, item in value.items():
        if key in formatters:
            try:
                yield key, formatters[key](item)
            except (TypeError, ValueError) as exc:
                raise type(exc)("Could not format value %r as field %r" % (item, key)) from exc
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


def map_collection(func, collection):
    '''
    Apply func to each element of a collection, or value of a dictionary.
    If the value is not a collection, return it unmodified
    '''
    datatype = type(collection)
    if isinstance(collection, Mapping):
        return datatype((key, func(val)) for key, val in collection.items())
    if is_string(collection):
        return collection
    elif isinstance(collection, Iterable):
        return datatype(map(func, collection))
    else:
        return collection


@reject_recursive_repeats
def recursive_map(func, data):
    '''
    Apply func to data, and any collection items inside data (using map_collection).
    Define func so that it only applies to the type of value that you want it to apply to.
    '''
    def recurse(item):
        return recursive_map(func, item)
    items_mapped = map_collection(recurse, data)
    return func(items_mapped)


def static_return(value):
    def inner(*args, **kwargs):
        return value
    return inner


def static_result(value):
    def inner(*args, **kwargs):
        return {'result': value}
    return inner


@curry
@to_dict
def apply_key_map(key_mappings, value):
    for key, item in value.items():
        if key in key_mappings:
            yield key_mappings[key], item
        else:
            yield key, item


def is_array_of_strings(value):
    if not is_list_like(value):
        return False
    return all((is_string(item) for item in value))


def is_array_of_dicts(value):
    if not is_list_like(value):
        return False
    return all((is_dict(item) for item in value))


@curry
def remove_key_if(key, remove_if, input_dict):
    if key in input_dict and remove_if(input_dict):
        return dissoc(input_dict, key)
    else:
        return input_dict
