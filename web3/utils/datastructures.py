
from collections import (
    Mapping,
    MutableMapping,
    Hashable,
)

# Hashable must be immutable:
# "the implementation of hashable collections requires that a key's hash value is immutable"
# https://docs.python.org/3/reference/datamodel.html#object.__hash__


class ReadableAttributeDict(Mapping):
    """
    The read attributes for the AttributeDict types
    """

    def __init__(self, dictionary, *args, **kwargs):
        self.__dict__ = dict(dictionary)
        self.__dict__.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return self.__class__.__name__ + "(%r)" % self.__dict__

    def _repr_pretty_(self, builder, cycle):
        """
        Custom pretty output for the IPython console
        """
        builder.text(self.__class__.__name__ + "(")
        if cycle:
            builder.text("<cycle>")
        else:
            builder.pretty(self.__dict__)
        builder.text(")")


class MutableAttributeDict(MutableMapping, ReadableAttributeDict):

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def __delitem__(self, key):
        del self.__dict__[key]


class AttributeDict(ReadableAttributeDict, Hashable):
    """
    This provides superficial immutability, someone could hack around it
    """

    def __setattr__(self, attr, val):
        if attr == '__dict__':
            super(AttributeDict, self).__setattr__(attr, val)
        else:
            raise TypeError('This data is immutable -- create a copy instead of modifying')

    def __delattr__(self, key):
        raise TypeError('This data is immutable -- create a copy instead of modifying')

    def __hash__(self):
        return hash(tuple(sorted(self.items())))

    def __eq__(self, other):
        if isinstance(other, Mapping):
            return self.__dict__ == dict(other)
        else:
            return False
