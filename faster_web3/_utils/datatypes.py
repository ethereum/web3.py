from typing import (
    Any,
    Collection,
    Dict,
    Final,
    Optional,
    Tuple,
    Type,
)

import faster_eth_utils
import faster_eth_utils.toolz
from mypy_extensions import (
    mypyc_attr,
)

from faster_web3.exceptions import (
    Web3AttributeError,
)


apply_formatters_to_dict: Final = faster_eth_utils.apply_formatters_to_dict
concat: Final = faster_eth_utils.toolz.concat


def verify_attr(class_name: str, key: str, namespace: Collection[str]) -> None:
    if key not in namespace:
        raise Web3AttributeError(
            f"Property {key} not found on {class_name} class. "
            f"`{class_name}.factory` only accepts keyword arguments which are "
            f"present on the {class_name} class"
        )


@mypyc_attr(native_class=False)
class PropertyCheckingFactory(type):
    def __init__(
        cls,
        name: str,
        bases: Tuple[Type[Any], ...],
        namespace: Dict[str, Any],
        **kwargs: Dict[str, Any],
    ) -> None:
        # see PEP487.  To accept kwargs in __new__, they need to be
        # filtered out here.
        type.__init__(cls, name, bases, namespace)

    # __new__ must return a class instance
    def __new__(
        mcs,
        name: str,
        bases: Tuple[type],
        namespace: Dict[str, Any],
        normalizers: Optional[Dict[str, Any]] = None,
    ) -> "PropertyCheckingFactory":
        all_bases = set(concat(base.__mro__ for base in bases))
        all_keys = set(concat(base.__dict__.keys() for base in all_bases))

        for key in namespace:
            verify_attr(name, key, all_keys)

        if normalizers:
            processed_namespace = apply_formatters_to_dict(
                normalizers,
                namespace,
            )
        else:
            processed_namespace = namespace

        return type.__new__(mcs, name, bases, processed_namespace)
