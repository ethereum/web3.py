from abc import (
    abstractmethod,
)
import os
from pathlib import (
    Path,
)
from typing import (
    Dict,
    List,
    Type,
)

from eth_utils import (
    import_string,
    to_bytes,
)
import ipfshttpclient

from ethpm import (
    get_ethpm_spec_dir,
)
from ethpm._utils.ipfs import (
    dummy_ipfs_pin,
    extract_ipfs_path_from_uri,
    generate_file_hash,
    is_ipfs_uri,
)
from ethpm.backends.base import (
    BaseURIBackend,
)
from ethpm.constants import (
    DEFAULT_IPFS_BACKEND,
    INFURA_GATEWAY_MULTIADDR,
    IPFS_GATEWAY_PREFIX,
)
from ethpm.exceptions import (
    CannotHandleURI,
    EthPMValidationError,
)


class BaseIPFSBackend(BaseURIBackend):
    """
    Base class for all URIs with an IPFS scheme.
    """

    def can_resolve_uri(self, uri: str) -> bool:
        """
        Return a bool indicating whether or not this backend
        is capable of serving the content located at the URI.
        """
        return is_ipfs_uri(uri)

    def can_translate_uri(self, uri: str) -> bool:
        """
        Return False. IPFS URIs cannot be used to point
        to another content-addressed URI.
        """
        return False

    @abstractmethod
    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        """
        Pin assets found at `file_or_dir_path` and return a
        list containing pinned asset data.
        """
        pass


class IPFSOverHTTPBackend(BaseIPFSBackend):
    """
    Base class for all IPFS URIs served over an http connection.
    All subclasses must implement: base_uri
    """

    def __init__(self) -> None:
        self.client = ipfshttpclient.connect(self.base_uri)

    def fetch_uri_contents(self, uri: str) -> bytes:
        ipfs_hash = extract_ipfs_path_from_uri(uri)
        contents = self.client.cat(ipfs_hash)
        # Local validation of hashed contents only works for non-chunked files ~< 256kb
        # Improved validation WIP @ https://github.com/ethpm/py-ethpm/pull/165
        if len(contents) <= 262144:
            validation_hash = generate_file_hash(contents)
            if validation_hash != ipfs_hash:
                raise EthPMValidationError(
                    f"Hashed IPFS contents retrieved from uri: {uri} do not match its content hash."
                )
        return contents

    @property
    @abstractmethod
    def base_uri(self) -> str:
        pass

    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        if file_or_dir_path.is_dir():
            dir_data = self.client.add(str(file_or_dir_path), recursive=True)
            return dir_data
        elif file_or_dir_path.is_file():
            file_data = self.client.add(str(file_or_dir_path), recursive=False)
            return [file_data]
        else:
            raise TypeError(
                f"{file_or_dir_path} is not a valid file or directory path."
            )


class IPFSGatewayBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served over the IPFS gateway.
    """

    # todo update this gateway to work r&w
    # https://discuss.ipfs.io/t/writeable-http-gateways/210
    @property
    def base_uri(self) -> str:
        return IPFS_GATEWAY_PREFIX

    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        raise CannotHandleURI(
            "IPFS gateway is currently disabled, please use a different IPFS backend."
        )

    def fetch_uri_contents(self, uri: str) -> bytes:
        raise CannotHandleURI(
            "IPFS gateway is currently disabled, please use a different IPFS backend."
        )


class InfuraIPFSBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served over the Infura IFPS gateway.
    """

    @property
    def base_uri(self) -> str:
        return INFURA_GATEWAY_MULTIADDR


class LocalIPFSBackend(IPFSOverHTTPBackend):
    """
    Backend class for all IPFS URIs served through a direct connection to an IPFS node.
    Default IPFS port = 5001
    """

    @property
    def base_uri(self) -> str:
        return "/ip4/127.0.0.1/tcp/5001"


MANIFEST_URIS = {
    "ipfs://QmQNffBrmbB3TuBCtYfYsJWJVLssatWXa3H6CkGeyNUySA": "standard-token",
    "ipfs://QmWnPsiS3Xb8GvCDEBFnnKs8Yk4HaAX6rCqJAaQXGbCoPk": "safe-math-lib",
    "ipfs://QmcxvhkJJVpbxEAa6cgW3B6XwPJb79w9GpNUv2P2THUzZR": "owned",
}


class DummyIPFSBackend(BaseIPFSBackend):
    """
    Backend class to serve IPFS URIs without having to make an HTTP request.
    Used primarily for testing purposes, returns a locally stored manifest or contract.
    ---
    `ipfs_uri` can either be:
    - Valid IPFS URI -> safe-math-lib manifest (ALWAYS)
    - Path to manifest/contract in ethpm_spec_dir -> defined manifest/contract
    """

    def fetch_uri_contents(self, ipfs_uri: str) -> bytes:
        pkg_name = MANIFEST_URIS[ipfs_uri]
        ethpm_spec_dir = get_ethpm_spec_dir()
        pkg_contents = (ethpm_spec_dir / "examples" / pkg_name / "v3.json").read_text()
        return to_bytes(text=pkg_contents)

    def can_resolve_uri(self, uri: str) -> bool:
        return uri in MANIFEST_URIS

    def pin_assets(self, file_or_dir_path: Path) -> List[Dict[str, str]]:
        """
        Return a dict containing the IPFS hash, file name, and size of a file.
        """
        if file_or_dir_path.is_dir():
            asset_data = [dummy_ipfs_pin(path) for path in file_or_dir_path.glob("*")]
        elif file_or_dir_path.is_file():
            asset_data = [dummy_ipfs_pin(file_or_dir_path)]
        else:
            raise FileNotFoundError(
                f"{file_or_dir_path} is not a valid file or directory path."
            )
        return asset_data


def get_ipfs_backend(import_path: str = None) -> BaseIPFSBackend:
    """
    Return the `BaseIPFSBackend` class specified by import_path, default, or env variable.
    """
    backend_class = get_ipfs_backend_class(import_path)
    return backend_class()


def get_ipfs_backend_class(import_path: str = None) -> Type[BaseIPFSBackend]:
    if import_path is None:
        import_path = os.environ.get("ETHPM_IPFS_BACKEND_CLASS", DEFAULT_IPFS_BACKEND)
        if not import_path:
            raise CannotHandleURI(
                "Please provide an import class or set "
                "`ETHPM_IPFS_BACKEND_CLASS` environment variable."
            )
    return import_string(import_path)
