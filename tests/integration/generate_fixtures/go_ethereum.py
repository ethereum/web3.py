import contextlib
import json
import os
import pprint
import shutil
import subprocess
import sys
import time

from eth_utils.curried import (
    apply_formatter_if,
    is_bytes,
    is_dict,
    is_same_address,
    to_hex,
    to_text,
)
from eth_utils.toolz import (
    merge,
    valmap,
)

import common
from tests.utils import (
    get_open_port,
)
from web3 import Web3
from web3._utils.module_testing.emitter_contract import (
    CONTRACT_EMITTER_ABI,
    CONTRACT_EMITTER_CODE,
    EMITTER_ENUM,
)
from web3._utils.module_testing.math_contract import (
    MATH_ABI,
    MATH_BYTECODE,
)
from web3._utils.module_testing.revert_contract import (
    _REVERT_CONTRACT_ABI,
    REVERT_CONTRACT_BYTECODE,
)


@contextlib.contextmanager
def graceful_kill_on_exit(proc):
    try:
        yield proc
    finally:
        common.kill_proc_gracefully(proc)


@contextlib.contextmanager
def get_geth_process(geth_binary,
                     datadir,
                     genesis_file_path,
                     geth_ipc_path,
                     geth_port):
    init_datadir_command = (
        geth_binary,
        '--datadir', datadir,
        'init',
        genesis_file_path,
    )
    subprocess.check_output(
        init_datadir_command,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    run_geth_command = (
        geth_binary,
        '--datadir', datadir,
        '--ipcpath', geth_ipc_path,
        '--ethash.dagsondisk', '1',
        '--gcmode', 'archive',
        '--nodiscover',
        '--port', geth_port,
        '--miner.etherbase', common.COINBASE[2:],
    )

    popen_proc = subprocess.Popen(
        run_geth_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    with popen_proc as proc:
        with graceful_kill_on_exit(proc) as graceful_proc:
            yield graceful_proc

        output, errors = proc.communicate()

    print(
        "Geth Process Exited:\n"
        f"stdout:{to_text(output)}\n\n"
        f"stderr:{to_text(errors)}\n\n"
    )


def write_config_json(config, datadir):
    bytes_to_hex = apply_formatter_if(is_bytes, to_hex)
    config_json_dict = valmap(bytes_to_hex, config)

    config_path = os.path.join(datadir, 'config.json')
    with open(config_path, 'w') as config_file:
        config_file.write(json.dumps(config_json_dict))
        config_file.write('\n')


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

        geth_port = get_open_port()
        geth_binary = common.get_geth_binary()

        with get_geth_process(
                geth_binary=geth_binary,
                datadir=datadir,
                genesis_file_path=genesis_file_path,
                geth_ipc_path=geth_ipc_path,
                geth_port=geth_port):

            common.wait_for_socket(geth_ipc_path)
            w3 = Web3(Web3.IPCProvider(geth_ipc_path))
            chain_data = setup_chain_state(w3)
            # close geth by exiting context
            # must be closed before copying data dir
            verify_chain_state(w3, chain_data)

        # verify that chain state is still valid after closing
        # and re-opening geth
        with get_geth_process(
                geth_binary=geth_binary,
                datadir=datadir,
                genesis_file_path=genesis_file_path,
                geth_ipc_path=geth_ipc_path,
                geth_port=geth_port):

            common.wait_for_socket(geth_ipc_path)
            w3 = Web3(Web3.IPCProvider(geth_ipc_path))
            verify_chain_state(w3, chain_data)

        static_data = {
            'raw_txn_account': common.RAW_TXN_ACCOUNT,
            'keyfile_pw': common.KEYFILE_PW,
        }
        config = merge(chain_data, static_data)
        pprint.pprint(config)
        write_config_json(config, datadir)

        shutil.make_archive(destination_dir, 'zip', datadir)


def verify_chain_state(w3, chain_data):
    receipt = w3.eth.wait_for_transaction_receipt(chain_data['mined_txn_hash'])
    latest = w3.eth.get_block('latest')
    assert receipt.blockNumber <= latest.number


def mine_transaction_hash(w3, txn_hash):
    w3.geth.miner.start(1)
    try:
        return w3.eth.wait_for_transaction_receipt(txn_hash, timeout=120)
    finally:
        w3.geth.miner.stop()


def mine_block(w3):
    origin_block_number = w3.eth.block_number

    start_time = time.time()
    w3.geth.miner.start(1)
    while time.time() < start_time + 120:
        block_number = w3.eth.block_number
        if block_number > origin_block_number:
            w3.geth.miner.stop()
            return block_number
        else:
            time.sleep(0.1)
    else:
        raise ValueError("No block mined during wait period")


def setup_chain_state(w3):
    coinbase = w3.eth.coinbase

    assert is_same_address(coinbase, common.COINBASE)

    #
    # Math Contract
    #
    math_contract_factory = w3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_BYTECODE,
    )
    math_deploy_receipt = common.deploy_contract(w3, 'math', math_contract_factory)
    assert is_dict(math_deploy_receipt)

    #
    # Emitter Contract
    #
    emitter_contract_factory = w3.eth.contract(
        abi=CONTRACT_EMITTER_ABI,
        bytecode=CONTRACT_EMITTER_CODE,
    )
    emitter_deploy_receipt = common.deploy_contract(w3, 'emitter', emitter_contract_factory)
    emitter_contract = emitter_contract_factory(emitter_deploy_receipt['contractAddress'])

    txn_hash_with_log = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321,
    ).transact({
        'from': w3.eth.coinbase,
    })
    print('TXN_HASH_WITH_LOG:', txn_hash_with_log)
    txn_receipt_with_log = mine_transaction_hash(w3, txn_hash_with_log)
    block_with_log = w3.eth.get_block(txn_receipt_with_log['blockHash'])
    print('BLOCK_HASH_WITH_LOG:', block_with_log['hash'])

    #
    # Revert Contract
    #
    revert_contract_factory = w3.eth.contract(
        abi=_REVERT_CONTRACT_ABI,
        bytecode=REVERT_CONTRACT_BYTECODE,
    )
    revert_deploy_receipt = common.deploy_contract(w3, 'revert', revert_contract_factory)
    revert_contract = revert_contract_factory(revert_deploy_receipt['contractAddress'])

    txn_hash_normal_function = revert_contract.functions.normalFunction().transact(
        {'gas': 320000, 'from': w3.eth.coinbase}
    )
    print('TXN_HASH_REVERT_NORMAL:', txn_hash_normal_function)
    txn_hash_revert_with_msg = revert_contract.functions.revertWithMessage().transact(
        {'gas': 320000, 'from': w3.eth.coinbase}
    )
    print('TXN_HASH_REVERT_WITH_MSG:', txn_hash_revert_with_msg)
    txn_receipt_revert_with_msg = common.mine_transaction_hash(w3, txn_hash_revert_with_msg)
    block_hash_revert_with_msg = w3.eth.get_block(txn_receipt_revert_with_msg['blockHash'])
    print('BLOCK_HASH_REVERT_WITH_MSG:', block_hash_revert_with_msg['hash'])

    txn_hash_revert_with_no_msg = revert_contract.functions.revertWithoutMessage().transact(
        {'gas': 320000, 'from': w3.eth.coinbase}
    )
    print('TXN_HASH_REVERT_WITH_NO_MSG:', txn_hash_revert_with_no_msg)
    txn_receipt_revert_with_no_msg = common.mine_transaction_hash(w3, txn_hash_revert_with_no_msg)
    block_hash_revert_no_msg = w3.eth.get_block(txn_receipt_revert_with_no_msg['blockHash'])
    print('BLOCK_HASH_REVERT_NO_MSG:', block_hash_revert_no_msg['hash'])

    #
    # Empty Block
    #
    empty_block_number = mine_block(w3)
    print('MINED_EMPTY_BLOCK')
    empty_block = w3.eth.get_block(empty_block_number)
    assert is_dict(empty_block)
    assert not empty_block['transactions']
    print('EMPTY_BLOCK_HASH:', empty_block['hash'])

    #
    # Block with Transaction
    #
    w3.geth.personal.unlock_account(coinbase, common.KEYFILE_PW)
    w3.geth.miner.start(1)
    mined_txn_hash = w3.eth.send_transaction({
        'from': coinbase,
        'to': coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': w3.eth.gas_price,
    })
    mined_txn_receipt = mine_transaction_hash(w3, mined_txn_hash)
    print('MINED_TXN_HASH:', mined_txn_hash)
    block_with_txn = w3.eth.get_block(mined_txn_receipt['blockHash'])
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
        'revert_address': revert_deploy_receipt['contractAddress'],
        'block_hash_revert_with_msg': block_hash_revert_with_msg['hash'],
        'block_hash_revert_no_msg': block_hash_revert_no_msg['hash'],
    }
    return geth_fixture


if __name__ == '__main__':
    fixture_dir = sys.argv[1]
    generate_go_ethereum_fixture(fixture_dir)
