from collections.abc import (
    Mapping,
)
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Mapping,
    Optional,
    Tuple,
    TypeVar,
    overload,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    is_dict,
    is_list_like,
    is_string,
    to_dict,
)
from eth_utils.curried import (
    apply_formatter_at_index,
)
from eth_utils.toolz import (
    compose,
    curry,
    dissoc,
    pipe,
)

from web3._utils.decorators import (
    reject_recursive_repeats,
)
from web3.types import (
    RPCResponse,
)

__TReturn = TypeVar("__TReturn")
__TKey = TypeVar("__TKey")
__TValue = TypeVar("__TValue")


def hex_to_integer(value: HexStr) -> int:
    return int(value, 16)


integer_to_hex = hex


def apply_formatters_to_args(
    *formatters: Callable[[__TValue], __TReturn]
) -> Callable[..., __TReturn]:
    return compose(
        *(
            apply_formatter_at_index(formatter, index)
            for index, formatter in enumerate(formatters)
        )
    )


@overload
def map_collection(func: Callable[[__TValue], __TReturn], mapping: Mapping[__TKey, __TValue]) -> Mapping[__TKey, __TReturn]:
    """
    Apply `func` to each value of a mapping.
    If `collection` is not a collection, return it unmodified.
    """
@overload
def map_collection(func: Callable[..., __TReturn], collection: str) -> str:
    """
    Return `collection` unmodified, since it is not a collection.
    """
@overload
def map_collection(func: Callable[[__TValue], __TReturn], iterable: Iterator[__TValue]) -> Iterator[__TReturn]:
    """
    Apply `func` to each element of an iteratol.
    """
@overload
def map_collection(func: Callable[[__TValue], __TReturn], iterable: Iterable[__TValue]) -> Iterable[__TReturn]:
    """
    Apply `func` to each element of an iterable.
    """
@overload
def map_collection(func: Callable[[__TValue], __TReturn], collection: __TValue) -> __TValue:
    """
    Return `collection` unmodified, since it is not a collection.
    """
def map_collection(func: Callable[..., __TReturn], collection: Any) -> Any:
    """
    Apply `func` to each element of a collection, or value of a mapping.
    If `collection` is not a collection, return it unmodified.
    """
    if isinstance(collection, Mapping):
        return type(collection)(
            zip(collection.keys(), map(func, collection.values()))
        )
    elif not is_string(collection) and isinstance(collection, Iterable):
        return type(collection)(map(func, collection))
    else:
        return collection


@reject_recursive_repeats
def recursive_map(func: Callable[..., __TReturn], data: Any) -> __TReturn:
    """
    Apply func to data, and any collection items inside data (using map_collection).
    Define func so that it only applies to the type of value that you
    want it to apply to.
    """

    def recurse(item: Any) -> __TReturn:
        return recursive_map(func, item)

    items_mapped = map_collection(recurse, data)
    return func(items_mapped)


def static_return(value: __TValue) -> Callable[..., __TValue]:
    def inner(*args: Any, **kwargs: Any) -> __TValue:
        return value

    return inner


def static_result(value: __TValue) -> Callable[..., Dict[str, __TValue]]:
    def inner(*args: Any, **kwargs: Any) -> Dict[str, __TValue]:
        return {"result": value}

    return inner


@curry
@to_dict
def apply_key_map(
    key_mappings: Dict[Any, Any], value: Dict[Any, Any]
) -> Iterable[Tuple[Any, Any]]:
    for key, item in value.items():
        if key in key_mappings:
            yield key_mappings[key], item
        else:
            yield key, item


def is_array_of_strings(value: Any) -> bool:
    if not is_list_like(value):
        return False
    return all(is_string(item) for item in value)


def is_array_of_dicts(value: Any) -> bool:
    if not is_list_like(value):
        return False
    return all(is_dict(item) for item in value)


@curry
def remove_key_if(
    key: Any, remove_if: Callable[[Dict[Any, Any]], bool], input_dict: Dict[Any, Any]
) -> Dict[Any, Any]:
    if key in input_dict and remove_if(input_dict):
        return dissoc(input_dict, key)
    else:
        return input_dict


def apply_error_formatters(
    error_formatters: Callable[..., Any],
    response: RPCResponse,
) -> RPCResponse:
    if error_formatters:
        formatted_resp = pipe(response, error_formatters)
        return formatted_resp
    else:
        return response


def apply_null_result_formatters(
    null_result_formatters: Callable[..., Any],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> RPCResponse:
    if null_result_formatters:
        formatted_resp = pipe(params, null_result_formatters)
        return formatted_resp
    else:
        return response
