import json
import os
from pathlib import (
    Path,
)
import pytest
import subprocess
import zipfile

from eth_utils import (
    is_checksum_address,
    is_dict,
    to_text,
)

from web3._utils.contract_sources.contract_data.panic_errors_contract import (
    PANIC_ERRORS_CONTRACT_DATA,
)
from web3._utils.contract_sources.contract_data.storage_contract import (
    STORAGE_CONTRACT_DATA,
)

from .utils import (
    kill_proc_gracefully,
)

KEYFILE_PW = "web3py-test"

GETH_FIXTURE_ZIP = "geth-1.11.6-fixture.zip"


@pytest.fixture(scope="module")
def geth_binary():
    from geth.install import (
        get_executable_path,
        install_geth,
    )

    if "GETH_BINARY" in os.environ:
        return os.environ["GETH_BINARY"]
    elif "GETH_VERSION" in os.environ:
        geth_version = os.environ["GETH_VERSION"]
        _geth_binary = get_executable_path(geth_version)
        if not os.path.exists(_geth_binary):
            install_geth(geth_version)
        assert os.path.exists(_geth_binary)
        return _geth_binary
    else:
        return "geth"


def absolute_datadir(directory_name):
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            directory_name,
        )
    )


@pytest.fixture(scope="module")
def get_geth_version(geth_binary):
    from geth import (
        get_geth_version,
    )

    return get_geth_version(geth_executable=os.path.expanduser(geth_binary))


@pytest.fixture(scope="module")
def base_geth_command_arguments(geth_binary, datadir):
    return (
        geth_binary,
        "--datadir",
        str(datadir),
        "--nodiscover",
        "--fakepow",
    )


@pytest.fixture(scope="module")
def geth_zipfile_version(get_geth_version):
    if get_geth_version.major == 1 and get_geth_version.minor in [10, 11]:
        return GETH_FIXTURE_ZIP
    raise AssertionError("Unsupported geth version")


@pytest.fixture(scope="module")
def datadir(tmpdir_factory, geth_zipfile_version):
    zipfile_path = absolute_datadir(geth_zipfile_version)
    base_dir = tmpdir_factory.mktemp("goethereum")
    tmp_datadir = os.path.join(str(base_dir), "datadir")
    with zipfile.ZipFile(zipfile_path, "r") as zip_ref:
        zip_ref.extractall(tmp_datadir)
    return tmp_datadir


@pytest.fixture(scope="module")
def geth_fixture_data(datadir):
    config_file_path = Path(datadir) / "config.json"
    return json.loads(config_file_path.read_text())


@pytest.fixture(scope="module")
def genesis_file(datadir):
    genesis_file_path = os.path.join(datadir, "genesis.json")
    return genesis_file_path


@pytest.fixture(scope="module")
def geth_process(geth_binary, datadir, genesis_file, geth_command_arguments):
    init_datadir_command = (
        geth_binary,
        "--datadir",
        str(datadir),
        "init",
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
    )
    try:
        yield proc
    finally:
        kill_proc_gracefully(proc)
        output, errors = proc.communicate()
        print(
            "Geth Process Exited:\n"
            f"stdout:{to_text(output)}\n\n"
            f"stderr:{to_text(errors)}\n\n"
        )


@pytest.fixture(scope="module")
def coinbase(w3):
    return w3.eth.coinbase


@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(geth_fixture_data):
    return geth_fixture_data["math_deploy_txn_hash"]


@pytest.fixture(scope="module")
def math_contract(math_contract_factory, geth_fixture_data):
    return math_contract_factory(address=geth_fixture_data["math_address"])


@pytest.fixture(scope="module")
def math_contract_address(math_contract, address_conversion_func):
    return address_conversion_func(math_contract.address)


@pytest.fixture(scope="module")
def emitter_contract(emitter_contract_factory, geth_fixture_data):
    return emitter_contract_factory(address=geth_fixture_data["emitter_address"])


@pytest.fixture(scope="module")
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture(scope="module")
def unlocked_account(w3, unlockable_account, unlockable_account_pw):
    w3.geth.personal.unlock_account(unlockable_account, unlockable_account_pw)
    yield unlockable_account
    w3.geth.personal.lock_account(unlockable_account)


@pytest.fixture(scope="module")
def unlockable_account_pw(geth_fixture_data):
    return geth_fixture_data["keyfile_pw"]


@pytest.fixture(scope="module")
def unlockable_account(coinbase):
    yield coinbase


@pytest.fixture()
def unlockable_account_dual_type(unlockable_account, address_conversion_func):
    return address_conversion_func(unlockable_account)


@pytest.fixture
def unlocked_account_dual_type(w3, unlockable_account_dual_type, unlockable_account_pw):
    w3.geth.personal.unlock_account(unlockable_account_dual_type, unlockable_account_pw)
    yield unlockable_account_dual_type
    w3.geth.personal.lock_account(unlockable_account_dual_type)


@pytest.fixture(scope="module")
def funded_account_for_raw_txn(geth_fixture_data):
    account = geth_fixture_data["raw_txn_account"]
    assert is_checksum_address(account)
    return account


@pytest.fixture(scope="module")
def empty_block(w3, geth_fixture_data):
    block = w3.eth.get_block(geth_fixture_data["empty_block_hash"])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def block_with_txn(w3, geth_fixture_data):
    block = w3.eth.get_block(geth_fixture_data["block_with_txn_hash"])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(geth_fixture_data):
    return geth_fixture_data["mined_txn_hash"]


@pytest.fixture(scope="module")
def block_with_txn_with_log(w3, geth_fixture_data):
    block = w3.eth.get_block(geth_fixture_data["block_hash_with_log"])
    assert is_dict(block)
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(geth_fixture_data):
    return geth_fixture_data["txn_hash_with_log"]


@pytest.fixture(scope="module")
def block_hash_revert_no_msg(geth_fixture_data):
    return geth_fixture_data["block_hash_revert_no_msg"]


@pytest.fixture(scope="module")
def block_hash_revert_with_msg(geth_fixture_data):
    return geth_fixture_data["block_hash_revert_with_msg"]


@pytest.fixture(scope="module")
def revert_contract(revert_contract_factory, geth_fixture_data):
    return revert_contract_factory(address=geth_fixture_data["revert_address"])


@pytest.fixture(scope="module")
def offchain_lookup_contract(offchain_lookup_contract_factory, geth_fixture_data):
    return offchain_lookup_contract_factory(
        address=geth_fixture_data["offchain_lookup_address"]
    )


@pytest.fixture(scope="module")
def panic_errors_contract(
    w3,
    geth_fixture_data,
):
    contract_factory = w3.eth.contract(**PANIC_ERRORS_CONTRACT_DATA)
    return contract_factory(address=geth_fixture_data["panic_errors_contract_address"])


@pytest.fixture(scope="module")
def storage_contract(
    w3,
    geth_fixture_data,
):
    contract_factory = w3.eth.contract(**STORAGE_CONTRACT_DATA)
    return contract_factory(address=geth_fixture_data["storage_contract_address"])


# --- async --- #


@pytest.fixture(scope="module")
def async_offchain_lookup_contract(
    async_offchain_lookup_contract_factory, geth_fixture_data
):
    return async_offchain_lookup_contract_factory(
        address=geth_fixture_data["offchain_lookup_address"]
    )


@pytest.fixture(scope="module")
def async_panic_errors_contract(
    async_w3,
    geth_fixture_data,
):
    contract_factory = async_w3.eth.contract(**PANIC_ERRORS_CONTRACT_DATA)
    return contract_factory(address=geth_fixture_data["panic_errors_contract_address"])


@pytest.fixture(scope="module")
def async_storage_contract(
    async_w3,
    geth_fixture_data,
):
    contract_factory = async_w3.eth.contract(**STORAGE_CONTRACT_DATA)
    return contract_factory(address=geth_fixture_data["storage_contract_address"])
