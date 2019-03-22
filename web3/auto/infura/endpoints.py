import os

from eth_utils import (
    ValidationError,
)

from web3.exceptions import (
    InfuraKeyNotFound,
)

INFURA_MAINNET_DOMAIN = 'mainnet.infura.io'
INFURA_ROPSTEN_DOMAIN = 'ropsten.infura.io'

WEBSOCKET_SCHEME = 'wss'
HTTP_SCHEME = 'https'


def load_api_key():
    # at web3py v5, drop old variable name INFURA_API_KEY
    key = os.environ.get(
        'WEB3_INFURA_API_KEY',
        os.environ.get('INFURA_API_KEY', '')
    )
    if key == '':
        raise InfuraKeyNotFound(
            "No Infura Project ID found. Please ensure "
            "that the environment variable WEB3_INFURA_API_KEY is set."
        )
    return key


def build_infura_url(domain):
    scheme = os.environ.get('WEB3_INFURA_SCHEME', WEBSOCKET_SCHEME)
    key = load_api_key()

    secret = os.environ.get('WEB3_INFURA_API_SECRET', '')

    if secret and scheme == WEBSOCKET_SCHEME:
        return "%s://:%s@%s/ws/v3/%s" % (scheme, secret, domain, key)
    elif secret and scheme == HTTP_SCHEME:
        return "%s://:%s@%s/v3/%s" % (scheme, secret, domain, key)
    elif scheme == WEBSOCKET_SCHEME:
        return "%s://%s/ws/" % (scheme, domain)
    elif scheme == HTTP_SCHEME:
        return "%s://%s/v3/%s" % (scheme, domain, key)
    else:
        raise ValidationError("Cannot connect to Infura with scheme %r" % scheme)
