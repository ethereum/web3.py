import pytest

from web3.contract.async_contract import (
    AsyncContract,
)
from web3.contract.contract import (
    Contract,
)
from web3.exceptions import (
    Web3ValueError,
)


def test_functions_find_by_name(event_contract: "Contract") -> None:
    functions = event_contract.functions.find_by_name("logTwoEvents")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function logTwoEvents(uint256)>"]


def test_functions_find_by_name_with_ambiguous_name(math_contract: "Contract") -> None:
    functions = math_contract.functions.find_by_name("incrementCounter")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == [
        "<Function incrementCounter()>",
        "<Function incrementCounter(uint256)>",
    ]


def test_functions_find_by_name_no_result(
    math_contract: "Contract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching name"
    ):
        math_contract.functions.find_by_name("notafunction")


def test_async_functions_find_by_name(
    async_math_contract: "AsyncContract",
) -> None:
    functions = async_math_contract.functions.find_by_name("add")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function add(int256,int256)>"]


def test_async_ambiguous_functions_find_by_name(
    async_math_contract: "AsyncContract",
) -> None:
    functions = async_math_contract.functions.find_by_name("incrementCounter")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == [
        "<Function incrementCounter()>",
        "<Function incrementCounter(uint256)>",
    ]


def test_async_functions_find_by_name_no_result(
    async_math_contract: "AsyncContract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching name"
    ):
        async_math_contract.functions.find_by_name("notafunction")


def test_functions_find_by_signature(event_contract: "Contract") -> None:
    functions = event_contract.functions.find_by_signature("logTwoEvents(uint256)")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function logTwoEvents(uint256)>"]


def test_functions_find_by_signature_with_ambiguous_name(
    math_contract: "Contract",
) -> None:
    functions = math_contract.functions.find_by_signature("incrementCounter(uint256)")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function incrementCounter(uint256)>"]


def test_functions_find_by_signature_no_result(
    math_contract: "Contract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching signature"
    ):
        math_contract.functions.find_by_signature("notafunction()")


def test_async_functions_find_by_signature(
    async_math_contract: "AsyncContract",
) -> None:
    functions = async_math_contract.functions.find_by_signature("add(int256,int256)")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function add(int256,int256)>"]


def test_async_functions_find_by_signature_with_ambiguous_name(
    async_math_contract: "AsyncContract",
) -> None:
    functions = async_math_contract.functions.find_by_signature(
        "incrementCounter(uint256)"
    )

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function incrementCounter(uint256)>"]


def test_async_functions_find_by_signature_no_result(
    async_math_contract: "AsyncContract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching signature"
    ):
        async_math_contract.functions.find_by_signature("notafunction()")


def test_functions_find_by_selector(event_contract: "Contract") -> None:
    # keccak(text="logTwoEvents(uint256)")[:4] == b"X\x18\xfa\xd7"
    functions = event_contract.functions.find_by_selector(b"X\x18\xfa\xd7")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function logTwoEvents(uint256)>"]


def test_functions_find_by_selector_no_result(
    math_contract: "Contract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching selector"
    ):
        # keccak(text="notafunction()")[:4] == b'j(\x15>'
        math_contract.functions.find_by_selector(b"j(\x15>")


def test_async_functions_find_by_selector(async_math_contract: "AsyncContract") -> None:
    # keccak(text="add(int256,int256)")[:4] == b"\xa5\xf3\xc2;"
    functions = async_math_contract.functions.find_by_selector(b"\xa5\xf3\xc2;")

    expected_functions = [repr(fn) for fn in functions]
    assert expected_functions == ["<Function add(int256,int256)>"]


def test_async_functions_find_by_selector_no_result(
    async_math_contract: "AsyncContract",
) -> None:
    with pytest.raises(
        Web3ValueError, match="Could not find any function with matching selector"
    ):
        # keccak(text="notafunction()")[:4] == b'j(\x15>'
        async_math_contract.functions.find_by_selector(b"j(\x15>")
