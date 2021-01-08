import os
import pytest
import tempfile
import zipfile

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


PARITY_2_5_13_FIXTURE = {
    'zip': 'parity-2.5.13-fixture.zip',
    'coinbase': 'dc544d1aa88ff8bbd2f2aec754b1f1e99e1812fd',
    'block_hash_revert_no_msg': '0x0496eca70b312db0d7b14753f5545e48f43ad70e8a2dd4fa5dc6c6409448c394',  # noqa: E501
    'block_hash_revert_with_msg': '0xf117005506c338177df21519008e3805cb718c2cad5f4a4c07754bf59bfd996c',  # noqa: E501
    'block_hash_with_log': '0xeb1cd5061f8e8c0a1a3b75dd48600fa126b6c0e753406276f2a6a544f1e41ec1',
    'block_with_txn_hash': '0xabf9142af100741620657e5a9a46e788c776303ca4986478f892384b83d8761c',
    'emitter_address': '0x4aA591a07989b4F810E2F5cE97e769D60710f168',
    'emitter_deploy_txn_hash': '0xef44cd36d86c41640c710026acf45f3b63731f72ac2a1744a005f6690bfa7613',
    'empty_block_hash': '0x63b0e0f16340e65662948cde20ba93c96ae311997db672b0101357f15b071fe5',
    'keyfile_pw': 'web3py-test',
    'math_address': '0xd794C821fCCFF5D96F5Db44af7e29977630A9dc2',
    'math_deploy_txn_hash': '0x356278504f40db914545888674cedc0d8ccd4a939665eb4ab83b569db0c477cb',
    'mined_txn_hash': '0x86fbfe56cce542ff0a2a2716c31675a0c9c43701725c4a751d20ee2ddf8a733d',
    'raw_txn_account': '0x39EEed73fb1D3855E90Cbd42f348b3D7b340aAA6',
    'revert_address': '0x14F3674571D76Bf66cA8EBD84dC02060933400b4',
    'txn_hash_with_log': '0x1407ae0fbc79622e60c21b59b0cb047a5f8d0219ad95969096c8c0e23f342f5c'}


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
    return PARITY_2_5_13_FIXTURE


@pytest.fixture(scope='module')
def datadir(tmpdir_factory, parity_fixture_data):
    zipfile_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        parity_fixture_data['zip'],
    ))
    base_dir = tmpdir_factory.mktemp('parity')
    tmp_datadir = os.path.join(str(base_dir), 'datadir')
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(tmp_datadir)
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
    block = web3.eth.get_block(parity_fixture_data['empty_block_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def block_with_txn(web3, parity_fixture_data):
    block = web3.eth.get_block(parity_fixture_data['block_with_txn_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(parity_fixture_data):
    return parity_fixture_data['mined_txn_hash']


@pytest.fixture(scope="module")
def block_with_txn_with_log(web3, parity_fixture_data):
    block = web3.eth.get_block(parity_fixture_data['block_hash_with_log'])
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


@pytest.fixture(scope="module")
def block_hash_revert_no_msg(parity_fixture_data):
    return parity_fixture_data['block_hash_revert_no_msg']


@pytest.fixture(scope="module")
def block_hash_revert_with_msg(parity_fixture_data):
    return parity_fixture_data['block_hash_revert_with_msg']


@pytest.fixture(scope="module")
def revert_contract(revert_contract_factory, parity_fixture_data):
    return revert_contract_factory(address=parity_fixture_data['revert_address'])
