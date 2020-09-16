import pytest

from web3.exceptions import (
    ABIEventFunctionNotFound,
    ABIFunctionNotFound,
)


@pytest.fixture()
def abi():
    return '''[{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"function"}, {"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]'''  # noqa: E501


@pytest.mark.parametrize(
    'attribute',
    ('functions', 'events', 'caller')
)
def test_getattr(web3, abi, attribute):
    contract = web3.eth.contract(abi=abi)
    contract_attribute = getattr(contract, attribute)
    assert getattr(contract_attribute, "Increased")


@pytest.mark.parametrize(
    'attribute,error', (
        ('functions', ABIFunctionNotFound),
        ('events', ABIEventFunctionNotFound),
        ('caller', ABIFunctionNotFound),
    )
)
def test_getattr_raises_error(web3, abi, attribute, error):
    contract = web3.eth.contract(abi=abi)
    contract_attribute = getattr(contract, attribute)

    with pytest.raises(error):
        getattr(contract_attribute, "Decreased")


@pytest.mark.parametrize(
    'attribute',
    ('functions', 'events', 'caller')
)
def test_hasattr(web3, abi, attribute):
    contract = web3.eth.contract(abi=abi)
    contract_attribute = getattr(contract, attribute)

    assert hasattr(contract_attribute, "Increased") is True
    assert hasattr(contract_attribute, "Decreased") is False
