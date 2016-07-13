from __future__ import absolute_import

import codecs

from sha3 import sha3_256


def sha3(value, encoding=None):
    from .encoding import (
        remove_0x_prefix,
        force_bytes,
    )

    if encoding:
        value = codecs.decode(remove_0x_prefix(value), encoding)

    return sha3_256(force_bytes(value)).hexdigest()
