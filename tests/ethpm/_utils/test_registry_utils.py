import pytest

from ethpm.exceptions import (
    ValidationError,
)
from ethpm.validation.uri import (
    validate_registry_uri,
)


@pytest.mark.parametrize(
    "uri",
    (
        ("ercxxx://zeppelinos.eth/erc20/"),
        ("ercXXX://zeppelinos.eth/erc20/"),
        ("ercXXX://zeppelinos.eth/erc20//"),
        ("ercXXX://zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX://zeppelinos.eth/erc20?version=1.0.0/"),
        ("ercXXX://packages.zeppelinos.eth/erc20?version="),
        ("ercXXX://packages.zeppelinos.eth/erc20?version=/"),
        ("ercXXX://packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX://packages.zeppelinos.eth/erc20?version=1.0.0/"),
        ("ercXXX://packages.ethereum.eth/greeter?version=%3E%3D1.0.2%2C%3C2"),
        ("ercXXX://0xd3CdA913deB6f67967B99D67aCDFa1712C293601/erc20?version=1.0.0"),
        ("ercXXX://0xd3CdA913deB6f67967B99D67aCDFa1712C293601/erc20?version=1.0.0/"),
    ),
)
def test_is_registry_uri_validates(uri):
    assert validate_registry_uri(uri) is None


@pytest.mark.parametrize(
    "uri",
    (
        # invalid authority
        ("ercXXX://packages.zeppelinos.com/erc20?version=1.0.0"),
        ("ercXXX://package.manager.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX://packageszeppelinoseth/erc20?version=1.0.0"),
        ("ercXXX://0xd3cda913deb6f67967b99d67acdfa1712c293601/erc20?version=1.0.0"),
        # invalid package name
        ("ercXXX://packages.zeppelinos.eth/"),
        ("ercXXX://packages.zeppelinos.eth///"),
        ("ercXXX://packages.zeppelinos.eth/?version=1.0.0"),
        ("ercXXX://packages.zeppelinos.eth/!rc20?version=1.0.0"),
        # invalid version param
        ("ercXXX://zeppelinos.eth/erc20?versions=1.0.0"),
        ("ercXXX://zeppelinos.eth/erc20?version1.0.0"),
        # malformed
        ("ercXXXpackageszeppelinosetherc20version1.0.0"),
        ("ercXXX:packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX:packages.zeppelinos.eth/erc20?version=1.0.0/"),
        ("ercXXX:/packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX:/packages.zeppelinos.eth/erc20?version=1.0.0/"),
        ("ercXXX/packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXX//packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXXXpackages.zeppelinos.eth/erc20?version=1.0.0"),
        # wrong scheme
        ("http://packages.zeppelinos.eth/erc20?version=1.0.0"),
        ("ercXX://packages.zeppelinos.eth/erc20?version=1.0.0"),
        # no path
        ("ercXXX://"),
        # weird values
        (b"ercXXX://zeppelinos.eth/erc20?version=1.0.0"),
        ("1234"),
        ({}),
    ),
)
def test_is_registry_uri_raises_exception_for_invalid_uris(uri):
    with pytest.raises(ValidationError):
        validate_registry_uri(uri)
