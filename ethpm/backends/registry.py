from collections import (
    namedtuple,
)
from typing import (
    Tuple,
)
from urllib import (
    parse,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    is_address,
)

from ens import ENS
from ethpm._utils.registry import (
    fetch_standard_registry_abi,
)
from ethpm.backends.base import (
    BaseURIBackend,
)
from ethpm.exceptions import (
    CannotHandleURI,
    EthPMValidationError,
)
from ethpm.validation.uri import (
    validate_registry_uri,
)

# TODO: Update registry ABI once ERC is finalized.
REGISTRY_ABI = fetch_standard_registry_abi()
RegistryURI = namedtuple("RegistryURI", ["address", "chain_id", "name", "version", "ens"])


class RegistryURIBackend(BaseURIBackend):
    """
    Backend class to handle Registry URIs.

    A Registry URI must resolve to a resolvable content-addressed URI.
    """

    def __init__(self) -> None:
        from web3.auto.infura import w3
        self.w3 = w3

    def can_translate_uri(self, uri: str) -> bool:
        return is_valid_registry_uri(uri)

    def can_resolve_uri(self, uri: str) -> bool:
        return False

    def fetch_uri_contents(self, uri: str) -> URI:
        """
        Return content-addressed URI stored at registry URI.
        """
        address, chain_id, pkg_name, pkg_version, _ = parse_registry_uri(uri)
        if chain_id != '1':
            # todo: support all testnets
            raise CannotHandleURI(
                "Currently only mainnet registry uris are supported."
            )
        self.w3.enable_unstable_package_management_api()
        self.w3.pm.set_registry(address)
        _, _, manifest_uri = self.w3.pm.get_release_data(pkg_name, pkg_version)
        return URI(manifest_uri)


def is_valid_registry_uri(uri: str) -> bool:
    """
    Return a boolean indicating whether `uri` argument
    conforms to the Registry URI scheme.
    """
    try:
        validate_registry_uri(uri)
    except EthPMValidationError:
        return False
    else:
        return True


def parse_registry_uri(uri: str) -> RegistryURI:
    """
    Validate and return (authority, chain_id, pkg_name, version) from a valid registry URI.
    """
    from web3.auto.infura import w3
    validate_registry_uri(uri)
    parsed_uri = parse.urlparse(uri)
    address_or_ens, chain_id = parsed_uri.netloc.split(":")
    ns = ENS.fromWeb3(w3)
    if is_address(address_or_ens):
        address = address_or_ens
        ens = None
    elif ns.address(address_or_ens):
        address = ns.address(address_or_ens)
        ens = address_or_ens
    else:
        raise CannotHandleURI(
            f"Invalid address or ENS domain found in uri: {uri}."
        )
    pkg_name, pkg_version = process_pkg_path(parsed_uri.path)
    return RegistryURI(address, chain_id, pkg_name, pkg_version, ens)


def process_pkg_path(pkg_path: str) -> Tuple[str, str]:
    pkg_id = pkg_path.strip("/")
    if not pkg_id:
        return None, None

    if "@" not in pkg_id:
        return pkg_id, None
    pkg_name, safe_pkg_version = pkg_id.split("@")
    pkg_version = parse.unquote(safe_pkg_version)
    return pkg_name, pkg_version
