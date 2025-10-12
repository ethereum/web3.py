from collections.abc import (
    Mapping,
)
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    Optional,
    TypeVar,
    Union,
)

from eth_typing import (
    HexStr,
)
from faster_eth_utils import (
    is_dict,
    is_list_like,
    is_string,
)
from faster_eth_utils.curried import (
    apply_formatter_at_index,
)
from faster_eth_utils.toolz import (
    compose,
    curry,
    dissoc,
)

from faster_web3._utils.decorators import (
    reject_recursive_repeats,
)
from faster_web3.types import (
    RPCResponse,
)

TReturn = TypeVar("TReturn")
TValue = TypeVar("TValue")


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


def map_collection(func: Callable[..., TReturn], collection: Any) -> Any:
    """
    Apply func to each element of a collection, or value of a dictionary.
    If the value is not a collection, return it unmodified
    """
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
    result = {"result": value}

    def inner(*args: Any, **kwargs: Any) -> Dict[str, TValue]:
        return result

    return inner


def apply_key_map(
    key_mappings: Dict[Any, Any]
) -> Callable[[Dict[Any, Any]], Dict[Any, Any]]:
    
    def get_key(key: Any) -> Any:
        return key_mappings[key] if key in key_mappings else key
    
    def apply_key_map_curried(value: Dict[Any, Any]) -> Dict[Any, Any]:
        return {get_key(k): v for k, v in value.items()}

    return apply_key_map_curried


def is_array_of_strings(value: Any) -> bool:
    return is_list_like(value) and all(map(is_string, value))


def is_array_of_dicts(value: Any) -> bool:
    return is_list_like(value) and all(map(is_dict, value))


@curry
def remove_key_if(
    key: Any, remove_if: Callable[[Dict[Any, Any]], bool], input_dict: Dict[Any, Any]
) -> Dict[Any, Any]:
    if key in input_dict and remove_if(input_dict):
        return dissoc(input_dict, key)
    else:
        return input_dict


def apply_error_formatters(
    error_formatters: Union[Callable[..., TReturn], None],
    response: RPCResponse,
) -> Union[RPCResponse, TReturn]:  # sourcery skip: assign-if-exp
    if error_formatters:
        return error_formatters(response)
    else:
        return response


def apply_null_result_formatters(
    null_result_formatters: Union[Callable[..., TReturn], None],
    response: RPCResponse,
    params: Optional[Any] = None,
) -> Union[RPCResponse, TReturn]:  # sourcery skip: assign-if-exp
    if null_result_formatters:
        return null_result_formatters(params)
    else:
        return response
