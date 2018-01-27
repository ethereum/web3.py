import os
import pytest
import shutil
import signal
import socket
import subprocess
import tempfile
import time

from eth_utils import (
    force_text,
    is_checksum_address,
    is_dict,
)

from web3 import Web3
from web3.utils.module_testing import (
    EthModuleTest,
    NetModuleTest,
    PersonalModuleTest,
    VersionModuleTest,
    Web3ModuleTest,
)

KEYFILE_PW = 'web3py-test'


GETH_16_FIXTURE = {
    'datadir': 'geth-16-datadir-fixture',
    'block_hash_with_log': '0x5d84bd72195aacbbf6f3ed66be7a16495ed470cbc3e4764c69e4be75ab084148',
    'block_with_txn_hash': '0x4000549a8a573ed2e436de3a9014fdf71922f59aa11753870baa2ad03a32ebfc',
    'emitter_address': '0x4aA591a07989b4F810E2F5cE97e769D60710f168',
    'emitter_deploy_txn_hash': '0x1f676a3d88a8eb3210df677f3dca96edd78b646f8dcecab82d186d7394c8ab6c',
    'empty_block_hash': '0xd09336bcc6164d8d958914f7800356a3bb0cf05f98e20aefc00ce23d9ca62d2d',
    'keyfile_pw': 'web3py-test',
    'math_address': '0xd794C821fCCFF5D96F5Db44af7e29977630A9dc2',
    'math_deploy_txn_hash': '0xbefcf394f431fd983901d16c155da2d009da720b7b88cb9c7dce66f5d3ac44e7',
    'mined_txn_hash': '0x95110dd5943f513a1fd29767b48fe2178b973e99f5d73693d889081d7bdcd0c2',
    'raw_txn_account': '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6',
    'txn_hash_with_log': '0x2fd8dcd6ab1318245f8423df8e31f66f5d0fac2db34d7ab4a2a21a71037beae1',
}
GETH_17_FIXTURE = {
    'datadir': 'geth-17-datadir-fixture',
    'block_hash_with_log': '0x78a60c6b31c7af5e5ce87bad73b595dfe5b8715b161f4d3ded468ddcb14b5aeb',
    'block_with_txn_hash': '0x034faac7d0932774d9d837a97d55061a2dca9724c9779427a075f0a475aa3f43',
    'emitter_address': '0x4aA591a07989b4F810E2F5cE97e769D60710f168',
    'emitter_deploy_txn_hash': '0x1f676a3d88a8eb3210df677f3dca96edd78b646f8dcecab82d186d7394c8ab6c',
    'empty_block_hash': '0xc7a1b4c19f6c1d830a743f7a93a58bab129f4671f1eb1a82ae77e6643d733b9b',
    'keyfile_pw': 'web3py-test',
    'math_address': '0xd794C821fCCFF5D96F5Db44af7e29977630A9dc2',
    'math_deploy_txn_hash': '0xbefcf394f431fd983901d16c155da2d009da720b7b88cb9c7dce66f5d3ac44e7',
    'mined_txn_hash': '0x95110dd5943f513a1fd29767b48fe2178b973e99f5d73693d889081d7bdcd0c2',
    'raw_txn_account': '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6',
    'txn_hash_with_log': '0x2fd8dcd6ab1318245f8423df8e31f66f5d0fac2db34d7ab4a2a21a71037beae1',
}


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


@pytest.fixture(scope="session")
def geth_fixture_data(geth_binary):
    from geth import get_geth_version
    version = get_geth_version(geth_executable=os.path.expanduser(geth_binary))
    if version.major == 1:
        if version.minor == 6:
            return GETH_16_FIXTURE
        elif version.minor == 7:
            return GETH_17_FIXTURE
    assert False, "Unsupported geth version"


@pytest.fixture(scope='session')
def datadir(tmpdir_factory, geth_fixture_data):
    fixture_datadir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        geth_fixture_data['datadir'],
    ))
    base_dir = tmpdir_factory.mktemp('goethereum')
    tmp_datadir = os.path.join(str(base_dir), 'datadir')
    shutil.copytree(fixture_datadir, tmp_datadir)
    return tmp_datadir


@pytest.fixture(scope='session')
def genesis_file(datadir):
    genesis_file_path = os.path.join(datadir, 'genesis.json')
    return genesis_file_path


@pytest.fixture(scope='session')
def geth_ipc_path(datadir):
    geth_ipc_dir_path = tempfile.mkdtemp()
    _geth_ipc_path = os.path.join(geth_ipc_dir_path, 'geth.ipc')
    yield _geth_ipc_path

    if os.path.exists(_geth_ipc_path):
        os.remove(_geth_ipc_path)


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


@pytest.fixture(scope='session')
def geth_process(geth_binary, datadir, genesis_file, geth_ipc_path):
    geth_port = get_open_port()
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
    )

    run_geth_command = (
        geth_binary,
        '--datadir', str(datadir),
        '--ipcpath', geth_ipc_path,
        '--nodiscover',
        '--fakepow',
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
    finally:
        kill_proc_gracefully(proc)
        output, errors = proc.communicate()
        print(
            "Geth Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                force_text(output),
                force_text(errors),
            )
        )


@pytest.fixture(scope="session")
def web3(geth_process, geth_ipc_path):
    wait_for_socket(geth_ipc_path)
    _web3 = Web3(Web3.IPCProvider(geth_ipc_path))
    return _web3


@pytest.fixture(scope='session')
def coinbase(web3):
    return web3.eth.coinbase


@pytest.fixture(scope="session")
def math_contract_deploy_txn_hash(geth_fixture_data):
    return geth_fixture_data['math_deploy_txn_hash']


@pytest.fixture(scope="session")
def math_contract(web3, math_contract_factory, geth_fixture_data):
    return math_contract_factory(address=geth_fixture_data['math_address'])


@pytest.fixture(scope="session")
def emitter_contract(web3, emitter_contract_factory, geth_fixture_data):
    return emitter_contract_factory(address=geth_fixture_data['emitter_address'])


@pytest.fixture
def unlocked_account(web3, unlockable_account, unlockable_account_pw):
    web3.personal.unlockAccount(unlockable_account, unlockable_account_pw)
    yield unlockable_account
    web3.personal.lockAccount(unlockable_account)


@pytest.fixture(scope='session')
def unlockable_account_pw(geth_fixture_data):
    return geth_fixture_data['keyfile_pw']


@pytest.fixture(scope="session")
def unlockable_account(web3, coinbase):
    yield coinbase


@pytest.fixture(scope="session")
def funded_account_for_raw_txn(geth_fixture_data):
    account = geth_fixture_data['raw_txn_account']
    assert is_checksum_address(account)
    return account


@pytest.fixture(scope="session")
def empty_block(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['empty_block_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def block_with_txn(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['block_with_txn_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def mined_txn_hash(geth_fixture_data):
    return geth_fixture_data['mined_txn_hash']


@pytest.fixture(scope="session")
def block_with_txn_with_log(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['block_hash_with_log'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def txn_hash_with_log(geth_fixture_data):
    return geth_fixture_data['txn_hash_with_log']


class TestGoEthereum(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Geth/')


class TestGoEthereumEthModule(EthModuleTest):
    pass


class TestGoEthereumVersionModule(VersionModuleTest):
    pass


class TestGoEthereumNetModule(NetModuleTest):
    pass


class TestGoEthereumPersonalModule(PersonalModuleTest):
    pass


#
# Geth Process Utils
#
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


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)
