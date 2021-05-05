import random

from ethpm._utils.cache import (
    cached_property,
)


def test_cached_property():
    class FOO:
        def __int__(self):
            pass

        @cached_property
        def generate_number(self):
            return random.random()

    foo = FOO()
    foo_number = foo.generate_number
    foo_cached_number = foo.generate_number
    assert foo_number == foo_cached_number
