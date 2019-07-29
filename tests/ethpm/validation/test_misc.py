import pytest

from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.misc import (
    validate_empty_bytes,
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
