import logging
import os

NODESMITH_URL_FORMAT = 'https://ethereum.api.nodesmith.io/v1/%s/jsonrpc?apiKey=%s'

def load_api_key():
    key = os.environ.get('NODESMITH_API_KEY', '')
    if key == '':
        logging.getLogger('web3.auto.nodesmith').error(
             "No Nodesmith API key found. Add environment variable NODESMITH_API_KEY with your key. " +
            "Get a free API key at https://nodesmith.io"
        )
    return key


def build_nodesmith_url(network):
    key = load_api_key()
    url = NODESMITH_URL_FORMAT % (network, key)
    return url
