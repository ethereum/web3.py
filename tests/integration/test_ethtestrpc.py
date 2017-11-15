import functools
import sys

import pytest

from eth_utils import (
    is_checksum_address,
    is_dict,
)

from web3 import Web3

from web3.utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    PersonalModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)
from web3.utils.module_testing.math_contract import (
    MATH_BYTECODE,
    MATH_ABI,
)


# Ignore warning in pyethereum 1.6 - will go away with the upgrade
pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture(scope="session")
def web3():
    _web3 = Web3(Web3.EthereumTesterProvider())
    return _web3


@pytest.fixture(scope="session")
def math_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="session")
def math_contract_deploy_txn_hash(math_contract_factory):
    deploy_txn_hash = math_contract_factory.deploy()
    return deploy_txn_hash


@pytest.fixture(scope="session")
def math_contract(web3, math_contract_factory, math_contract_deploy_txn_hash):
    deploy_receipt = web3.eth.getTransactionReceipt(math_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return math_contract_factory(contract_address)


@pytest.fixture(scope="session")
def empty_block(web3):
    web3.testing.mine()
    block = web3.eth.getBlock("latest")
    assert not block['transactions']
    return block


@pytest.fixture(scope="session")
def block_with_txn(web3):
    txn_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': web3.eth.coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': 1,
    })
    txn = web3.eth.getTransaction(txn_hash)
    block = web3.eth.getBlock(txn['blockNumber'])
    return block


@pytest.fixture(scope="session")
def mined_txn_hash(block_with_txn):
    return block_with_txn['transactions'][0]


@pytest.fixture
def unlocked_account(web3):
    return web3.eth.coinbase


UNLOCKABLE_PRIVATE_KEY = '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'


@pytest.fixture(scope='session')
def unlockable_account_pw(web3):
    return 'web3-testing'


@pytest.fixture(scope='session')
def unlockable_account(web3, unlockable_account_pw):
    account = web3.personal.importRawKey(UNLOCKABLE_PRIVATE_KEY, unlockable_account_pw)
    web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': account,
        'value': web3.toWei(10, 'ether'),
    })
    yield account
    web3.personal.lockAccount(account)


@pytest.fixture(scope="session")
def funded_account_for_raw_txn(web3):
    account = '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6'
    web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': account,
        'value': web3.toWei(10, 'ether'),
        'gas': 21000,
        'gas_price': 1,
    })
    return account


@pytest.fixture(scope="session")
def block_with_txn_with_log():
    # skip any tests that need this for now since it's deprecated.
    pytest.skip()


class TestEthTestRPCWeb3Module(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('TestRPC/')


def not_implemented(method, exc_type=AttributeError):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        if sys.version_info.major == 2:
            # pytest doesn't do the right thing with the fixture arguments in
            # python2 so just don't run it.
            return
        with pytest.raises(exc_type):
            method(*args, **kwargs)
    return inner


class TestEthTestRPCEthModule(EthModuleTest):
    #
    # Eth-Testrpc doesn't comply with RPC spec in many ways.
    #
    test_eth_hashrate = not_implemented(EthModuleTest.test_eth_hashrate)

    test_eth_getBlockTransactionCountByHash_empty_block = not_implemented(
        EthModuleTest.test_eth_getBlockTransactionCountByHash_empty_block,
    )
    test_eth_getBlockTransactionCountByNumber_empty_block = not_implemented(
        EthModuleTest.test_eth_getBlockTransactionCountByNumber_empty_block,
    )

    test_eth_getBlockTransactionCountByHash_block_with_txn = not_implemented(
        EthModuleTest.test_eth_getBlockTransactionCountByHash_block_with_txn,
    )
    test_eth_getBlockTransactionCountByNumber_block_with_txn = not_implemented(
        EthModuleTest.test_eth_getBlockTransactionCountByNumber_block_with_txn,
    )

    test_eth_getUncleCountByBlockHash = not_implemented(
        EthModuleTest.test_eth_getUncleCountByBlockHash,
    )
    test_eth_getUncleCountByBlockNumber = not_implemented(
        EthModuleTest.test_eth_getUncleCountByBlockNumber,
    )

    test_eth_sign = not_implemented(
        EthModuleTest.test_eth_sign,
    )

    test_eth_sendRawTransaction = not_implemented(
        EthModuleTest.test_eth_sendRawTransaction, ValueError,
    )

    test_eth_getTransactionByBlockHashAndIndex = not_implemented(
        EthModuleTest.test_eth_getTransactionByBlockHashAndIndex,
    )
    test_eth_getTransactionByBlockNumberAndIndex = not_implemented(
        EthModuleTest.test_eth_getTransactionByBlockNumberAndIndex,
    )

    test_eth_getTransactionReceipt_unmined = not_implemented(
        EthModuleTest.test_eth_getTransactionReceipt_unmined, AssertionError,
    )

    test_eth_newBlockFilter = not_implemented(
        EthModuleTest.test_eth_newBlockFilter, NotImplementedError,
    )

    test_eth_newPendingTransactionFilter = not_implemented(
        EthModuleTest.test_eth_newPendingTransactionFilter, NotImplementedError,
    )


class TestEthTestRPCVersionModule(VersionModuleTest):
    pass


class TestEthTestRPCNetModule(NetModuleTest):
    pass


class TestEthTestRPCPersonalModule(PersonalModuleTest):
    test_personal_sign_and_ecrecover = not_implemented(
        PersonalModuleTest.test_personal_sign_and_ecrecover,
    )
