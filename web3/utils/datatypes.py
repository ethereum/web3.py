from functools import (
    partial,
)
from eth_utils import (
    to_dict,
)
from toolz.itertoolz import (
    concat
)


def verify_attr(class_name, key, base):
    if not hasattr(base, key):
        raise AttributeError(
            "Property {0} not found on {1} class. "
            "`{1}.factory` only accepts keyword arguments which are "
            "present on the {1} class".format(key, class_name)
        )


class PropertyCheckingFactory(type):
    @to_dict
    def normalize_properties(attributes, values, normalizers):
        for attribute, value in zip(attributes, values):
            if attribute in normalizers:
                normalizer = normalizers[attribute]
                yield attribute, normalizer(value)
            else:
                yield attribute, value

    def __new__(mcs, name, bases, namespace, normalizers={}):
        for key in namespace:
            verify_key_attr = partial(verify_attr, name, key)
            map(verify_key_attr, set(concat(base.__mro__ for base in bases)))

        attributes, values = zip(*namespace.items())
        if normalizers:
            processed_namespace = mcs.normalize_properties(
                tuple(attributes),
                tuple(values),
                normalizers)
        else:
            processed_namespace = namespace

        return super().__new__(mcs, name, bases, processed_namespace)
