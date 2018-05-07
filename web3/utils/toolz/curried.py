try:
    from cytoolz.curried import (
        keymap,
        valmap,
    )
except ImportError:
    from toolz.curried import (  # noqa: F401
        keymap,
        valmap,
    )
