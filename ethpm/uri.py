import json
from typing import (
    TYPE_CHECKING,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    encode_hex,
    to_hex,
)
from eth_utils.toolz import (
    curry,
)
import requests

from ethpm._utils.backend import (
    get_resolvable_backends_for_uri,
    get_translatable_backends_for_uri,
)
from ethpm._utils.chains import (
    BLOCK,
    create_block_uri,
    get_genesis_block_hash,
    parse_BIP122_uri,
)
from ethpm._utils.ipfs import (
    is_ipfs_uri,
)
from ethpm.backends.http import (
    is_valid_api_github_uri,
    is_valid_content_addressed_github_uri,
)
from ethpm.backends.registry import (
    RegistryURIBackend,
)
from ethpm.exceptions import (
    CannotHandleURI,
)
from web3.types import (
    BlockNumber,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa F401


def resolve_uri_contents(uri: URI, fingerprint: bool = None) -> bytes:
    resolvable_backends = get_resolvable_backends_for_uri(uri)
    if resolvable_backends:
        for backend in resolvable_backends:
            try:
                # type ignored to handle case if URI is returned
                contents: bytes = backend().fetch_uri_contents(uri)  # type: ignore
            except CannotHandleURI:
                continue
            return contents

    translatable_backends = get_translatable_backends_for_uri(uri)
    if translatable_backends:
        if fingerprint:
            raise CannotHandleURI(
                "Registry URIs must point to a resolvable content-addressed URI."
            )
        package_id = RegistryURIBackend().fetch_uri_contents(uri)
        return resolve_uri_contents(package_id, True)

    raise CannotHandleURI(
        f"URI: {uri} cannot be resolved by any of the available backends."
    )


def create_content_addressed_github_uri(uri: URI) -> URI:
    """
    Returns a content-addressed Github "git_url" that conforms to this scheme.
    https://api.github.com/repos/:owner/:repo/git/blobs/:file_sha

    Accepts Github-defined "url" that conforms to this scheme
    https://api.github.com/repos/:owner/:repo/contents/:path/:to/manifest.json
    """
    if not is_valid_api_github_uri(uri):
        raise CannotHandleURI(f"{uri} does not conform to Github's API 'url' scheme.")
    response = requests.get(uri)
    response.raise_for_status()
    contents = json.loads(response.content)
    if contents["type"] != "file":
        raise CannotHandleURI(
            "Expected url to point to a 'file' type, "
            f"instead received {contents['type']}."
        )
    return contents["git_url"]


def is_supported_content_addressed_uri(uri: URI) -> bool:
    """
    Returns a bool indicating whether provided uri is currently supported.
    Currently Py-EthPM only supports IPFS and Github blob content-addressed uris.
    """
    if not is_ipfs_uri(uri) and not is_valid_content_addressed_github_uri(uri):
        return False
    return True


def create_latest_block_uri(w3: "Web3", from_blocks_ago: int = 3) -> URI:
    """
    Creates a block uri for the given w3 instance.
    Defaults to 3 blocks prior to the "latest" block to accommodate for block reorgs.
    If using a testnet with less than 3 mined blocks, adjust :from_blocks_ago:.
    """
    chain_id = to_hex(get_genesis_block_hash(w3))
    latest_block_tx_receipt = w3.eth.get_block("latest")
    target_block_number = BlockNumber(
        latest_block_tx_receipt["number"] - from_blocks_ago
    )
    if target_block_number < 0:
        raise Exception(
            f"Only {latest_block_tx_receipt['number']} blocks avaible on provided w3, "
            f"cannot create latest block uri for {from_blocks_ago} blocks ago."
        )
    recent_block = to_hex(w3.eth.get_block(target_block_number)["hash"])
    return create_block_uri(chain_id, recent_block)


@curry
def check_if_chain_matches_chain_uri(w3: "Web3", blockchain_uri: URI) -> bool:
    chain_id, resource_type, resource_hash = parse_BIP122_uri(blockchain_uri)
    genesis_block = w3.eth.get_block("earliest")

    if encode_hex(genesis_block["hash"]) != chain_id:
        return False

    if resource_type == BLOCK:
        resource = w3.eth.get_block(resource_hash)
    else:
        raise ValueError(f"Unsupported resource type: {resource_type}")

    if encode_hex(resource["hash"]) == resource_hash:
        return True
    else:
        return False
