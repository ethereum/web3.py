from unittest.mock import patch
import pytest
from web3 import Web3
from web3._utils.contract_sources.contract_data.contract_logic_error_tester import (
    MEAS_PUB_DATA,
)
from web3.exceptions import ContractLogicError


@pytest.fixture
def web3_instance():
    return Web3(Web3.EthereumTesterProvider())


def test_get_subscriber_count_with_invalid_address(web3_instance):
    invalid_contract_address = "0x0000000000000000000000000000000000000000"
    contract_instance = web3_instance.eth.contract(
        address=invalid_contract_address, abi=MEAS_PUB_DATA["abi"]
    )

    # Mock the responses for eth_call and get_code
    with patch.object(web3_instance.eth, "call", return_value=b""):
        with patch.object(web3_instance.eth, "get_code", return_value=""):
            # Expect the ContractLogicError due to the mocked conditions
            with pytest.raises(ContractLogicError):
                contract_instance.functions.getSubscriberCount().call()
