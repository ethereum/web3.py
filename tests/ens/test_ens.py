import pytest
from unittest.mock import (
    AsyncMock,
    MagicMock,
    patch,
)

from ens import (
    ENS,
    AsyncENS,
)
from ens._normalization import (
    normalize_name_ensip15,
)
from ens.utils import (
    raw_name_to_hash,
)
from web3 import (
    AsyncWeb3,
)
from web3.middleware import (
    GasPriceStrategyMiddleware,
    ValidationMiddleware,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
)


def _args_list_to_set(call_args_list):
    return {call_arg.args[0] for call_arg in call_args_list}


def test_from_web3_inherits_web3_middleware(w3):
    test_middleware = GasPriceStrategyMiddleware
    w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = ENS.from_web3(w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


def test_from_web3_does_not_set_w3_object_reference(w3):
    assert w3.strict_bytes_type_checking

    ns = ENS.from_web3(w3)
    assert ns.w3.strict_bytes_type_checking

    assert w3 != ns.w3  # assert not the same object

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking

    assert ns.w3.strict_bytes_type_checking  # assert unchanged instance property


def test_w3_ens_for_empty_ens_sets_w3_object_reference(w3):
    assert w3.strict_bytes_type_checking
    assert w3.ens.w3.strict_bytes_type_checking

    assert w3 == w3.ens.w3  # assert same object

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert not w3.ens.w3.strict_bytes_type_checking


def test_w3_ens_setter_sets_w3_object_reference_on_ens(w3):
    ns = ENS.from_web3(w3)
    w3.ens = ns
    assert ns == w3.ens
    assert w3 == w3.ens.w3

    assert w3.strict_bytes_type_checking
    assert w3.ens.strict_bytes_type_checking
    assert w3.ens.w3.strict_bytes_type_checking

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert not w3.ens.strict_bytes_type_checking
    assert not w3.ens.w3.strict_bytes_type_checking


def test_ens_strict_bytes_type_checking_is_distinct_from_w3_instance(w3):
    ns = ENS.from_web3(w3)
    assert ns.w3 != w3  # assert unique instance for ns
    assert ns.w3 == ns._resolver_contract.w3  # assert same instance used under the hood

    assert w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking

    w3.strict_bytes_type_checking = False
    assert not w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking
    assert ns.w3.strict_bytes_type_checking
    assert ns._resolver_contract.w3.strict_bytes_type_checking

    w3.strict_bytes_type_checking = True
    assert w3.strict_bytes_type_checking

    ns.strict_bytes_type_checking = False
    assert not ns.strict_bytes_type_checking
    assert not ns.w3.strict_bytes_type_checking
    assert not ns._resolver_contract.w3.strict_bytes_type_checking


@pytest.mark.parametrize(
    "method_str,args",
    (
        ("owner", ("tester.eth",)),
        ("resolver", ("tester.eth",)),
        ("set_text", ("tester.eth", "url", "https://www.ethereum.org")),
        ("get_text", ("tester.eth", "url")),
    ),
)
def test_ens_methods_normalize_name(
    ens,
    method_str,
    args,
):
    address = ens.w3.eth.accounts[2]
    method = ens.__getattribute__(method_str)

    # normalizes the full name and each label
    expected_call_args = {"tester.eth", "tester", "eth"}

    with patch(
        "ens._normalization.normalize_name_ensip15"
    ) as mock_normalize_name_ensip15:
        mock_normalize_name_ensip15.side_effect = normalize_name_ensip15

        # test setup address while appropriately setting up the test
        ens.setup_address("tester.eth", address)
        assert expected_call_args.issubset(
            _args_list_to_set(mock_normalize_name_ensip15.call_args_list)
        )

        # reset the mock
        mock_normalize_name_ensip15.reset_mock()
        assert len(mock_normalize_name_ensip15.call_args_list) == 0

        # test parametrized method
        method(*args)
        assert expected_call_args.issubset(
            _args_list_to_set(mock_normalize_name_ensip15.call_args_list)
        )

    # cleanup
    ens.setup_address("tester.eth", None)


def test_ens_address_lookup_when_no_coin_type(ens):
    """
    Test that when coin_type is None, the method calls _resolve(name, "addr")
    and returns the expected address.
    """
    name = "tester.eth"
    address = ens.w3.eth.accounts[0]

    with patch("ens.ENS.resolver") as mock_resolver_for_coin_types:
        with patch("ens.ENS._resolve") as mock_resolver:
            mock_resolver.return_value = address

            returned_address = ens.address(name)

            mock_resolver.assert_called_once_with(name, "addr")
            mock_resolver_for_coin_types.assert_not_called()
            assert returned_address == address


def test_ens_address_lookup_with_coin_type(ens):
    """
    Test that when coin_type is specified, it calls:
      1) _validate_resolver_and_interface_id
      2) resolver.caller.addr(node, coin_type)
      3) returns the checksum address
    """
    name = "tester.eth"
    address = ens.w3.eth.accounts[0]
    coin_type = 60
    node = raw_name_to_hash(name)

    mock_resolver = MagicMock()
    mock_resolver.caller.addr.return_value = address

    with patch("ens.ENS.resolver") as resolver:
        resolver.return_value = mock_resolver

        with patch("ens.ens._validate_resolver_and_interface_id") as mock_validate:
            returned_address = ens.address(name, coin_type=coin_type)

            mock_validate.assert_called_once()
            mock_resolver.caller.addr.assert_called_once_with(node, coin_type)
            assert returned_address == address


# -- async -- #


@pytest.fixture
def local_async_w3():
    return AsyncWeb3(AsyncEthereumTesterProvider())


def test_async_from_web3_inherits_web3_middleware(local_async_w3):
    test_middleware = ValidationMiddleware
    local_async_w3.middleware_onion.add(test_middleware, "test_middleware")

    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3.middleware_onion.get("test_middleware") == test_middleware


def test_async_from_web3_does_not_set_w3_object_reference(local_async_w3):
    assert local_async_w3.strict_bytes_type_checking

    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3.strict_bytes_type_checking

    assert local_async_w3 != ns.w3  # assert not the same object

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking

    assert ns.w3.strict_bytes_type_checking  # assert unchanged instance property


def test_async_w3_ens_for_empty_ens_sets_w3_object_reference(local_async_w3):
    assert local_async_w3.strict_bytes_type_checking
    assert local_async_w3.ens.w3.strict_bytes_type_checking

    assert local_async_w3 == local_async_w3.ens.w3  # assert same object

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert not local_async_w3.ens.w3.strict_bytes_type_checking


def test_async_w3_ens_setter_sets_w3_object_reference_on_ens(local_async_w3):
    ns = AsyncENS.from_web3(local_async_w3)
    local_async_w3.ens = ns
    assert ns == local_async_w3.ens
    assert local_async_w3 == local_async_w3.ens.w3

    assert local_async_w3.strict_bytes_type_checking
    assert local_async_w3.ens.w3.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert not local_async_w3.ens.w3.strict_bytes_type_checking


def test_async_ens_strict_bytes_type_checking_is_distinct_from_w3_instance(
    local_async_w3,
):
    ns = AsyncENS.from_web3(local_async_w3)
    assert ns.w3 != local_async_w3  # assert unique instance for ns
    assert ns.w3 == ns._resolver_contract.w3  # assert same instance used under the hood

    assert local_async_w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = False
    assert not local_async_w3.strict_bytes_type_checking
    assert ns.strict_bytes_type_checking
    assert ns.w3.strict_bytes_type_checking
    assert ns._resolver_contract.w3.strict_bytes_type_checking

    local_async_w3.strict_bytes_type_checking = True
    assert local_async_w3.strict_bytes_type_checking

    ns.strict_bytes_type_checking = False
    assert not ns.strict_bytes_type_checking
    assert not ns.w3.strict_bytes_type_checking
    assert not ns._resolver_contract.w3.strict_bytes_type_checking


@pytest.mark.parametrize(
    "method_str,args",
    (
        ("owner", ("tester.eth",)),
        ("resolver", ("tester.eth",)),
        ("set_text", ("tester.eth", "url", "https://www.ethereum.org")),
        ("get_text", ("tester.eth", "url")),
    ),
)
@pytest.mark.asyncio
async def test_async_ens_methods_normalize_name_with_ensip15(
    async_ens,
    method_str,
    args,
):
    accounts = await async_ens.w3.eth.accounts
    address = accounts[2]
    method = async_ens.__getattribute__(method_str)

    # normalizes the full name and each label
    expected_call_args = {"tester.eth", "tester", "eth"}

    with patch(
        "ens._normalization.normalize_name_ensip15"
    ) as mock_normalize_name_ensip15:
        mock_normalize_name_ensip15.side_effect = normalize_name_ensip15

        # test setup address while appropriately setting up the test
        await async_ens.setup_address("tester.eth", address)
        assert expected_call_args.issubset(
            _args_list_to_set(mock_normalize_name_ensip15.call_args_list)
        )

        # reset the mock
        mock_normalize_name_ensip15.reset_mock()
        assert len(mock_normalize_name_ensip15.call_args_list) == 0

        # test parametrized method
        await method(*args)
        assert expected_call_args.issubset(
            _args_list_to_set(mock_normalize_name_ensip15.call_args_list)
        )

    # cleanup
    await async_ens.setup_address("tester.eth", None)


@pytest.mark.asyncio
async def test_async_ens_address_lookup_when_no_coin_type(async_ens):
    """
    Test that when coin_type is None, the method calls _resolve(name, "addr")
    and returns the expected address.
    """
    name = "tester.eth"
    accounts = await async_ens.w3.eth.accounts
    address = accounts[2]

    with patch("ens.AsyncENS.resolver") as mock_resolver_for_coin_types:
        with patch("ens.AsyncENS._resolve") as mock_resolver:
            mock_resolver.return_value = address

            returned_address = await async_ens.address(name)

            mock_resolver.assert_called_once_with(name, "addr")
            mock_resolver_for_coin_types.assert_not_called()
            assert returned_address == address


@pytest.mark.asyncio
async def test_async_ens_address_lookup_with_coin_type(async_ens):
    """
    Test that when coin_type is specified, it calls:
      1) _async_validate_resolver_and_interface_id
      2) async resolver.caller.addr(node, coin_type)
      3) returns the checksum address
    """
    name = "tester.eth"
    accounts = await async_ens.w3.eth.accounts
    address = accounts[2]
    coin_type = 60
    node = raw_name_to_hash(name)

    mock_resolver = AsyncMock()
    mock_resolver.caller.addr.return_value = address

    with patch("ens.AsyncENS.resolver") as resolver:
        resolver.return_value = mock_resolver

        with patch(
            "ens.async_ens._async_validate_resolver_and_interface_id"
        ) as mock_validate:
            returned_address = await async_ens.address(name, coin_type=coin_type)

            mock_validate.assert_called_once()
            mock_resolver.caller.addr.assert_called_once_with(node, coin_type)
            assert returned_address == address
