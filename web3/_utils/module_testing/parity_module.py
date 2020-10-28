import pytest
from typing import (
    TYPE_CHECKING,
    Dict,
)

from eth_typing import (
    ChecksumAddress,
    HexStr,
)
from eth_utils import (
    add_0x_prefix,
)

from web3._utils.formatters import (
    hex_to_integer,
)
from web3.types import (
    BlockData,
    EnodeURI,
    ParityFilterParams,
    ParityMode,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.contract import Contract  # noqa: F401


class ParityTraceModuleTest:

    def test_trace_replay_transaction(
        self, web3: "Web3", parity_fixture_data: Dict[str, str],
    ) -> None:
        trace = web3.parity.traceReplayTransaction(HexStr(parity_fixture_data['mined_txn_hash']))

        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        assert trace['trace'][0]['action']['from'] == add_0x_prefix(
            HexStr(parity_fixture_data['coinbase']),
        )

    def test_trace_replay_block_with_transactions(
        self, web3: "Web3", block_with_txn: BlockData, parity_fixture_data: Dict[str, str]
    ) -> None:
        trace = web3.parity.traceReplayBlockTransactions(block_with_txn['number'])
        assert len(trace) > 0
        trace_0_action = trace[0]['trace'][0]['action']
        assert trace_0_action['from'] == add_0x_prefix(HexStr(parity_fixture_data['coinbase']))

    def test_trace_replay_block_without_transactions(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        trace = web3.parity.traceReplayBlockTransactions(empty_block['number'])
        assert len(trace) == 0

    def test_trace_block(self, web3: "Web3", block_with_txn: BlockData) -> None:
        trace = web3.parity.traceBlock(block_with_txn['number'])
        assert trace[0]['blockNumber'] == block_with_txn['number']

    def test_trace_transaction(self, web3: "Web3", parity_fixture_data: Dict[str, str]) -> None:
        trace = web3.parity.traceTransaction(HexStr(parity_fixture_data['mined_txn_hash']))
        assert trace[0]['action']['from'] == add_0x_prefix(HexStr(parity_fixture_data['coinbase']))

    def test_trace_call(
        self, web3: "Web3", math_contract: "Contract", math_contract_address: ChecksumAddress
    ) -> None:
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(7, 11),
            transaction={'from': coinbase, 'to': math_contract_address},
        )
        trace = web3.parity.traceCall(txn_params)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        result = hex_to_integer(trace['output'])
        assert result == 18

    def test_eth_call_with_0_result(
        self, web3: "Web3", math_contract: "Contract", math_contract_address: ChecksumAddress
    ) -> None:
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(0, 0),
            transaction={'from': coinbase, 'to': math_contract_address},
        )
        trace = web3.parity.traceCall(txn_params)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        result = hex_to_integer(trace['output'])
        assert result == 0

    @pytest.mark.parametrize(
        'raw_transaction',
        [
            (
                # address 0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6
                '0xf8648085174876e8008252089439eeed73fb1d3855e90cbd42f348b3d7b340aaa601801ba0ec1295f00936acd0c2cb90ab2cdaacb8bf5e11b3d9957833595aca9ceedb7aada05dfc8937baec0e26029057abd3a1ef8c505dca2cdc07ffacb046d090d2bea06a'  # noqa: E501
            ),
        ]
    )
    def test_trace_raw_transaction(
        self,
        web3: "Web3",
        raw_transaction: HexStr,
        funded_account_for_raw_txn: ChecksumAddress,
    ) -> None:
        trace = web3.parity.traceRawTransaction(raw_transaction)
        assert trace['stateDiff'] is None
        assert trace['vmTrace'] is None
        assert trace['trace'][0]['action']['from'] == funded_account_for_raw_txn.lower()

    def test_trace_filter(
        self,
        web3: "Web3",
        txn_filter_params: ParityFilterParams,
        parity_fixture_data: Dict[str, str],
    ) -> None:
        trace = web3.parity.traceFilter(txn_filter_params)
        assert isinstance(trace, list)
        assert trace[0]['action']['from'] == add_0x_prefix(HexStr(parity_fixture_data['coinbase']))


class ParityModuleTest:

    def test_add_reserved_peer(self, web3: "Web3") -> None:
        peer_addr = EnodeURI('enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30300')  # noqa: E501
        assert web3.parity.addReservedPeer(peer_addr)

    def test_list_storage_keys_no_support(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        keys = web3.parity.listStorageKeys(emitter_contract_address, 10, None)
        assert keys == []

    def test_mode(self, web3: "Web3") -> None:
        assert web3.parity.mode() is not None


class ParitySetModuleTest:

    @pytest.mark.parametrize(
        'mode',
        [
            ('dark'),
            ('offline'),
            ('active'),
            ('passive'),
        ]
    )
    def test_set_mode(self, web3: "Web3", mode: ParityMode) -> None:
        assert web3.parity.setMode(mode) is True

    def test_set_mode_with_bad_string(self, web3: "Web3") -> None:
        with pytest.raises(ValueError, match="Couldn't parse parameters: mode"):
            # type ignored b/c it's an invalid literal ParityMode
            web3.parity.setMode('not a mode')  # type: ignore

    def test_set_mode_with_no_argument(self, web3: "Web3") -> None:
        with pytest.raises(TypeError, match='missing 1 required positional argument'):
            # type ignored b/c setMode expects arguments
            web3.parity.setMode()  # type: ignore
