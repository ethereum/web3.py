import contextlib
import json
import os
import pprint
import shutil
import sys

from eth_utils import (
    is_dict,
    is_same_address,
)

import common
from web3 import Web3
from web3.utils.module_testing.emitter_contract import (
    EMITTER_ABI,
    EMITTER_BYTECODE,
    EMITTER_ENUM,
)
from web3.utils.module_testing.math_contract import (
    MATH_ABI,
    MATH_BYTECODE,
)
from web3.utils.toolz import (
    merge,
)


def generate_go_ethereum_fixture(destination_dir):
    with contextlib.ExitStack() as stack:
        datadir = stack.enter_context(common.tempdir())

        keystore_dir = os.path.join(datadir, 'keystore')
        common.ensure_path_exists(keystore_dir)
        keyfile_path = os.path.join(keystore_dir, common.KEYFILE_FILENAME)
        with open(keyfile_path, 'w') as keyfile:
            keyfile.write(common.KEYFILE_DATA)
        genesis_file_path = os.path.join(datadir, 'genesis.json')
        with open(genesis_file_path, 'w') as genesis_file:
            genesis_file.write(json.dumps(common.GENESIS_DATA))

        geth_ipc_path_dir = stack.enter_context(common.tempdir())
        geth_ipc_path = os.path.join(geth_ipc_path_dir, 'geth.ipc')

        geth_port = common.get_open_port()
        geth_binary = common.get_geth_binary()

        geth_proc = stack.enter_context(common.get_geth_process(  # noqa: F841
            geth_binary=geth_binary,
            datadir=datadir,
            genesis_file_path=genesis_file_path,
            ipc_path=geth_ipc_path,
            port=geth_port,
            networkid=str(common.GENESIS_DATA['config']['chainId'])
        ))

        common.wait_for_socket(geth_ipc_path)
        web3 = Web3(Web3.IPCProvider(geth_ipc_path))
        chain_data = setup_chain_state(web3)
        static_data = {
            'raw_txn_account': common.RAW_TXN_ACCOUNT,
            'keyfile_pw': common.KEYFILE_PW,
        }
        pprint.pprint(merge(chain_data, static_data))

        shutil.copytree(datadir, destination_dir)


def setup_chain_state(web3):
    coinbase = web3.eth.coinbase

    assert is_same_address(coinbase, common.COINBASE)

    #
    # Math Contract
    #
    math_contract_factory = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_BYTECODE,
    )
    math_deploy_receipt = common.deploy_contract(web3, 'math', math_contract_factory)
    assert is_dict(math_deploy_receipt)

    #
    # Emitter Contract
    #
    emitter_contract_factory = web3.eth.contract(
        abi=EMITTER_ABI,
        bytecode=EMITTER_BYTECODE,
    )
    emitter_deploy_receipt = common.deploy_contract(web3, 'emitter', emitter_contract_factory)
    emitter_contract = emitter_contract_factory(emitter_deploy_receipt['contractAddress'])

    txn_hash_with_log = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321,
    ).transact({
        'from': web3.eth.coinbase,
    })
    print('TXN_HASH_WITH_LOG:', txn_hash_with_log)
    txn_receipt_with_log = common.mine_transaction_hash(web3, txn_hash_with_log)
    block_with_log = web3.eth.getBlock(txn_receipt_with_log['blockHash'])
    print('BLOCK_HASH_WITH_LOG:', block_with_log['hash'])

    #
    # Empty Block
    #
    empty_block_number = common.mine_block(web3)
    print('MINED_EMPTY_BLOCK')
    empty_block = web3.eth.getBlock(empty_block_number)
    assert is_dict(empty_block)
    assert not empty_block['transactions']
    print('EMPTY_BLOCK_HASH:', empty_block['hash'])

    #
    # Block with Transaction
    #
    web3.personal.unlockAccount(coinbase, common.KEYFILE_PW)
    web3.miner.start(1)
    mined_txn_hash = web3.eth.sendTransaction({
        'from': coinbase,
        'to': coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': web3.eth.gasPrice,
    })
    mined_txn_receipt = common.mine_transaction_hash(web3, mined_txn_hash)
    print('MINED_TXN_HASH:', mined_txn_hash)
    block_with_txn = web3.eth.getBlock(mined_txn_receipt['blockHash'])
    print('BLOCK_WITH_TXN_HASH:', block_with_txn['hash'])

    geth_fixture = {
        'math_deploy_txn_hash': math_deploy_receipt['transactionHash'],
        'math_address': math_deploy_receipt['contractAddress'],
        'emitter_deploy_txn_hash': emitter_deploy_receipt['transactionHash'],
        'emitter_address': emitter_deploy_receipt['contractAddress'],
        'txn_hash_with_log': txn_hash_with_log,
        'block_hash_with_log': block_with_log['hash'],
        'empty_block_hash': empty_block['hash'],
        'mined_txn_hash': mined_txn_hash,
        'block_with_txn_hash': block_with_txn['hash'],
    }
    return geth_fixture


if __name__ == '__main__':
    fixture_dir = sys.argv[1]
    generate_go_ethereum_fixture(fixture_dir)
