from collections import (
    OrderedDict,
)
from collections.abc import (
    Hashable,
)
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
    cast,
)

from eth_utils import (
    is_integer,
)

from web3._utils.formatters import (
    recursive_map,
)

# Hashable must be immutable:
# "the implementation of hashable collections requires that a key's hash value is immutable"
# https://docs.python.org/3/reference/datamodel.html#object.__hash__

T = TypeVar("T")
TKey = TypeVar("TKey", bound=Hashable)
TValue = TypeVar("TValue")


class ReadableAttributeDict(Mapping[TKey, TValue]):
    """
    The read attributes for the AttributeDict types
    """

    def __init__(self, dictionary: Dict[TKey, TValue], *args: Any, **kwargs: Any) -> None:
        # type ignored on 46/50 b/c dict() expects str index type not TKey
        self.__dict__ = dict(dictionary)  # type: ignore
        self.__dict__.update(dict(*args, **kwargs))

    def __getitem__(self, key: TKey) -> TValue:
        return self.__dict__[key]  # type: ignore

    def __iter__(self) -> Iterator[Any]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __repr__(self) -> str:
        return self.__class__.__name__ + "(%r)" % self.__dict__

    def _repr_pretty_(self, builder: Any, cycle: bool) -> None:
        """
        Custom pretty output for the IPython console
        https://ipython.readthedocs.io/en/stable/api/generated/IPython.lib.pretty.html#extending
        """
        builder.text(self.__class__.__name__ + "(")
        if cycle:
            builder.text("<cycle>")
        else:
            builder.pretty(self.__dict__)
        builder.text(")")

    @classmethod
    def _apply_if_mapping(cls: Type[T], value: TValue) -> Union[T, TValue]:
        if isinstance(value, Mapping):
            # error: Too many arguments for "object"
            return cls(value)  # type: ignore
        else:
            return value

    @classmethod
    def recursive(cls, value: TValue) -> 'ReadableAttributeDict[TKey, TValue]':
        return recursive_map(cls._apply_if_mapping, value)


class MutableAttributeDict(MutableMapping[TKey, TValue], ReadableAttributeDict[TKey, TValue]):

    def __setitem__(self, key: Any, val: Any) -> None:
        self.__dict__[key] = val

    def __delitem__(self, key: Any) -> None:
        del self.__dict__[key]


class AttributeDict(ReadableAttributeDict[TKey, TValue], Hashable):
    """
    This provides superficial immutability, someone could hack around it
    """

    def __setattr__(self, attr: str, val: TValue) -> None:
        if attr == '__dict__':
            super().__setattr__(attr, val)
        else:
            raise TypeError('This data is immutable -- create a copy instead of modifying')

    def __delattr__(self, key: str) -> None:
        raise TypeError('This data is immutable -- create a copy instead of modifying')

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.items())))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Mapping):
            return self.__dict__ == dict(other)
        else:
            return False


class NamedElementOnion(Mapping[TKey, TValue]):
    """
    Add layers to an onion-shaped structure. Optionally, inject to a specific layer.
    This structure is iterable, where the outermost layer is first, and innermost is last.
    """

    def __init__(
        self, init_elements: Sequence[Any], valid_element: Callable[..., bool] = callable
    ) -> None:
        self._queue: 'OrderedDict[Any, Any]' = OrderedDict()
        for element in reversed(init_elements):
            if valid_element(element):
                self.add(element)
            else:
                self.add(*element)

    def add(self, element: TValue, name: Optional[TKey] = None) -> None:
        if name is None:
            name = cast(TKey, element)

        if name in self._queue:
            if name is element:
                raise ValueError("You can't add the same un-named instance twice")
            else:
                raise ValueError("You can't add the same name again, use replace instead")

        self._queue[name] = element

    def inject(self, element: TValue, name: Optional[TKey] = None,
               layer: Optional[int] = None) -> None:
        """
        Inject a named element to an arbitrary layer in the onion.

        The current implementation only supports insertion at the innermost layer,
        or at the outermost layer. Note that inserting to the outermost is equivalent
        to calling :meth:`add` .
        """
        if not is_integer(layer):
            raise TypeError("The layer for insertion must be an int.")
        elif layer != 0 and layer != len(self._queue):
            raise NotImplementedError(
                "You can only insert to the beginning or end of a %s, currently. "
                "You tried to insert to %d, but only 0 and %d are permitted. " % (
                    type(self),
                    layer,
                    len(self._queue),
                )
            )

        self.add(element, name=name)

        if layer == 0:
            if name is None:
                name = cast(TKey, element)
            self._queue.move_to_end(name, last=False)
        elif layer == len(self._queue):
            return
        else:
            raise AssertionError("Impossible to reach: earlier validation raises an error")

    def clear(self) -> None:
        self._queue.clear()

    def replace(self, old: TKey, new: TKey) -> TValue:
        if old not in self._queue:
            raise ValueError("You can't replace unless one already exists, use add instead")
        to_be_replaced = self._queue[old]
        if to_be_replaced is old:
            # re-insert with new name in old slot
            self._replace_with_new_name(old, new)
        else:
            self._queue[old] = new
        return to_be_replaced

    def remove(self, old: TKey) -> None:
        if old not in self._queue:
            raise ValueError("You can only remove something that has been added")
        del self._queue[old]

    def _replace_with_new_name(self, old: TKey, new: TKey) -> None:
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

    def __iter__(self) -> Iterator[TKey]:
        elements = self._queue.values()
        if not isinstance(elements, Sequence):
            # type ignored b/c elements is set as _OrderedDictValuesView[Any] on 210
            elements = list(elements)  # type: ignore
        return iter(reversed(elements))

    def __add__(self, other: Any) -> 'NamedElementOnion[TKey, TValue]':
        if not isinstance(other, NamedElementOnion):
            raise NotImplementedError("You can only combine with another NamedElementOnion")
        combined = self._queue.copy()
        combined.update(other._queue)
        return NamedElementOnion(cast(List[Any], combined.items()))

    def __contains__(self, element: Any) -> bool:
        return element in self._queue

    def __getitem__(self, element: TKey) -> TValue:
        return self._queue[element]

    def __len__(self) -> int:
        return len(self._queue)

    def __reversed__(self) -> Iterator[TValue]:
        elements = cast(List[Any], self._queue.values())
        if not isinstance(elements, Sequence):
            elements = list(elements)
        return iter(elements)
