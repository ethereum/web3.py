# -*- coding: utf-8 -*-

import json
import math
import pytest
import time
from typing import (
    TYPE_CHECKING,
    Callable,
    Sequence,
    Union,
    cast,
)

from eth_typing import (
    BlockNumber,
    ChecksumAddress,
    HexAddress,
    HexStr,
)
from eth_utils import (
    is_boolean,
    is_bytes,
    is_checksum_address,
    is_dict,
    is_integer,
    is_list_like,
    is_same_address,
    is_string,
)
from eth_utils.toolz import (
    assoc,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.ens import (
    ens_addresses,
)
from web3._utils.method_formatters import (
    to_hex_if_integer,
)
from web3.exceptions import (
    BlockNotFound,
    ContractLogicError,
    InvalidAddress,
    InvalidTransaction,
    NameNotFound,
    TransactionNotFound,
    TransactionTypeMismatch,
)
from web3.types import (  # noqa: F401
    BlockData,
    FilterParams,
    LogReceipt,
    Nonce,
    SyncStatus,
    TxParams,
    Wei,
)

UNKNOWN_ADDRESS = ChecksumAddress(HexAddress(HexStr('0xdEADBEeF00000000000000000000000000000000')))
UNKNOWN_HASH = HexStr('0xdeadbeef00000000000000000000000000000000000000000000000000000000')

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.contract import Contract  # noqa: F401


def mine_pending_block(web3: "Web3") -> None:
    timeout = 10

    web3.geth.miner.start()  # type: ignore
    start = time.time()
    while time.time() < start + timeout:
        if len(web3.eth.get_block('pending')['transactions']) == 0:
            break
    web3.geth.miner.stop()  # type: ignore


class AsyncEthModuleTest:
    @pytest.mark.asyncio
    async def test_eth_gas_price(self, async_w3: "Web3") -> None:
        gas_price = await async_w3.eth.gas_price  # type: ignore
        assert gas_price > 0

    @pytest.mark.asyncio
    async def test_isConnected(self, async_w3: "Web3") -> None:
        is_connected = await async_w3.isConnected()  # type: ignore
        assert is_connected is True

    @pytest.mark.asyncio
    async def test_eth_send_transaction_legacy(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': await async_w3.eth.gas_price,  # type: ignore
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['gasPrice'] == txn_params['gasPrice']

    @pytest.mark.asyncio
    async def test_eth_send_transaction(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': async_w3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': async_w3.toWei(1, 'gwei'),
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == txn_params['maxFeePerGas']
        assert txn['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
        assert txn['gasPrice'] == txn_params['maxFeePerGas']

    @pytest.mark.asyncio
    async def test_eth_send_transaction_default_fees(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxPriorityFeePerGas'] == 1 * 10**9
        assert txn['maxFeePerGas'] >= 1 * 10**9
        assert txn['gasPrice'] == txn['maxFeePerGas']

    @pytest.mark.asyncio
    async def test_eth_send_transaction_hex_fees(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': hex(250 * 10**9),
            'maxPriorityFeePerGas': hex(2 * 10**9),
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == 250 * 10**9
        assert txn['maxPriorityFeePerGas'] == 2 * 10**9

    @pytest.mark.asyncio
    async def test_eth_send_transaction_no_gas(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'maxFeePerGas': Wei(250 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 121000  # 21000 + buffer

    @pytest.mark.asyncio
    async def test_eth_send_transaction_with_gas_price(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(1),
            'maxFeePerGas': Wei(250 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        with pytest.raises(TransactionTypeMismatch):
            await async_w3.eth.send_transaction(txn_params)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_send_transaction_no_priority_fee(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(250 * 10**9),
        }
        with pytest.raises(InvalidTransaction, match='maxPriorityFeePerGas must be defined'):
            await async_w3.eth.send_transaction(txn_params)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_send_transaction_no_max_fee(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        maxPriorityFeePerGas = async_w3.toWei(2, 'gwei')
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxPriorityFeePerGas': maxPriorityFeePerGas,
        }
        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000

        block = await async_w3.eth.get_block('latest')  # type: ignore
        assert txn['maxFeePerGas'] == maxPriorityFeePerGas + 2 * block['baseFeePerGas']

    @pytest.mark.asyncio
    async def test_eth_send_transaction_max_fee_less_than_tip(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(1 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        with pytest.raises(
            InvalidTransaction, match="maxFeePerGas must be >= maxPriorityFeePerGas"
        ):
            await async_w3.eth.send_transaction(txn_params)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_send_raw_transaction(self, async_w3: "Web3") -> None:
        # private key 0x3c2ab4e8f17a7dea191b8c991522660126d681039509dc3bb31af7c9bdb63518
        # This is an unfunded account, but the transaction has a 0 gas price, so is valid.
        # It never needs to be mined, we just want the transaction hash back to confirm.
        # tx = {'to': '0x0000000000000000000000000000000000000000', 'value': 0,  'nonce': 1, 'gas': 21000, 'gasPrice': 0, 'chainId': 131277322940537}  # noqa: E501
        # NOTE: nonce=1 to make txn unique from the non-async version of this test
        raw_txn = HexBytes('0xf8650180825208940000000000000000000000000000000000000000808086eecac466e115a0ffdd42d7dee4ac85427468bc616812e49432e285e4e8f5cd9381163ac3b28108a04ec6b0d89ecbd5e89b0399f336ad50f283fafd70e86593250bf5a2adfb93d17e')  # noqa: E501
        expected_hash = HexStr('0x52b0ff9cb472f25872fa8ec6a62fa59454fc2ae7901cfcc6cc89d096f49b8fc1')
        txn_hash = await async_w3.eth.send_raw_transaction(raw_txn)  # type: ignore
        assert txn_hash == async_w3.toBytes(hexstr=expected_hash)

    @pytest.mark.asyncio
    async def test_gas_price_strategy_middleware(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
        }
        two_gwei_in_wei = async_w3.toWei(2, 'gwei')

        def gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return two_gwei_in_wei

        async_w3.eth.set_gas_price_strategy(gas_price_strategy)

        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        assert txn['gasPrice'] == two_gwei_in_wei
        async_w3.eth.set_gas_price_strategy(None)  # reset strategy

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "max_fee",
        (1000000000, None),
        ids=["with_max_fee", "without_max_fee"]
    )
    async def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress, max_fee: Wei,
    ) -> None:
        max_priority_fee = async_w3.toWei(1, 'gwei')
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxPriorityFeePerGas': max_priority_fee,
        }
        if max_fee is not None:
            txn_params = assoc(txn_params, "maxFeePerGas", max_fee)

        def gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return async_w3.toWei(2, 'gwei')
        async_w3.eth.set_gas_price_strategy(gas_price_strategy)

        txn_hash = await async_w3.eth.send_transaction(txn_params)  # type: ignore
        txn = await async_w3.eth.get_transaction(txn_hash)  # type: ignore

        latest_block = await async_w3.eth.get_block('latest')  # type: ignore
        assert txn['maxFeePerGas'] == max_fee if max_fee is not None \
            else 2 * latest_block['baseFeePerGas'] + max_priority_fee
        assert txn['maxPriorityFeePerGas'] == max_priority_fee
        assert txn['gasPrice'] == txn['maxFeePerGas']

        async_w3.eth.set_gas_price_strategy(None)  # reset strategy

    @pytest.mark.asyncio
    async def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress,
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(1000000000),
        }

        def gas_price_strategy(_web3: "Web3", _txn: TxParams) -> Wei:
            return async_w3.toWei(2, 'gwei')
        async_w3.eth.set_gas_price_strategy(gas_price_strategy)

        with pytest.raises(InvalidTransaction, match="maxPriorityFeePerGas must be defined"):
            await async_w3.eth.send_transaction(txn_params)  # type: ignore

        async_w3.eth.set_gas_price_strategy(None)  # reset strategy

    @pytest.mark.asyncio
    async def test_eth_estimate_gas(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        gas_estimate = await async_w3.eth.estimate_gas({  # type: ignore
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
        })
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    @pytest.mark.asyncio
    async def test_eth_fee_history(self, async_w3: "Web3") -> None:
        fee_history = await async_w3.eth.fee_history(1, 'latest', [50])  # type: ignore
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0
        assert is_list_like(fee_history['reward'])
        assert is_list_like(fee_history['reward'][0])

    @pytest.mark.asyncio
    async def test_eth_fee_history_with_integer(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        fee_history = await async_w3.eth.fee_history(1, empty_block['number'], [50])  # type: ignore
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0
        assert is_list_like(fee_history['reward'])
        assert is_list_like(fee_history['reward'][0])

    @pytest.mark.asyncio
    async def test_eth_fee_history_no_reward_percentiles(self, async_w3: "Web3") -> None:
        fee_history = await async_w3.eth.fee_history(1, 'latest')  # type: ignore
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0

    @pytest.mark.asyncio
    async def test_eth_max_priority_fee(self, async_w3: "Web3") -> None:
        max_priority_fee = await async_w3.eth.max_priority_fee  # type: ignore
        assert is_integer(max_priority_fee)

    @pytest.mark.asyncio
    async def test_eth_getBlockByHash(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        block = await async_w3.eth.get_block(empty_block['hash'])  # type: ignore
        assert block['hash'] == empty_block['hash']

    @pytest.mark.asyncio
    async def test_eth_getBlockByHash_not_found(self, async_w3: "Web3") -> None:
        with pytest.raises(BlockNotFound):
            await async_w3.eth.get_block(UNKNOWN_HASH)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_getBlockByHash_pending(
        self, async_w3: "Web3"
    ) -> None:
        block = await async_w3.eth.get_block('pending')  # type: ignore
        assert block['hash'] is None

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_with_integer(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        block = await async_w3.eth.get_block(empty_block['number'])  # type: ignore
        assert block['number'] == empty_block['number']

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_latest(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = await async_w3.eth.block_number  # type: ignore
        block = await async_w3.eth.get_block('latest')  # type: ignore
        assert block['number'] == current_block_number

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_not_found(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.raises(BlockNotFound):
            await async_w3.eth.get_block(BlockNumber(12345))  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_pending(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = await async_w3.eth.block_number  # type: ignore
        block = await async_w3.eth.get_block('pending')  # type: ignore
        assert block['number'] == current_block_number + 1

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_earliest(
        self, async_w3: "Web3", empty_block: BlockData
    ) -> None:
        genesis_block = await async_w3.eth.get_block(BlockNumber(0))  # type: ignore
        block = await async_w3.eth.get_block('earliest')  # type: ignore
        assert block['number'] == 0
        assert block['hash'] == genesis_block['hash']

    @pytest.mark.asyncio
    async def test_eth_getBlockByNumber_full_transactions(
        self, async_w3: "Web3", block_with_txn: BlockData
    ) -> None:
        block = await async_w3.eth.get_block(block_with_txn['number'], True)  # type: ignore
        transaction = block['transactions'][0]
        assert transaction['hash'] == block_with_txn['transactions'][0]

    @pytest.mark.asyncio
    async def test_eth_get_raw_transaction(
        self, async_w3: "Web3", mined_txn_hash: HexStr
    ) -> None:
        raw_transaction = await async_w3.eth.get_raw_transaction(mined_txn_hash)  # type: ignore
        assert is_bytes(raw_transaction)

    @pytest.mark.asyncio
    async def test_eth_get_raw_transaction_raises_error(self, async_w3: "Web3") -> None:
        with pytest.raises(TransactionNotFound, match=f"Transaction with hash: '{UNKNOWN_HASH}'"):
            await async_w3.eth.get_raw_transaction(UNKNOWN_HASH)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_get_raw_transaction_by_block(
        self,
        async_w3: "Web3",
        block_with_txn: BlockData,
        unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        # eth_getRawTransactionByBlockNumberAndIndex: block identifier
        # send a txn to make sure pending block has at least one txn
        await async_w3.eth.send_transaction(  # type: ignore
            {
                'from': unlocked_account_dual_type,
                'to': unlocked_account_dual_type,
                'value': Wei(1),
            }
        )
        pending_block = await async_w3.eth.get_block('pending')  # type: ignore
        last_pending_txn_index = len(pending_block['transactions']) - 1
        raw_txn = await async_w3.eth.get_raw_transaction_by_block(  # type: ignore
            'pending', last_pending_txn_index
        )
        assert is_bytes(raw_txn)

        # eth_getRawTransactionByBlockNumberAndIndex: block number
        block_with_txn_number = block_with_txn['number']
        raw_transaction = await async_w3.eth.get_raw_transaction_by_block(  # type: ignore
            block_with_txn_number, 0
        )
        assert is_bytes(raw_transaction)

        # eth_getRawTransactionByBlockHashAndIndex: block hash
        block_with_txn_hash = block_with_txn['hash']
        raw_transaction = await async_w3.eth.get_raw_transaction_by_block(  # type: ignore
            block_with_txn_hash, 0
        )
        assert is_bytes(raw_transaction)

    @pytest.mark.asyncio
    @pytest.mark.parametrize('unknown_block_num_or_hash', (1234567899999, UNKNOWN_HASH))
    async def test_eth_get_raw_transaction_by_block_raises_error(
        self, async_w3: "Web3", unknown_block_num_or_hash: Union[int, HexBytes]
    ) -> None:
        with pytest.raises(TransactionNotFound, match=(
            f"Transaction index: 0 on block id: {to_hex_if_integer(unknown_block_num_or_hash)!r} "
            f"not found."
        )):
            await async_w3.eth.get_raw_transaction_by_block(    # type: ignore
                unknown_block_num_or_hash, 0
            )

    @pytest.mark.asyncio
    async def test_eth_get_raw_transaction_by_block_raises_error_block_identifier(
        self, async_w3: "Web3"
    ) -> None:
        unknown_identifier = "unknown"
        with pytest.raises(
            ValueError, match=(
                f"Value did not match any of the recognized block identifiers: {unknown_identifier}"
            )
        ):
            await async_w3.eth.get_raw_transaction_by_block(unknown_identifier, 0)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_get_balance(self, async_w3: "Web3") -> None:
        coinbase = await async_w3.eth.coinbase  # type: ignore

        with pytest.raises(InvalidAddress):
            await async_w3.eth.get_balance(  # type: ignore
                ChecksumAddress(HexAddress(HexStr(coinbase.lower())))
            )

        balance = await async_w3.eth.get_balance(coinbase)  # type: ignore

        assert is_integer(balance)
        assert balance >= 0

    @pytest.mark.asyncio
    async def test_eth_get_code(
        self, async_w3: "Web3", math_contract_address: ChecksumAddress
    ) -> None:
        code = await async_w3.eth.get_code(math_contract_address)  # type: ignore
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    @pytest.mark.asyncio
    async def test_eth_get_code_invalid_address(
        self, async_w3: "Web3", math_contract: "Contract"
    ) -> None:
        with pytest.raises(InvalidAddress):
            await async_w3.eth.get_code(  # type: ignore
                ChecksumAddress(HexAddress(HexStr(math_contract.address.lower())))
            )

    @pytest.mark.asyncio
    async def test_eth_get_code_with_block_identifier(
        self, async_w3: "Web3", emitter_contract: "Contract"
    ) -> None:
        block_id = await async_w3.eth.block_number  # type: ignore
        code = await async_w3.eth.get_code(emitter_contract.address, block_id)  # type: ignore
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    @pytest.mark.asyncio
    async def test_eth_get_transaction_count(
        self, async_w3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        transaction_count = await async_w3.eth.get_transaction_count(unlocked_account_dual_type)  # type: ignore # noqa E501
        assert is_integer(transaction_count)
        assert transaction_count >= 0

    @pytest.mark.asyncio
    async def test_eth_call(
        self, async_w3: "Web3", math_contract: "Contract"
    ) -> None:
        coinbase = await async_w3.eth.coinbase  # type: ignore
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(7, 11),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = await async_w3.eth.call(txn_params)  # type: ignore
        assert is_string(call_result)
        result = async_w3.codec.decode_single('uint256', call_result)
        assert result == 18

    @pytest.mark.asyncio
    async def test_eth_call_with_override(
        self, async_w3: "Web3", revert_contract: "Contract"
    ) -> None:
        coinbase = await async_w3.eth.coinbase  # type: ignore
        txn_params = revert_contract._prepare_transaction(
            fn_name='normalFunction',
            transaction={'from': coinbase, 'to': revert_contract.address},
        )
        call_result = await async_w3.eth.call(txn_params)  # type: ignore
        result = async_w3.codec.decode_single('bool', call_result)
        assert result is True

        # override runtime bytecode: `normalFunction` returns `false`
        override_code = '0x6080604052348015600f57600080fd5b5060043610603c5760003560e01c8063185c38a4146041578063c06a97cb146049578063d67e4b84146051575b600080fd5b60476071565b005b604f60df565b005b605760e4565b604051808215151515815260200191505060405180910390f35b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601b8152602001807f46756e6374696f6e20686173206265656e2072657665727465642e000000000081525060200191505060405180910390fd5b600080fd5b60008090509056fea2646970667358221220bb71e9e9a2e271cd0fbe833524a3ea67df95f25ea13aef5b0a761fa52b538f1064736f6c63430006010033'  # noqa: E501
        call_result = await async_w3.eth.call(  # type: ignore
            txn_params,
            'latest',
            {revert_contract.address: {'code': override_code}}
        )
        result = async_w3.codec.decode_single('bool', call_result)
        assert result is False

    @pytest.mark.asyncio
    async def test_eth_call_with_0_result(
        self, async_w3: "Web3", math_contract: "Contract"
    ) -> None:
        coinbase = await async_w3.eth.coinbase  # type: ignore
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(0, 0),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = await async_w3.eth.call(txn_params)  # type: ignore
        assert is_string(call_result)
        result = async_w3.codec.decode_single('uint256', call_result)
        assert result == 0

    @pytest.mark.asyncio
    async def test_eth_call_revert_with_msg(
        self,
        async_w3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError,
                           match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            await async_w3.eth.call(txn_params)  # type: ignore

    @pytest.mark.asyncio
    async def test_eth_call_revert_without_msg(
        self,
        async_w3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithoutMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            await async_w3.eth.call(txn_params)  # type: ignore


class EthModuleTest:
    def test_eth_protocol_version(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning,
                          match="This method has been deprecated in some clients"):
            protocol_version = web3.eth.protocol_version

        assert is_string(protocol_version)
        assert protocol_version.isdigit()

    def test_eth_protocolVersion(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            protocol_version = web3.eth.protocolVersion

        assert is_string(protocol_version)
        assert protocol_version.isdigit()

    def test_eth_syncing(self, web3: "Web3") -> None:
        syncing = web3.eth.syncing

        assert is_boolean(syncing) or is_dict(syncing)

        if is_boolean(syncing):
            assert syncing is False
        elif is_dict(syncing):
            sync_dict = cast(SyncStatus, syncing)
            assert 'startingBlock' in sync_dict
            assert 'currentBlock' in sync_dict
            assert 'highestBlock' in sync_dict

            assert is_integer(sync_dict['startingBlock'])
            assert is_integer(sync_dict['currentBlock'])
            assert is_integer(sync_dict['highestBlock'])

    def test_eth_coinbase(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase
        assert is_checksum_address(coinbase)

    def test_eth_mining(self, web3: "Web3") -> None:
        mining = web3.eth.mining
        assert is_boolean(mining)

    def test_eth_hashrate(self, web3: "Web3") -> None:
        hashrate = web3.eth.hashrate
        assert is_integer(hashrate)
        assert hashrate >= 0

    def test_eth_chain_id(self, web3: "Web3") -> None:
        chain_id = web3.eth.chain_id
        # chain id value from geth fixture genesis file
        assert chain_id == 131277322940537

    def test_eth_chainId(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            chain_id = web3.eth.chainId
        # chain id value from geth fixture genesis file
        assert chain_id == 131277322940537

    def test_eth_fee_history(self, web3: "Web3") -> None:
        fee_history = web3.eth.fee_history(1, 'latest', [50])
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0
        assert is_list_like(fee_history['reward'])
        assert is_list_like(fee_history['reward'][0])

    def test_eth_fee_history_with_integer(self,
                                          web3: "Web3",
                                          empty_block: BlockData) -> None:
        fee_history = web3.eth.fee_history(1, empty_block['number'], [50])
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0
        assert is_list_like(fee_history['reward'])
        assert is_list_like(fee_history['reward'][0])

    def test_eth_fee_history_no_reward_percentiles(self, web3: "Web3") -> None:
        fee_history = web3.eth.fee_history(1, 'latest')
        assert is_list_like(fee_history['baseFeePerGas'])
        assert is_list_like(fee_history['gasUsedRatio'])
        assert is_integer(fee_history['oldestBlock'])
        assert fee_history['oldestBlock'] >= 0

    def test_eth_gas_price(self, web3: "Web3") -> None:
        gas_price = web3.eth.gas_price
        assert is_integer(gas_price)
        assert gas_price > 0

    def test_eth_gasPrice_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            gas_price = web3.eth.gasPrice
        assert is_integer(gas_price)
        assert gas_price > 0

    def test_eth_max_priority_fee(self, web3: "Web3") -> None:
        max_priority_fee = web3.eth.max_priority_fee
        assert is_integer(max_priority_fee)

    def test_eth_accounts(self, web3: "Web3") -> None:
        accounts = web3.eth.accounts
        assert is_list_like(accounts)
        assert len(accounts) != 0
        assert all((
            is_checksum_address(account)
            for account
            in accounts
        ))
        assert web3.eth.coinbase in accounts

    def test_eth_block_number(self, web3: "Web3") -> None:
        block_number = web3.eth.block_number
        assert is_integer(block_number)
        assert block_number >= 0

    def test_eth_get_block_number(self, web3: "Web3") -> None:
        block_number = web3.eth.get_block_number()
        assert is_integer(block_number)
        assert block_number >= 0

    def test_eth_blockNumber(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            block_number = web3.eth.blockNumber

        assert is_integer(block_number)
        assert block_number >= 0

    def test_eth_get_balance(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase

        with pytest.raises(InvalidAddress):
            web3.eth.get_balance(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))))

        balance = web3.eth.get_balance(coinbase)

        assert is_integer(balance)
        assert balance >= 0

    def test_eth_getBalance_deprecated(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase

        with pytest.warns(DeprecationWarning,
                          match='getBalance is deprecated in favor of get_balance'):
            balance = web3.eth.getBalance(coinbase)

        assert is_integer(balance)
        assert balance >= 0

    def test_eth_get_balance_with_block_identifier(self, web3: "Web3") -> None:
        miner_address = web3.eth.get_block(1)['miner']
        genesis_balance = web3.eth.get_balance(miner_address, 0)
        later_balance = web3.eth.get_balance(miner_address, 1)

        assert is_integer(genesis_balance)
        assert is_integer(later_balance)
        assert later_balance > genesis_balance

    @pytest.mark.parametrize('address, expect_success', [
        ('test-address.eth', True),
        ('not-an-address.eth', False)
    ])
    def test_eth_get_balance_with_ens_name(
        self, web3: "Web3", address: ChecksumAddress, expect_success: bool
    ) -> None:
        with ens_addresses(web3, {'test-address.eth': web3.eth.accounts[0]}):
            if expect_success:
                balance = web3.eth.get_balance(address)
                assert is_integer(balance)
                assert balance >= 0
            else:
                with pytest.raises(NameNotFound):
                    web3.eth.get_balance(address)

    def test_eth_get_storage_at(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        storage = web3.eth.get_storage_at(emitter_contract_address, 0)
        assert isinstance(storage, HexBytes)

    def test_eth_getStorageAt_deprecated(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        with pytest.warns(DeprecationWarning):
            storage = web3.eth.getStorageAt(emitter_contract_address, 0)
        assert isinstance(storage, HexBytes)

    def test_eth_get_storage_at_ens_name(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'emitter.eth': emitter_contract_address}):
            storage = web3.eth.get_storage_at('emitter.eth', 0)
            assert isinstance(storage, HexBytes)

    def test_eth_get_storage_at_invalid_address(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase
        with pytest.raises(InvalidAddress):
            web3.eth.get_storage_at(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))), 0)

    def test_eth_get_transaction_count(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        transaction_count = web3.eth.get_transaction_count(unlocked_account_dual_type)
        assert is_integer(transaction_count)
        assert transaction_count >= 0

    def test_eth_getTransactionCount_deprecated(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        with pytest.warns(DeprecationWarning):
            transaction_count = web3.eth.getTransactionCount(unlocked_account_dual_type)
        assert is_integer(transaction_count)
        assert transaction_count >= 0

    def test_eth_get_transaction_count_ens_name(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'unlocked-acct-dual-type.eth': unlocked_account_dual_type}):
            transaction_count = web3.eth.get_transaction_count('unlocked-acct-dual-type.eth')
            assert is_integer(transaction_count)
            assert transaction_count >= 0

    def test_eth_get_transaction_count_invalid_address(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase
        with pytest.raises(InvalidAddress):
            web3.eth.get_transaction_count(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))))

    def test_eth_getBlockTransactionCountByHash_empty_block(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        transaction_count = web3.eth.get_block_transaction_count(empty_block['hash'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByNumber_empty_block(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        transaction_count = web3.eth.get_block_transaction_count(empty_block['number'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByHash_block_with_txn(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        transaction_count = web3.eth.get_block_transaction_count(block_with_txn['hash'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getBlockTransactionCountByNumber_block_with_txn(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        transaction_count = web3.eth.get_block_transaction_count(block_with_txn['number'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getBlockTransactionCountByHash_block_with_txn_deprecated(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        with pytest.warns(
            DeprecationWarning,
            match="getBlockTransactionCount is deprecated in favor of get_block_transaction_count"
        ):
            transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['hash'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getBlockTransactionCountByNumber_block_with_txn_deprecated(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        with pytest.warns(
            DeprecationWarning,
            match="getBlockTransactionCount is deprecated in favor of get_block_transaction_count"
        ):
            transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['number'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getUncleCountByBlockHash(self, web3: "Web3", empty_block: BlockData) -> None:
        uncle_count = web3.eth.get_uncle_count(empty_block['hash'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getUncleCountByBlockHash_deprecated(self,
                                                     web3: "Web3",
                                                     empty_block: BlockData) -> None:
        with pytest.warns(DeprecationWarning,
                          match='getUncleCount is deprecated in favor of get_uncle_count'):
            uncle_count = web3.eth.getUncleCount(empty_block['hash'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getUncleCountByBlockNumber(self, web3: "Web3", empty_block: BlockData) -> None:
        uncle_count = web3.eth.get_uncle_count(empty_block['number'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getUncleCountByBlockNumber_deprecated(self,
                                                       web3: "Web3",
                                                       empty_block: BlockData) -> None:
        with pytest.warns(DeprecationWarning,
                          match='getUncleCount is deprecated in favor of get_uncle_count'):
            uncle_count = web3.eth.getUncleCount(empty_block['number'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_get_code(self, web3: "Web3", math_contract_address: ChecksumAddress) -> None:
        code = web3.eth.get_code(math_contract_address)
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    def test_eth_getCode_deprecated(self,
                                    web3: "Web3",
                                    math_contract_address: ChecksumAddress) -> None:
        with pytest.warns(DeprecationWarning, match='getCode is deprecated in favor of get_code'):
            code = web3.eth.getCode(math_contract_address)
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    def test_eth_get_code_ens_address(
        self, web3: "Web3", math_contract_address: ChecksumAddress
    ) -> None:
        with ens_addresses(
            web3, {'mathcontract.eth': math_contract_address}
        ):
            code = web3.eth.get_code('mathcontract.eth')
            assert isinstance(code, HexBytes)
            assert len(code) > 0

    def test_eth_get_code_invalid_address(self, web3: "Web3", math_contract: "Contract") -> None:
        with pytest.raises(InvalidAddress):
            web3.eth.get_code(ChecksumAddress(HexAddress(HexStr(math_contract.address.lower()))))

    def test_eth_get_code_with_block_identifier(
        self, web3: "Web3", emitter_contract: "Contract"
    ) -> None:
        code = web3.eth.get_code(emitter_contract.address, block_identifier=web3.eth.block_number)
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    def test_eth_sign(self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress) -> None:
        signature = web3.eth.sign(
            unlocked_account_dual_type, text='Message tö sign. Longer than hash!'
        )
        assert is_bytes(signature)
        assert len(signature) == 32 + 32 + 1

        # test other formats
        hexsign = web3.eth.sign(
            unlocked_account_dual_type,
            hexstr=HexStr(
                '0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821'
            )
        )
        assert hexsign == signature

        intsign = web3.eth.sign(
            unlocked_account_dual_type,
            0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821
        )
        assert intsign == signature

        bytessign = web3.eth.sign(
            unlocked_account_dual_type, b'Message t\xc3\xb6 sign. Longer than hash!'
        )
        assert bytessign == signature

        new_signature = web3.eth.sign(
            unlocked_account_dual_type, text='different message is different'
        )
        assert new_signature != signature

    def test_eth_sign_ens_names(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'unlocked-acct.eth': unlocked_account_dual_type}):
            signature = web3.eth.sign(
                'unlocked-acct.eth', text='Message tö sign. Longer than hash!'
            )
            assert is_bytes(signature)
            assert len(signature) == 32 + 32 + 1

    def test_eth_sign_typed_data(
        self,
        web3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        skip_if_testrpc: Callable[["Web3"], None],
    ) -> None:
        validJSONMessage = '''
            {
                "types": {
                    "EIP712Domain": [
                        {"name": "name", "type": "string"},
                        {"name": "version", "type": "string"},
                        {"name": "chainId", "type": "uint256"},
                        {"name": "verifyingContract", "type": "address"}
                    ],
                    "Person": [
                        {"name": "name", "type": "string"},
                        {"name": "wallet", "type": "address"}
                    ],
                    "Mail": [
                        {"name": "from", "type": "Person"},
                        {"name": "to", "type": "Person"},
                        {"name": "contents", "type": "string"}
                    ]
                },
                "primaryType": "Mail",
                "domain": {
                    "name": "Ether Mail",
                    "version": "1",
                    "chainId": "0x01",
                    "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"
                },
                "message": {
                    "from": {
                        "name": "Cow",
                        "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"
                    },
                    "to": {
                        "name": "Bob",
                        "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"
                    },
                    "contents": "Hello, Bob!"
                }
            }
        '''
        skip_if_testrpc(web3)
        signature = HexBytes(web3.eth.sign_typed_data(
            unlocked_account_dual_type,
            json.loads(validJSONMessage)
        ))
        assert len(signature) == 32 + 32 + 1

    def test_eth_signTypedData_deprecated(
        self,
        web3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        skip_if_testrpc: Callable[["Web3"], None],
    ) -> None:
        validJSONMessage = '''
            {
                "types": {
                    "EIP712Domain": [
                        {"name": "name", "type": "string"},
                        {"name": "version", "type": "string"},
                        {"name": "chainId", "type": "uint256"},
                        {"name": "verifyingContract", "type": "address"}
                    ],
                    "Person": [
                        {"name": "name", "type": "string"},
                        {"name": "wallet", "type": "address"}
                    ],
                    "Mail": [
                        {"name": "from", "type": "Person"},
                        {"name": "to", "type": "Person"},
                        {"name": "contents", "type": "string"}
                    ]
                },
                "primaryType": "Mail",
                "domain": {
                    "name": "Ether Mail",
                    "version": "1",
                    "chainId": "0x01",
                    "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"
                },
                "message": {
                    "from": {
                        "name": "Cow",
                        "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"
                    },
                    "to": {
                        "name": "Bob",
                        "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"
                    },
                    "contents": "Hello, Bob!"
                }
            }
        '''
        skip_if_testrpc(web3)
        signature = HexBytes(web3.eth.signTypedData(
            unlocked_account_dual_type,
            json.loads(validJSONMessage)
        ))
        assert len(signature) == 32 + 32 + 1

    def test_invalid_eth_sign_typed_data(
        self,
        web3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        skip_if_testrpc: Callable[["Web3"], None]
    ) -> None:
        skip_if_testrpc(web3)
        invalid_typed_message = '''
            {
                "types": {
                    "EIP712Domain": [
                        {"name": "name", "type": "string"},
                        {"name": "version", "type": "string"},
                        {"name": "chainId", "type": "uint256"},
                        {"name": "verifyingContract", "type": "address"}
                    ],
                    "Person": [
                        {"name": "name", "type": "string"},
                        {"name": "wallet", "type": "address"}
                    ],
                    "Mail": [
                        {"name": "from", "type": "Person"},
                        {"name": "to", "type": "Person[2]"},
                        {"name": "contents", "type": "string"}
                    ]
                },
                "primaryType": "Mail",
                "domain": {
                    "name": "Ether Mail",
                    "version": "1",
                    "chainId": "0x01",
                    "verifyingContract": "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC"
                },
                "message": {
                    "from": {
                        "name": "Cow",
                        "wallet": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826"
                    },
                    "to": [{
                        "name": "Bob",
                        "wallet": "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB"
                    }],
                    "contents": "Hello, Bob!"
                }
            }
        '''
        with pytest.raises(ValueError,
                           match=r".*Expected 2 items for array type Person\[2\], got 1 items.*"):
            web3.eth.sign_typed_data(
                unlocked_account_dual_type,
                json.loads(invalid_typed_message)
            )

    def test_eth_sign_transaction_legacy(
        self,
        web3: "Web3",
        unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gas_price,
            'nonce': Nonce(0),
        }
        result = web3.eth.sign_transaction(txn_params)
        signatory_account = web3.eth.account.recover_transaction(result['raw'])
        assert unlocked_account == signatory_account
        assert result['tx']['to'] == txn_params['to']
        assert result['tx']['value'] == txn_params['value']
        assert result['tx']['gas'] == txn_params['gas']
        assert result['tx']['gasPrice'] == txn_params['gasPrice']
        assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_sign_transaction(
        self,
        web3: "Web3",
        unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(2, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
            'nonce': Nonce(0),
        }
        result = web3.eth.sign_transaction(txn_params)
        signatory_account = web3.eth.account.recover_transaction(result['raw'])
        assert unlocked_account == signatory_account
        assert result['tx']['to'] == txn_params['to']
        assert result['tx']['value'] == txn_params['value']
        assert result['tx']['gas'] == txn_params['gas']
        assert result['tx']['maxFeePerGas'] == txn_params['maxFeePerGas']
        assert result['tx']['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
        assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_sign_transaction_hex_fees(
        self,
        web3: "Web3",
        unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': hex(web3.toWei(2, 'gwei')),
            'maxPriorityFeePerGas': hex(web3.toWei(1, 'gwei')),
            'nonce': Nonce(0),
        }
        result = web3.eth.sign_transaction(txn_params)
        signatory_account = web3.eth.account.recover_transaction(result['raw'])
        assert unlocked_account == signatory_account
        assert result['tx']['to'] == txn_params['to']
        assert result['tx']['value'] == txn_params['value']
        assert result['tx']['gas'] == txn_params['gas']
        assert result['tx']['maxFeePerGas'] == int(str(txn_params['maxFeePerGas']), 16)
        assert result['tx']['maxPriorityFeePerGas'] == int(
            str(txn_params['maxPriorityFeePerGas']), 16
        )
        assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_signTransaction_deprecated(self,
                                            web3: "Web3",
                                            unlocked_account: ChecksumAddress) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gas_price,
            'nonce': Nonce(0),
        }
        with pytest.warns(DeprecationWarning,
                          match='signTransaction is deprecated in favor of sign_transaction'):
            result = web3.eth.signTransaction(txn_params)
        signatory_account = web3.eth.account.recover_transaction(result['raw'])
        assert unlocked_account == signatory_account
        assert result['tx']['to'] == txn_params['to']
        assert result['tx']['value'] == txn_params['value']
        assert result['tx']['gas'] == txn_params['gas']
        assert result['tx']['gasPrice'] == txn_params['gasPrice']
        assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_sign_transaction_ens_names(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'unlocked-account.eth': unlocked_account}):
            txn_params: TxParams = {
                'from': 'unlocked-account.eth',
                'to': 'unlocked-account.eth',
                'value': Wei(1),
                'gas': Wei(21000),
                'maxFeePerGas': web3.toWei(2, 'gwei'),
                'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
                'nonce': Nonce(0),
            }
            result = web3.eth.sign_transaction(txn_params)
            signatory_account = web3.eth.account.recover_transaction(result['raw'])
            assert unlocked_account == signatory_account
            assert result['tx']['to'] == unlocked_account
            assert result['tx']['value'] == txn_params['value']
            assert result['tx']['gas'] == txn_params['gas']
            assert result['tx']['maxFeePerGas'] == txn_params['maxFeePerGas']
            assert result['tx']['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
            assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_send_transaction_addr_checksum_required(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        non_checksum_addr = unlocked_account.lower()
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(2, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }

        with pytest.raises(InvalidAddress):
            invalid_params = cast(TxParams, dict(txn_params, **{'from': non_checksum_addr}))
            web3.eth.send_transaction(invalid_params)

        with pytest.raises(InvalidAddress):
            invalid_params = cast(TxParams, dict(txn_params, **{'to': non_checksum_addr}))
            web3.eth.send_transaction(invalid_params)

    def test_eth_send_transaction_legacy(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(1, 'gwei'),  # post-london needs to be more than the base fee
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['gasPrice'] == txn_params['gasPrice']

    def test_eth_send_transaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == txn_params['maxFeePerGas']
        assert txn['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
        assert txn['gasPrice'] == txn_params['maxFeePerGas']

    def test_eth_sendTransaction_deprecated(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        with pytest.warns(DeprecationWarning,
                          match="sendTransaction is deprecated in favor of send_transaction"):
            txn_hash = web3.eth.sendTransaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == txn_params['maxFeePerGas']
        assert txn['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
        assert txn['gasPrice'] == txn_params['maxFeePerGas']

    def test_eth_send_transaction_with_nonce(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        mine_pending_block(web3)  # gives an accurate transaction count after mining

        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            # unique maxFeePerGas to ensure transaction hash different from other tests
            'maxFeePerGas': web3.toWei(4.321, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
            'nonce': web3.eth.get_transaction_count(unlocked_account),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == txn_params['maxFeePerGas']
        assert txn['maxPriorityFeePerGas'] == txn_params['maxPriorityFeePerGas']
        assert txn['nonce'] == txn_params['nonce']
        assert txn['gasPrice'] == txn_params['maxFeePerGas']

    def test_eth_send_transaction_default_fees(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxPriorityFeePerGas'] == 1 * 10**9
        assert txn['maxFeePerGas'] >= 1 * 10**9
        assert txn['gasPrice'] == txn['maxFeePerGas']

    def test_eth_send_transaction_hex_fees(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': hex(250 * 10**9),
            'maxPriorityFeePerGas': hex(2 * 10**9),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['maxFeePerGas'] == 250 * 10**9
        assert txn['maxPriorityFeePerGas'] == 2 * 10**9

    def test_eth_send_transaction_no_gas(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'maxFeePerGas': Wei(250 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 121000  # 21000 + buffer

    def test_eth_send_transaction_with_gas_price(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(1),
            'maxFeePerGas': Wei(250 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        with pytest.raises(TransactionTypeMismatch):
            web3.eth.send_transaction(txn_params)

    def test_eth_send_transaction_no_priority_fee(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(250 * 10**9),
        }
        with pytest.raises(InvalidTransaction, match='maxPriorityFeePerGas must be defined'):
            web3.eth.send_transaction(txn_params)

    def test_eth_send_transaction_no_max_fee(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        maxPriorityFeePerGas = web3.toWei(2, 'gwei')
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxPriorityFeePerGas': maxPriorityFeePerGas,
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000

        block = web3.eth.get_block('latest')
        assert txn['maxFeePerGas'] == maxPriorityFeePerGas + 2 * block['baseFeePerGas']

    def test_eth_send_transaction_max_fee_less_than_tip(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(1 * 10**9),
            'maxPriorityFeePerGas': Wei(2 * 10**9),
        }
        with pytest.raises(
            InvalidTransaction, match="maxFeePerGas must be >= maxPriorityFeePerGas"
        ):
            web3.eth.send_transaction(txn_params)

    @pytest.mark.parametrize(
        "max_fee",
        (1000000000, None),
        ids=["with_max_fee", "without_max_fee"]
    )
    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress, max_fee: Wei
    ) -> None:
        max_priority_fee = web3.toWei(1, 'gwei')
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxPriorityFeePerGas': max_priority_fee,
        }
        if max_fee is not None:
            txn_params = assoc(txn_params, "maxFeePerGas", max_fee)

        def gas_price_strategy(_web3: "Web3", _txn: TxParams) -> Wei:
            return web3.toWei(2, 'gwei')
        web3.eth.set_gas_price_strategy(gas_price_strategy)

        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        latest_block = web3.eth.get_block('latest')
        assert txn['maxFeePerGas'] == max_fee if max_fee is not None \
            else 2 * latest_block['baseFeePerGas'] + max_priority_fee
        assert txn['maxPriorityFeePerGas'] == max_priority_fee
        assert txn['gasPrice'] == txn['maxFeePerGas']

        web3.eth.set_gas_price_strategy(None)  # reset strategy

    def test_gas_price_from_strategy_bypassed_for_dynamic_fee_txn_no_tip(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress,
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': Wei(1000000000),
        }

        def gas_price_strategy(_web3: "Web3", _txn: TxParams) -> Wei:
            return web3.toWei(2, 'gwei')
        web3.eth.set_gas_price_strategy(gas_price_strategy)

        with pytest.raises(InvalidTransaction, match="maxPriorityFeePerGas must be defined"):
            web3.eth.send_transaction(txn_params)

        web3.eth.set_gas_price_strategy(None)  # reset strategy

    def test_eth_replace_transaction_legacy(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(1, 'gwei'),  # must be greater than base_fee post London
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        txn_params['gasPrice'] = web3.toWei(2, 'gwei')
        replace_txn_hash = web3.eth.replace_transaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)

        assert is_same_address(replace_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(replace_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert replace_txn['value'] == 1
        assert replace_txn['gas'] == 21000
        assert replace_txn['gasPrice'] == txn_params['gasPrice']

    def test_eth_replace_transaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        two_gwei_in_wei = web3.toWei(2, 'gwei')
        three_gwei_in_wei = web3.toWei(3, 'gwei')

        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': two_gwei_in_wei,
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        txn_params['maxFeePerGas'] = three_gwei_in_wei
        txn_params['maxPriorityFeePerGas'] = two_gwei_in_wei

        replace_txn_hash = web3.eth.replace_transaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)

        assert is_same_address(replace_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(replace_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert replace_txn['value'] == 1
        assert replace_txn['gas'] == 21000
        assert replace_txn['maxFeePerGas'] == three_gwei_in_wei
        assert replace_txn['maxPriorityFeePerGas'] == two_gwei_in_wei

    def test_eth_replace_transaction_underpriced(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(2, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        one_gwei_in_wei = web3.toWei(1, 'gwei')
        txn_params['maxFeePerGas'] = one_gwei_in_wei
        txn_params['maxPriorityFeePerGas'] = one_gwei_in_wei

        with pytest.raises(ValueError, match="replacement transaction underpriced"):
            web3.eth.replace_transaction(txn_hash, txn_params)

    def test_eth_replaceTransaction_deprecated(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        two_gwei_in_wei = web3.toWei(2, 'gwei')
        three_gwei_in_wei = web3.toWei(3, 'gwei')

        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': two_gwei_in_wei,
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        txn_params['maxFeePerGas'] = three_gwei_in_wei
        txn_params['maxPriorityFeePerGas'] = two_gwei_in_wei
        with pytest.warns(
            DeprecationWarning,
            match="replaceTransaction is deprecated in favor of replace_transaction"
        ):
            replace_txn_hash = web3.eth.replaceTransaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)

        assert is_same_address(replace_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(replace_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert replace_txn['value'] == 1
        assert replace_txn['gas'] == 21000
        assert replace_txn['maxFeePerGas'] == three_gwei_in_wei
        assert replace_txn['maxPriorityFeePerGas'] == two_gwei_in_wei

    def test_eth_replace_transaction_non_existing_transaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        with pytest.raises(TransactionNotFound):
            web3.eth.replace_transaction(
                HexStr('0x98e8cc09b311583c5079fa600f6c2a3bea8611af168c52e4b60b5b243a441997'),
                txn_params
            )

    def test_eth_replace_transaction_already_mined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(2, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        try:
            web3.geth.miner.start()  # type: ignore
            web3.eth.wait_for_transaction_receipt(txn_hash, timeout=10)
        finally:
            web3.geth.miner.stop()  # type: ignore

        txn_params['maxFeePerGas'] = web3.toWei(3, 'gwei')
        txn_params['maxPriorityFeePerGas'] = web3.toWei(2, 'gwei')
        with pytest.raises(ValueError, match="Supplied transaction with hash"):
            web3.eth.replace_transaction(txn_hash, txn_params)

    def test_eth_replace_transaction_incorrect_nonce(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(2, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        txn = web3.eth.get_transaction(txn_hash)

        txn_params['maxFeePerGas'] = web3.toWei(3, 'gwei')
        txn_params['maxPriorityFeePerGas'] = web3.toWei(2, 'gwei')
        txn_params['nonce'] = Nonce(txn['nonce'] + 1)
        with pytest.raises(ValueError):
            web3.eth.replace_transaction(txn_hash, txn_params)

    def test_eth_replace_transaction_gas_price_too_low(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(2, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        txn_params['gasPrice'] = web3.toWei(1, 'gwei')
        with pytest.raises(ValueError):
            web3.eth.replace_transaction(txn_hash, txn_params)

    def test_eth_replace_transaction_gas_price_defaulting_minimum(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        gas_price = web3.toWei(1, 'gwei')

        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': gas_price,
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replace_transaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)

        assert replace_txn['gasPrice'] == math.ceil(gas_price * 1.125)  # minimum gas price

    def test_eth_replace_transaction_gas_price_defaulting_strategy_higher(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        two_gwei_in_wei = web3.toWei(2, 'gwei')

        def higher_gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return two_gwei_in_wei

        web3.eth.set_gas_price_strategy(higher_gas_price_strategy)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replace_transaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)
        assert replace_txn['gasPrice'] == two_gwei_in_wei  # Strategy provides higher gas price
        web3.eth.set_gas_price_strategy(None)  # reset strategy

    def test_eth_replace_transaction_gas_price_defaulting_strategy_lower(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        gas_price = web3.toWei(2, 'gwei')

        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': gas_price,
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        def lower_gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return web3.toWei(1, 'gwei')

        web3.eth.set_gas_price_strategy(lower_gas_price_strategy)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replace_transaction(txn_hash, txn_params)
        replace_txn = web3.eth.get_transaction(replace_txn_hash)
        # Strategy provides lower gas price - minimum preferred
        assert replace_txn['gasPrice'] == math.ceil(gas_price * 1.125)
        web3.eth.set_gas_price_strategy(None)  # reset strategy

    def test_eth_modify_transaction_legacy(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(1, 'gwei'),  # must be greater than base_fee post London
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        modified_txn_hash = web3.eth.modify_transaction(
            txn_hash, gasPrice=(cast(int, txn_params['gasPrice']) * 2), value=2
        )
        modified_txn = web3.eth.get_transaction(modified_txn_hash)

        assert is_same_address(modified_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(modified_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert modified_txn['value'] == 2
        assert modified_txn['gas'] == 21000
        assert modified_txn['gasPrice'] == cast(int, txn_params['gasPrice']) * 2

    def test_eth_modify_transaction(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei'),
            'maxFeePerGas': web3.toWei(2, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)

        modified_txn_hash = web3.eth.modify_transaction(
            txn_hash,
            value=2,
            maxPriorityFeePerGas=(cast(Wei, txn_params['maxPriorityFeePerGas']) * 2),
            maxFeePerGas=(cast(Wei, txn_params['maxFeePerGas']) * 2),
        )
        modified_txn = web3.eth.get_transaction(modified_txn_hash)

        assert is_same_address(modified_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(modified_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert modified_txn['value'] == 2
        assert modified_txn['gas'] == 21000
        assert modified_txn['maxPriorityFeePerGas'] == cast(Wei, txn_params[
            'maxPriorityFeePerGas']) * 2
        assert modified_txn['maxFeePerGas'] == cast(Wei, txn_params['maxFeePerGas']) * 2

    def test_eth_modifyTransaction_deprecated(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.toWei(1, 'gwei'),
        }
        txn_hash = web3.eth.send_transaction(txn_params)
        with pytest.warns(
                DeprecationWarning,
                match="modifyTransaction is deprecated in favor of modify_transaction"):
            modified_txn_hash = web3.eth.modifyTransaction(
                txn_hash, gasPrice=(cast(int, txn_params['gasPrice']) * 2), value=2
            )
        modified_txn = web3.eth.get_transaction(modified_txn_hash)
        assert is_same_address(modified_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(modified_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert modified_txn['value'] == 2
        assert modified_txn['gas'] == 21000
        assert modified_txn['gasPrice'] == cast(int, txn_params['gasPrice']) * 2

    def test_eth_send_raw_transaction(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        signed_tx = web3.eth.account.sign_transaction(
            {
                'to': '0x0000000000000000000000000000000000000000',
                'value': 0,
                'nonce': web3.eth.get_transaction_count(unlocked_account),
                'gas': 21000,
                'maxFeePerGas': 1000000000,
                'maxPriorityFeePerGas': 1000000000,
                'chainId': 131277322940537
            },
            # unlocked_account private key:
            '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'
        )
        txn_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        assert txn_hash == signed_tx.hash

    def test_eth_call(
        self, web3: "Web3", math_contract: "Contract"
    ) -> None:
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(7, 11),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = web3.eth.call(txn_params)
        assert is_string(call_result)
        result = web3.codec.decode_single('uint256', call_result)
        assert result == 18

    def test_eth_call_with_override(
        self, web3: "Web3", revert_contract: "Contract"
    ) -> None:
        coinbase = web3.eth.coinbase
        txn_params = revert_contract._prepare_transaction(
            fn_name='normalFunction',
            transaction={'from': coinbase, 'to': revert_contract.address},
        )
        call_result = web3.eth.call(txn_params)
        result = web3.codec.decode_single('bool', call_result)
        assert result is True

        # override runtime bytecode: `normalFunction` returns `false`
        override_code = '0x6080604052348015600f57600080fd5b5060043610603c5760003560e01c8063185c38a4146041578063c06a97cb146049578063d67e4b84146051575b600080fd5b60476071565b005b604f60df565b005b605760e4565b604051808215151515815260200191505060405180910390f35b6040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601b8152602001807f46756e6374696f6e20686173206265656e2072657665727465642e000000000081525060200191505060405180910390fd5b600080fd5b60008090509056fea2646970667358221220bb71e9e9a2e271cd0fbe833524a3ea67df95f25ea13aef5b0a761fa52b538f1064736f6c63430006010033'  # noqa: E501
        call_result = web3.eth.call(
            txn_params,
            'latest',
            {revert_contract.address: {'code': override_code}}
        )
        result = web3.codec.decode_single('bool', call_result)
        assert result is False

    def test_eth_call_with_0_result(
        self, web3: "Web3", math_contract: "Contract"
    ) -> None:
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(0, 0),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = web3.eth.call(txn_params)
        assert is_string(call_result)
        result = web3.codec.decode_single('uint256', call_result)
        assert result == 0

    def test_eth_call_revert_with_msg(
        self,
        web3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError,
                           match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.call(txn_params)

    def test_eth_call_revert_without_msg(
        self,
        web3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithoutMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.call(txn_params)

    def test_eth_estimate_gas_revert_with_msg(
        self,
        web3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError,
                           match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.estimate_gas(txn_params)

    def test_eth_estimate_gas_revert_without_msg(
        self,
        web3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(ContractLogicError, match="execution reverted"):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithoutMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.estimate_gas(txn_params)

    def test_eth_estimate_gas(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        gas_estimate = web3.eth.estimate_gas({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
        })
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_estimateGas_deprecated(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        with pytest.warns(DeprecationWarning,
                          match="estimateGas is deprecated in favor of estimate_gas"):
            gas_estimate = web3.eth.estimateGas({
                'from': unlocked_account_dual_type,
                'to': unlocked_account_dual_type,
                'value': Wei(1),
            })
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_estimate_gas_with_block(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        gas_estimate = web3.eth.estimate_gas({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
        }, 'latest')
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_getBlock_deprecated(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.warns(DeprecationWarning, match="getBlock is deprecated in favor of get_block"):
            block = web3.eth.getBlock(empty_block['hash'])
        assert block['hash'] == empty_block['hash']

    def test_eth_getBlockByHash(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        block = web3.eth.get_block(empty_block['hash'])
        assert block['hash'] == empty_block['hash']

    def test_eth_getBlockByHash_not_found(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.raises(BlockNotFound):
            web3.eth.get_block(UNKNOWN_HASH)

    def test_eth_getBlockByHash_pending(
        self, web3: "Web3"
    ) -> None:
        block = web3.eth.get_block('pending')
        assert block['hash'] is None

    def test_eth_getBlockByNumber_with_integer(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        block = web3.eth.get_block(empty_block['number'])
        assert block['number'] == empty_block['number']

    def test_eth_getBlockByNumber_with_integer_deprecated(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.warns(DeprecationWarning, match="getBlock is deprecated in favor of get_block"):
            block = web3.eth.getBlock(empty_block['number'])
        assert block['number'] == empty_block['number']

    def test_eth_getBlockByNumber_latest(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = web3.eth.block_number
        block = web3.eth.get_block('latest')
        assert block['number'] == current_block_number

    def test_eth_getBlockByNumber_not_found(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.raises(BlockNotFound):
            web3.eth.get_block(BlockNumber(12345))

    def test_eth_getBlockByNumber_pending(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = web3.eth.block_number
        block = web3.eth.get_block('pending')
        assert block['number'] == current_block_number + 1

    def test_eth_getBlockByNumber_earliest(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        genesis_block = web3.eth.get_block(BlockNumber(0))
        block = web3.eth.get_block('earliest')
        assert block['number'] == 0
        assert block['hash'] == genesis_block['hash']

    def test_eth_getBlockByNumber_full_transactions(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        block = web3.eth.get_block(block_with_txn['number'], True)
        transaction = block['transactions'][0]
        assert transaction['hash'] == block_with_txn['transactions'][0]  # type: ignore

    def test_eth_getTransactionByHash(
        self, web3: "Web3", mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.get_transaction(mined_txn_hash)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByHash_deprecated(
        self, web3: "Web3", mined_txn_hash: HexStr
    ) -> None:
        with pytest.warns(DeprecationWarning,
                          match='getTransaction is deprecated in favor of get_transaction'):
            transaction = web3.eth.getTransaction(mined_txn_hash)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByHash_contract_creation(
        self, web3: "Web3", math_contract_deploy_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.get_transaction(math_contract_deploy_txn_hash)
        assert is_dict(transaction)
        assert transaction['to'] is None, "to field is %r" % transaction['to']

    def test_eth_getTransactionByBlockHashAndIndex(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.get_transaction_by_block(block_with_txn['hash'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByBlockHashAndIndex_deprecated(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        with pytest.warns(
            DeprecationWarning,
            match='getTransactionByBlock is deprecated in favor of get_transaction_by_block'
        ):
            transaction = web3.eth.getTransactionByBlock(block_with_txn['hash'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByBlockNumberAndIndex(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.get_transaction_by_block(block_with_txn['number'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByBlockNumberAndIndex_deprecated(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        with pytest.warns(
            DeprecationWarning,
            match='getTransactionByBlock is deprecated in favor of get_transaction_by_block'
        ):
            transaction = web3.eth.getTransactionByBlock(block_with_txn['number'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_get_transaction_receipt_mined(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        receipt = web3.eth.get_transaction_receipt(mined_txn_hash)
        assert is_dict(receipt)
        assert receipt['blockNumber'] == block_with_txn['number']
        assert receipt['blockHash'] == block_with_txn['hash']
        assert receipt['transactionIndex'] == 0
        assert receipt['transactionHash'] == HexBytes(mined_txn_hash)
        assert is_checksum_address(receipt['to'])
        assert receipt['from'] is not None
        assert is_checksum_address(receipt['from'])

        effective_gas_price = receipt['effectiveGasPrice']
        assert isinstance(effective_gas_price, int)
        assert effective_gas_price > 0

    def test_eth_getTransactionReceipt_mined_deprecated(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        with pytest.warns(
                DeprecationWarning,
                match="getTransactionReceipt is deprecated in favor of get_transaction_receipt"):
            receipt = web3.eth.getTransactionReceipt(mined_txn_hash)
        assert is_dict(receipt)
        assert receipt['blockNumber'] == block_with_txn['number']
        assert receipt['blockHash'] == block_with_txn['hash']
        assert receipt['transactionIndex'] == 0
        assert receipt['transactionHash'] == HexBytes(mined_txn_hash)
        assert is_checksum_address(receipt['to'])
        assert receipt['from'] is not None
        assert is_checksum_address(receipt['from'])

    def test_eth_get_transaction_receipt_unmined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_hash = web3.eth.send_transaction({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'maxFeePerGas': web3.toWei(3, 'gwei'),
            'maxPriorityFeePerGas': web3.toWei(1, 'gwei')
        })
        with pytest.raises(TransactionNotFound):
            web3.eth.get_transaction_receipt(txn_hash)

    def test_eth_get_transaction_receipt_with_log_entry(
        self,
        web3: "Web3",
        block_with_txn_with_log: BlockData,
        emitter_contract: "Contract",
        txn_hash_with_log: HexStr,
    ) -> None:
        receipt = web3.eth.get_transaction_receipt(txn_hash_with_log)
        assert is_dict(receipt)
        assert receipt['blockNumber'] == block_with_txn_with_log['number']
        assert receipt['blockHash'] == block_with_txn_with_log['hash']
        assert receipt['transactionIndex'] == 0
        assert receipt['transactionHash'] == HexBytes(txn_hash_with_log)

        assert len(receipt['logs']) == 1
        log_entry = receipt['logs'][0]

        assert log_entry['blockNumber'] == block_with_txn_with_log['number']
        assert log_entry['blockHash'] == block_with_txn_with_log['hash']
        assert log_entry['logIndex'] == 0
        assert is_same_address(log_entry['address'], emitter_contract.address)
        assert log_entry['transactionIndex'] == 0
        assert log_entry['transactionHash'] == HexBytes(txn_hash_with_log)

    def test_eth_getUncleByBlockHashAndIndex(self, web3: "Web3") -> None:
        # TODO: how do we make uncles....
        pass

    def test_eth_getUncleByBlockNumberAndIndex(self, web3: "Web3") -> None:
        # TODO: how do we make uncles....
        pass

    def test_eth_newFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter({})

        changes = web3.eth.get_filter_changes(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        logs = web3.eth.get_filter_logs(filter.filter_id)
        assert is_list_like(logs)
        assert not logs

        result = web3.eth.uninstall_filter(filter.filter_id)
        assert result is True

    def test_eth_newFilter_deprecated(self, web3: "Web3") -> None:
        filter = web3.eth.filter({})

        changes = web3.eth.get_filter_changes(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        with pytest.warns(DeprecationWarning,
                          match="getFilterLogs is deprecated in favor of get_filter_logs"):
            logs = web3.eth.getFilterLogs(filter.filter_id)
        assert is_list_like(logs)
        assert not logs

        result = web3.eth.uninstall_filter(filter.filter_id)
        assert result is True

    def test_eth_newBlockFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter('latest')
        assert is_string(filter.filter_id)

        changes = web3.eth.get_filter_changes(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        # TODO: figure out why this fails in go-ethereum
        # logs = web3.eth.get_filter_logs(filter.filter_id)
        # assert is_list_like(logs)
        # assert not logs

        result = web3.eth.uninstall_filter(filter.filter_id)
        assert result is True

    def test_eth_newPendingTransactionFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter('pending')
        assert is_string(filter.filter_id)

        changes = web3.eth.get_filter_changes(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        # TODO: figure out why this fails in go-ethereum
        # logs = web3.eth.get_filter_logs(filter.filter_id)
        # assert is_list_like(logs)
        # assert not logs

        result = web3.eth.uninstall_filter(filter.filter_id)
        assert result is True

    def test_eth_get_logs_without_logs(
        self, web3: "Web3", block_with_txn_with_log: BlockData
    ) -> None:
        # Test with block range

        filter_params: FilterParams = {
            "fromBlock": BlockNumber(0),
            "toBlock": BlockNumber(block_with_txn_with_log['number'] - 1),
        }
        result = web3.eth.get_logs(filter_params)
        assert len(result) == 0

        # the range is wrong
        filter_params = {
            "fromBlock": block_with_txn_with_log['number'],
            "toBlock": BlockNumber(block_with_txn_with_log['number'] - 1),
        }
        result = web3.eth.get_logs(filter_params)
        assert len(result) == 0

        # Test with `address`

        # filter with other address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": UNKNOWN_ADDRESS,
        }
        result = web3.eth.get_logs(filter_params)
        assert len(result) == 0

        # Test with multiple `address`

        # filter with other address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": [UNKNOWN_ADDRESS, UNKNOWN_ADDRESS],
        }
        result = web3.eth.get_logs(filter_params)
        assert len(result) == 0

    def test_eth_get_logs_with_logs(
        self,
        web3: "Web3",
        block_with_txn_with_log: BlockData,
        emitter_contract_address: ChecksumAddress,
        txn_hash_with_log: HexStr,
    ) -> None:
        def assert_contains_log(result: Sequence[LogReceipt]) -> None:
            assert len(result) == 1
            log_entry = result[0]
            assert log_entry['blockNumber'] == block_with_txn_with_log['number']
            assert log_entry['blockHash'] == block_with_txn_with_log['hash']
            assert log_entry['logIndex'] == 0
            assert is_same_address(log_entry['address'], emitter_contract_address)
            assert log_entry['transactionIndex'] == 0
            assert log_entry['transactionHash'] == HexBytes(txn_hash_with_log)

        # Test with block range

        # the range includes the block where the log resides in
        filter_params: FilterParams = {
            "fromBlock": block_with_txn_with_log['number'],
            "toBlock": block_with_txn_with_log['number'],
        }
        result = web3.eth.get_logs(filter_params)
        assert_contains_log(result)

        # specify only `from_block`. by default `to_block` should be 'latest'
        filter_params = {
            "fromBlock": BlockNumber(0),
        }
        result = web3.eth.get_logs(filter_params)
        assert_contains_log(result)

        # Test with `address`

        # filter with emitter_contract.address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": emitter_contract_address,
        }

    def test_eth_get_logs_with_logs_topic_args(
        self,
        web3: "Web3",
        block_with_txn_with_log: BlockData,
        emitter_contract_address: ChecksumAddress,
        txn_hash_with_log: HexStr,
    ) -> None:
        def assert_contains_log(result: Sequence[LogReceipt]) -> None:
            assert len(result) == 1
            log_entry = result[0]
            assert log_entry['blockNumber'] == block_with_txn_with_log['number']
            assert log_entry['blockHash'] == block_with_txn_with_log['hash']
            assert log_entry['logIndex'] == 0
            assert is_same_address(log_entry['address'], emitter_contract_address)
            assert log_entry['transactionIndex'] == 0
            assert log_entry['transactionHash'] == HexBytes(txn_hash_with_log)

        # Test with None event sig

        filter_params: FilterParams = {
            "fromBlock": BlockNumber(0),
            "topics": [
                None,
                HexStr('0x000000000000000000000000000000000000000000000000000000000000d431')],
        }

        result = web3.eth.get_logs(filter_params)
        assert_contains_log(result)

        # Test with None indexed arg
        filter_params = {
            "fromBlock": BlockNumber(0),
            "topics": [
                HexStr('0x057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca'),
                None],
        }
        result = web3.eth.get_logs(filter_params)
        assert_contains_log(result)

    def test_eth_get_logs_with_logs_none_topic_args(self, web3: "Web3") -> None:
        # Test with None overflowing
        filter_params: FilterParams = {
            "fromBlock": BlockNumber(0),
            "topics": [None, None, None],
        }

        result = web3.eth.get_logs(filter_params)
        assert len(result) == 0

    def test_eth_call_old_contract_state(
        self, web3: "Web3", math_contract: "Contract", unlocked_account: ChecksumAddress
    ) -> None:
        start_block = web3.eth.get_block('latest')
        block_num = start_block["number"]
        block_hash = start_block["hash"]

        math_contract.functions.increment().transact({'from': unlocked_account})

        # This isn't an incredibly convincing test since we can't mine, and
        # the default resolved block is latest, So if block_identifier was ignored
        # we would get the same result. For now, we mostly depend on core tests.
        # Ideas to improve this test:
        #  - Enable on-demand mining in more clients
        #  - Increment the math contract in all of the fixtures, and check the value in an old block
        block_hash_call_result = math_contract.functions.counter().call(block_identifier=block_hash)
        block_num_call_result = math_contract.functions.counter().call(block_identifier=block_num)
        latest_call_result = math_contract.functions.counter().call(block_identifier='latest')
        default_call_result = math_contract.functions.counter().call()
        pending_call_result = math_contract.functions.counter().call(block_identifier='pending')

        assert block_hash_call_result == 0
        assert block_num_call_result == 0
        assert latest_call_result == 0
        assert default_call_result == 0

        if pending_call_result != 1:
            raise AssertionError("pending call result was %d instead of 1" % pending_call_result)

    def test_eth_uninstallFilter_deprecated(self, web3: "Web3") -> None:
        filter = web3.eth.filter({})
        assert is_string(filter.filter_id)

        with pytest.warns(DeprecationWarning,
                          match="uninstallFilter is deprecated in favor of uninstall_filter"):
            success = web3.eth.uninstallFilter(filter.filter_id)
        assert success is True

        with pytest.warns(DeprecationWarning,
                          match="uninstallFilter is deprecated in favor of uninstall_filter"):
            failure = web3.eth.uninstallFilter(filter.filter_id)
        assert failure is False

    def test_eth_uninstall_filter(self, web3: "Web3") -> None:
        filter = web3.eth.filter({})
        assert is_string(filter.filter_id)

        success = web3.eth.uninstall_filter(filter.filter_id)
        assert success is True

        failure = web3.eth.uninstall_filter(filter.filter_id)
        assert failure is False

    def test_eth_getTransactionFromBlock_deprecation(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        with pytest.raises(DeprecationWarning):
            web3.eth.getTransactionFromBlock(block_with_txn['hash'], 0)

    def test_eth_getCompilers_deprecation(self, web3: "Web3") -> None:
        with pytest.raises(DeprecationWarning):
            web3.eth.getCompilers()

    def test_eth_submit_hashrate(self, web3: "Web3") -> None:
        # node_id from EIP 1474: https://github.com/ethereum/EIPs/pull/1474/files
        node_id = HexStr('59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c')
        result = web3.eth.submit_hashrate(5000, node_id)
        assert result is True

    def test_eth_submitHashrate_deprecated(self, web3: "Web3") -> None:
        # node_id from EIP 1474: https://github.com/ethereum/EIPs/pull/1474/files
        node_id = HexStr('59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c')
        with pytest.warns(DeprecationWarning,
                          match='submitHashrate is deprecated in favor of submit_hashrate'):
            result = web3.eth.submitHashrate(5000, node_id)
        assert result is True

    def test_eth_submit_work(self, web3: "Web3") -> None:
        nonce = 1
        pow_hash = HexStr('0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')
        mix_digest = HexStr('0xD1FE5700000000000000000000000000D1FE5700000000000000000000000000')
        result = web3.eth.submit_work(nonce, pow_hash, mix_digest)
        assert result is False

    def test_eth_submitWork_deprecated(self, web3: "Web3") -> None:
        nonce = 1
        pow_hash = HexStr('0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')
        mix_digest = HexStr('0xD1FE5700000000000000000000000000D1FE5700000000000000000000000000')
        with pytest.warns(DeprecationWarning,
                          match="submitWork is deprecated in favor of submit_work"):
            result = web3.eth.submitWork(nonce, pow_hash, mix_digest)
        assert result is False

    def test_eth_get_raw_transaction(
        self, web3: "Web3", mined_txn_hash: HexStr
    ) -> None:
        raw_transaction = web3.eth.get_raw_transaction(mined_txn_hash)
        assert is_bytes(raw_transaction)

    def test_eth_get_raw_transaction_raises_error(self, web3: "Web3") -> None:
        with pytest.raises(TransactionNotFound, match=f"Transaction with hash: '{UNKNOWN_HASH}'"):
            web3.eth.get_raw_transaction(UNKNOWN_HASH)

    def test_eth_get_raw_transaction_by_block(
        self, web3: "Web3",
        unlocked_account_dual_type: ChecksumAddress,
        block_with_txn: BlockData,
    ) -> None:
        # eth_getRawTransactionByBlockNumberAndIndex: block identifier
        # send a txn to make sure pending block has at least one txn
        web3.eth.send_transaction(
            {
                'from': unlocked_account_dual_type,
                'to': unlocked_account_dual_type,
                'value': Wei(1),
            }
        )
        last_pending_txn_index = len(web3.eth.get_block('pending')['transactions']) - 1
        raw_transaction = web3.eth.get_raw_transaction_by_block('pending', last_pending_txn_index)
        assert is_bytes(raw_transaction)

        # eth_getRawTransactionByBlockNumberAndIndex: block number
        block_with_txn_number = block_with_txn['number']
        assert is_integer(block_with_txn_number)
        raw_transaction = web3.eth.get_raw_transaction_by_block(block_with_txn_number, 0)
        assert is_bytes(raw_transaction)

        # eth_getRawTransactionByBlockHashAndIndex: block hash
        block_with_txn_hash = block_with_txn['hash']
        assert is_bytes(block_with_txn_hash)
        raw_transaction = web3.eth.get_raw_transaction_by_block(block_with_txn_hash, 0)
        assert is_bytes(raw_transaction)

    @pytest.mark.parametrize('unknown_block_num_or_hash', (1234567899999, UNKNOWN_HASH))
    def test_eth_get_raw_transaction_by_block_raises_error(
        self, web3: "Web3", unknown_block_num_or_hash: Union[int, HexBytes]
    ) -> None:
        with pytest.raises(
            TransactionNotFound, match=(
                f"Transaction index: 0 on block id: "
                f"{to_hex_if_integer(unknown_block_num_or_hash)!r} not found."
            )
        ):
            web3.eth.get_raw_transaction_by_block(unknown_block_num_or_hash, 0)

    def test_eth_get_raw_transaction_by_block_raises_error_block_identifier(
        self, web3: "Web3"
    ) -> None:
        unknown_identifier = "unknown"
        with pytest.raises(
            ValueError, match=(
                f"Value did not match any of the recognized block identifiers: {unknown_identifier}"
            )
        ):
            web3.eth.get_raw_transaction_by_block(unknown_identifier, 0)  # type: ignore
