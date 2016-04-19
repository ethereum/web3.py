from __future__ import absolute_import

import codecs

import six

from sha3 import sha3_256


def force_bytes(s):
    if isinstance(s, six.binary_type):
        return s
    return s.encode('utf8')


def strip_0x_prefix(s):
    if isinstance(s, six.binary_type):
        s = six.text_type(s, 'utf8')
    if s[:2] == '0x':
        return s[2:]
    return s


def sha3(s, encoding=None):
    if isinstance(s, six.text_type):
        s = s.encode('utf8')
    if encoding:
        s = codecs.decode(strip_0x_prefix(s), encoding)
    return sha3_256(s).hexdigest()
