import os
import pytest
import shutil
import tempfile

from eth_utils import (
    is_checksum_address,
    is_dict,
)

from .install_parity import (
    get_executable_path,
    install_parity,
)
from .utils import (
    get_process,
)

KEYFILE_PW = 'web3py-test'


PARITY_2_3_5_FIXTURE = {
    'datadir': 'parity-235-fixture',
    'coinbase': 'dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd',
    'block_hash_with_log': '0x8633d4b5497e5a7e81356cbe3f0a49b63fb2020ddeb6c8c27bcecec541055a3b',
    'block_with_txn_hash': '0xf474a7b80cb6cb2b728b290ce6a0893f5f85d2998c4b252d73300da56de205de',
    'emitter_address': '0x4aA591a07989b4F810E2F5cE97e769D60710f168',
    'emitter_deploy_txn_hash': '0xa3e3838c01e73dafc7fc9d7e4e6c97523445006ae125ad1085abcf065feed382',
    'empty_block_hash': '0xc46c025ae50a970408a429a5a2baa65f056a173ff1dae0cab4b490d2ee94413f',
    'keyfile_pw': 'web3py-test',
    'math_address': '0xd794C821fCCFF5D96F5Db44af7e29977630A9dc2',
    'math_deploy_txn_hash': '0xb680f86c00d69484ce68b4d3932c27c4e858c91d6ba8a27f8c499006fe4ced4a',
    'mined_txn_hash': '0x6401f455c01f9eb79fa672a4d24cc7cbbe3891e89eea8db8be39969dc9c480bc',
    'raw_txn_account': '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6',
    'txn_hash_with_log': '0xf6ffb7387cd0288cd1db1b1e368e7d4a21bc6e70fd2ef0e9af41f6c32b9e2cc7'
}


@pytest.fixture(scope='module')
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


@pytest.fixture(scope="module")
def parity_fixture_data(parity_binary):
    return PARITY_2_3_5_FIXTURE


@pytest.fixture(scope='module')
def datadir(tmpdir_factory, parity_fixture_data):
    fixture_datadir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        parity_fixture_data['datadir'],
    ))
    base_dir = tmpdir_factory.mktemp('parity')
    tmp_datadir = os.path.join(str(base_dir), 'datadir')
    shutil.copytree(fixture_datadir, tmp_datadir)
    return tmp_datadir


@pytest.fixture(scope="module")
def author(parity_fixture_data):
    # need the address to unlock before web3 module has been opened
    author = parity_fixture_data['coinbase']
    return author


@pytest.fixture(scope="module")
def passwordfile():
    password_dir = tempfile.mkdtemp()
    password_path = os.path.join(password_dir, 'password')
    with open(password_path, 'w') as f:
        f.write(KEYFILE_PW)

    yield password_path

    if os.path.exists(password_path):
        os.remove(password_path)


@pytest.fixture(scope="module")
def parity_process(parity_command_arguments):
    yield from get_process(parity_command_arguments)


@pytest.fixture(scope="module")
def parity_import_blocks_process(parity_import_blocks_command):
    yield from get_process(parity_import_blocks_command, terminates=True)


@pytest.fixture(scope='module')
def coinbase(web3):
    return web3.eth.coinbase


@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(parity_fixture_data):
    return parity_fixture_data['math_deploy_txn_hash']


@pytest.fixture(scope="module")
def math_contract(web3, math_contract_factory, parity_fixture_data):
    return math_contract_factory(address=parity_fixture_data['math_address'])


@pytest.fixture()
def math_contract_address(math_contract, address_conversion_func):
    return address_conversion_func(math_contract.address)


@pytest.fixture(scope="module")
def emitter_contract(web3, emitter_contract_factory, parity_fixture_data):
    return emitter_contract_factory(address=parity_fixture_data['emitter_address'])


@pytest.fixture()
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture(scope="module")
def unlocked_account(web3, unlockable_account, unlockable_account_pw):
    yield unlockable_account


@pytest.fixture(scope='module')
def unlockable_account_pw(parity_fixture_data):
    return parity_fixture_data['keyfile_pw']


@pytest.fixture(scope="module")
def unlockable_account(web3, coinbase):
    yield coinbase


@pytest.fixture()
def unlockable_account_dual_type(unlockable_account, address_conversion_func):
    return address_conversion_func(unlockable_account)


@pytest.fixture
def unlocked_account_dual_type(unlockable_account_dual_type):
    return unlockable_account_dual_type


@pytest.fixture(scope="module")
def funded_account_for_raw_txn(parity_fixture_data):
    account = parity_fixture_data['raw_txn_account']
    assert is_checksum_address(account)
    return account


@pytest.fixture(scope="module")
def empty_block(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['empty_block_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def block_with_txn(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['block_with_txn_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(parity_fixture_data):
    return parity_fixture_data['mined_txn_hash']


@pytest.fixture(scope="module")
def block_with_txn_with_log(web3, parity_fixture_data):
    block = web3.eth.getBlock(parity_fixture_data['block_hash_with_log'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(parity_fixture_data):
    return parity_fixture_data['txn_hash_with_log']


@pytest.fixture(scope="module")
def txn_filter_params(coinbase):
    return {
        "fromBlock": "earliest",
        "toBlock": "latest",
        "fromAddress": [coinbase],
    }
