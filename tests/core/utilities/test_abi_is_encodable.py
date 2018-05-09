import pytest

from web3.utils.abi import (
    is_encodable,
)


@pytest.mark.parametrize(
    'value,_type,expected',
    (
        # bytes
        ('12', 'bytes2', True),  # undersize OK
        ('0x12', 'bytes2', True),  # with or without 0x OK
        ('0123', 'bytes2', True),  # exact size OK
        (b'\x12', 'bytes2', True),  # as bytes value undersize OK
        (b'\x01\x23', 'bytes2', True),  # as bytes value exact size OK
        (b'\x01\x23', 'bytes1', False),  # no oversize bytes
        ('0123', 'bytes1', False),  # no oversize hex strings
        ('1', 'bytes2', False),  # no odd length
        ('0x1', 'bytes2', False),  # no odd length
        (True, 'bytes32', False),  # no wrong types
        (0, 'bytes32', False),  # no wrong types
        # int
        (-1 * 2**255 - 1, 'int256', False),
        (-1 * 2**255, 'int256', True),
        (-1, 'int256', True),
        (0, 'int256', True),
        (1, 'int256', True),
        (2**255 - 1, 'int256', True),
        (2**255, 'int256', False),
        ('abc', 'int256', False),
        (True, 'int256', False),
        # uint
        (-1, 'uint256', False),
        (0, 'uint256', True),
        (1, 'uint256', True),
        (2**256 - 1, 'uint256', True),
        (2**256, 'uint256', False),
        ('abc', 'uint256', False),
        (True, 'uint256', False),
        # function
        (0, 'function', False),
        (b'\0' * 24, 'function', True),
        (b'\0' * 25, 'function', False),
        (True, 'function', False),
        (False, 'function', False),
        # address
        ('0x' + '00' * 20, 'address', True),
        ('0x' + '00' * 32, 'address', False),
        (None, 'address', False),
        ('dennisthepeasant.eth', 'address', True),  # passes because eth_utils converts to bytes :/
        ('autonomouscollective.eth', 'address', True),
        ('all-TLDs-valid-now.test', 'address', True),
        ('-rejects-invalid-names.test', 'address', False),
        ('ff', 'address', True),  # this could theoretically be a top-level domain (TLD)
        ('0xname.eth', 'address', True),  # 0x in name is fine, if it is not a TLD
        ('0xff', 'address', False),  # but any valid hex starting with 0x should be rejected
        # string
        ('', 'string', True),
        ('anything', 'string', True),
        (b'', 'string', True),
        (b'anything', 'string', True),
        (b'\x80', 'string', False),  # bytes that cannot be decoded with utf-8 are invalid
    ),
)
def test_is_encodable(value, _type, expected):
    actual = is_encodable(_type, value)
    assert actual is expected
