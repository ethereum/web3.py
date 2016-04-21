import pytest
import web3.utils.abi as abi


@pytest.mark.parametrize(
    "value,expected",
    [
    (
        "helloworld()",
        "helloworld"
    ),
    (
        "helloworld1(int)",
        "helloworld1"
    ),
    (
        "helloworld2(int,string)",
        "helloworld2"
    )
    ]
)
def test_extractDisplayName(value, expected):
    assert abi.extractDisplayName(value) == expected

@pytest.mark.parametrize(
   "value,expected",
    [
    (
        "helloworld()",
        ""
    ),
    (
        "helloworld1(int)",
        "int"
    ),
    (
        "helloworld2(int,string)",
        "int,string"
    ),
    (
        "helloworld3(int, string)",
        "int,string"
    )
    ]
)
def test_extractTypeName(value, expected):
    assert abi.extractTypeName(value) == expected