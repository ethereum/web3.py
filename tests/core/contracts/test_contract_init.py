import pytest

from eth_tester import EthereumTester

from web3 import Web3
from web3.exceptions import BadFunctionCallOutput
from web3.providers.eth_tester import EthereumTesterProvider


@pytest.fixture
def mock_ens(mocker):
    ENS = mocker.patch('web3.middleware.names.ENS.fromWeb3')
    return ENS.return_value


@pytest.fixture
def MathContract_MockedENS(MathContract, mock_ens):
    provider = EthereumTesterProvider(EthereumTester())
    web3 = Web3(provider)
    MathContract.web3 = web3
    return MathContract


@pytest.fixture
def math_addr(MathContract_MockedENS):
    web3 = MathContract_MockedENS.web3
    deploy_txn = MathContract_MockedENS.deploy({'from': web3.eth.coinbase})
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    return deploy_receipt['contractAddress']


def test_contract_with_unset_address(MathContract, mock_ens):
    mock_ens.address.return_value = None
    with pytest.raises(ValueError):
        MathContract(address='unsetname.eth')


def test_contract_with_name_address(MathContract_MockedENS, math_addr, mock_ens):
    mock_ens.address.return_value = math_addr
    mc = MathContract_MockedENS(address='thedao.eth')
    caller = mc.web3.eth.coinbase
    assert mc.address == 'thedao.eth'
    assert mc.call({'from': caller}).return13() == 13


def test_contract_with_name_address_changing(MathContract_MockedENS, math_addr, mock_ens):
    # show valid address for creating the contract
    mock_ens.address.return_value = math_addr

    mc = MathContract_MockedENS(address='thedao.eth')
    caller = mc.web3.eth.coinbase
    assert mc.address == 'thedao.eth'

    # set up name to return no address at all
    mock_ens.address.return_value = None

    with pytest.raises(ValueError):
        mc.call({'from': caller}).return13()

    # set up name to return address with no contract
    mock_ens.address.return_value = '0x' + '11' * 20

    with pytest.raises(BadFunctionCallOutput):
        mc.call({'from': caller}).return13()

    # set up name to return valid address again
    mock_ens.address.return_value = math_addr

    assert mc.call({'from': caller}).return13() == 13
