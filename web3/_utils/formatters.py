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

TReturn = TypeVar("TReturn")
TValue = TypeVar("TValue")
TMapping = TypeVar("TMapping", bound=Mapping)
TIterable = TypeVar("TIterable", bound=Iterable)


def hex_to_integer(value: HexStr) -> int:
    return int(value, 16)


integer_to_hex = hex


def apply_formatters_to_args(
    *formatters: Callable[[TValue], TReturn]
) -> Callable[..., TReturn]:
    return compose(
        *(
            apply_formatter_at_index(formatter, index)
            for index, formatter in enumerate(formatters)
        )
    )


@overload
def map_collection(func: Callable[[TValue], TReturn], mapping: TMapping[Any, TValue]) -> TMapping[Any, TReturn]:
    """
    Apply `func` to each value of a mapping.
    If `collection` is not a collection, return it unmodified.
    """
@overload
def map_collection(func: Callable[..., TReturn], collection: str) -> str:
    """
    Return `collection` unmodified, since it is not a collection.
    """
@overload
def map_collection(func: Callable[[TValue], TReturn], iterable: TIterable[TValue]) -> TIterable[TReturn]:
    """
    Apply `func` to each element of an iterable.
    """
@overload
def map_collection(func: Callable[[TValue], TReturn], collection: TValue) -> TValue:
    """
    Return `collection` unmodified, since it is not a collection.
    """
def map_collection(func: Callable[..., TReturn], collection: Any) -> Any:
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
def recursive_map(func: Callable[..., TReturn], data: Any) -> TReturn:
    """
    Apply func to data, and any collection items inside data (using map_collection).
    Define func so that it only applies to the type of value that you
    want it to apply to.
    """

    def recurse(item: Any) -> TReturn:
        return recursive_map(func, item)

    items_mapped = map_collection(recurse, data)
    return func(items_mapped)


def static_return(value: TValue) -> Callable[..., TValue]:
    def inner(*args: Any, **kwargs: Any) -> TValue:
        return value

    return inner


def static_result(value: TValue) -> Callable[..., Dict[str, TValue]]:
    def inner(*args: Any, **kwargs: Any) -> Dict[str, TValue]:
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
