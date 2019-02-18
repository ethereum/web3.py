import logging
import os

from eth_utils import (
    ValidationError,
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
        logging.getLogger('web3.auto.infura').warning(
            "No Infura Project ID found. Add environment variable WEB3_INFURA_PROJECT_ID to "
            " ensure continued API access after March 27th. "
            "New keys are available at https://infura.io/register"
        )
    return key


def build_infura_url(domain):
    scheme = os.environ.get('WEB3_INFURA_SCHEME', WEBSOCKET_SCHEME)
    key = load_api_key()

    if key and scheme == WEBSOCKET_SCHEME:
        return "%s://%s/ws/v3/%s" % (scheme, domain, key)
    elif key and scheme == HTTP_SCHEME:
        return "%s://%s/v3/%s" % (scheme, domain, key)
    elif scheme == WEBSOCKET_SCHEME:
        return "%s://%s/ws/" % (scheme, domain)
    elif scheme == HTTP_SCHEME:
        return "%s://%s/%s" % (scheme, domain, key)
    else:
        raise ValidationError("Cannot connect to Infura with scheme %r" % scheme)
