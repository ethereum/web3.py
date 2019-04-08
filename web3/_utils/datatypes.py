from eth_utils.toolz import (
    concat,
)

import web3._utils.formatters


def verify_attr(class_name, key, namespace):
    if key not in namespace:
        raise AttributeError(
            "Property {0} not found on {1} class. "
            "`{1}.factory` only accepts keyword arguments which are "
            "present on the {1} class".format(key, class_name)
        )


class PropertyCheckingFactory(type):
    def __init__(cls, name, bases, namespace, **kargs):
        # see PEP487.  To accept kwargs in __new__, they need to be
        # filtered out here.
        super().__init__(name, bases, namespace)

    def __new__(mcs, name, bases, namespace, normalizers=None):
        all_bases = set(concat(base.__mro__ for base in bases))
        all_keys = set(concat(base.__dict__.keys() for base in all_bases))

        for key in namespace:
            verify_attr(name, key, all_keys)

        if normalizers:
            processed_namespace = web3._utils.formatters.apply_formatters_to_dict(
                normalizers,
                namespace,
            )
        else:
            processed_namespace = namespace

        return super().__new__(mcs, name, bases, processed_namespace)
