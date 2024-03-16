import pytest

from aiohttp import (
    ClientSession,
)
import requests

from ens.utils import (
    ens_encode_name,
)
from web3.exceptions import (
    OffchainLookup,
    Web3ValidationError,
)

# the encoded calldata for the initiating ``addr(namehash(name))`` call
ENCODED_ADDR_CALLDATA = "0x3b3b57de42041b0018edd29d7c17154b0c671acc0502ea0b3693cafbeadf58e6beaaa16c"  # noqa: E501

# This is one of the actual returned payloads from the GET request that
# is triggered when resolving ``ns.address('offchainexample.eth')``
# on mainnet. Since we got rid of the time expiration constraint for our
# OffchainResolver.sol, this hash ends up working for our local test
# case as well since the signer is able to be recovered.
OFFCHAIN_RESOLVER_DATA = (
    "0x0000000000000000000000000000000000000000000000000000000000000060"
    "000000000000000000000000000000000000000000000000000000006271abd2"
    "00000000000000000000000000000000000000000000000000000000000000a0"
    "0000000000000000000000000000000000000000000000000000000000000020"
    "000000000000000000000000d8da6bf26964af9d7eed9e03e53415d37aa96045"
    "0000000000000000000000000000000000000000000000000000000000000040"
    "1774ff038dbf6d7a5e5924c00d739f507c7d3ca6bf6c99abaf7d2f0042f00b75"
    "e30fdda27b9291dc035b38114d08495ca5d70f3c859facaa23b06c39b6757034"
)

EXPECTED_GET_URL = (
    "https://web3.py/gateway/0x05ca7c4bc9886f11ae031d5c397a8b4827b4a4fd/0x9061b923000"
    "00000000000000000000000000000000000000000000000000000000000400000000000000000000"
    "00000000000000000000000000000000000000000008000000000000000000000000000000000000"
    "000000000000000000000000000150f6f6666636861696e6578616d706c650365746800000000000"
    "000000000000000000000000000000000000000000000000000000000000000000000000000243b3"
    "b57de42041b0018edd29d7c17154b0c671acc0502ea0b3693cafbeadf58e6beaaa16c00000000000"
    "000000000000000000000000000000000000000000000.json"
)
EXPECTED_POST_URL = (
    "https://web3.py/gateway/0x05ca7c4bc9886f11ae031d5c397a8b4827b4a4fd.json"
)
EXPECTED_RESOLVED_ADDRESS = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

EXPECTED_DOT_COM_POST_URL = "https://dnssec-oracle.ens.domains/"
EXPECTED_DOT_COM_RESOLVED_ADDRESS = "0x179A862703a4adfb29896552DF9e307980D19285"
DOTCOM_RESOLVER_DATA = "0x0000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000480000000000000000000000000000000000000000000000000000000000000066000000000000000000000000000000000000000000000000000000000000007e000000000000000000000000000000000000000000000000000000000000009000000000000000000000000000000000000000000000000000000000000000aa0000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000002a00000000000000000000000000000000000000000000000000000000000000239003008000002a3006609f90065ee49804f660000003000010002a30001080100030803010001e9ed09c2049dd2e1d9048afa91c5abf3e4282c22a31b7be5deea34e52e4cf328d0572d7bf35bc033dba1cbdb67f78d6f9455ff141d6a968901243fa032ecab30f41f5f8990736eb8a73624bb69331838825484e029d15d3d829c54d6e48c0e4442fecdea991f2ebc397cb99e05b92802db7af458460feadaa15ecd1b42490d249e6c8fc2016c8215582cac22d75ea8c70114e7267a5bb9e958cc6de59f90b3c7623cd5ab4b96972e026dad6506208b857ee6705d8ce21913ffcf7a3511f328f73654d7d28ba299282d75fb2ecfdd8825dd4847495d3b4503cc34fce290be2b8979b7cab1ca049424ecc2e915675557e606da144a36c5684727d528eb7c18693900003000010002a30001080101030803010001acffb409bcc939f831f7a1e5ec88f7a59255ec53040be432027390a4ce896d6f9086f3c5e177fbfe118163aaec7af1462c47945944c4e2c026be5e98bbcded25978272e1e3e079c5094d573f0e83c92f02b32d3513b1550b826929c80dd0f92cac966d17769fd5867b647c3f38029abdc48152eb8f207159ecc5d232c7c1537c79f4b7ac28ff11682f21681bf6d6aba555032bf6f9f036beb2aaa5b3778d6eebfba6bf9ea191be4ab0caea759e2f773a1f9029c73ecb8d5735b9321db085f1b8e2d8038fe2941992548cee0d67dd4547e11dd63af9c9fc1c5466fb684cf009d7197c2cf79e792ab501e6a8a1ca519af2cb9b5f6367e94c0d47502451357be1b50000000000000000000000000000000000000000000000000000000000000000000000000001001a41c0c07b7da3063c8d978b433a6b2f60ae7a5573facdbeb7fe6903960a3e13195924d72b08961a2f79d9d0628036caa99437e57324b6a28e1316a5e077e3cfe6132ce45be4de06afa5af7c4b36087aafe61eb1ac2e88ddcc8583dc92d4a0bc421aea6dae1f9d98ca191a5178befc48951d5e55deb80f4af575ced4f0e8f4625ec602cd4339c0d1f8801f289488f6f4618589260f8da8661c1f715bbc404db5819c5c196d4ea8bee0a21ff155d131670273132c92f522e3eb6f5a2fa457374b9da8b1b77dbb51d3331a6723c0edb81541b7d53fd7af72c5572266b67bab4947a2a19c682518b5ccf78af9ac264769236d1c3c5619056e350d9d68270fb2c7bf000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000046002b08010001518066064ad065f5194078b70003636f6d00002b00010001518000244d060d028acbb0cd28f41250a80a491389424d341522d946b0da0c0291f2d3d771d7805a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001009c431f354f8e22e891dcbf9a948ffba2bd10249b52d6c635a3c4110e28a401184a5dd21787580764296b645a6237a9e85b231561addd899f6b3af6bef247d838d41c99f283facfbd21f79d6b5afec4eed925144c8f48e88abc6f3d23fe19e2a1dca7dcd90b8c17e1bf2dd865fe7a63075dd0d03156a1d19dcb5ed4f57ec6363cd21d5de20fa777a1401132adbfc53b036f8d6b7c151b4fdb7f96419a86b022c490ab66b277217f87cdd52e24ce48021a2e2a2bbfbdae67caac2656e9ef73a99261d2d07b32449da123b0d7420863c7f5bda64ee2daf13459c767e7a7f1378f36d95483d2a7610d82ef75c935b3549b374717af924a549b3b3d27d51f320f9bec0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000012000000000000000000000000000000000000000000000000000000000000000bd00300d010001518065feef0b65eb275f4d0603636f6d0003636f6d00003000010001518000440100030de62f6a8c98321fef4c073ed53b6ebdfecacb401ff1451965c94a15abca0b059b213dee021b30d21469d700cdcbfd03f307d50ba49baecbb8dcc66059e446e8ec03636f6d00003000010001518000440101030db71f0465101ddbe2bf0c9455d12fa16c1cda44f4bf1ba2553418ad1f3aa9b06973f21b84eb532cf4035ee8d4832ca26d89306a7d32560c0cb0129d450ac1083500000000000000000000000000000000000000000000000000000000000000000000405bede0e12b60be8086c645ed93778fe32a83e6530d5dc6d66f2b0f04d38feae53a39e6db007170fab736d1387a2ea86e4416f3795f9a1ab74101fdbe9e0fc23d000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000054002b0d020001518065fbd30f65f2882711b603636f6d000967726567736b72696c03636f6d00002b000100015180002409430d0276d0bcaf81bcb9e06ce1a172cd849fb5806258dbff8b6f079b085f6bda6f193d000000000000000000000000000000000000000000000000000000000000000000000000000000000000004025dad1167a8f9d32c5f9929ac92afbd9c310ca946deb135bf4755b0b04e154ab10a808cb8d09cfcc15cd58fe8ed5ffbc42db1da12615f2e027f59bc3553fa0450000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000014000000000000000000000000000000000000000000000000000000000000000db00300d0200000e10662bace565db416509430967726567736b72696c03636f6d000967726567736b72696c03636f6d000030000100000e1000440100030da09311112cf9138818cd2feae970ebbd4d6a30f6088c25b325a39abbc5cd1197aa098283e5aaf421177c2aa5d714992a9957d1bcc18f98cd71f1f1806b65e1480967726567736b72696c03636f6d000030000100000e1000440101030d99db2cc14cabdc33d6d77da63a2f15f71112584f234e8d1dc428e39e8a4a97e1aa271a555dc90701e17e2a4c4b6f120b7c32d44f4ac02bd894cf2d4be7778a19000000000000000000000000000000000000000000000000000000000000000000000000405329d06a5f0662a5d941e50d4c6485db67726439397af6da9522c8f099a3f0611afbe4cfa4ba34c0687f91dd004ccd020e7b534d6341a0543292a391dbc1fb3800000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000000000000000000000000000000000180000000000000000000000000000000000000000000000000000000000000011500100d020000012c65f6d5d765f416b786c90967726567736b72696c03636f6d000967726567736b72696c03636f6d00001000010000012c002423763d7370663120696e636c7564653a5f7370662e676f6f676c652e636f6d202d616c6c0967726567736b72696c03636f6d00001000010000012c00403f454e533120646e736e616d652e656e732e657468203078313739413836323730336134616466623239383936353532444639653330373938304431393238350967726567736b72696c03636f6d00001000010000012c004544676f6f676c652d736974652d766572696669636174696f6e3d4845644f62304f5a647a547171795a585878435f5f4b7751434e7a4f545f6461737857766f72364e46686700000000000000000000000000000000000000000000000000000000000000000000000000000000000040518f547429c1ea5c7dac1c9027ef0cd9a579567b6403c772d89e73b0ea995a3d70ea36c908e3984cb3ef1fcf39d29259f38844e00d19cd0377828cfb90c78874"


class MockHttpSuccessResponse:
    status_code = 200

    def __init__(self, request_type, *args, **_kwargs):
        # validate the expected urls
        if request_type == "get":
            assert args[1] == EXPECTED_GET_URL
        elif request_type == "post":
            assert args[1] == EXPECTED_POST_URL

    @staticmethod
    def raise_for_status():
        pass  # noqa: E704

    @staticmethod
    def json():
        return {"data": OFFCHAIN_RESOLVER_DATA}  # noqa: E704


class MockHttpBadFormatResponse:
    status_code = 200

    def __init__(self, *args):
        assert args[1] == EXPECTED_GET_URL

    @staticmethod
    def raise_for_status():
        pass  # noqa: E704

    @staticmethod
    def json():
        return {"not_data": OFFCHAIN_RESOLVER_DATA}  # noqa: E704


class MockDotcomResolverSuccessResponse:
    status_code = 200

    def __init__(self, request_type, *args, **_kwargs):
        # validate the expected urls
        assert args[1] == EXPECTED_DOT_COM_POST_URL

    @staticmethod
    def raise_for_status():
        pass  # noqa: E704

    @staticmethod
    def json():
        return {"data": DOTCOM_RESOLVER_DATA}  # noqa: E704


class AsyncMockHttpSuccessResponse:
    status_code = 200

    def __init__(self, request_type, *args, **_kwargs):
        # validate the expected urls
        if request_type == "get":
            assert args[1] == EXPECTED_GET_URL
        elif request_type == "post":
            assert args[1] == EXPECTED_POST_URL

    @staticmethod
    def raise_for_status():
        pass  # noqa: E704

    @staticmethod
    async def json():
        return {"data": OFFCHAIN_RESOLVER_DATA}  # noqa: E704

    @property
    def status(self):
        return self.status_code


class AsyncMockHttpBadFormatResponse:
    status_code = 200

    def __init__(self, *args):
        assert args[1] == EXPECTED_GET_URL

    @staticmethod
    def raise_for_status():
        pass  # noqa: E704

    @staticmethod
    async def json():
        return {"not_data": OFFCHAIN_RESOLVER_DATA}  # noqa: E704'

    @property
    def status(self):
        return self.status_code


def test_offchain_resolution_with_get_request(ens, monkeypatch):
    # mock GET response with real return data from 'offchainexample.eth' resolver
    def mock_get(*args, **kwargs):
        return MockHttpSuccessResponse("get", *args, **kwargs)

    monkeypatch.setattr(requests.Session, "get", mock_get)

    assert ens.address("offchainexample.eth") == EXPECTED_RESOLVED_ADDRESS


def test_offchain_resolution_with_post_request(ens, monkeypatch):
    # mock POST response with real return data from 'offchainexample.eth' resolver
    def mock_post(*args, **kwargs):
        return MockHttpSuccessResponse("post", *args, **kwargs)

    monkeypatch.setattr(requests.Session, "post", mock_post)

    assert ens.address("offchainexample.eth") == EXPECTED_RESOLVED_ADDRESS


def test_offchain_dotcom_resolution_with_post_request(ens, monkeypatch):
    # mock POST response with real return data from 'gregskril.com' resolver
    def mock_post(*args, **kwargs):
        return MockDotcomResolverSuccessResponse("post", *args, **kwargs)

    monkeypatch.setattr(requests.Session, "post", mock_post)

    assert ens.address("gregskril.com") == EXPECTED_DOT_COM_RESOLVED_ADDRESS


def test_offchain_resolution_raises_when_all_supplied_urls_fail(ens):
    # with no mocked responses, requests to all urls will fail
    with pytest.raises(Exception, match="Offchain lookup failed for supplied urls."):
        ens.address("offchainexample.eth")


def test_offchain_resolution_with_improperly_formatted_http_response(ens, monkeypatch):
    def mock_get(*args, **_):
        return MockHttpBadFormatResponse(*args)

    monkeypatch.setattr(requests.Session, "get", mock_get)
    with pytest.raises(
        Web3ValidationError,
        match=(
            "Improperly formatted response for offchain lookup HTTP request "
            "- missing 'data' field."
        ),
    ):
        ens.address("offchainexample.eth")


def test_offchain_resolver_function_call_raises_with_ccip_read_disabled(
    ens, monkeypatch
):
    offchain_resolver = ens.resolver("offchainexample.eth")

    # should fail here with `ccip_read_enabled` flag set to False
    with pytest.raises(OffchainLookup):
        offchain_resolver.functions.resolve(
            ens_encode_name("offchainexample.eth"),
            ENCODED_ADDR_CALLDATA,
        ).call(ccip_read_enabled=False)

    # pass flag on specific call via ContractCaller is also an option
    with pytest.raises(OffchainLookup):
        offchain_resolver.caller(ccip_read_enabled=False).resolve(
            ens_encode_name("offchainexample.eth"),
            ENCODED_ADDR_CALLDATA,
        )


# -- async -- #


@pytest.mark.asyncio
async def test_async_offchain_resolution_with_get_request(async_ens, monkeypatch):
    # mock GET response with real return data from 'offchainexample.eth' resolver
    async def mock_get(*args, **kwargs):
        return AsyncMockHttpSuccessResponse("get", *args, **kwargs)

    monkeypatch.setattr(ClientSession, "get", mock_get)

    assert await async_ens.address("offchainexample.eth") == EXPECTED_RESOLVED_ADDRESS


@pytest.mark.asyncio
async def test_async_offchain_resolution_with_post_request(async_ens, monkeypatch):
    # mock POST response with real return data from 'offchainexample.eth' resolver
    async def mock_post(*args, **kwargs):
        return AsyncMockHttpSuccessResponse("post", *args, **kwargs)

    monkeypatch.setattr(ClientSession, "post", mock_post)

    assert await async_ens.address("offchainexample.eth") == EXPECTED_RESOLVED_ADDRESS


@pytest.mark.asyncio
async def test_async_offchain_resolution_raises_when_all_supplied_urls_fail(async_ens):
    # with no mocked responses, requests to all urls will fail
    with pytest.raises(Exception, match="Offchain lookup failed for supplied urls."):
        await async_ens.address("offchainexample.eth")


@pytest.mark.asyncio
async def test_async_offchain_resolution_with_improperly_formatted_http_response(
    async_ens, monkeypatch
):
    async def mock_get(*args, **_):
        return AsyncMockHttpBadFormatResponse(*args)

    monkeypatch.setattr(ClientSession, "get", mock_get)
    with pytest.raises(
        Web3ValidationError,
        match=(
            "Improperly formatted response for offchain lookup HTTP request "
            "- missing 'data' field."
        ),
    ):
        await async_ens.address("offchainexample.eth")
