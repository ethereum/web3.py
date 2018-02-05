import json
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

from install_parity import (
    get_executable_path,
    install_parity,
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

PARITY_FIXTURE = {
    'datadir': 'parity-187-fixture',
    'block_hash_with_log': '0x342e12ab6d24d7fb1d774a6b47cd2cc04430a3295bee5662d5a1a0b766480031',
    'block_with_txn_hash': '0xa866266a5a348948c38855cc6e990093b35a3d2c43fdddfe3b1259c9c3fc7404',
    'emitter_address': '0x4aA591a07989b4F810E2F5cE97e769D60710f168',
    'emitter_deploy_txn_hash': '0xa81e903e9953758c8da5aaae66451ff909edd7bd6aefc3ebeab1e709e3229bcc',
    'empty_block_hash': '0xbcb2826e4376c23e66750607af72965f177f93b39e5024be259e6b0ff4f95e9d',
    'keyfile_pw': 'web3py-test',
    'math_address': '0xd794C821fCCFF5D96F5Db44af7e29977630A9dc2',
    'math_deploy_txn_hash': '0x03cc47c8f58608576187825aed01c4fc64786f1172d182d432336881a75a0fa3',
    'mined_txn_hash': '0x9839fde5fce7f0ed29b49a687d4f7630076069e65c2e1df87ffab9b2844d3899',
    'raw_txn_account': '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6',
    'txn_hash_with_log': '0x26bad3318b3466833f96d04ac9ba46fbbce11c15be2f83c9fe0b5dc15b2646cd'
}


@pytest.fixture(scope='session')
def parity_binary():
    if 'PARITY_BINARY' in os.environ:
        return os.environ['PARITY_BINARY']
    elif 'PARITY_VERSION' in os.environ:
        parity_version = os.environ['PARITY_VERSION']
        _parity_binary = get_executable_path(parity_version)
        if not os.path.exists(_parity_binary):
            install_parity(parity_version)
        assert os.path.exists(_parity_binary)
        return _parity_binary
    else:
        return 'parity'


def get_parity_version(parity_binary):
    pass


@pytest.fixture(scope="session")
def parity_fixture_data(parity_binary):
    return PARITY_FIXTURE


@pytest.fixture(scope='session')
def datadir(tmpdir_factory, parity_fixture_data):
    fixture_datadir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        parity_fixture_data['datadir'],
    ))
    base_dir = tmpdir_factory.mktemp('parity')
    tmp_datadir = os.path.join(str(base_dir), 'datadir')
    shutil.copytree(fixture_datadir, tmp_datadir)
    return tmp_datadir


@pytest.fixture(scope="session")
def accounts(datadir):
    # need the address to unlock before web3 session has been opened
    chain_config_path = os.path.join(datadir, "chain_config.json")
    with open(chain_config_path, 'r') as f:
        chain_config = json.load(f)
    accounts = chain_config['accounts'].keys()
    return accounts


@pytest.fixture(scope='session')
def ipc_path(datadir):
    ipc_dir_path = tempfile.mkdtemp()
    _ipc_path = os.path.join(ipc_dir_path, 'jsonrpc.ipc')
    yield _ipc_path

    if os.path.exists(_ipc_path):
        os.remove(_ipc_path)


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
def passwordfile():
    password_dir = tempfile.mkdtemp()
    password_path = os.path.join(password_dir, 'password')
    with open(password_path, 'w') as f:
        f.write(KEYFILE_PW)

    yield password_path

    if os.path.exists(password_path):
        os.remove(password_path)


@pytest.fixture(scope="session")
def parity_process(
        parity_import_blocks_process,
        parity_binary,
        ipc_path, datadir,
        passwordfile,
        accounts):
    coinbase = list(accounts)[0]

    run_parity_command = (
        parity_binary,
        '--chain', os.path.join(datadir, 'chain_config.json'),
        '--ipc-path', ipc_path,
        '--base-path', str(datadir),
        '--unlock', coinbase,
        '--password', str(passwordfile),
    )
    proc = subprocess.Popen(
        run_parity_command,
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
            "Parity Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                force_text(output),
                force_text(errors),
            )
        )


@pytest.fixture(scope="session")
def parity_import_blocks_process(parity_binary, ipc_path, datadir, passwordfile, accounts):
    coinbase = list(accounts)[0]

    run_parity_command = (
        parity_binary,
        'import', os.path.join(datadir, 'blocks_export.rlp'),
        '--chain', os.path.join(datadir, 'chain_config.json'),
        '--ipc-path', ipc_path,
        '--base-path', str(datadir),
        '--unlock', coinbase,
        '--password', str(passwordfile),
    )
    proc = subprocess.Popen(
        run_parity_command,
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
            "Parity Process Exited:\n"
            "stdout:{0}\n\n"
            "stderr:{1}\n\n".format(
                force_text(output),
                force_text(errors),
            )
        )


@pytest.fixture(scope="session")
def web3(parity_process, ipc_path):
    wait_for_socket(ipc_path)
    _web3 = Web3(Web3.IPCProvider(ipc_path))
    return _web3


@pytest.fixture(scope='session')
def coinbase(web3):
    return web3.eth.coinbase


@pytest.fixture(scope="session")
def math_contract_deploy_txn_hash(parity_fixture_data):
    return parity_fixture_data['math_deploy_txn_hash']


@pytest.fixture(scope="session")
def math_contract(web3, math_contract_factory, parity_fixture_data):
    return math_contract_factory(address=parity_fixture_data['math_address'])


@pytest.fixture(scope="session")
def emitter_contract(web3, emitter_contract_factory, parity_fixture_data):
    return emitter_contract_factory(address=parity_fixture_data['emitter_address'])


@pytest.fixture
def unlocked_account(web3, unlockable_account, unlockable_account_pw):
    yield unlockable_account


@pytest.fixture(scope='session')
def unlockable_account_pw(parity_fixture_data):
    return parity_fixture_data['keyfile_pw']


@pytest.fixture(scope="session")
def unlockable_account(web3, coinbase):
    yield coinbase


@pytest.fixture(scope="session")
def funded_account_for_raw_txn(parity_fixture_data):
    account = parity_fixture_data['raw_txn_account']
    assert is_checksum_address(account)
    return account


@pytest.fixture(scope="session")
def empty_block(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['empty_block_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def block_with_txn(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['block_with_txn_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def mined_txn_hash(parity_fixture_data):
    return parity_fixture_data['mined_txn_hash']


@pytest.fixture(scope="session")
def block_with_txn_with_log(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['block_hash_with_log'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="session")
def txn_hash_with_log(parity_fixture_data):
    return parity_fixture_data['txn_hash_with_log']


class TestParity(Web3ModuleTest):
    def _check_web3_clientVersion(self, client_version):
        assert client_version.startswith('Parity/')


class TestParityEthModule(EthModuleTest):
    def test_eth_uninstallFilter(self, web3):
        pytest.xfail('eth_uninstallFilter calls to parity always return true')
        super().test_eth_uninstallFilter(web3)

    def test_eth_newBlockFilter(self, web3):
        pytest.xfail('Parity returns latest block on first polling for new blocks')
        super().test_eth_newBlockFilter(web3)


class TestParityVersionModule(VersionModuleTest):
    pass


class TestParityNetModule(NetModuleTest):
    pass


class TestParityPersonalModule(PersonalModuleTest):
    def test_personal_importRawKey(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_importRawKey(web3)

    def test_personal_listAccounts(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_listAccounts(web3)

    def test_personal_lockAccount(self, web3, unlocked_account):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_lockAccount(web3, unlocked_account)

    def test_personal_unlockAccount_success(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_unlockAccount_success(web3)

    def test_personal_unlockAccount_failure(self, web3, unlockable_account):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_unlockAccount_failure(web3, unlockable_account)

    def test_personal_newAccount(self, web3):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_newAccount(web3)

    def test_personal_sendTransaction(
            self,
            web3,
            unlockable_account,
            unlockable_account_pw):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_sendTransaction(
            web3,
            unlockable_account,
            unlockable_account_pw)

    def test_personal_sign_and_ecrecover(
            self,
            web3,
            unlockable_account,
            unlockable_account_pw):
        pytest.xfail('this non-standard json-rpc method is not implemented on parity')
        super().test_personal_sign_and_ecrecover(
            web3,
            unlockable_account,
            unlockable_account_pw)


#
# Parity Process Utils
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
