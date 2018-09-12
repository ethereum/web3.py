from eth_utils import (
    is_dict,
)

from web3._utils.toolz import (
    assoc,
)
from web3.datastructures import (
    AttributeDict,
)


def attrdict_middleware(make_request, web3):
    """
    Converts any result which is a dictionary into an a
    """
    def middleware(method, params):
        response = make_request(method, params)

        if 'result' in response:
            result = response['result']
            if is_dict(result) and not isinstance(result, AttributeDict):
                return assoc(response, 'result', AttributeDict.recursive(result))
            else:
                return response
        else:
            return response
    return middleware
