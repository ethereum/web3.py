import functools
import pytest

from eth_tester import (
    EthereumTester,
)
from eth_utils import (
    is_checksum_address,
    is_dict,
)

from web3 import Web3
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    PersonalModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)
from web3.utils.module_testing.emitter_contract import (
    EMITTER_ENUM,
)

pytestmark = pytest.mark.filterwarnings("ignore:implicit cast from 'char *'")


@pytest.fixture(scope="session")
def eth_tester():
    _eth_tester = EthereumTester()
    return _eth_tester


@pytest.fixture(scope="session")
def eth_tester_provider(eth_tester):
    provider = EthereumTesterProvider(eth_tester)
    return provider


@pytest.fixture(scope="session")
def web3(eth_tester_provider):
    _web3 = Web3(eth_tester_provider)
    return _web3


#
# Math Contract Setup
#
@pytest.fixture(scope="session")
def math_contract_deploy_txn_hash(web3, math_contract_factory):
    deploy_txn_hash = math_contract_factory.deploy({'from': web3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="session")
def math_contract(web3, math_contract_factory, math_contract_deploy_txn_hash):
    deploy_receipt = web3.eth.getTransactionReceipt(math_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return math_contract_factory(contract_address)


#
# Emitter Contract Setup
#
@pytest.fixture(scope="session")
def emitter_contract_deploy_txn_hash(web3, emitter_contract_factory):
    deploy_txn_hash = emitter_contract_factory.deploy({'from': web3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="session")
def emitter_contract(web3, emitter_contract_factory, emitter_contract_deploy_txn_hash):
    deploy_receipt = web3.eth.getTransactionReceipt(emitter_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return emitter_contract_factory(contract_address)


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


@pytest.fixture(scope="session")
def block_with_txn_with_log(web3, emitter_contract):
    txn_hash = emitter_contract.transact({
        'from': web3.eth.coinbase,
    }).logDouble(which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321)
    txn = web3.eth.getTransaction(txn_hash)
    block = web3.eth.getBlock(txn['blockNumber'])
    return block


@pytest.fixture(scope="session")
def txn_hash_with_log(block_with_txn_with_log):
    return block_with_txn_with_log['transactions'][0]


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


@pytest.fixture
def unlocked_account(web3, unlockable_account, unlockable_account_pw):
    web3.personal.unlockAccount(unlockable_account, unlockable_account_pw)
    yield unlockable_account
    web3.personal.lockAccount(unlockable_account)


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


class TestEthereumTesterWeb3Module(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('EthereumTester/')


def not_implemented(method, exc_type=NotImplementedError):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        with pytest.raises(exc_type):
            method(*args, **kwargs)
    return inner


class TestEthereumTesterEthModule(EthModuleTest):
    test_eth_sign = not_implemented(EthModuleTest.test_eth_sign, ValueError)

    def test_eth_getTransactionReceipt_unmined(self, eth_tester, web3, unlocked_account):
        eth_tester.disable_auto_mine_transactions()
        try:
            super(TestEthereumTesterEthModule, self).test_eth_getTransactionReceipt_unmined(
                web3, unlocked_account,
            )
        finally:
            eth_tester.enable_auto_mine_transactions()
            eth_tester.mine_block()


class TestEthereumTesterVersionModule(VersionModuleTest):
    pass


class TestEthereumTesterNetModule(NetModuleTest):
    pass


class TestEthereumTesterPersonalModule(PersonalModuleTest):
    test_personal_sign_and_ecrecover = not_implemented(
        PersonalModuleTest.test_personal_sign_and_ecrecover,
        ValueError,
    )
