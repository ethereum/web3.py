import sys

try:
    from cytoolz import (
        assoc,
        complement,
        compose,
        curried,
        curry,
        dicttoolz,
        dissoc,
        functoolz,
        groupby,
        identity,
        itertoolz,
        merge,
        partial,
        pipe,
        sliding_window,
        valmap,
    )
except ImportError:
    from toolz import (  # noqa: F401
        assoc,
        complement,
        compose,
        curried,
        curry,
        dicttoolz,
        dissoc,
        functoolz,
        groupby,
        identity,
        itertoolz,
        merge,
        partial,
        pipe,
        sliding_window,
        valmap,
    )


modules = [curried, dicttoolz, functoolz, itertoolz]
for module in modules:
    module_name = module.__name__.split('.')[-1]
    sys.modules['web3.utils.toolz.{0}'.format(module_name)] = module
del sys, modules
