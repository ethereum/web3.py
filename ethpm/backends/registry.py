from collections import (
    namedtuple,
)
from typing import (
    Optional,
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

from ens import (
    ENS,
)
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
RegistryURI = namedtuple(
    "RegistryURI", ["address", "chain_id", "name", "version", "namespaced_asset", "ens"]
)


class RegistryURIBackend(BaseURIBackend):
    """
    Backend class to handle Registry URIs.

    A Registry URI must resolve to a resolvable content-addressed URI.
    """

    def __init__(self) -> None:
        from web3 import (
            Web3,
            WebsocketProvider,
        )

        w3 = Web3(WebsocketProvider())

        self.w3 = w3

    def can_translate_uri(self, uri: str) -> bool:
        return is_valid_registry_uri(uri)

    def can_resolve_uri(self, uri: str) -> bool:
        return False

    def fetch_uri_contents(self, uri: str) -> URI:
        """
        Return content-addressed URI stored at registry URI.
        """
        address, chain_id, pkg_name, pkg_version, _, _ = parse_registry_uri(uri)
        if chain_id != "1":
            # todo: support all testnets
            raise CannotHandleURI("Currently only mainnet registry uris are supported.")
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
    Validate and return (authority, chain_id, pkg_name, version)
    from a valid registry URI.
    """
    from web3 import (
        Web3,
        WebsocketProvider,
    )

    w3 = Web3(WebsocketProvider())

    validate_registry_uri(uri)
    parsed_uri = parse.urlparse(uri)
    if ":" in parsed_uri.netloc:
        address_or_ens, chain_id = parsed_uri.netloc.split(":")
    else:
        address_or_ens, chain_id = parsed_uri.netloc, "1"
    ns = ENS.from_web3(w3)
    if is_address(address_or_ens):
        address = address_or_ens
        ens = None
    elif ns.address(address_or_ens):
        address = ns.address(address_or_ens)
        ens = address_or_ens
    else:
        raise CannotHandleURI(f"Invalid address or ENS domain found in uri: {uri}.")
    pkg_name, pkg_version, namespaced_asset = _process_pkg_path(parsed_uri.path)
    return RegistryURI(address, chain_id, pkg_name, pkg_version, namespaced_asset, ens)


def _process_pkg_path(
    raw_pkg_path: str,
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    pkg_path = raw_pkg_path.strip("/")
    if not pkg_path:
        return None, None, None

    pkg_id, namespaced_asset = _parse_pkg_path(pkg_path)
    pkg_name, pkg_version = _parse_pkg_id(pkg_id)
    if not pkg_version and namespaced_asset:
        raise EthPMValidationError(
            "Invalid registry URI, missing package version."
            "Version is required if namespaced assets are defined."
        )
    return pkg_name, pkg_version, namespaced_asset


def _parse_pkg_path(pkg_path: str) -> Tuple[str, Optional[str]]:
    if "/" in pkg_path:
        pkg_id, _, namespaced_asset = pkg_path.partition("/")
        return pkg_id, namespaced_asset
    else:
        return pkg_path, None


def _parse_pkg_id(pkg_id: str) -> Tuple[str, Optional[str]]:
    if "@" not in pkg_id:
        return pkg_id, None
    pkg_name, _, safe_pkg_version = pkg_id.partition("@")
    pkg_version = parse.unquote(safe_pkg_version)
    return pkg_name, pkg_version
