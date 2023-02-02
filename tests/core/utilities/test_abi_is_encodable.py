import pytest


@pytest.mark.parametrize(
    "value,_type,expected",
    (
        # Some sanity checks to make sure our custom registrations didn't bork
        # anything
        ("0x" + "00" * 20, "address", True),
        ("0x" + "00" * 32, "address", False),  # no oversized addresses
        ("0xff", "address", False),  # no undersized addresses
        (None, "address", False),  # no wrong types
        (b"\x01\x23", "bytes2", True),  # valid cases should be same
        (b"\x01\x23", "bytes1", False),  # no oversize bytes
        (True, "bytes32", False),  # no wrong types
        (0, "bytes32", False),  # no wrong types
        (b"\x12", "bytes", True),
        ("", "string", True),
        ("anything", "string", True),
        (["0x" + "00" * 20, 0], "(address,uint256)", True),
        (("0x" + "00" * 20, 0), "(address,uint256)", True),
        ([0], "(address,uint256)", False),
        (["0x" + "00" * 20], "(uint256)", False),
        # Special address behavior
        (
            "dennisthepeasant.eth",
            "address",
            True,
        ),  # passes because eth_utils converts to bytes :/
        ("autonomouscollective.eth", "address", True),
        ("all-TLDs-valid-now.test", "address", True),
        ("ff", "address", True),  # this could theoretically be a top-level domain (TLD)
        ("0xname.eth", "address", True),  # 0x in name is fine, if it is not a TLD
        (
            "rejects_invalid_names.eth",
            "address",
            False,
        ),  # no underscore in domain names
        # Special bytes<M> behavior
        ("0x1234", "bytes2", True),  # with or without 0x OK
        (b"\x124", "bytes2", True),  # as bytes value undersize not OK
        ("1", "bytes2", False),  # no odd length
        ("0x1", "bytes2", False),  # no odd length
        # Special bytes behavior
        ("0x12", "bytes", True),
        ("1", "bytes", False),
        ("0x1", "bytes", False),
        # Special string behavior
        (b"", "string", False),
        (b"anything", "string", False),
        (
            b"\x80",
            "string",
            False,
        ),  # bytes that cannot be decoded with utf-8 are invalid
        # Special tuple behavior
        (("0x1234", 0), "(bytes2,int128)", True),
        (("0x123456", 0), "(bytes2,int128)", False),
        (("0x1234", 0), "(bytes,int128)", True),
        (("1", 0), "(bytes,int128)", False),
        (("dennisthepeasant.eth", 0), "(address,int128)", True),
        (("rejects_invalid_domains.eth", 0), "(address,int128)", False),
        ((b"anything", 0), "(string,int128)", False),
        ((b"\x80", 0), "(string,int128)", False),
    ),
)
def test_is_encodable(w3, value, _type, expected):
    actual = w3.is_encodable(_type, value)
    assert actual is expected


@pytest.mark.parametrize(
    "value,_type,expected",
    (
        # Special bytes<M> behavior
        ("0x12", "bytes1", True),
        (b"\x12", "bytes2", True),  # undersized bytes OK
        ("12", "bytes2", True),  # hex strings without leading 0x OK
        ("0123", "bytes2", True),
        ("0123", "bytes1", False),  # no oversize hex strings
        ("1", "bytes2", False),  # no odd length
        ("0x1", "bytes2", False),  # no odd length
        # Special bytes behavior
        ("12", "bytes", True),  # hex strings without leading 0x OK
        ("1", "bytes", False),
        ("0x12", "bytes", True),
        ("0x1", "bytes", False),  # can be decoded as hex
        ("0x0x0x0x", "bytes", False),  # cannot be decoded as hex
        # Special string behavior
        (b"", "string", True),
        (b"anything", "string", True),
        (
            b"\x80",
            "string",
            False,
        ),  # bytes that cannot be decoded with utf-8 are invalid
    ),
)
def test_is_encodable_non_strict(w3, value, _type, expected):
    w3.strict_bytes_type_checking = False
    actual = w3.is_encodable(_type, value)
    assert actual is expected
