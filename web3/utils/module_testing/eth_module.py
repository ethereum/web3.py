# -*- coding: utf-8 -*-

import pytest

from eth_abi import (
    decode_single,
)

from eth_utils import (
    is_checksum_address,
    is_bytes,
    is_string,
    is_boolean,
    is_dict,
    is_integer,
    is_list_like,
    is_same_address,
)

from web3.exceptions import (
    InvalidAddress,
)

from web3.utils.datastructures import (
    HexBytes,
)

UNKOWN_HASH = '0xdeadbeef00000000000000000000000000000000000000000000000000000000'


class EthModuleTest(object):
    def test_eth_protocolVersion(self, web3):
        protocol_version = web3.version.ethereum

        assert is_string(protocol_version)
        assert protocol_version.isdigit()

    def test_eth_syncing(self, web3):
        syncing = web3.eth.syncing

        assert is_boolean(syncing) or is_dict(syncing)

        if is_boolean(syncing):
            assert syncing is False
        elif is_dict(syncing):
            assert 'startingBlock' in syncing
            assert 'currentBlock' in syncing
            assert 'highestBlock' in syncing

            assert is_integer(syncing['startingBlock'])
            assert is_integer(syncing['currentBlock'])
            assert is_integer(syncing['highestBlock'])

    def test_eth_coinbase(self, web3):
        coinbase = web3.eth.coinbase
        assert is_checksum_address(coinbase)

    def test_eth_mining(self, web3):
        mining = web3.eth.mining
        assert is_boolean(mining)

    def test_eth_hashrate(self, web3):
        hashrate = web3.eth.hashrate
        assert is_integer(hashrate)
        assert hashrate >= 0

    def test_eth_gasPrice(self, web3):
        gas_price = web3.eth.gasPrice
        assert is_integer(gas_price)
        assert gas_price > 0

    def test_eth_accounts(self, web3):
        accounts = web3.eth.accounts
        assert is_list_like(accounts)
        assert len(accounts) != 0
        assert all((
            is_checksum_address(account)
            for account
            in accounts
        ))
        assert web3.eth.coinbase in accounts

    def test_eth_blockNumber(self, web3):
        block_number = web3.eth.blockNumber
        assert is_integer(block_number)
        assert block_number >= 0

    def test_eth_getBalance(self, web3):
        coinbase = web3.eth.coinbase

        with pytest.raises(InvalidAddress):
            web3.eth.getBalance(coinbase.lower())

        balance = web3.eth.getBalance(coinbase)

        assert is_integer(balance)
        assert balance >= 0

    def test_eth_getStorageAt(self, web3):
        coinbase = web3.eth.coinbase

        with pytest.raises(InvalidAddress):
            web3.eth.getStorageAt(coinbase.lower(), 0)

    def test_eth_getTransactionCount(self, web3):
        coinbase = web3.eth.coinbase
        transaction_count = web3.eth.getTransactionCount(coinbase)
        with pytest.raises(InvalidAddress):
            web3.eth.getTransactionCount(coinbase.lower())

        assert is_integer(transaction_count)
        assert transaction_count >= 0

    def test_eth_getBlockTransactionCountByHash_empty_block(self, web3, empty_block):
        transaction_count = web3.eth.getBlockTransactionCount(empty_block['hash'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByNumber_empty_block(self, web3, empty_block):
        transaction_count = web3.eth.getBlockTransactionCount(empty_block['number'])

        assert is_integer(transaction_count)
        assert transaction_count == 0

    def test_eth_getBlockTransactionCountByHash_block_with_txn(self, web3, block_with_txn):
        transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['hash'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getBlockTransactionCountByNumber_block_with_txn(self, web3, block_with_txn):
        transaction_count = web3.eth.getBlockTransactionCount(block_with_txn['number'])

        assert is_integer(transaction_count)
        assert transaction_count >= 1

    def test_eth_getUncleCountByBlockHash(self, web3, empty_block):
        uncle_count = web3.eth.getUncleCount(empty_block['hash'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getUncleCountByBlockNumber(self, web3, empty_block):
        uncle_count = web3.eth.getUncleCount(empty_block['number'])

        assert is_integer(uncle_count)
        assert uncle_count == 0

    def test_eth_getCode(self, web3, math_contract):
        code = web3.eth.getCode(math_contract.address)
        with pytest.raises(InvalidAddress):
            code = web3.eth.getCode(math_contract.address.lower())
        assert is_string(code)
        assert len(code) > 2

    def test_eth_sign(self, web3, unlocked_account):
        signature = web3.eth.sign(unlocked_account, text='Message tö sign. Longer than hash!')
        assert is_bytes(signature)
        assert len(signature) == 32 + 32 + 1

        # test other formats
        hexsign = web3.eth.sign(
            unlocked_account,
            hexstr='0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821'
        )
        assert hexsign == signature

        intsign = web3.eth.sign(
            unlocked_account,
            0x4d6573736167652074c3b6207369676e2e204c6f6e676572207468616e206861736821
        )
        assert intsign == signature

        bytessign = web3.eth.sign(unlocked_account, b'Message t\xc3\xb6 sign. Longer than hash!')
        assert bytessign == signature

        new_signature = web3.eth.sign(unlocked_account, text='different message is different')
        assert new_signature != signature

    def test_eth_sendTransaction_addr_checksum_required(self, web3, unlocked_account):
        non_checksum_addr = unlocked_account.lower()
        txn_params = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': 1,
            'gas': 21000,
            'gas_price': web3.eth.gasPrice,
        }

        with pytest.raises(InvalidAddress):
            invalid_params = dict(txn_params, **{'from': non_checksum_addr})
            web3.eth.sendTransaction(invalid_params)

        with pytest.raises(InvalidAddress):
            invalid_params = dict(txn_params, **{'to': non_checksum_addr})
            web3.eth.sendTransaction(invalid_params)

    def test_eth_sendTransaction(self, web3, unlocked_account):
        txn_params = {
            'from': unlocked_account,
            'to': unlocked_account,
            'value': 1,
            'gas': 21000,
            'gas_price': web3.eth.gasPrice,
        }
        txn_hash = web3.eth.sendTransaction(txn_params)
        txn = web3.eth.getTransaction(txn_hash)

        assert is_same_address(txn['from'], txn_params['from'])
        assert is_same_address(txn['to'], txn_params['to'])
        assert txn['value'] == 1
        assert txn['gas'] == 21000
        assert txn['gasPrice'] == txn_params['gas_price']

    @pytest.mark.parametrize(
        'raw_transaction, expected_hash',
        [
            (
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
    def test_eth_sendRawTransaction(self, web3, raw_transaction, expected_hash):
        txn_hash = web3.eth.sendRawTransaction(raw_transaction)
        assert txn_hash == web3.toBytes(hexstr=expected_hash)

    def test_eth_call(self, web3, math_contract):
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(7, 11),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = web3.eth.call(txn_params)
        assert is_string(call_result)
        result = decode_single('uint256', call_result)
        assert result == 18

    def test_eth_call_with_0_result(self, web3, math_contract):
        coinbase = web3.eth.coinbase
        txn_params = math_contract._prepare_transaction(
            fn_name='add',
            fn_args=(0, 0),
            transaction={'from': coinbase, 'to': math_contract.address},
        )
        call_result = web3.eth.call(txn_params)
        assert is_string(call_result)
        result = decode_single('uint256', call_result)
        assert result == 0

    def test_eth_estimateGas(self, web3):
        coinbase = web3.eth.coinbase
        gas_estimate = web3.eth.estimateGas({
            'from': coinbase,
            'to': coinbase,
            'value': 1,
        })
        assert is_integer(gas_estimate)
        assert gas_estimate > 0

    def test_eth_getBlockByHash(self, web3, empty_block):
        block = web3.eth.getBlock(empty_block['hash'])
        assert block['hash'] == empty_block['hash']

    def test_eth_getBlockByHash_not_found(self, web3, empty_block):
        block = web3.eth.getBlock(UNKOWN_HASH)
        assert block is None

    def test_eth_getBlockByNumber_with_integer(self, web3, empty_block):
        block = web3.eth.getBlock(empty_block['number'])
        assert block['number'] == empty_block['number']

    def test_eth_getBlockByNumber_latest(self, web3, empty_block):
        current_block_number = web3.eth.blockNumber
        block = web3.eth.getBlock('latest')
        assert block['number'] == current_block_number

    def test_eth_getBlockByNumber_not_found(self, web3, empty_block):
        block = web3.eth.getBlock(12345)
        assert block is None

    def test_eth_getBlockByNumber_pending(self, web3, empty_block):
        current_block_number = web3.eth.blockNumber
        block = web3.eth.getBlock('pending')
        assert block['number'] == current_block_number + 1

    def test_eth_getBlockByNumber_earliest(self, web3, empty_block):
        genesis_block = web3.eth.getBlock(0)
        block = web3.eth.getBlock('earliest')
        assert block['number'] == 0
        assert block['hash'] == genesis_block['hash']

    def test_eth_getBlockByNumber_full_transactions(self, web3, block_with_txn):
        block = web3.eth.getBlock(block_with_txn['number'], True)
        transaction = block['transactions'][0]
        assert transaction['hash'] == block_with_txn['transactions'][0]

    def test_eth_getTransactionByHash(self, web3, mined_txn_hash):
        transaction = web3.eth.getTransaction(mined_txn_hash)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByHash_contract_creation(self,
                                                        web3,
                                                        math_contract_deploy_txn_hash):
        transaction = web3.eth.getTransaction(math_contract_deploy_txn_hash)
        assert is_dict(transaction)
        assert transaction['to'] is None

    def test_eth_getTransactionByBlockHashAndIndex(self, web3, block_with_txn, mined_txn_hash):
        transaction = web3.eth.getTransactionFromBlock(block_with_txn['hash'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionByBlockNumberAndIndex(self, web3, block_with_txn, mined_txn_hash):
        transaction = web3.eth.getTransactionFromBlock(block_with_txn['number'], 0)
        assert is_dict(transaction)
        assert transaction['hash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionReceipt_mined(self, web3, block_with_txn, mined_txn_hash):
        receipt = web3.eth.getTransactionReceipt(mined_txn_hash)
        assert is_dict(receipt)
        assert receipt['blockNumber'] == block_with_txn['number']
        assert receipt['blockHash'] == block_with_txn['hash']
        assert receipt['transactionIndex'] == 0
        assert receipt['transactionHash'] == HexBytes(mined_txn_hash)

    def test_eth_getTransactionReceipt_unmined(self, web3, unlocked_account):
        txn_hash = web3.eth.sendTransaction({
            'from': unlocked_account,
            'to': unlocked_account,
            'value': 1,
            'gas': 21000,
            'gas_price': web3.eth.gasPrice,
        })
        receipt = web3.eth.getTransactionReceipt(txn_hash)
        assert receipt is None

    def test_eth_getTransactionReceipt_with_log_entry(self,
                                                      web3,
                                                      block_with_txn_with_log,
                                                      emitter_contract,
                                                      txn_hash_with_log):
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

    def test_eth_getUncleByBlockHashAndIndex(self, web3):
        # TODO: how do we make uncles....
        pass

    def test_eth_getUncleByBlockNumberAndIndex(self, web3):
        # TODO: how do we make uncles....
        pass

    def test_eth_getCompilers(self, web3):
        # TODO: do we want to test this?
        pass

    def test_eth_compileSolidity(self, web3):
        # TODO: do we want to test this?
        pass

    def test_eth_compileLLL(self, web3):
        # TODO: do we want to test this?
        pass

    def test_eth_compileSerpent(self, web3):
        # TODO: do we want to test this?
        pass

    def test_eth_newFilter(self, web3):
        filter = web3.eth.filter({})

        changes = web3.eth.getFilterChanges(filter.filter_id)
        assert is_list_like(changes)
        assert not changes

        logs = web3.eth.getFilterLogs(filter.filter_id)
        assert is_list_like(logs)
        assert not logs

        result = web3.eth.uninstallFilter(filter.filter_id)
        assert result is True

    def test_eth_newBlockFilter(self, web3):
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

    def test_eth_newPendingTransactionFilter(self, web3):
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

    def test_eth_uninstallFilter(self, web3):
        filter = web3.eth.filter({})
        assert is_string(filter.filter_id)

        success = web3.eth.uninstallFilter(filter.filter_id)
        assert success is True

        failure = web3.eth.uninstallFilter(filter.filter_id)
        assert failure is False
