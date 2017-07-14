
from collections import (
        Mapping,
        MutableMapping,
        Hashable,
        )

# Hashable must be immutable:
# "the implementation of hashable collections requires that a key's hash value is immutable"
# https://docs.python.org/3/reference/datamodel.html#object.__hash__


class ReadableAttributeDict(Mapping):
    'the read attributes for the AttributeDict types'

    def __init__(self, dictionary, *args, **kwargs):
        self.__dict__ = dict(dictionary)
        self.__dict__.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        dict_lines = ['\n\t' + repr(k) + ': ' + repr(self[k]) + ',' for k in sorted(self.__dict__)]
        return self.__class__.__name__ + '({' + ''.join(dict_lines) + '\n})'


class MutableAttributeDict(MutableMapping, ReadableAttributeDict):

    def __setitem__(self, key, val):
        self.__dict__[key] = val

    def __delitem__(self, key):
        del self.__dict__[key]


class AttributeDict(ReadableAttributeDict, Hashable):
    'This provides superficial immutability, someone could hack around it'

    def __setattr__(self, attr, val):
        if attr == '__dict__':
            super(AttributeDict, self).__setattr__(attr, val)
        else:
            raise TypeError('This data is immutable -- create a copy instead of modifying')

    def __delattr__(self, key):
        raise TypeError('This data is immutable -- create a copy instead of modifying')

    def _sorteditems(self):
        return tuple(sorted(self.items()))

    def __hash__(self):
        return hash(self._sorteditems())

    def __eq__(self, other):
        if hasattr(other, '__dict__'):
            return self.__dict__ == other.__dict__
        elif isinstance(other, Mapping):
            return other == self.__dict__
        else:
            return False
