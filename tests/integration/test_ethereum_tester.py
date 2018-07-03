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


@pytest.fixture(scope="module")
def eth_tester():
    _eth_tester = EthereumTester()
    return _eth_tester


@pytest.fixture(scope="module")
def eth_tester_provider(eth_tester):
    provider = EthereumTesterProvider(eth_tester)
    return provider


@pytest.fixture(scope="module")
def web3(eth_tester_provider):
    _web3 = Web3(eth_tester_provider)
    return _web3


#
# Math Contract Setup
#
@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(web3, math_contract_factory):
    deploy_txn_hash = math_contract_factory.constructor().transact({'from': web3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="module")
def math_contract(web3, math_contract_factory, math_contract_deploy_txn_hash):
    deploy_receipt = web3.eth.waitForTransactionReceipt(math_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return math_contract_factory(contract_address)


@pytest.fixture(scope="module")
def math_contract_address(math_contract, address_conversion_func):
    return address_conversion_func(math_contract.address)

#
# Emitter Contract Setup
#


@pytest.fixture(scope="module")
def emitter_contract_deploy_txn_hash(web3, emitter_contract_factory):
    deploy_txn_hash = emitter_contract_factory.constructor().transact({'from': web3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="module")
def emitter_contract(web3, emitter_contract_factory, emitter_contract_deploy_txn_hash):
    deploy_receipt = web3.eth.waitForTransactionReceipt(emitter_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return emitter_contract_factory(contract_address)


@pytest.fixture(scope="module")
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture(scope="module")
def empty_block(web3):
    web3.testing.mine()
    block = web3.eth.getBlock("latest")
    assert not block['transactions']
    return block


@pytest.fixture(scope="module")
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


@pytest.fixture(scope="module")
def mined_txn_hash(block_with_txn):
    return block_with_txn['transactions'][0]


@pytest.fixture(scope="module")
def block_with_txn_with_log(web3, emitter_contract):
    txn_hash = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321,
    ).transact({
        'from': web3.eth.coinbase,
    })
    txn = web3.eth.getTransaction(txn_hash)
    block = web3.eth.getBlock(txn['blockNumber'])
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(block_with_txn_with_log):
    return block_with_txn_with_log['transactions'][0]


UNLOCKABLE_PRIVATE_KEY = '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'


@pytest.fixture(scope='module')
def unlockable_account_pw(web3):
    return 'web3-testing'


@pytest.fixture(scope='module')
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


@pytest.fixture()
def unlockable_account_dual_type(unlockable_account, address_conversion_func):
    return address_conversion_func(unlockable_account)


@pytest.fixture
def unlocked_account_dual_type(web3, unlockable_account_dual_type, unlockable_account_pw):
    web3.personal.unlockAccount(unlockable_account_dual_type, unlockable_account_pw)
    yield unlockable_account_dual_type
    web3.personal.lockAccount(unlockable_account_dual_type)


@pytest.fixture(scope="module")
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


def disable_auto_mine(func):
    @functools.wraps(func)
    def func_wrapper(self, eth_tester, *args, **kwargs):
        snapshot = eth_tester.take_snapshot()
        eth_tester.disable_auto_mine_transactions()
        try:
            func(self, eth_tester, *args, **kwargs)
        finally:
            eth_tester.enable_auto_mine_transactions()
            eth_tester.mine_block()
            eth_tester.revert_to_snapshot(snapshot)
    return func_wrapper


class TestEthereumTesterEthModule(EthModuleTest):
    test_eth_sign = not_implemented(EthModuleTest.test_eth_sign, ValueError)

    @disable_auto_mine
    def test_eth_getTransactionReceipt_unmined(self, eth_tester, web3, unlocked_account):
        super().test_eth_getTransactionReceipt_unmined(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction(self, eth_tester, web3, unlocked_account):
        super().test_eth_replaceTransaction(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction_incorrect_nonce(self, eth_tester, web3, unlocked_account):
        super().test_eth_replaceTransaction_incorrect_nonce(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction_gas_price_too_low(self, eth_tester, web3, unlocked_account):
        super().test_eth_replaceTransaction_gas_price_too_low(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction_gas_price_defaulting_minimum(self,
                                                                 eth_tester,
                                                                 web3,
                                                                 unlocked_account):
        super().test_eth_replaceTransaction_gas_price_defaulting_minimum(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction_gas_price_defaulting_strategy_higher(self,
                                                                         eth_tester,
                                                                         web3,
                                                                         unlocked_account):
        super().test_eth_replaceTransaction_gas_price_defaulting_strategy_higher(
            web3, unlocked_account
        )

    @disable_auto_mine
    def test_eth_replaceTransaction_gas_price_defaulting_strategy_lower(self,
                                                                        eth_tester,
                                                                        web3,
                                                                        unlocked_account):
        super().test_eth_replaceTransaction_gas_price_defaulting_strategy_lower(
            web3, unlocked_account
        )

    @disable_auto_mine
    def test_eth_modifyTransaction(self, eth_tester, web3, unlocked_account):
        super().test_eth_modifyTransaction(web3, unlocked_account)

    @disable_auto_mine
    def test_eth_call_old_contract_state(self, eth_tester, web3, math_contract, unlocked_account):
        # For now, ethereum tester cannot give call results in the pending block.
        # Once that feature is added, then delete the except/else blocks.
        try:
            super().test_eth_call_old_contract_state(web3, math_contract, unlocked_account)
        except AssertionError as err:
            if str(err) == "pending call result was 0 instead of 1":
                pass
            else:
                raise err
        else:
            raise AssertionError("eth-tester was unexpectedly able to give the pending call result")

    def test_eth_getStorageAt(self, web3, emitter_contract_address):
        pytest.xfail('json-rpc method is not implemented on eth-tester')
        super().test_eth_getStorageAt(web3, emitter_contract_address)


class TestEthereumTesterVersionModule(VersionModuleTest):
    pass


class TestEthereumTesterNetModule(NetModuleTest):
    pass


class TestEthereumTesterPersonalModule(PersonalModuleTest):
    test_personal_sign_and_ecrecover = not_implemented(
        PersonalModuleTest.test_personal_sign_and_ecrecover,
        ValueError,
    )
