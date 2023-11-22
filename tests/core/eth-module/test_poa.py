import pytest

from web3.exceptions import (
    BlockNotFound,
    ExtraDataLengthError,
)
from web3.middleware import (
    extradata_to_poa_middleware,
)


# In the spec, a block with extra data longer than 32 bytes is invalid
def test_long_extra_data(w3, request_mocker):
    with request_mocker(
        w3, mock_results={"eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33}}
    ):
        with pytest.raises(ExtraDataLengthError):
            w3.eth.get_block("latest")


def test_full_extra_data(w3, request_mocker):
    with request_mocker(
        w3, mock_results={"eth_getBlockByNumber": {"extraData": "0x" + "ff" * 32}}
    ):
        block = w3.eth.get_block("latest")
        assert block.extraData == b"\xff" * 32


def test_geth_proof_of_authority(w3, request_mocker):
    w3.middleware_onion.inject(extradata_to_poa_middleware, layer=0)

    with request_mocker(
        w3,
        mock_results={
            "eth_getBlockByNumber": {"extraData": "0x" + "ff" * 33},
        },
    ):
        block = w3.eth.get_block("latest")
        assert "extraData" not in block
        assert block.proofOfAuthorityData == b"\xff" * 33


def test_returns_none_response(w3, request_mocker):
    with request_mocker(w3, mock_results={"eth_getBlockByNumber": None}):
        with pytest.raises(BlockNotFound):
            w3.eth.get_block("latest")
