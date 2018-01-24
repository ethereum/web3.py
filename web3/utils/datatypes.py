from functools import (
    partial,
)
from eth_utils import (
    to_dict,
)

from web3.utils.normalizers import (
    normalize_abi,
    normalize_address,
    normalize_bytecode,
)


class PropertyCheckingFactory(type):
    ens = None

    @to_dict
    def normalize_properties(attributes, values, ens):
        normalizers = {
            'abi': normalize_abi,
            'address': partial(normalize_address, ens),
            'bytecode': normalize_bytecode,
            'bytecode_runtime': normalize_bytecode,
        }

        for attribute, value in zip(attributes, values):
            if attribute in normalizers:
                normalizer = normalizers[attribute]
                yield attribute, normalizer(value)
            else:
                yield attribute, value

    def __new__(mcs, name, bases, namespace):
        for key in namespace:
            if not hasattr(bases[0], key):
                raise AttributeError(
                    "Property {0} not found on {1} class. "
                    "`{1}.factory` only accepts keyword arguments which are "
                    "present on the {1} class".format(key, name)
                )
        attributes, values = zip(*namespace.items())
        ens = namespace['web3'].ens
        normalized_namespace = mcs.normalize_properties(tuple(attributes), tuple(values), ens)
        return super().__new__(mcs, name, bases, normalized_namespace)
