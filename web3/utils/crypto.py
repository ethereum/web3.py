from __future__ import absolute_import

import codecs

from sha3 import sha3_256


def sha3(value, encoding=None):
    from .formatting import (
        remove_0x_prefix,
    )
    from .string import (
        force_bytes,
    )

    if encoding:
        value = codecs.decode(remove_0x_prefix(value), encoding)

    return sha3_256(force_bytes(value)).hexdigest()


# ensure we have the *right* sha3 installed
assert sha3('') == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'
