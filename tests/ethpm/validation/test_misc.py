import pytest

from ethpm.exceptions import ValidationError
from ethpm.validation.misc import validate_address, validate_empty_bytes


@pytest.mark.parametrize(
    "address", (b"\xd3\xcd\xa9\x13\xde\xb6\xf6yg\xb9\x9dg\xac\xdf\xa1q,)6\x01",)
)
def test_validate_address_accepts_canonicalized_addresses(address):
    result = validate_address(address)
    assert result is None


@pytest.mark.parametrize(
    "address",
    (
        "d3cda913deb6f67967b99d67acdfa1712c293601",
        "0xd3cda913deb6f67967b99d67acdfa1712c293601",
        "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
        "\xd3\xcd\xa9\x13\xde\xb6\xf6yg\xb9\x9dg\xac\xdf\xa1q,)6\x01xd",
    ),
)
def test_validate_address_rejects_incorrectly_formatted_adresses(address):
    with pytest.raises(ValidationError):
        validate_address(address)


@pytest.mark.parametrize(
    "offset,length,bytecode",
    (
        (0, 3, b"\00\00\00"),
        (1, 20, b"\01" + bytearray(20) + b"\01"),
        (26, 20, b"\01" + bytearray(20) + b"\01" * 5 + bytearray(20) + b"\01"),
    ),
)
def test_validate_empty_bytes(offset, length, bytecode):
    result = validate_empty_bytes(offset, length, bytecode)
    assert result is None


@pytest.mark.parametrize(
    "offset,length,bytecode",
    (
        (0, 2, b"\00"),
        (0, 3, b"\01\01\01"),
        (1, 1, b"\00\01\00\01"),
        (1, 20, bytearray(20) + b"\01"),
    ),
)
def test_validate_empty_bytes_invalidates(offset, length, bytecode):
    with pytest.raises(ValidationError):
        validate_empty_bytes(offset, length, bytecode)
