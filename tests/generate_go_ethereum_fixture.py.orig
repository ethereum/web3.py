import contextlib
import json
import os
import pprint
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time

from eth_utils.curried import (
    apply_formatter_if,
    is_bytes,
    is_checksum_address,
    is_dict,
    is_same_address,
    remove_0x_prefix,
    to_hex,
    to_text,
    to_wei,
)

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
    valmap,
)

COINBASE = '0xdc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd'
COINBASE_PK = '0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d'

KEYFILE_DATA = '{"address":"dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd","crypto":{"cipher":"aes-128-ctr","ciphertext":"52e06bc9397ea9fa2f0dae8de2b3e8116e92a2ecca9ad5ff0061d1c449704e98","cipherparams":{"iv":"aa5d0a5370ef65395c1a6607af857124"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"9fdf0764eb3645ffc184e166537f6fe70516bf0e34dc7311dea21f100f0c9263"},"mac":"4e0b51f42b865c15c485f4faefdd1f01a38637e5247f8c75ffe6a8c0eba856f6"},"id":"5a6124e0-10f1-4c1c-ae3e-d903eacb740a","version":3}'  # noqa: E501

KEYFILE_PW = 'web3py-test'
KEYFILE_FILENAME = 'UTC--2017-08-24T19-42-47.517572178Z--dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd'  # noqa: E501

RAW_TXN_ACCOUNT = '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6'

UNLOCKABLE_PRIVATE_KEY = '0x392f63a79b1ff8774845f3fa69de4a13800a59e7083f5187f1558f0797ad0f01'
UNLOCKABLE_ACCOUNT = '0x12efdc31b1a8fa1a1e756dfd8a1601055c971e13'
UNLOCKABLE_ACCOUNT_PW = KEYFILE_PW


GENESIS_DATA = {
    "nonce": "0xdeadbeefdeadbeef",
    "timestamp": "0x0",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
    "extraData": "0x7765623370792d746573742d636861696e",
    "gasLimit": "0x47d5cc",
    "difficulty": "0x01",
    "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
    "coinbase": "0x3333333333333333333333333333333333333333",
    "alloc": {
        remove_0x_prefix(COINBASE): {
            'balance': str(to_wei(1000000000, 'ether')),
        },
        remove_0x_prefix(RAW_TXN_ACCOUNT): {
            'balance': str(to_wei(10, 'ether')),
        },
        remove_0x_prefix(UNLOCKABLE_ACCOUNT): {
            'balance': str(to_wei(10, 'ether')),
        },
    },
    "config": {
        "chainId": 131277322940537,  # the string 'web3py' as an integer
        "homesteadBlock": 0,
        "eip155Block": 0,
        "eip158Block": 0
    },
}


def ensure_path_exists(dir_path):
    """
    Make sure that a path exists
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False


@contextlib.contextmanager
def tempdir():
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)


def get_geth_binary():
    from geth.install import (
        get_executable_path,
        install_geth,
    )

    if 'GETH_BINARY' in os.environ:
        return os.environ['GETH_BINARY']
    elif 'GETH_VERSION' in os.environ:
        geth_version = os.environ['GETH_VERSION']
        _geth_binary = get_executable_path(geth_version)
        if not os.path.exists(_geth_binary):
            install_geth(geth_version)
        assert os.path.exists(_geth_binary)
        return _geth_binary
    else:
        return 'geth'


def wait_for_popen(proc, timeout):
    start = time.time()
    while time.time() < start + timeout:
        if proc.poll() is None:
            time.sleep(0.01)
        else:
            break


def kill_proc_gracefully(proc):
    if proc.poll() is None:
        proc.send_signal(signal.SIGINT)
        wait_for_popen(proc, 13)

    if proc.poll() is None:
        proc.terminate()
        wait_for_popen(proc, 5)

    if proc.poll() is None:
        proc.kill()
        wait_for_popen(proc, 2)


def wait_for_socket(ipc_path, timeout=30):
    start = time.time()
    while time.time() < start + timeout:
        try:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.connect(ipc_path)
            sock.settimeout(timeout)
        except (FileNotFoundError, socket.error):
            time.sleep(0.01)
        else:
            break


@contextlib.contextmanager
def graceful_kill_on_exit(proc):
    try:
        yield proc
    finally:
        kill_proc_gracefully(proc)


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
        '--etherbase', COINBASE[2:],
    )

    popen_proc = subprocess.Popen(
        run_geth_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
    )
    with popen_proc as proc:
        with graceful_kill_on_exit(proc) as graceful_proc:
            yield graceful_proc

        output, errors = proc.communicate()

    print(
        "Geth Process Exited:\n"
        "stdout:{0}\n\n"
        "stderr:{1}\n\n".format(
            to_text(output),
            to_text(errors),
        )
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
        datadir = stack.enter_context(tempdir())

        keystore_dir = os.path.join(datadir, 'keystore')
        ensure_path_exists(keystore_dir)
        keyfile_path = os.path.join(keystore_dir, KEYFILE_FILENAME)
        with open(keyfile_path, 'w') as keyfile:
            keyfile.write(KEYFILE_DATA)
        genesis_file_path = os.path.join(datadir, 'genesis.json')
        with open(genesis_file_path, 'w') as genesis_file:
            genesis_file.write(json.dumps(GENESIS_DATA))

        geth_ipc_path_dir = stack.enter_context(tempdir())
        geth_ipc_path = os.path.join(geth_ipc_path_dir, 'geth.ipc')

        geth_port = get_open_port()
        geth_binary = get_geth_binary()

        with get_geth_process(
                geth_binary=geth_binary,
                datadir=datadir,
                genesis_file_path=genesis_file_path,
                geth_ipc_path=geth_ipc_path,
                geth_port=geth_port):

            wait_for_socket(geth_ipc_path)
            web3 = Web3(Web3.IPCProvider(geth_ipc_path))
            chain_data = setup_chain_state(web3)
            # close geth by exiting context
            # must be closed before copying data dir
            verify_chain_state(web3, chain_data)

        # verify that chain state is still valid after closing
        # and re-opening geth
        with get_geth_process(
                geth_binary=geth_binary,
                datadir=datadir,
                genesis_file_path=genesis_file_path,
                geth_ipc_path=geth_ipc_path,
                geth_port=geth_port):

            wait_for_socket(geth_ipc_path)
            web3 = Web3(Web3.IPCProvider(geth_ipc_path))
            verify_chain_state(web3, chain_data)

        static_data = {
            'raw_txn_account': RAW_TXN_ACCOUNT,
            'keyfile_pw': KEYFILE_PW,
        }
        config = merge(chain_data, static_data)
        pprint.pprint(config)
        write_config_json(config, datadir)

        shutil.copytree(datadir, destination_dir)


def verify_chain_state(web3, chain_data):
    receipt = web3.eth.waitForTransactionReceipt(chain_data['mined_txn_hash'])
    latest = web3.eth.getBlock('latest')
    assert receipt.blockNumber <= latest.number


def mine_transaction_hash(web3, txn_hash):
    start_time = time.time()
    web3.miner.start(1)
    while time.time() < start_time + 60:
        receipt = web3.eth.waitForTransactionReceipt(txn_hash)
        if receipt is not None:
            web3.miner.stop()
            return receipt
        else:
            time.sleep(0.1)
    else:
        raise ValueError("Math contract deploy transaction not mined during wait period")


def mine_block(web3):
    origin_block_number = web3.eth.blockNumber

    start_time = time.time()
    web3.miner.start(1)
    while time.time() < start_time + 60:
        block_number = web3.eth.blockNumber
        if block_number > origin_block_number:
            web3.miner.stop()
            return block_number
        else:
            time.sleep(0.1)
    else:
        raise ValueError("No block mined during wait period")


def deploy_contract(web3, name, factory):
    web3.personal.unlockAccount(web3.eth.coinbase, KEYFILE_PW)
    deploy_txn_hash = factory.constructor().transact({'from': web3.eth.coinbase})
    print('{0}_CONTRACT_DEPLOY_HASH: '.format(name.upper()), deploy_txn_hash)
    deploy_receipt = mine_transaction_hash(web3, deploy_txn_hash)
    print('{0}_CONTRACT_DEPLOY_TRANSACTION_MINED'.format(name.upper()))
    contract_address = deploy_receipt['contractAddress']
    assert is_checksum_address(contract_address)
    print('{0}_CONTRACT_ADDRESS:'.format(name.upper()), contract_address)
    return deploy_receipt


def setup_chain_state(web3):
    coinbase = web3.eth.coinbase

    assert is_same_address(coinbase, COINBASE)

    #
    # Math Contract
    #
    math_contract_factory = web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_BYTECODE,
    )
    math_deploy_receipt = deploy_contract(web3, 'math', math_contract_factory)
    assert is_dict(math_deploy_receipt)

    #
    # Emitter Contract
    #
    emitter_contract_factory = web3.eth.contract(
        abi=EMITTER_ABI,
        bytecode=EMITTER_BYTECODE,
    )
    emitter_deploy_receipt = deploy_contract(web3, 'emitter', emitter_contract_factory)
    emitter_contract = emitter_contract_factory(emitter_deploy_receipt['contractAddress'])

    txn_hash_with_log = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM['LogDoubleWithIndex'], arg0=12345, arg1=54321,
    ).transact({
        'from': web3.eth.coinbase,
    })
    print('TXN_HASH_WITH_LOG:', txn_hash_with_log)
    txn_receipt_with_log = mine_transaction_hash(web3, txn_hash_with_log)
    block_with_log = web3.eth.getBlock(txn_receipt_with_log['blockHash'])
    print('BLOCK_HASH_WITH_LOG:', block_with_log['hash'])

    #
    # Empty Block
    #
    empty_block_number = mine_block(web3)
    print('MINED_EMPTY_BLOCK')
    empty_block = web3.eth.getBlock(empty_block_number)
    assert is_dict(empty_block)
    assert not empty_block['transactions']
    print('EMPTY_BLOCK_HASH:', empty_block['hash'])

    #
    # Block with Transaction
    #
    web3.personal.unlockAccount(coinbase, KEYFILE_PW)
    web3.miner.start(1)
    mined_txn_hash = web3.eth.sendTransaction({
        'from': coinbase,
        'to': coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': web3.eth.gasPrice,
    })
    mined_txn_receipt = mine_transaction_hash(web3, mined_txn_hash)
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
