import functools
import pytest
from typing import (
    TYPE_CHECKING,
)

from eth_tester.exceptions import (
    TransactionFailed,
)
from eth_utils import (
    is_integer,
)

from web3._utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    Web3ModuleTest,
)
from web3._utils.module_testing.eth_module import (
    UNKNOWN_ADDRESS,
)
from web3.exceptions import (
    MethodUnavailable,
    Web3TypeError,
)
from web3.types import (
    BlockData,
)

if TYPE_CHECKING:
    from web3 import (
        Web3,
    )


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
            eth_tester.revert_to_snapshot(snapshot)

    return func_wrapper


class EthereumTesterWeb3Module(Web3ModuleTest):
    def _check_web3_client_version(self, client_version):
        assert client_version.startswith("EthereumTester/")

    test_batch_requests = not_implemented(
        Web3ModuleTest.test_batch_requests, Web3TypeError
    )
    test_batch_requests_raises_for_common_unsupported_methods = not_implemented(
        Web3ModuleTest.test_batch_requests_raises_for_common_unsupported_methods,
        Web3TypeError,
    )
    test_batch_requests_initialized_as_object = not_implemented(
        Web3ModuleTest.test_batch_requests_initialized_as_object, Web3TypeError
    )
    test_batch_requests_cancel = not_implemented(
        Web3ModuleTest.test_batch_requests_cancel, Web3TypeError
    )
    test_batch_requests_clear = not_implemented(
        Web3ModuleTest.test_batch_requests_clear, Web3TypeError
    )


class EthereumTesterEthModule(EthModuleTest):
    test_eth_sign = not_implemented(EthModuleTest.test_eth_sign, MethodUnavailable)
    test_eth_sign_ens_names = not_implemented(
        EthModuleTest.test_eth_sign_ens_names, MethodUnavailable
    )
    test_eth_sign_typed_data = not_implemented(
        EthModuleTest.test_eth_sign_typed_data, MethodUnavailable
    )
    test_eth_sign_transaction_legacy = not_implemented(
        EthModuleTest.test_eth_sign_transaction_legacy, MethodUnavailable
    )
    test_eth_sign_transaction = not_implemented(
        EthModuleTest.test_eth_sign_transaction, MethodUnavailable
    )
    test_eth_sign_transaction_hex_fees = not_implemented(
        EthModuleTest.test_eth_sign_transaction_hex_fees, MethodUnavailable
    )
    test_eth_sign_transaction_ens_names = not_implemented(
        EthModuleTest.test_eth_sign_transaction_ens_names, MethodUnavailable
    )
    test_eth_get_raw_transaction = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction, MethodUnavailable
    )
    test_eth_get_raw_transaction_raises_error = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction, MethodUnavailable
    )
    test_eth_get_raw_transaction_by_block = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction_by_block, MethodUnavailable
    )
    test_eth_get_raw_transaction_by_block_raises_error = not_implemented(
        EthModuleTest.test_eth_get_raw_transaction_by_block, MethodUnavailable
    )
    test_eth_call_with_override_param_type_check = not_implemented(
        EthModuleTest.test_eth_call_with_override_param_type_check,
        TypeError,
    )
    test_eth_estimate_gas_with_override_param_type_check = not_implemented(
        EthModuleTest.test_eth_estimate_gas_with_override_param_type_check,
        TypeError,
    )
    test_eth_create_access_list = not_implemented(
        EthModuleTest.test_eth_create_access_list,
        MethodUnavailable,
    )
    test_eth_call_with_override_code = not_implemented(
        EthModuleTest.test_eth_call_with_override_code,
        TypeError,
    )
    test_eth_getBlockReceipts_hash = not_implemented(
        EthModuleTest.test_eth_getBlockReceipts_hash,
        MethodUnavailable,
    )
    test_eth_getBlockReceipts_not_found = not_implemented(
        EthModuleTest.test_eth_getBlockReceipts_not_found,
        MethodUnavailable,
    )
    test_eth_getBlockReceipts_with_integer = not_implemented(
        EthModuleTest.test_eth_getBlockReceipts_with_integer,
        MethodUnavailable,
    )
    test_eth_getBlockReceipts_safe = not_implemented(
        EthModuleTest.test_eth_getBlockReceipts_safe,
        MethodUnavailable,
    )
    test_eth_getBlockReceipts_finalized = not_implemented(
        EthModuleTest.test_eth_getBlockReceipts_finalized,
        MethodUnavailable,
    )

    def test_eth_getBlockByHash_pending(self, w3: "Web3") -> None:
        block = w3.eth.get_block("pending")
        assert block["hash"] is not None

    @disable_auto_mine
    def test_eth_get_transaction_receipt_unmined(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_get_transaction_receipt_unmined(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_replace_transaction_legacy(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_legacy(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_replace_transaction(self, eth_tester, w3, keyfile_account_address):
        super().test_eth_replace_transaction(w3, keyfile_account_address)

    @disable_auto_mine
    @pytest.mark.xfail(
        reason="py-evm does not raise on EIP-1559 transaction underpriced"
    )
    # TODO: This might also be an issue in py-evm worth looking into. See reason above.
    def test_eth_replace_transaction_underpriced(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_underpriced(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_replace_transaction_incorrect_nonce(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_incorrect_nonce(
            w3, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_too_low(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_gas_price_too_low(
            w3, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_minimum(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_gas_price_defaulting_minimum(
            w3, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_strategy_higher(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_gas_price_defaulting_strategy_higher(
            w3, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_replace_transaction_gas_price_defaulting_strategy_lower(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_replace_transaction_gas_price_defaulting_strategy_lower(
            w3, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_modify_transaction_legacy(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_modify_transaction_legacy(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_modify_transaction(self, eth_tester, w3, keyfile_account_address):
        super().test_eth_modify_transaction(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_get_logs_without_logs(
        self, eth_tester, w3: "Web3", block_with_txn_with_log: BlockData
    ) -> None:
        # Note: This was the old way the test was written before geth started returning
        # an error when the `toBlock` was before the `fromBlock`

        # Test with block range
        filter_params = {
            "fromBlock": 0,
            "toBlock": block_with_txn_with_log["number"] - 1,
        }
        result = w3.eth.get_logs(filter_params)
        assert len(result) == 0

        # the range is wrong
        filter_params = {
            "fromBlock": block_with_txn_with_log["number"],
            "toBlock": block_with_txn_with_log["number"] - 1,
        }
        result = w3.eth.get_logs(filter_params)
        assert len(result) == 0

        # Test with `address`

        # filter with other address
        filter_params = {
            "fromBlock": 0,
            "address": UNKNOWN_ADDRESS,
        }
        result = w3.eth.get_logs(filter_params)
        assert len(result) == 0

        # Test with multiple `address`

        # filter with other address
        filter_params = {
            "fromBlock": 0,
            "address": [UNKNOWN_ADDRESS, UNKNOWN_ADDRESS],
        }
        result = w3.eth.get_logs(filter_params)
        assert len(result) == 0

    def test_eth_call_old_contract_state(
        self, eth_tester, w3, math_contract, keyfile_account_address
    ):
        super().test_eth_call_old_contract_state(
            w3, math_contract, keyfile_account_address
        )

    @disable_auto_mine
    def test_eth_wait_for_transaction_receipt_unmined(
        self, eth_tester, w3, keyfile_account_address_dual_type
    ):
        super().test_eth_wait_for_transaction_receipt_unmined(
            w3, keyfile_account_address_dual_type
        )

    def test_eth_call_revert_with_msg(
        self, w3, revert_contract, keyfile_account_address
    ):
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="revertWithMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        with pytest.raises(
            TransactionFailed, match="execution reverted: Function has been reverted"
        ):
            w3.eth.call(txn_params)

    def test_eth_call_revert_without_msg(
        self, w3, revert_contract, keyfile_account_address
    ):
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="revertWithoutMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        with pytest.raises(TransactionFailed, match="execution reverted"):
            w3.eth.call(txn_params)

    def test_eth_estimate_gas_revert_with_msg(
        self, w3, revert_contract, keyfile_account_address
    ):
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="revertWithMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        with pytest.raises(
            TransactionFailed, match="execution reverted: Function has been reverted"
        ):
            w3.eth.estimate_gas(txn_params)

    def test_eth_estimate_gas_revert_without_msg(
        self, w3, revert_contract, keyfile_account_address
    ):
        with pytest.raises(TransactionFailed, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                abi_element_identifier="revertWithoutMessage",
                transaction={
                    "from": keyfile_account_address,
                    "to": revert_contract.address,
                },
            )
            w3.eth.estimate_gas(txn_params)

    def test_eth_call_custom_error_revert_with_msg(
        self,
        w3,
        revert_contract,
        keyfile_account_address,
    ) -> None:
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="customErrorWithMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        # test that the error message matches the custom error text from the contract
        with pytest.raises(TransactionFailed, match="You are not authorized"):
            w3.eth.call(txn_params)

    def test_eth_call_custom_error_revert_without_msg(
        self, w3, revert_contract, keyfile_account_address
    ):
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="customErrorWithoutMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        with pytest.raises(TransactionFailed, match="execution reverted"):
            w3.eth.call(txn_params)

    def test_eth_estimate_gas_custom_error_revert_with_msg(
        self,
        w3,
        revert_contract,
        keyfile_account_address,
    ) -> None:
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="customErrorWithMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        # test that the error message matches the custom error text from the contract
        with pytest.raises(TransactionFailed, match="You are not authorized"):
            w3.eth.estimate_gas(txn_params)

    def test_eth_estimate_gas_custom_error_revert_without_msg(
        self,
        w3,
        revert_contract,
        keyfile_account_address,
    ) -> None:
        txn_params = revert_contract._prepare_transaction(
            abi_element_identifier="customErrorWithoutMessage",
            transaction={
                "from": keyfile_account_address,
                "to": revert_contract.address,
            },
        )
        with pytest.raises(TransactionFailed, match="execution reverted"):
            w3.eth.estimate_gas(txn_params)

    @disable_auto_mine
    def test_eth_send_transaction(self, eth_tester, w3, keyfile_account_address):
        super().test_eth_send_transaction(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_send_transaction_legacy(self, eth_tester, w3, keyfile_account_address):
        super().test_eth_send_transaction_legacy(w3, keyfile_account_address)

    def test_eth_send_raw_transaction(self, eth_tester, w3, keyfile_account_pkey):
        super().test_eth_send_raw_transaction(w3, keyfile_account_pkey)

    @disable_auto_mine
    @pytest.mark.parametrize(
        "max_fee", (1000000000, None), ids=["with_max_fee", "without_max_fee"]
    )
    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
        self,
        eth_tester,
        w3,
        keyfile_account_address,
        max_fee,
    ):
        super().test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
            w3, keyfile_account_address, max_fee
        )

    @disable_auto_mine
    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
            w3,
            keyfile_account_address,
        )

    @disable_auto_mine
    def test_eth_send_transaction_default_fees(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_send_transaction_default_fees(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_send_transaction_hex_fees(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_send_transaction_hex_fees(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_send_transaction_no_gas(self, eth_tester, w3, keyfile_account_address):
        super().test_eth_send_transaction_no_gas(w3, keyfile_account_address)

    @disable_auto_mine
    def test_eth_send_transaction_no_max_fee(
        self, eth_tester, w3, keyfile_account_address
    ):
        super().test_eth_send_transaction_no_max_fee(w3, keyfile_account_address)

    def test_eth_fee_history_with_integer(
        self, w3: "Web3", empty_block: BlockData
    ) -> None:
        super().test_eth_fee_history_with_integer(w3, empty_block)

    def test_eth_get_balance_with_block_identifier(self, w3: "Web3") -> None:
        w3.testing.mine()
        miner_address = w3.eth.get_block(1)["miner"]
        genesis_balance = w3.eth.get_balance(miner_address, 0)
        later_balance = w3.eth.get_balance(miner_address, 1)

        assert is_integer(genesis_balance)
        assert is_integer(later_balance)
        assert later_balance > genesis_balance


class EthereumTesterNetModule(NetModuleTest):
    pass
