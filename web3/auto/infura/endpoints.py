import os

from eth_utils import (
    ValidationError,
)

from web3.exceptions import (
    InfuraKeyNotFound,
)

INFURA_MAINNET_DOMAIN = 'mainnet.infura.io'
INFURA_ROPSTEN_DOMAIN = 'ropsten.infura.io'
INFURA_RINKEBY_DOMAIN = 'rinkeby.infura.io'
INFURA_KOVAN_DOMAIN = 'kovan.infura.io'

WEBSOCKET_SCHEME = 'wss'
HTTP_SCHEME = 'https'


def load_api_key():
    # in web3py v6 remove outdated WEB3_INFURA_API_KEY
    key = os.environ.get('WEB3_INFURA_PROJECT_ID',
                         os.environ.get('WEB3_INFURA_API_KEY', ''))
    if key == '':
        raise InfuraKeyNotFound(
            "No Infura Project ID found. Please ensure "
            "that the environment variable WEB3_INFURA_PROJECT_ID is set."
        )
    return key


def build_infura_url(domain):
    scheme = os.environ.get('WEB3_INFURA_SCHEME', WEBSOCKET_SCHEME)
    key = load_api_key()

    if scheme == WEBSOCKET_SCHEME:
        return "%s://%s/ws/v3/%s" % (scheme, domain, key)
    elif scheme == HTTP_SCHEME:
        return "%s://%s/v3/%s" % (scheme, domain, key)
    else:
        raise ValidationError("Cannot connect to Infura with scheme %r" % scheme)
