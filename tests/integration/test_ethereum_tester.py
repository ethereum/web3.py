import functools
import pytest

from eth_tester import (
    EthereumTester,
)
from eth_tester.exceptions import (
    TransactionFailed,
)
from eth_utils import (
    is_checksum_address,
    is_dict,
    is_integer,
)

from web3 import Web3
from web3._utils.module_testing import (
    EthModuleTest,
    GoEthereumPersonalModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)
from web3._utils.module_testing.emitter_contract import (
    EMITTER_ENUM,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.types import (  # noqa: F401
    BlockData,
)


@pytest.fixture(scope="module")
def eth_tester():
    _eth_tester = EthereumTester()
    return _eth_tester


@pytest.fixture(scope="module")
def eth_tester_provider(eth_tester):
    provider = EthereumTesterProvider(eth_tester)
    return provider


@pytest.fixture(scope="module")
def w3(eth_tester_provider):
    _w3 = Web3(eth_tester_provider)
    return _w3


#
# Math Contract Setup
#
@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(w3, math_contract_factory):
    deploy_txn_hash = math_contract_factory.constructor().transact({'from': w3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="module")
def math_contract(w3, math_contract_factory, math_contract_deploy_txn_hash):
    deploy_receipt = w3.eth.wait_for_transaction_receipt(math_contract_deploy_txn_hash)
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
def emitter_contract_deploy_txn_hash(w3, emitter_contract_factory):
    deploy_txn_hash = emitter_contract_factory.constructor().transact({'from': w3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="module")
def emitter_contract(w3, emitter_contract_factory, emitter_contract_deploy_txn_hash):
    deploy_receipt = w3.eth.wait_for_transaction_receipt(emitter_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return emitter_contract_factory(contract_address)


@pytest.fixture(scope="module")
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture(scope="module")
def empty_block(w3):
    w3.testing.mine()
    block = w3.eth.get_block("latest")
    assert not block['transactions']
    return block


@pytest.fixture(scope="module")
def block_with_txn(w3):
    txn_hash = w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': w3.eth.coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': 1000000000,  # needs to be greater than base_fee post London
    })
    txn = w3.eth.get_transaction(txn_hash)
    block = w3.eth.get_block(txn['blockNumber'])
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(block_with_txn):
    return block_with_txn['transactions'][0]


@pytest.fixture(scope="module")
def block_with_txn_with_log(w3, emitter_contract):
    txn_hash = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321,
    ).transact({
        'from': w3.eth.coinbase,
    })
    txn = w3.eth.get_transaction(txn_hash)
    block = w3.eth.get_block(txn['blockNumber'])
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(block_with_txn_with_log):
    return block_with_txn_with_log['transactions'][0]


#
# Revert Contract Setup
#
@pytest.fixture(scope="module")
def revert_contract_deploy_txn_hash(w3, revert_contract_factory):
    deploy_txn_hash = revert_contract_factory.constructor().transact({'from': w3.eth.coinbase})
    return deploy_txn_hash


@pytest.fixture(scope="module")
def revert_contract(w3, revert_contract_factory, revert_contract_deploy_txn_hash):
    deploy_receipt = w3.eth.wait_for_transaction_receipt(revert_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    return revert_contract_factory(contract_address)


UNLOCKABLE_PRIVATE_KEY = '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'


@pytest.fixture(scope='module')
def unlockable_account_pw():
    return 'web3-testing'


@pytest.fixture(scope='module')
def unlockable_account(w3, unlockable_account_pw):
    account = w3.geth.personal.import_raw_key(UNLOCKABLE_PRIVATE_KEY, unlockable_account_pw)
    w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': account,
        'value': w3.toWei(10, 'ether'),
        'gas': 21000,
    })
    yield account


@pytest.fixture
def unlocked_account(w3, unlockable_account, unlockable_account_pw):
    w3.geth.personal.unlock_account(unlockable_account, unlockable_account_pw)
    yield unlockable_account
    w3.geth.personal.lock_account(unlockable_account)


@pytest.fixture()
def unlockable_account_dual_type(unlockable_account, address_conversion_func):
    return address_conversion_func(unlockable_account)


@pytest.fixture
def unlocked_account_dual_type(w3, unlockable_account_dual_type, unlockable_account_pw):
    w3.geth.personal.unlock_account(unlockable_account_dual_type, unlockable_account_pw)
    yield unlockable_account_dual_type
    w3.geth.personal.lock_account(unlockable_account_dual_type)


@pytest.fixture(scope="module")
def funded_account_for_raw_txn(w3):
    account = '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6'
    w3.eth.send_transaction({
        'from': w3.eth.coinbase,
        'to': account,
        'value': w3.toWei(10, 'ether'),
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
    test_eth_max_priority_fee_with_fee_history_calculation = not_implemented(
        EthModuleTest.test_eth_max_priority_fee_with_fee_history_calculation,
        ValueError
    )
    test_eth_sign = not_implemented(EthModuleTest.test_eth_sign, ValueError)
    test_eth_sign_ens_names = not_implemented(
        EthModuleTest.test_eth_sign_ens_names, ValueError
    )
    test_eth_signTypedData_deprecated = not_implemented(
        EthModuleTest.test_eth_signTypedData_deprecated,
        ValueError
    )
    test_eth_sign_typed_data = not_implemented(
        EthModuleTest.test_eth_sign_typed_data,
        ValueError
    )
    test_eth_signTransaction_deprecated = not_implemented(
        EthModuleTest.test_eth_signTransaction_deprecated,
        ValueError
    )
    test_eth_sign_transaction_legacy = not_implemented(
        EthModuleTest.test_eth_sign_transaction_legacy,
        ValueError
    )
    test_eth_sign_transaction = not_implemented(EthModuleTest.test_eth_sign_transaction, ValueError)
    test_eth_sign_transaction_hex_fees = not_implemented(
        EthModuleTest.test_eth_sign_transaction_hex_fees, ValueError
    )
    test_eth_sign_transaction_ens_names = not_implemented(
        EthModuleTest.test_eth_sign_transaction_ens_names, ValueError
    )
    test_eth_submitHashrate_deprecated = not_implemented(
        EthModuleTest.test_eth_submitHashrate_deprecated, ValueError)
    test_eth_submit_hashrate = not_implemented(EthModuleTest.test_eth_submit_hashrate, ValueError)
    test_eth_submitWork_deprecated = not_implemented(
        EthModuleTest.test_eth_submitWork_deprecated, ValueError)
    test_eth_submit_work = not_implemented(EthModuleTest.test_eth_submit_work, ValueError)
    test_eth_get_raw_transaction = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction, ValueError)
    test_eth_get_raw_transaction_raises_error = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction, ValueError)
    test_eth_get_raw_transaction_by_block = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction_by_block, ValueError
    )
    test_eth_get_raw_transaction_by_block_raises_error = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction_by_block, ValueError
    )
    test_eth_replace_transaction_already_mined = not_implemented(
        EthModuleTest.test_eth_replace_transaction_already_mined, ValueError
    )

    def test_eth_getBlockByHash_pending(
        self, w3: "Web3"
    ) -> None:
        block = w3.eth.get_block('pending')
        assert block['hash'] is not None

    @pytest.mark.xfail(reason='eth_feeHistory is not implemented on eth-tester')
    def test_eth_fee_history(self, w3: "Web3"):
        super().test_eth_fee_history(w3)

    @pytest.mark.xfail(reason='eth_feeHistory is not implemented on eth-tester')
    def test_eth_fee_history_with_integer(self, w3: "Web3"):
        super().test_eth_fee_history_with_integer(w3)

    @pytest.mark.xfail(reason='eth_feeHistory is not implemented on eth-tester')
    def test_eth_fee_history_no_reward_percentiles(self, w3: "Web3"):
        super().test_eth_fee_history_no_reward_percentiles(w3)

    @disable_auto_mine
    def test_eth_get_transaction_receipt_unmined(self, eth_tester, w3, unlocked_account):
        super().test_eth_get_transaction_receipt_unmined(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction_legacy(self, eth_tester, w3, unlocked_account):
        super().test_eth_replace_transaction_legacy(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction(self, eth_tester, w3, unlocked_account):
        super().test_eth_replace_transaction(w3, unlocked_account)

    @disable_auto_mine
    @pytest.mark.xfail(reason='py-evm does not raise on EIP-1559 transaction underpriced')
    # TODO: This might also be an issue in py-evm worth looking into. See reason above.
    def test_eth_replace_transaction_underpriced(self, eth_tester, w3, unlocked_account):
        super().test_eth_replace_transaction_underpriced(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replaceTransaction_deprecated(self, eth_tester, w3, unlocked_account):
        super().test_eth_replaceTransaction_deprecated(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction_incorrect_nonce(self, eth_tester, w3, unlocked_account):
        super().test_eth_replace_transaction_incorrect_nonce(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_too_low(self, eth_tester, w3, unlocked_account):
        super().test_eth_replace_transaction_gas_price_too_low(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_minimum(self,
                                                                  eth_tester,
                                                                  w3,
                                                                  unlocked_account):
        super().test_eth_replace_transaction_gas_price_defaulting_minimum(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_strategy_higher(self,
                                                                          eth_tester,
                                                                          w3,
                                                                          unlocked_account):
        super().test_eth_replace_transaction_gas_price_defaulting_strategy_higher(
            w3, unlocked_account
        )

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_strategy_lower(self,
                                                                         eth_tester,
                                                                         w3,
                                                                         unlocked_account):
        super().test_eth_replace_transaction_gas_price_defaulting_strategy_lower(
            w3, unlocked_account
        )

    @disable_auto_mine
    def test_eth_modifyTransaction_deprecated(self, eth_tester, w3, unlocked_account):
        super().test_eth_modifyTransaction_deprecated(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_modify_transaction_legacy(self, eth_tester, w3, unlocked_account):
        super().test_eth_modify_transaction_legacy(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_modify_transaction(self, eth_tester, w3, unlocked_account):
        super().test_eth_modify_transaction(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_call_old_contract_state(self, eth_tester, w3, math_contract, unlocked_account):
        # For now, ethereum tester cannot give call results in the pending block.
        # Once that feature is added, then delete the except/else blocks.
        try:
            super().test_eth_call_old_contract_state(w3, math_contract, unlocked_account)
        except AssertionError as err:
            if str(err) == "pending call result was 0 instead of 1":
                pass
            else:
                raise err
        else:
            raise AssertionError("eth-tester was unexpectedly able to give the pending call result")

    @pytest.mark.xfail(reason='json-rpc method is not implemented on eth-tester')
    def test_eth_get_storage_at(self, w3, emitter_contract_address):
        super().test_eth_get_storage_at(w3, emitter_contract_address)

    @pytest.mark.xfail(reason='json-rpc method is not implemented on eth-tester')
    def test_eth_getStorageAt_deprecated(self, w3, emitter_contract_address):
        super().test_eth_getStorageAt_deprecated(w3, emitter_contract_address)

    @pytest.mark.xfail(reason='json-rpc method is not implemented on eth-tester')
    def test_eth_get_storage_at_ens_name(self, w3, emitter_contract_address):
        super().test_eth_get_storage_at_ens_name(w3, emitter_contract_address)

    def test_eth_estimate_gas_with_block(self,
                                         w3,
                                         unlocked_account_dual_type):
        super().test_eth_estimate_gas_with_block(
            w3, unlocked_account_dual_type
        )

    def test_eth_chain_id(self, w3):
        chain_id = w3.eth.chain_id
        assert is_integer(chain_id)
        assert chain_id == 61

    def test_eth_chainId(self, w3):
        with pytest.warns(DeprecationWarning):
            chain_id = w3.eth.chainId
        assert is_integer(chain_id)
        assert chain_id == 61

    @disable_auto_mine
    def test_eth_wait_for_transaction_receipt_unmined(self,
                                                      eth_tester,
                                                      w3,
                                                      unlocked_account_dual_type):
        super().test_eth_wait_for_transaction_receipt_unmined(w3, unlocked_account_dual_type)

    @pytest.mark.xfail(raises=TypeError, reason="call override param not implemented on eth-tester")
    def test_eth_call_with_override(self, w3, revert_contract):
        super().test_eth_call_with_override(w3, revert_contract)

    def test_eth_call_revert_with_msg(self, w3, revert_contract, unlocked_account):
        with pytest.raises(TransactionFailed,
                           match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            w3.eth.call(txn_params)

    def test_eth_call_revert_without_msg(self, w3, revert_contract, unlocked_account):
        with pytest.raises(TransactionFailed, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithoutMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            w3.eth.call(txn_params)

    def test_eth_estimate_gas_revert_with_msg(self, w3, revert_contract, unlocked_account):
        with pytest.raises(TransactionFailed,
                           match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            w3.eth.estimate_gas(txn_params)

    def test_eth_estimate_gas_revert_without_msg(self, w3, revert_contract, unlocked_account):
        with pytest.raises(TransactionFailed, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithoutMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            w3.eth.estimate_gas(txn_params)

    @disable_auto_mine
    def test_eth_send_transaction(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_transaction_legacy(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_legacy(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_raw_transaction(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_raw_transaction(w3, unlocked_account)

    @disable_auto_mine
    @pytest.mark.parametrize("max_fee", (1000000000, None), ids=["with_max_fee", "without_max_fee"])
    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
        self, eth_tester, w3, unlocked_account, max_fee,
    ):
        super().test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
            w3, unlocked_account, max_fee
        )

    @disable_auto_mine
    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
        self, eth_tester, w3, unlocked_account
    ):
        super().test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
            w3, unlocked_account,
        )

    @disable_auto_mine
    def test_eth_sendTransaction_deprecated(self, eth_tester, w3, unlocked_account):
        super().test_eth_sendTransaction_deprecated(w3, unlocked_account)

    @pytest.mark.xfail(raises=ValueError, reason="eth-tester does not have miner_start support")
    def test_eth_send_transaction_with_nonce(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_with_nonce(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_transaction_default_fees(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_default_fees(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_transaction_hex_fees(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_hex_fees(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_transaction_no_gas(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_no_gas(w3, unlocked_account)

    @disable_auto_mine
    def test_eth_send_transaction_no_max_fee(self, eth_tester, w3, unlocked_account):
        super().test_eth_send_transaction_no_max_fee(w3, unlocked_account)


class TestEthereumTesterVersionModule(VersionModuleTest):
    pass


class TestEthereumTesterNetModule(NetModuleTest):
    pass


# Use web3.geth.personal namespace for testing eth-tester
class TestEthereumTesterPersonalModule(GoEthereumPersonalModuleTest):
    test_personal_sign_and_ecrecover = not_implemented(
        GoEthereumPersonalModuleTest.test_personal_sign_and_ecrecover,
        ValueError,
    )
    test_personal_sign_and_ecrecover_deprecated = not_implemented(
        GoEthereumPersonalModuleTest.test_personal_sign_and_ecrecover,
        ValueError,
    )

    # Test overridden here since eth-tester returns False rather than None for failed unlock
    def test_personal_unlock_account_failure(self,
                                             w3,
                                             unlockable_account_dual_type):
        result = w3.geth.personal.unlock_account(unlockable_account_dual_type, 'bad-password')
        assert result is False

    def test_personal_unlockAccount_failure_deprecated(self,
                                                       w3,
                                                       unlockable_account_dual_type):
        with pytest.warns(DeprecationWarning,
                          match="unlockAccount is deprecated in favor of unlock_account"):
            result = w3.geth.personal.unlockAccount(unlockable_account_dual_type, 'bad-password')
            assert result is False

    @pytest.mark.xfail(raises=ValueError, reason="list_wallets not implemented in eth-tester")
    def test_personal_list_wallets(self, w3: "Web3") -> None:
        super().test_personal_list_wallets(w3)
