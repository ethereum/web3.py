import pytest

from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.uri import (
    validate_registry_uri,
)


@pytest.mark.parametrize(
    "uri",
    (
        # no package id in uri
        ("erc1319://zeppelinos.eth:1"),
        ("erc1319://zeppelinos.eth:1/"),
        ("erc1319://packages.zeppelinos.eth:1"),
        ("erc1319://packages.zeppelinos.eth:1/"),
        ("erc1319://0xd3CdA913deB6f67967B99D67aCDFa1712C293601:1"),
        ("erc1319://0xd3CdA913deB6f67967B99D67aCDFa1712C293601:1/"),
        # with package id in uri
        ("erc1319://zeppelinos.eth:1/erc20/"),
        ("erc1319://zeppelinos.eth:1/erc20//"),
        ("erc1319://zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319://zeppelinos.eth:1/erc20?version=1.0.0/"),
        ("erc1319://packages.zeppelinos.eth:1/erc20?version="),
        ("erc1319://packages.zeppelinos.eth:1/erc20?version=/"),
        ("erc1319://packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319://packages.zeppelinos.eth:1/erc20?version=1.0.0/"),
        ("erc1319://packages.ethereum.eth:1/greeter?version=%3E%3D1.0.2%2C%3C2"),
        ("erc1319://0xd3CdA913deB6f67967B99D67aCDFa1712C293601:1/erc20?version=1.0.0"),
        ("erc1319://0xd3CdA913deB6f67967B99D67aCDFa1712C293601:1/erc20?version=1.0.0/"),
    ),
)
def test_is_registry_uri_validates(uri):
    assert validate_registry_uri(uri) is None


@pytest.mark.parametrize(
    "uri",
    (
        # invalid authority
        ("erc1319://zeppelinos.eth"),
        ("erc1319://zeppelinos.eth/"),
        ("erc1319://zeppelinos.eth/erc20?version=1.0.0"),
        ("erc1319://zeppelinos.eth:333/erc20?version=1.0.0"),
        ("erc1319://packages.zeppelinos.com:1/erc20?version=1.0.0"),
        ("erc1319://package.manager.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319://packageszeppelinoseth:1/erc20?version=1.0.0"),
        ("erc1319://0xd3cda913deb6f67967b99d67acdfa1712c293601:1/erc20?version=1.0.0"),
        # invalid package name
        ("erc1319://packages.zeppelinos.eth:1/?version=1.0.0"),
        ("erc1319://packages.zeppelinos.eth:1/?version=1.0.0/"),
        ("erc1319://packages.zeppelinos.eth:1/!rc20?version=1.0.0"),
        ("erc1319://packages.zeppelinos.eth:1/!rc20?version=1.0.0/"),
        # invalid version param
        ("erc1319://zeppelinos.eth:1/erc20?versions=1.0.0"),
        ("erc1319://zeppelinos.eth:1/erc20?version1.0.0"),
        # malformed
        ("erc1319packageszeppelinosetherc20version1.0.0"),
        ("erc1319:packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319:packages.zeppelinos.eth:1/erc20?version=1.0.0/"),
        ("erc1319:/packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319:/packages.zeppelinos.eth:1/erc20?version=1.0.0/"),
        ("erc1319/packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319//packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("erc1319packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        # wrong scheme
        ("http://packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        ("ercXX://packages.zeppelinos.eth:1/erc20?version=1.0.0"),
        # no path
        ("erc1319://"),
        # weird values
        (b"erc1319://zeppelinos.eth:1/erc20?version=1.0.0"),
        ("1234"),
        ({}),
    ),
)
def test_is_registry_uri_raises_exception_for_invalid_uris(uri):
    with pytest.raises(EthPMValidationError):
        validate_registry_uri(uri)
