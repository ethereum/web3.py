from collections import namedtuple
import os
from urllib import parse

from eth_typing import URI
from web3 import Web3
from web3.providers.auto import load_provider_from_uri

from ethpm._utils.registry import fetch_standard_registry_abi
from ethpm.backends.base import BaseURIBackend
from ethpm.constants import INFURA_API_KEY
from ethpm.exceptions import ValidationError
from ethpm.validation.uri import validate_registry_uri

# TODO: Update registry ABI once ERC is finalized.
REGISTRY_ABI = fetch_standard_registry_abi()
RegistryURI = namedtuple("RegistryURI", ["auth", "name", "version"])


class RegistryURIBackend(BaseURIBackend):
    """
    Backend class to handle Registry URIs.

    A Registry URI must resolve to a resolvable content-addressed URI.
    """

    def __init__(self) -> None:
        os.environ.setdefault("INFUFA_API_KEY", INFURA_API_KEY)
        infura_url = f"wss://mainnet.infura.io/ws/v3/{INFURA_API_KEY}"
        self.w3 = Web3(load_provider_from_uri(infura_url))

    def can_translate_uri(self, uri: str) -> bool:
        return is_valid_registry_uri(uri)

    def can_resolve_uri(self, uri: str) -> bool:
        return False

    def fetch_uri_contents(self, uri: str) -> URI:
        """
        Return content-addressed URI stored at registry URI.
        """
        address, pkg_name, pkg_version = parse_registry_uri(uri)
        self.w3.enable_unstable_package_management_api()
        self.w3.pm.set_registry(address)
        _, _, manifest_uri = self.w3.pm.get_release_data(pkg_name, pkg_version)
        return manifest_uri


def is_valid_registry_uri(uri: str) -> bool:
    """
    Return a boolean indicating whether `uri` argument
    conforms to the Registry URI scheme.
    """
    try:
        validate_registry_uri(uri)
    except ValidationError:
        return False
    else:
        return True


def parse_registry_uri(uri: str) -> RegistryURI:
    """
    Validate and return (authority, pkg name, version) from a valid registry URI
    """
    validate_registry_uri(uri)
    parsed_uri = parse.urlparse(uri)
    authority = parsed_uri.netloc
    pkg_name = parsed_uri.path.strip("/")
    pkg_version = parsed_uri.query.lstrip("version=").strip("/")
    return RegistryURI(authority, pkg_name, pkg_version)
