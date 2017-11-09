
from collections import (
    Hashable,
    Mapping,
    MutableMapping,
    OrderedDict,
    Sequence,
)

from web3.utils.encoding import (
    hexstr_if_str,
    to_bytes,
)

from web3.utils.formatters import recursive_map

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

    @classmethod
    def _apply_if_mapping(cls, value):
        if isinstance(value, Mapping):
            return cls(value)
        else:
            return value

    @classmethod
    def recursive(cls, value):
        return recursive_map(cls._apply_if_mapping, value)


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


class NamedElementStack(Mapping):
    def __init__(self, init_elements, valid_element=callable):
        self._queue = OrderedDict()
        for element in reversed(init_elements):
            if valid_element(element):
                self.add(element)
            else:
                self.add(*element)

    def add(self, element, name=None):
        if name is None:
            name = element

        if name in self._queue:
            if name is element:
                raise ValueError("You can't add the same un-named instance twice")
            else:
                raise ValueError("You can't add the same name again, use replace instead")

        self._queue[name] = element

    def clear(self):
        self._queue.clear()

    def replace(self, old, new):
        if old not in self._queue:
            raise ValueError("You can't replace unless one already exists, use add instead")
        if self._queue[old] is old:
            # re-insert with new name in old slot
            self._replace_with_new_name(old, new)
        else:
            self._queue[old] = new

    def remove(self, old):
        if old not in self._queue:
            raise ValueError("You can only remove something that has been added")
        del self._queue[old]

    def _replace_with_new_name(self, old, new):
        self._queue[new] = new
        found_old = False
        for key in list(self._queue.keys()):
            if not found_old:
                if key == old:
                    found_old = True
                continue
            elif key != new:
                self._queue.move_to_end(key)
        del self._queue[old]

    def __iter__(self):
        elements = self._queue.values()
        if not isinstance(elements, Sequence):
            elements = list(elements)
        return iter(reversed(elements))

    def __add__(self, other):
        if not isinstance(other, NamedElementStack):
            raise NotImplementedError("You can only combine with another Stack")
        combined = self._queue.copy()
        combined.update(other._queue)
        return NamedElementStack(combined.items())

    def __contains__(self, element):
        return element in self._queue

    def __getitem__(self, element):
        return self._queue[element]

    def __len__(self):
        return len(self._queue)

    def __reversed__(self):
        elements = self._queue.values()
        if not isinstance(elements, Sequence):
            elements = list(elements)
        return iter(elements)


class HexBytes(bytes):
    def __new__(cls, val):
        bytesval = hexstr_if_str(to_bytes, val)
        return super(HexBytes, cls).__new__(cls, bytesval)

    def hex(self):
        return '0x' + super(HexBytes, self).hex()

    def __repr__(self):
        return 'HexBytes(%r)' % self.hex()
