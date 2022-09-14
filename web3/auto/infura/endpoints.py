import os
from typing import (
    Dict,
    Optional,
    Tuple,
)

from eth_typing import (
    URI,
)
from eth_utils import (
    ValidationError,
)

from web3.exceptions import (
    InfuraProjectIdNotFound,
)

INFURA_MAINNET_DOMAIN = "mainnet.infura.io"
INFURA_ROPSTEN_DOMAIN = "ropsten.infura.io"
INFURA_GOERLI_DOMAIN = "goerli.infura.io"
INFURA_RINKEBY_DOMAIN = "rinkeby.infura.io"
INFURA_SEPOLIA_DOMAIN = "sepolia.infura.io"

WEBSOCKET_SCHEME = "wss"
HTTP_SCHEME = "https"


def load_project_id() -> str:
    key = os.environ.get("WEB3_INFURA_PROJECT_ID", "")
    if key == "":
        raise InfuraProjectIdNotFound(
            "No Infura Project ID found. Please ensure "
            "that the environment variable WEB3_INFURA_PROJECT_ID is set."
        )
    return key


def load_secret() -> str:
    return os.environ.get("WEB3_INFURA_API_SECRET", "")


def build_http_headers() -> Optional[Dict[str, Tuple[str, str]]]:
    secret = load_secret()
    if secret:
        headers = {"auth": ("", secret)}
        return headers
    return None


def build_infura_url(domain: str) -> URI:
    scheme = os.environ.get("WEB3_INFURA_SCHEME", WEBSOCKET_SCHEME)
    key = load_project_id()
    secret = load_secret()

    if scheme == WEBSOCKET_SCHEME and secret != "":
        return URI(f"{scheme}://:{secret}@{domain}/ws/v3/{key}")
    elif scheme == WEBSOCKET_SCHEME and secret == "":
        return URI(f"{scheme}://{domain}/ws/v3/{key}")
    elif scheme == HTTP_SCHEME:
        return URI(f"{scheme}://{domain}/v3/{key}")
    else:
        raise ValidationError(f"Cannot connect to Infura with scheme {scheme!r}")
