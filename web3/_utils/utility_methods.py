from typing import (
    Any,
    Dict,
    Iterable,
    Union,
)

from web3.types import (
    TxData,
    TxParams,
)


def all_in_dict(
    values: Iterable[Any],
    d: Union[Dict[Any, Any], TxData, TxParams]
) -> bool:
    """
    Returns a bool based on whether ALL of the provided values exist among the keys of the provided
    dict-like object.

    :param values: An iterable with values to look for within the dict-like object
    :param d:      A dict-like object
    :return:       True if ALL values exist in keys; False if NOT ALL values exist in keys
    """
    return all(_ in dict(d) for _ in values)


def any_in_dict(
    values: Iterable[Any],
    d: Union[Dict[Any, Any], TxData, TxParams]
) -> bool:
    """
    Returns a bool based on whether ANY of the provided values exist among the keys of the provided
    dict-like object.

    :param values: An iterable with values to look for within the dict-like object
    :param d:      A dict-like object
    :return:       True if ANY value exists in keys; False if NONE of the values exist in keys
    """
    return any(_ in dict(d) for _ in values)


def none_in_dict(
    values: Iterable[Any],
    d: Union[Dict[Any, Any], TxData, TxParams]
) -> bool:
    """
    Returns a bool based on whether NONE of the provided values exist among the keys of the
    provided dict-like object.

    :param values: An iterable with values to look for within the dict-like object
    :param d:      A dict-like object
    :return:       True if NONE of the values exist in keys; False if ANY value exists in keys
    """
    return not any_in_dict(values, d)
