# -*- coding: utf-8 -*-

import json
import pytest
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
from hexbytes import (
    HexBytes,
)

from web3._utils.ens import (
    ens_addresses,
)
from web3.exceptions import (
    BlockNotFound,
    InvalidAddress,
    NameNotFound,
    SolidityError,
    TransactionNotFound,
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


class EthModuleTest:
    def test_eth_protocolVersion(self, web3: "Web3") -> None:
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

    def test_eth_chainId(self, web3: "Web3") -> None:
        chain_id = web3.eth.chainId
        # chain id value from geth fixture genesis file
        assert chain_id == 131277322940537

    def test_eth_gasPrice(self, web3: "Web3") -> None:
        gas_price = web3.eth.gasPrice
        assert is_integer(gas_price)
        assert gas_price > 0

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

    def test_eth_blockNumber(self, web3: "Web3") -> None:
        block_number = web3.eth.blockNumber
        assert is_integer(block_number)
        assert block_number >= 0

    def test_eth_getBalance(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase

        with pytest.raises(InvalidAddress):
            web3.eth.getBalance(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))))

        balance = web3.eth.getBalance(coinbase)

        assert is_integer(balance)
        assert balance >= 0

    def test_eth_getBalance_with_block_identifier(self, web3: "Web3") -> None:
        miner_address = web3.eth.getBlock(1)['miner']
        genesis_balance = web3.eth.getBalance(miner_address, 0)
        later_balance = web3.eth.getBalance(miner_address, 1)

        assert is_integer(genesis_balance)
        assert is_integer(later_balance)
        assert later_balance > genesis_balance

    @pytest.mark.parametrize('address, expect_success', [
        ('test-address.eth', True),
        ('not-an-address.eth', False)
    ])
    def test_eth_getBalance_with_ens_name(
        self, web3: "Web3", address: ChecksumAddress, expect_success: bool
    ) -> None:
        with ens_addresses(web3, {'test-address.eth': web3.eth.accounts[0]}):
            if expect_success:
                balance = web3.eth.getBalance(address)
                assert is_integer(balance)
                assert balance >= 0
            else:
                with pytest.raises(NameNotFound):
                    web3.eth.getBalance(address)

    def test_eth_getStorageAt(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        storage = web3.eth.getStorageAt(emitter_contract_address, 0)
        assert isinstance(storage, HexBytes)

    def test_eth_getStorageAt_ens_name(
        self, web3: "Web3", emitter_contract_address: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'emitter.eth': emitter_contract_address}):
            storage = web3.eth.getStorageAt('emitter.eth', 0)
            assert isinstance(storage, HexBytes)

    def test_eth_getStorageAt_invalid_address(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase
        with pytest.raises(InvalidAddress):
            web3.eth.getStorageAt(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))), 0)

    def test_eth_getTransactionCount(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        transaction_count = web3.eth.getTransactionCount(unlocked_account_dual_type)
        assert is_integer(transaction_count)
        assert transaction_count >= 0

    def test_eth_getTransactionCount_ens_name(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'unlocked-acct-dual-type.eth': unlocked_account_dual_type}):
            transaction_count = web3.eth.getTransactionCount('unlocked-acct-dual-type.eth')
            assert is_integer(transaction_count)
            assert transaction_count >= 0

    def test_eth_getTransactionCount_invalid_address(self, web3: "Web3") -> None:
        coinbase = web3.eth.coinbase
        with pytest.raises(InvalidAddress):
            web3.eth.getTransactionCount(ChecksumAddress(HexAddress(HexStr(coinbase.lower()))))

    def test_eth_getBlockTransactionCountByHash_empty_block(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        transaction_count = web3.eth.getBlockTransactionCount(empty_block['hash'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByNumber_empty_block(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        transaction_count = web3.eth.getBlockTransactionCount(empty_block['number'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByHash_block_with_txn(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['hash'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getBlockTransactionCountByNumber_block_with_txn(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['number'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getUncleCountByBlockHash(self, web3: "Web3", empty_block: BlockData) -> None:
        uncle_count = web3.eth.getUncleCount(empty_block['hash'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getUncleCountByBlockNumber(self, web3: "Web3", empty_block: BlockData) -> None:
        uncle_count = web3.eth.getUncleCount(empty_block['number'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getCode(self, web3: "Web3", math_contract_address: ChecksumAddress) -> None:
        code = web3.eth.getCode(math_contract_address)
        assert isinstance(code, HexBytes)
        assert len(code) > 0

    def test_eth_getCode_ens_address(
        self, web3: "Web3", math_contract_address: ChecksumAddress
    ) -> None:
        with ens_addresses(
            web3, {'mathcontract.eth': math_contract_address}
        ):
            code = web3.eth.getCode('mathcontract.eth')
            assert isinstance(code, HexBytes)
            assert len(code) > 0

    def test_eth_getCode_invalid_address(self, web3: "Web3", math_contract: "Contract") -> None:
        with pytest.raises(InvalidAddress):
            web3.eth.getCode(ChecksumAddress(HexAddress(HexStr(math_contract.address.lower()))))

    def test_eth_getCode_with_block_identifier(
        self, web3: "Web3", emitter_contract: "Contract"
    ) -> None:
        code = web3.eth.getCode(emitter_contract.address, block_identifier=web3.eth.blockNumber)
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

    def test_eth_signTypedData(
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

    def test_invalid_eth_signTypedData(
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
            web3.eth.signTypedData(
                unlocked_account_dual_type,
                json.loads(invalid_typed_message)
            )

    def test_eth_signTransaction(self, web3: "Web3", unlocked_account: ChecksumAddress) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
            'nonce': Nonce(0),
        }
        result = web3.eth.signTransaction(txn_params)
        signatory_account = web3.eth.account.recover_transaction(result['raw'])
        assert unlocked_account == signatory_account
        assert result['tx']['to'] == txn_params['to']
        assert result['tx']['value'] == txn_params['value']
        assert result['tx']['gas'] == txn_params['gas']
        assert result['tx']['gasPrice'] == txn_params['gasPrice']
        assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_signTransaction_ens_names(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        with ens_addresses(web3, {'unlocked-account.eth': unlocked_account}):
            txn_params: TxParams = {
                'from': 'unlocked-account.eth',
                'to': 'unlocked-account.eth',
                'value': Wei(1),
                'gas': Wei(21000),
                'gasPrice': web3.eth.gasPrice,
                'nonce': Nonce(0),
            }
            result = web3.eth.signTransaction(txn_params)
            signatory_account = web3.eth.account.recover_transaction(result['raw'])
            assert unlocked_account == signatory_account
            assert result['tx']['to'] == unlocked_account
            assert result['tx']['value'] == txn_params['value']
            assert result['tx']['gas'] == txn_params['gas']
            assert result['tx']['gasPrice'] == txn_params['gasPrice']
            assert result['tx']['nonce'] == txn_params['nonce']

    def test_eth_sendTransaction_addr_checksum_required(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        non_checksum_addr = unlocked_account.lower()
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }

        with pytest.raises(InvalidAddress):
            invalid_params = cast(TxParams, dict(txn_params, **{'from': non_checksum_addr}))
            web3.eth.sendTransaction(invalid_params)

        with pytest.raises(InvalidAddress):
            invalid_params = cast(TxParams, dict(txn_params, **{'to': non_checksum_addr}))
            web3.eth.sendTransaction(invalid_params)

    def test_eth_sendTransaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)
        txn = web3.eth.getTransaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['gasPrice'] == txn_params['gasPrice']

    def test_eth_sendTransaction_with_nonce(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            # Increased gas price to ensure transaction hash different from other tests
            'gasPrice': Wei(web3.eth.gasPrice * 3),
            'nonce': web3.eth.getTransactionCount(unlocked_account),
        }
        txn_hash = web3.eth.sendTransaction(txn_params)
        txn = web3.eth.getTransaction(txn_hash)

        assert is_same_address(txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['gasPrice'] == txn_params['gasPrice']
        assert txn['nonce'] == txn_params['nonce']

    def test_eth_replaceTransaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        txn_params['gasPrice'] = Wei(web3.eth.gasPrice * 2)
        replace_txn_hash = web3.eth.replaceTransaction(txn_hash, txn_params)
        replace_txn = web3.eth.getTransaction(replace_txn_hash)

        assert is_same_address(replace_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(replace_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert replace_txn['value'] == 1
        assert replace_txn['gas'] == 21000
        assert replace_txn['gasPrice'] == txn_params['gasPrice']

    def test_eth_replaceTransaction_non_existing_transaction(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        with pytest.raises(TransactionNotFound):
            web3.eth.replaceTransaction(
                HexStr('0x98e8cc09b311583c5079fa600f6c2a3bea8611af168c52e4b60b5b243a441997'),
                txn_params
            )

    def test_eth_replaceTransaction_already_mined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)
        web3.eth.waitForTransactionReceipt(txn_hash)

        txn_params['gasPrice'] = Wei(web3.eth.gasPrice * 2)
        with pytest.raises(ValueError, match="Supplied transaction with hash"):
            web3.eth.replaceTransaction(txn_hash, txn_params)

    def test_eth_replaceTransaction_incorrect_nonce(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)
        txn = web3.eth.getTransaction(txn_hash)

        txn_params['gasPrice'] = Wei(web3.eth.gasPrice * 2)
        txn_params['nonce'] = Nonce(txn['nonce'] + 1)
        with pytest.raises(ValueError):
            web3.eth.replaceTransaction(txn_hash, txn_params)

    def test_eth_replaceTransaction_gas_price_too_low(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(10),
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        txn_params['gasPrice'] = Wei(9)
        with pytest.raises(ValueError):
            web3.eth.replaceTransaction(txn_hash, txn_params)

    def test_eth_replaceTransaction_gas_price_defaulting_minimum(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(10),
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replaceTransaction(txn_hash, txn_params)
        replace_txn = web3.eth.getTransaction(replace_txn_hash)

        assert replace_txn['gasPrice'] == 12  # minimum gas price

    def test_eth_replaceTransaction_gas_price_defaulting_strategy_higher(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(10),
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        def higher_gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return Wei(20)

        web3.eth.setGasPriceStrategy(higher_gas_price_strategy)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replaceTransaction(txn_hash, txn_params)
        replace_txn = web3.eth.getTransaction(replace_txn_hash)
        assert replace_txn['gasPrice'] == 20  # Strategy provides higher gas price

    def test_eth_replaceTransaction_gas_price_defaulting_strategy_lower(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': Wei(10),
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        def lower_gas_price_strategy(web3: "Web3", txn: TxParams) -> Wei:
            return Wei(5)

        web3.eth.setGasPriceStrategy(lower_gas_price_strategy)

        txn_params.pop('gasPrice')
        replace_txn_hash = web3.eth.replaceTransaction(txn_hash, txn_params)
        replace_txn = web3.eth.getTransaction(replace_txn_hash)
        # Strategy provices lower gas price - minimum preferred
        assert replace_txn['gasPrice'] == 12

    def test_eth_modifyTransaction(
        self, web3: "Web3", unlocked_account: ChecksumAddress
    ) -> None:
        txn_params: TxParams = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)

        modified_txn_hash = web3.eth.modifyTransaction(
            txn_hash, gasPrice=(cast(int, txn_params['gasPrice']) * 2), value=2
        )
        modified_txn = web3.eth.getTransaction(modified_txn_hash)

        assert is_same_address(modified_txn['from'], cast(ChecksumAddress, txn_params['from']))
        assert is_same_address(modified_txn['to'], cast(ChecksumAddress, txn_params['to']))
        assert modified_txn['value'] == 2
        assert modified_txn['gas'] == 21000
        assert modified_txn['gasPrice'] == cast(int, txn_params['gasPrice']) * 2

    @pytest.mark.parametrize(
        'raw_transaction, expected_hash',
        [
            (
                # address 0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6
                '0xf8648085174876e8008252089439eeed73fb1d3855e90cbd42f348b3d7b340aaa601801ba0ec1295f00936acd0c2cb90ab2cdaacb8bf5e11b3d9957833595aca9ceedb7aada05dfc8937baec0e26029057abd3a1ef8c505dca2cdc07ffacb046d090d2bea06a',  # noqa: E501
                '0x1f80f8ab5f12a45be218f76404bda64d37270a6f4f86ededd0eb599f80548c13',
            ),
            (
                # private key 0x3c2ab4e8f17a7dea191b8c991522660126d681039509dc3bb31af7c9bdb63518
                # This is an unfunded account, but the transaction has a 0 gas price, so is valid.
                # It never needs to be mined, we just want the transaction hash back to confirm.
                HexBytes('0xf85f808082c35094d898d5e829717c72e7438bad593076686d7d164a80801ba005c2e99ecee98a12fbf28ab9577423f42e9e88f2291b3acc8228de743884c874a077d6bc77a47ad41ec85c96aac2ad27f05a039c4787fca8a1e5ee2d8c7ec1bb6a'),  # noqa: E501
                '0x98eeadb99454427f6aad7b558bac13e9d225512a6f5e5c11cf48e8d4067e51b5',
            ),
        ]
    )
    def test_eth_sendRawTransaction(
        self,
        web3: "Web3",
        raw_transaction: Union[HexStr, bytes],
        funded_account_for_raw_txn: ChecksumAddress,
        expected_hash: HexStr,
    ) -> None:
        txn_hash = web3.eth.sendRawTransaction(raw_transaction)
        assert txn_hash == web3.toBytes(hexstr=expected_hash)

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
        with pytest.raises(SolidityError, match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.call(txn_params)

    def test_eth_estimateGas_revert_with_msg(
        self,
        web3: "Web3",
        revert_contract: "Contract",
        unlocked_account: ChecksumAddress,
    ) -> None:
        with pytest.raises(SolidityError, match='execution reverted: Function has been reverted'):
            txn_params = revert_contract._prepare_transaction(
                fn_name="revertWithMessage",
                transaction={
                    "from": unlocked_account,
                    "to": revert_contract.address,
                },
            )
            web3.eth.estimateGas(txn_params)

    def test_eth_estimateGas(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        gas_estimate = web3.eth.estimateGas({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
        })
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_estimateGas_with_block(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        gas_estimate = web3.eth.estimateGas({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
        }, 'latest')
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_getBlockByHash(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        block = web3.eth.getBlock(empty_block['hash'])
        assert block['hash'] == empty_block['hash']

    def test_eth_getBlockByHash_not_found(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.raises(BlockNotFound):
            web3.eth.getBlock(UNKNOWN_HASH)

    def test_eth_getBlockByNumber_with_integer(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        block = web3.eth.getBlock(empty_block['number'])
        assert block['number'] == empty_block['number']

    def test_eth_getBlockByNumber_latest(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = web3.eth.blockNumber
        block = web3.eth.getBlock('latest')
        assert block['number'] == current_block_number

    def test_eth_getBlockByNumber_not_found(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        with pytest.raises(BlockNotFound):
            web3.eth.getBlock(BlockNumber(12345))

    def test_eth_getBlockByNumber_pending(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        current_block_number = web3.eth.blockNumber
        block = web3.eth.getBlock('pending')
        assert block['number'] == current_block_number + 1

    def test_eth_getBlockByNumber_earliest(
        self, web3: "Web3", empty_block: BlockData
    ) -> None:
        genesis_block = web3.eth.getBlock(BlockNumber(0))
        block = web3.eth.getBlock('earliest')
        assert block['number'] == 0
        assert block['hash'] == genesis_block['hash']

    def test_eth_getBlockByNumber_full_transactions(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        block = web3.eth.getBlock(block_with_txn['number'], True)
        transaction = block['transactions'][0]
        assert transaction['hash'] == block_with_txn['transactions'][0]  # type: ignore

    def test_eth_getTransactionByHash(
        self, web3: "Web3", mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.getTransaction(mined_txn_hash)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByHash_contract_creation(
        self, web3: "Web3", math_contract_deploy_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.getTransaction(math_contract_deploy_txn_hash)
        assert is_dict(transaction)
        assert transaction['to'] is None, "to field is %r" % transaction['to']

    def test_eth_getTransactionByBlockHashAndIndex(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.getTransactionByBlock(block_with_txn['hash'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByBlockNumberAndIndex(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        transaction = web3.eth.getTransactionByBlock(block_with_txn['number'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionReceipt_mined(
        self, web3: "Web3", block_with_txn: BlockData, mined_txn_hash: HexStr
    ) -> None:
        receipt = web3.eth.getTransactionReceipt(mined_txn_hash)
        assert is_dict(receipt)
        assert receipt['blockNumber'] == block_with_txn['number']
        assert receipt['blockHash'] == block_with_txn['hash']
        assert receipt['transactionIndex'] == 0
        assert receipt['transactionHash'] == HexBytes(mined_txn_hash)
        assert is_checksum_address(receipt['to'])
        assert receipt['from'] is not None
        assert is_checksum_address(receipt['from'])

    def test_eth_getTransactionReceipt_unmined(
        self, web3: "Web3", unlocked_account_dual_type: ChecksumAddress
    ) -> None:
        txn_hash = web3.eth.sendTransaction({
            'from': unlocked_account_dual_type,
            'to': unlocked_account_dual_type,
            'value': Wei(1),
            'gas': Wei(21000),
            'gasPrice': web3.eth.gasPrice,
        })
        with pytest.raises(TransactionNotFound):
            web3.eth.getTransactionReceipt(txn_hash)

    def test_eth_getTransactionReceipt_with_log_entry(
        self,
        web3: "Web3",
        block_with_txn_with_log: BlockData,
        emitter_contract: "Contract",
        txn_hash_with_log: HexStr,
    ) -> None:
        receipt = web3.eth.getTransactionReceipt(txn_hash_with_log)
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

        changes = web3.eth.getFilterChanges(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        logs = web3.eth.getFilterLogs(filter.filter_id)
        assert is_list_like(logs)
        assert not logs

        result = web3.eth.uninstallFilter(filter.filter_id)
        assert result is True

    def test_eth_newBlockFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter('latest')
        assert is_string(filter.filter_id)

        changes = web3.eth.getFilterChanges(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        # TODO: figure out why this fails in go-ethereum
        # logs = web3.eth.getFilterLogs(filter.filter_id)
        # assert is_list_like(logs)
        # assert not logs

        result = web3.eth.uninstallFilter(filter.filter_id)
        assert result is True

    def test_eth_newPendingTransactionFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter('pending')
        assert is_string(filter.filter_id)

        changes = web3.eth.getFilterChanges(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        # TODO: figure out why this fails in go-ethereum
        # logs = web3.eth.getFilterLogs(filter.filter_id)
        # assert is_list_like(logs)
        # assert not logs

        result = web3.eth.uninstallFilter(filter.filter_id)
        assert result is True

    def test_eth_getLogs_without_logs(
        self, web3: "Web3", block_with_txn_with_log: BlockData
    ) -> None:
        # Test with block range

        filter_params: FilterParams = {
            "fromBlock": BlockNumber(0),
            "toBlock": BlockNumber(block_with_txn_with_log['number'] - 1),
        }
        result = web3.eth.getLogs(filter_params)
        assert len(result) == 0

        # the range is wrong
        filter_params = {
            "fromBlock": block_with_txn_with_log['number'],
            "toBlock": BlockNumber(block_with_txn_with_log['number'] - 1),
        }
        result = web3.eth.getLogs(filter_params)
        assert len(result) == 0

        # Test with `address`

        # filter with other address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": UNKNOWN_ADDRESS,
        }
        result = web3.eth.getLogs(filter_params)
        assert len(result) == 0

        # Test with multiple `address`

        # filter with other address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": [UNKNOWN_ADDRESS, UNKNOWN_ADDRESS],
        }
        result = web3.eth.getLogs(filter_params)
        assert len(result) == 0

    def test_eth_getLogs_with_logs(
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
        result = web3.eth.getLogs(filter_params)
        assert_contains_log(result)

        # specify only `from_block`. by default `to_block` should be 'latest'
        filter_params = {
            "fromBlock": BlockNumber(0),
        }
        result = web3.eth.getLogs(filter_params)
        assert_contains_log(result)

        # Test with `address`

        # filter with emitter_contract.address
        filter_params = {
            "fromBlock": BlockNumber(0),
            "address": emitter_contract_address,
        }

    def test_eth_getLogs_with_logs_topic_args(
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

        result = web3.eth.getLogs(filter_params)
        assert_contains_log(result)

        # Test with None indexed arg
        filter_params = {
            "fromBlock": BlockNumber(0),
            "topics": [
                HexStr('0x057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca'),
                None],
        }
        result = web3.eth.getLogs(filter_params)
        assert_contains_log(result)

    def test_eth_getLogs_with_logs_none_topic_args(self, web3: "Web3") -> None:
        # Test with None overflowing
        filter_params: FilterParams = {
            "fromBlock": BlockNumber(0),
            "topics": [None, None, None],
        }

        result = web3.eth.getLogs(filter_params)
        assert len(result) == 0

    def test_eth_call_old_contract_state(
        self, web3: "Web3", math_contract: "Contract", unlocked_account: ChecksumAddress
    ) -> None:
        start_block = web3.eth.getBlock('latest')
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

    def test_eth_uninstallFilter(self, web3: "Web3") -> None:
        filter = web3.eth.filter({})
        assert is_string(filter.filter_id)

        success = web3.eth.uninstallFilter(filter.filter_id)
        assert success is True

        failure = web3.eth.uninstallFilter(filter.filter_id)
        assert failure is False

    def test_eth_getTransactionFromBlock_deprecation(
        self, web3: "Web3", block_with_txn: BlockData
    ) -> None:
        with pytest.raises(DeprecationWarning):
            web3.eth.getTransactionFromBlock(block_with_txn['hash'], 0)

    def test_eth_getCompilers_deprecation(self, web3: "Web3") -> None:
        with pytest.raises(DeprecationWarning):
            web3.eth.getCompilers()

    def test_eth_submitHashrate(self, web3: "Web3") -> None:
        # node_id from EIP 1474: https://github.com/ethereum/EIPs/pull/1474/files
        node_id = HexStr('59daa26581d0acd1fce254fb7e85952f4c09d0915afd33d3886cd914bc7d283c')
        result = web3.eth.submitHashrate(5000, node_id)
        assert result is True

    def test_eth_submitWork(self, web3: "Web3") -> None:
        nonce = 1
        pow_hash = HexStr('0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef')
        mix_digest = HexStr('0xD1FE5700000000000000000000000000D1FE5700000000000000000000000000')
        result = web3.eth.submitWork(nonce, pow_hash, mix_digest)
        assert result is False
