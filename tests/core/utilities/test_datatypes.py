import pytest

from web3._utils.datatypes import (
    PropertyCheckingFactory,
)
from web3.exceptions import (
    Web3AttributeError,
)


class InheritedBaseClass:
    arg0 = None
    arg1 = None


class BaseClass(InheritedBaseClass):
    arg2 = None
    arg3 = None


def test_property_checking_metaclass_attribute_error():
    # Test proper attribute checking, arg from both bases.
    namespace = {"arg2": True, "arg0": True, "arg4": True}
    with pytest.raises(Web3AttributeError):
        PropertyCheckingFactory("class_name", (BaseClass,), namespace)

    # Test proper attribute checking, only absent arg.
    namespace = {"arg4": True}
    with pytest.raises(AttributeError):
        PropertyCheckingFactory("class_name", (BaseClass,), namespace)


def test_property_checking_metaclass_inherited_attributes():
    from_inherited_namespace = {"arg0": True, "arg1": True}
    PropertyCheckingFactory("class_name", (BaseClass,), from_inherited_namespace)

    from_base_namespace = {"arg2": True, "arg3": True}
    PropertyCheckingFactory("class_name", (BaseClass,), from_base_namespace)
