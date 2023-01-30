import pytest

from eth_abi import (
    abi,
)

from web3._utils.contract_sources.contract_data.offchain_lookup import (
    OFFCHAIN_LOOKUP_DATA,
)
from web3._utils.module_testing.module_testing_utils import (
    mock_offchain_lookup_request_response,
)
from web3._utils.type_conversion import (
    to_hex_if_bytes,
)
from web3.exceptions import (
    OffchainLookup,
    TooManyRequests,
    Web3ValidationError,
)

# "test offchain lookup" as an abi-encoded string
OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA = "0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000001474657374206f6666636861696e206c6f6f6b7570000000000000000000000000"  # noqa: E501
# "web3py" as an abi-encoded string
WEB3PY_AS_HEXBYTES = "0x000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000067765623370790000000000000000000000000000000000000000000000000000"  # noqa: E501


@pytest.fixture
def offchain_lookup_contract_factory(w3):
    return w3.eth.contract(**OFFCHAIN_LOOKUP_DATA)


@pytest.fixture
def offchain_lookup_contract(
    w3,
    wait_for_block,
    offchain_lookup_contract_factory,
    wait_for_transaction,
    address_conversion_func,
):
    wait_for_block(w3)
    deploy_txn_hash = offchain_lookup_contract_factory.constructor().transact(
        {"gas": 10000000}
    )
    deploy_receipt = wait_for_transaction(w3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt["contractAddress"])

    bytecode = w3.eth.get_code(contract_address)
    assert bytecode == offchain_lookup_contract_factory.bytecode_runtime
    deployed_offchain_lookup = offchain_lookup_contract_factory(
        address=contract_address
    )
    assert deployed_offchain_lookup.address == contract_address
    return deployed_offchain_lookup


def test_offchain_lookup_functionality(
    offchain_lookup_contract,
    monkeypatch,
):
    normalized_address = to_hex_if_bytes(offchain_lookup_contract.address)
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_address}/{OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA}.json",  # noqa: E501
        mocked_json_data=WEB3PY_AS_HEXBYTES,
    )
    response = offchain_lookup_contract.caller.testOffchainLookup(
        OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
    )
    assert abi.decode(["string"], response)[0] == "web3py"


def test_eth_call_offchain_lookup_raises_when_ccip_read_is_disabled(
    w3, offchain_lookup_contract
):
    # test ContractFunction call
    with pytest.raises(OffchainLookup):
        offchain_lookup_contract.functions.testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        ).call(ccip_read_enabled=False)

    # test ContractCaller call
    with pytest.raises(OffchainLookup):
        offchain_lookup_contract.caller(ccip_read_enabled=False).testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        )

    # test global flag on the provider
    w3.provider.global_ccip_read_enabled = False

    with pytest.raises(OffchainLookup):
        offchain_lookup_contract.caller.testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        )

    with pytest.raises(OffchainLookup):
        offchain_lookup_contract.caller(ccip_read_enabled=False).testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        )

    w3.provider.global_ccip_read_enabled = True  # cleanup


def test_offchain_lookup_call_flag_overrides_provider_flag(
    w3,
    offchain_lookup_contract,
    monkeypatch,
):
    normalized_address = to_hex_if_bytes(offchain_lookup_contract.address)
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_address}/{OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA}.json",  # noqa: E501
        mocked_json_data=WEB3PY_AS_HEXBYTES,
    )

    w3.provider.global_ccip_read_enabled = False

    response = offchain_lookup_contract.functions.testOffchainLookup(
        OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
    ).call(ccip_read_enabled=True)
    assert abi.decode(["string"], response)[0] == "web3py"

    w3.provider.global_ccip_read_enabled = True


def test_offchain_lookup_raises_for_improperly_formatted_rest_request_response(
    offchain_lookup_contract,
    monkeypatch,
):
    normalized_address = to_hex_if_bytes(offchain_lookup_contract.address)
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_address}/{OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA}.json",  # noqa: E501
        mocked_json_data=WEB3PY_AS_HEXBYTES,
        json_data_field="not_data",
    )
    with pytest.raises(Web3ValidationError, match="missing 'data' field"):
        offchain_lookup_contract.caller.testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        )


@pytest.mark.parametrize("status_code_non_4xx_error", [100, 300, 500, 600])
def test_eth_call_offchain_lookup_tries_next_url_for_non_4xx_error_status_and_tests_POST(  # noqa: E501
    offchain_lookup_contract,
    monkeypatch,
    status_code_non_4xx_error,
) -> None:
    normalized_contract_address = to_hex_if_bytes(
        offchain_lookup_contract.address
    ).lower()

    # The next url in our test contract doesn't contain '{data}',
    # triggering the POST request logic. The idea here is to return
    # a bad status for the first url (GET) and a success status from the
    # second call (POST) to test both that we move on to the next url with
    # non 4xx status and that the POST logic is also working as expected.
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_contract_address}/{OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA}.json",  # noqa: E501
        mocked_status_code=status_code_non_4xx_error,
        mocked_json_data=WEB3PY_AS_HEXBYTES,
    )
    mock_offchain_lookup_request_response(
        monkeypatch,
        http_method="POST",
        mocked_request_url=f"https://web3.py/gateway/{normalized_contract_address}.json",  # noqa: E501
        mocked_status_code=200,
        mocked_json_data=WEB3PY_AS_HEXBYTES,
        sender=normalized_contract_address,
        calldata=OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA,
    )
    response = offchain_lookup_contract.caller.testOffchainLookup(
        OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
    )
    assert abi.decode(["string"], response)[0] == "web3py"


@pytest.mark.parametrize("status_code_4xx_error", [400, 410, 450, 499])
def test_eth_call_offchain_lookup_calls_raise_for_status_for_4xx_status_code(
    offchain_lookup_contract,
    monkeypatch,
    status_code_4xx_error,
) -> None:
    normalized_contract_address = to_hex_if_bytes(
        offchain_lookup_contract.address
    ).lower()
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_contract_address}/{OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA}.json",  # noqa: E501
        mocked_status_code=status_code_4xx_error,
        mocked_json_data=WEB3PY_AS_HEXBYTES,
    )
    with pytest.raises(Exception, match="called raise_for_status\\(\\)"):
        offchain_lookup_contract.caller.testOffchainLookup(
            OFFCHAIN_LOOKUP_CONTRACT_TEST_DATA
        )


def test_offchain_lookup_raises_on_continuous_redirect(
    offchain_lookup_contract,
    monkeypatch,
):
    normalized_address = to_hex_if_bytes(offchain_lookup_contract.address)
    mock_offchain_lookup_request_response(
        monkeypatch,
        mocked_request_url=f"https://web3.py/gateway/{normalized_address}/0x.json",
    )
    with pytest.raises(TooManyRequests, match="Too many CCIP read redirects"):
        offchain_lookup_contract.caller.continuousOffchainLookup()
