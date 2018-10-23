import logging
import os

from eth_utils import (
    ValidationError,
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
        logging.getLogger('web3.auto.infura').warning(
            "No Infura API Key found. Add environment variable WEB3_INFURA_API_KEY to ensure "
            "continued API access. New keys are available at https://infura.io/register"
        )
    return key


def build_infura_url(domain):
    scheme = os.environ.get('WEB3_INFURA_SCHEME', WEBSOCKET_SCHEME)

    if scheme == WEBSOCKET_SCHEME:
        # websockets doesn't use the API key (yet?)
        return "%s://%s/ws" % (scheme, domain)
    elif scheme == HTTP_SCHEME:
        key = load_api_key()
        return "%s://%s/%s" % (scheme, domain, key)
    else:
        raise ValidationError("Cannot connect to Infura with scheme %r" % scheme)
