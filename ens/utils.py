
from web3 import HTTPProvider, IPCProvider, Web3
from web3.contract import ConciseContract
from web3.middleware import make_stalecheck_middleware

from ens.constants import ACCEPTABLE_STALE_HOURS


def dict_copy(func):
    "copy dict keyword args, to avoid modifying caller's copy"
    def proxy(*args, **kwargs):
        new_kwargs = {}
        for var in kwargs:
            if isinstance(kwargs[var], dict):
                new_kwargs[var] = dict(kwargs[var])
            else:
                new_kwargs[var] = kwargs[var]
        return func(*args, **new_kwargs)
    return proxy


def ensure_hex(data):
    if not isinstance(data, str):
        return Web3.toHex(data)
    return data


def init_web3(providers=None):
    if not providers:
        providers = [IPCProvider(), HTTPProvider('http://localhost:8545')]
    w3 = Web3(providers)
    w3.middleware_stack.add(
        make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600),
        name='stalecheck'
    )
    w3.eth.setContractFactory(ConciseContract)
    return w3
