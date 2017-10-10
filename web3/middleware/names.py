
from ens import ENS

from web3.utils.ens import (
    is_ens_name,
)

from web3.utils.formatters import (
    apply_formatter_if,
    apply_formatter_at_index,
    apply_formatters_to_dict,
)


NAME_TO_ADDRESS_METHODS = {
    'eth_call',
    'eth_estimateGas',
    'eth_sendTransaction',
    'personal_sendTransaction',
}


def transaction_name_formatter(web3):
    ens = ENS(web3.manager.providers)

    def to_address(name):
        address = ens.address(name)
        if not address:
            raise ValueError("Could not find address for name %r" % name)
        return address

    transaction_formatter_fields = {
        'from': apply_formatter_if(to_address, is_ens_name),
        'to': apply_formatter_if(to_address, is_ens_name),
    }
    formatter = apply_formatters_to_dict(transaction_formatter_fields)
    return apply_formatter_at_index(formatter, 0)


def name_to_address_middleware(make_request, web3):
    transaction_formatter = transaction_name_formatter(web3)

    def middleware(method, params):
        if method in NAME_TO_ADDRESS_METHODS:
            formatted_params = transaction_formatter(params)
            return make_request(method, formatted_params)
        else:
            return make_request(method, params)
    return middleware
