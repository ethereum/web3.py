import pytest
from unittest.mock import patch
from web3 import Web3
from web3.manager import RequestManager
from web3.exceptions import Web3ValueError


def test_formatted_response_with_missing_trie_node_exception():
    # Simulated error response mimicking what might come from an RPC call
    error_response = {
        "jsonrpc": "2.0",
        "id": 1,
        "error": {
            "code": -32000,
            "message": "missing trie node 7a8d16362e6dbe9cd83ec5c1b865f687e66aaa704eb7e2fdc823518a650174af"
        }
    }

    # Initialize a RequestManager instance
    web3_instance = Web3()
    manager = RequestManager(w3=web3_instance)

    # Mock _make_request to return the error response
    with patch.object(RequestManager, '_make_request', return_value=error_response):
        # Verify that calling request_blocking raises a Web3ValueError due to the error in the response
        with pytest.raises(Web3ValueError) as exc_info:
            manager.request_blocking("eth_getBalance", ["0x0", "latest"])

        # Check that the exception message contains the expected error message and Web3ValueError type
        assert "missing trie node" in str(exc_info.value)
        assert exc_info.type == Web3ValueError
