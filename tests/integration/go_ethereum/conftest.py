import json
import os
import pytest
import shutil
import subprocess

from eth_utils import (
    is_checksum_address,
    is_dict,
    to_text,
)

from web3.utils.toolz import (
    assoc,
)

from .utils import (
    kill_proc_gracefully,
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
GETH_181_DIRECTORY_NAME = 'geth-1.8.1-datadir-fixture'


@pytest.fixture(scope='module')
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


def absolute_datadir(directory_name):
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..',
        directory_name,
    ))


def load_fixture_data(fixture_path):
    fixture_path = absolute_datadir(fixture_path)
    config_path = os.path.join(fixture_path, 'config.json')
    with open(config_path) as config_file:
        loaded_data = json.loads(config_file.read())
        return assoc(loaded_data, 'datadir', fixture_path)


@pytest.fixture(scope="module")
def geth_fixture_data(geth_binary):
    from geth import get_geth_version
    version = get_geth_version(geth_executable=os.path.expanduser(geth_binary))
    if version.major == 1:
        if version.minor == 6:
            return GETH_16_FIXTURE
        elif version.minor == 7:
            return GETH_17_FIXTURE
        elif version.minor == 8:
            return load_fixture_data(GETH_181_DIRECTORY_NAME)
    assert False, "Unsupported geth version"


@pytest.fixture(scope='module')
def datadir(tmpdir_factory, geth_fixture_data):
    fixture_datadir = absolute_datadir(geth_fixture_data['datadir'])
    base_dir = tmpdir_factory.mktemp('goethereum')
    tmp_datadir = os.path.join(str(base_dir), 'datadir')
    shutil.copytree(fixture_datadir, tmp_datadir)
    return tmp_datadir


@pytest.fixture(scope='module')
def genesis_file(datadir):
    genesis_file_path = os.path.join(datadir, 'genesis.json')
    return genesis_file_path


@pytest.fixture(scope='module')
def geth_process(geth_binary, datadir, genesis_file, geth_command_arguments):
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
    proc = subprocess.Popen(
        geth_command_arguments,
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
                to_text(output),
                to_text(errors),
            )
        )


@pytest.fixture(scope='module')
def coinbase(web3):
    return web3.eth.coinbase


@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(geth_fixture_data):
    return geth_fixture_data['math_deploy_txn_hash']


@pytest.fixture(scope="module")
def math_contract(web3, math_contract_factory, geth_fixture_data):
    return math_contract_factory(address=geth_fixture_data['math_address'])


@pytest.fixture(scope="module")
def math_contract_address(math_contract, address_conversion_func):
    return address_conversion_func(math_contract.address)


@pytest.fixture(scope="module")
def emitter_contract(web3, emitter_contract_factory, geth_fixture_data):
    return emitter_contract_factory(address=geth_fixture_data['emitter_address'])


@pytest.fixture(scope="module")
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture
def unlocked_account(web3, unlockable_account, unlockable_account_pw):
    web3.personal.unlockAccount(unlockable_account, unlockable_account_pw)
    yield unlockable_account
    web3.personal.lockAccount(unlockable_account)


@pytest.fixture(scope='module')
def unlockable_account_pw(geth_fixture_data):
    return geth_fixture_data['keyfile_pw']


@pytest.fixture(scope="module")
def unlockable_account(web3, coinbase):
    yield coinbase


@pytest.fixture()
def unlockable_account_dual_type(unlockable_account, address_conversion_func):
    return address_conversion_func(unlockable_account)


@pytest.yield_fixture
def unlocked_account_dual_type(web3, unlockable_account_dual_type, unlockable_account_pw):
    web3.personal.unlockAccount(unlockable_account_dual_type, unlockable_account_pw)
    yield unlockable_account_dual_type
    web3.personal.lockAccount(unlockable_account_dual_type)


@pytest.fixture(scope="module")
def funded_account_for_raw_txn(geth_fixture_data):
    account = geth_fixture_data['raw_txn_account']
    assert is_checksum_address(account)
    return account


@pytest.fixture(scope="module")
def empty_block(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['empty_block_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def block_with_txn(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['block_with_txn_hash'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(geth_fixture_data):
    return geth_fixture_data['mined_txn_hash']


@pytest.fixture(scope="module")
def block_with_txn_with_log(web3, geth_fixture_data):
    block = web3.eth.getBlock(geth_fixture_data['block_hash_with_log'])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(geth_fixture_data):
    return geth_fixture_data['txn_hash_with_log']
