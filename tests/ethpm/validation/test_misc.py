import pytest

from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.misc import (
    validate_empty_bytes,
    validate_escaped_string,
)


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
    with pytest.raises(EthPMValidationError):
        validate_empty_bytes(offset, length, bytecode)


@pytest.mark.parametrize(
    "string",
    (
        "abcd",
        "abcd%40",
        "%20%24%26",
    )
)
def test_validate_escaped_strings(string):
    validate_escaped_string(string)


@pytest.mark.parametrize(
    "string",
    (
        "@bcd",
        "@bcd%40",
        "!bcd%40",
        "&bcd%40",
    )
)
def test_validate_escaped_strings_invalidates(string):
    with pytest.raises(EthPMValidationError):
        validate_escaped_string(string)
