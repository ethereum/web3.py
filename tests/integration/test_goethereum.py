import json
import os
import signal
import socket
import subprocess
import time
import tempfile

import pytest

from eth_utils import (
    to_wei,
    remove_0x_prefix,
    is_dict,
    is_address,
)

from web3 import Web3

from web3.utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)
from web3.utils.module_testing.math_contract import (
    MATH_BYTECODE,
    MATH_ABI,
)


@pytest.fixture(scope='session')
def coinbase():
    return '0xdc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd'


@pytest.fixture(scope='session')
def private_key():
    return '0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d'


KEYFILE_DATA = '{"address":"dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd","crypto":{"cipher":"aes-128-ctr","ciphertext":"52e06bc9397ea9fa2f0dae8de2b3e8116e92a2ecca9ad5ff0061d1c449704e98","cipherparams":{"iv":"aa5d0a5370ef65395c1a6607af857124"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"9fdf0764eb3645ffc184e166537f6fe70516bf0e34dc7311dea21f100f0c9263"},"mac":"4e0b51f42b865c15c485f4faefdd1f01a38637e5247f8c75ffe6a8c0eba856f6"},"id":"5a6124e0-10f1-4c1c-ae3e-d903eacb740a","version":3}'  # noqa: E501

KEYFILE_PW = 'web3py-test'


@pytest.fixture(scope='session')
def datadir(tmpdir_factory):
    _datadir = tmpdir_factory.mktemp('geth-datadir')
    return _datadir


@pytest.fixture(scope='session')
def keystore(datadir):
    _keystore = datadir.mkdir('keystore')
    return _keystore


@pytest.fixture(scope='session')
def keyfile(keystore):
    _keyfile = keystore.join(
        'UTC--2017-08-24T19-42-47.517572178Z--dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd',
    )
    _keyfile.write(KEYFILE_DATA)
    return _keyfile


@pytest.fixture(scope='session')
def genesis_data(coinbase):
    return {
        "nonce": "0xdeadbeefdeadbeef",
        "timestamp": "0x0",
        "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
        "extraData": "0x7765623370792d746573742d636861696e",
        "gasLimit": "0x47d5cc",
        "difficulty": "0x01",
        "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",  # noqa: E501
        "coinbase": "0x3333333333333333333333333333333333333333",
        "alloc": {
            remove_0x_prefix(coinbase): {
                'balance': str(to_wei(1000000000, 'ether')),
            },
        },
        "config": {
            "chainId": 131277322940537,  # the string 'web3py' as an integer
            "homesteadBlock": 0,
            "eip155Block": 0,
            "eip158Block": 0
        },
    }


@pytest.fixture(scope='session')
def genesis_file(datadir, genesis_data):
    _genesis_file = datadir.join('genesis.json')
    _genesis_file.write(json.dumps(genesis_data))
    return _genesis_file


@pytest.fixture(scope='session')
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, 'geth.ipc')
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


class Timeout(Exception):
    pass


def wait_for_popen(proc, timeout):
    start = time.time()
    try:
        while time.time() < start + timeout:
            if proc.poll() is None:
                time.sleep(0.01)
            else:
                break
    except Timeout:
        pass


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


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)


@pytest.fixture(scope='session')
def geth_binary():
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


@pytest.fixture(scope='session')
def geth_port():
    return get_open_port()


@pytest.fixture(scope='session')
def geth_process(geth_binary, datadir, genesis_file, keyfile, geth_ipc_path, geth_port):
    init_datadir_command = (
        geth_binary,
        '--datadir', str(datadir),
        'init',
        str(genesis_file),
    )
    subprocess.check_output(
        init_datadir_command,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=10,
    )

    run_geth_command = (
        geth_binary,
        '--datadir', str(datadir),
        '--ipcpath', geth_ipc_path,
        '--nodiscover',
        '--mine',
        '--minerthreads', '1',
        '--port', geth_port,
    )
    proc = subprocess.Popen(
        run_geth_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
    )
    try:
        yield proc
    except:
        kill_proc_gracefully(proc)
        raise
    finally:
        output, errors = proc.communicate(timeout=10)
        print(
            "Geth Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                output.decode('utf8'),
                errors.decode('utf8'),
            )
        )


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


@pytest.fixture(scope="session")
def web3(geth_process, geth_ipc_path):
    wait_for_socket(geth_ipc_path)
    _web3 = Web3(Web3.IPCProvider(geth_ipc_path))
    return _web3


@pytest.fixture(scope="session")
def math_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="session")
def math_contract_deploy_txn_hash(web3, math_contract_factory):
    coinbase = web3.eth.coinbase
    web3.personal.unlockAccount(coinbase, KEYFILE_PW)
    deploy_txn_hash = math_contract_factory.deploy({'from': coinbase})
    web3.personal.lockAccount(coinbase)
    return deploy_txn_hash


@pytest.fixture(scope="session")
def math_contract(web3, math_contract_factory, math_contract_deploy_txn_hash):
    start_time = time.time()
    web3.miner.start(1)
    while time.time() < start_time + 60:
        deploy_receipt = web3.eth.getTransactionReceipt(math_contract_deploy_txn_hash)
        if deploy_receipt is not None:
            web3.miner.stop()
            break
        else:
            time.sleep(0.1)
    else:
        raise Timeout("Math contract deploy transaction not mined during wait period")
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt['contractAddress']
    assert is_address(contract_address)
    return math_contract_factory(contract_address)


@pytest.fixture
def unlocked_account(web3):
    coinbase = web3.eth.coinbase
    web3.personal.unlockAccount(coinbase, KEYFILE_PW)
    yield coinbase
    web3.personal.lockAccount(coinbase)


@pytest.fixture(scope="session")
def funded_account_for_raw_txn(web3):
    account = '0x39eeed73fb1d3855e90cbd42f348b3d7b340aaa6'
    coinbase = web3.eth.coinbase
    web3.personal.unlockAccount(coinbase, KEYFILE_PW)
    fund_txn_hash = web3.eth.sendTransaction({
        'from': coinbase,
        'to': account,
        'value': web3.toWei(10, 'ether'),
        'gas': 21000,
        'gas_price': web3.eth.gasPrice,
    })
    web3.personal.lockAccount(coinbase)
    web3.miner.start(1)
    start_time = time.time()
    while time.time() < start_time + 60:
        fund_receipt = web3.eth.getTransactionReceipt(fund_txn_hash)
        if fund_receipt is not None:
            web3.miner.stop()
            break
        else:
            time.sleep(0.1)
    else:
        raise Timeout("No block mined during wait period")
    return account


@pytest.fixture(scope="session")
def empty_block(web3):
    current_block_number = web3.eth.blockNumber
    web3.miner.start(1)
    start_time = time.time()
    while time.time() < start_time + 60:
        if web3.eth.blockNumber > current_block_number:
            web3.miner.stop()
            break
        else:
            time.sleep(0.1)
    else:
        raise Timeout("No block mined during wait period")
    block = web3.eth.getBlock(current_block_number + 1)
    return block


@pytest.fixture(scope="session")
def block_with_txn(web3):
    coinbase = web3.eth.coinbase
    web3.personal.unlockAccount(coinbase, KEYFILE_PW)
    web3.miner.start(1)
    txn_hash = web3.eth.sendTransaction({
        'from': coinbase,
        'to': coinbase,
        'value': 1,
        'gas': 21000,
        'gas_price': web3.eth.gasPrice,
    })
    start_time = time.time()
    while time.time() < start_time + 60:
        txn_receipt = web3.eth.getTransactionReceipt(txn_hash)
        if txn_receipt is not None:
            web3.miner.stop()
            break
        else:
            time.sleep(0.1)
    else:
        raise Timeout("Math contract deploy transaction not mined during wait period")
    web3.personal.lockAccount(coinbase)
    block = web3.eth.getBlock(txn_receipt['blockNumber'])
    return block


@pytest.fixture(scope="session")
def mined_txn_hash(block_with_txn):
    return block_with_txn['transactions'][0]


class TestGoEthereum(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class TestGoEthereumEthModule(EthModuleTest):
    pass


class TestGoEthereumVersionModule(VersionModuleTest):
    pass


class TestGoEthereumNetModule(NetModuleTest):
    pass
