import pytest

from web3.exceptions import (
    BadFunctionCallOutput,
    NameNotFound,
)
from web3.utils.ens import (
    contract_ens_addresses,
)


@pytest.fixture
def math_addr(MathContract):
    web3 = MathContract.web3
    deploy_txn = MathContract.deploy({'from': web3.eth.coinbase})
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    return deploy_receipt['contractAddress']


def test_contract_with_unset_address(MathContract):
    with contract_ens_addresses(MathContract, []):
        with pytest.raises(NameNotFound):
            MathContract(address='unsetname.eth')


def test_contract_with_name_address(MathContract, math_addr):
    with contract_ens_addresses(MathContract, [('thedao.eth', math_addr)]):
        mc = MathContract(address='thedao.eth')
        caller = mc.web3.eth.coinbase
        assert mc.address == 'thedao.eth'
        assert mc.call({'from': caller}).return13() == 13


def test_contract_with_name_address_changing(MathContract, math_addr):
    # Contract address is validated once on creation
    with contract_ens_addresses(MathContract, [('thedao.eth', math_addr)]):
        mc = MathContract(address='thedao.eth')

    caller = mc.web3.eth.coinbase
    assert mc.address == 'thedao.eth'

    # what happen when name returns no address at all
    with contract_ens_addresses(mc, []):
        with pytest.raises(NameNotFound):
            mc.call({'from': caller}).return13()

    # what happen when name returns address to different contract
    with contract_ens_addresses(mc, [('thedao.eth', '0x' + '11' * 20)]):
        with pytest.raises(BadFunctionCallOutput):
            mc.call({'from': caller}).return13()

    # contract works again when name resolves correctly
    with contract_ens_addresses(mc, [('thedao.eth', math_addr)]):
        assert mc.call({'from': caller}).return13() == 13
