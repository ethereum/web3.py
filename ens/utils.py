
import datetime
import idna

from ens.exceptions import InvalidName
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
    from web3 import Web3
    if not isinstance(data, str):
        return Web3.toHex(data)
    return data


def init_web3(providers=None):
    from web3 import HTTPProvider, IPCProvider, Web3
    from web3.contract import ConciseContract
    from web3.middleware import make_stalecheck_middleware

    if not providers:
        providers = [IPCProvider(), HTTPProvider('http://localhost:8545')]
    w3 = Web3(providers)
    w3.middleware_stack.add(
        make_stalecheck_middleware(ACCEPTABLE_STALE_HOURS * 3600),
        name='stalecheck'
    )
    w3.eth.setContractFactory(ConciseContract)
    return w3


def prepare_name(name):
    '''
    Clean the fully qualified name, as defined in ENS `EIP-137
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_

    :param str name: the dot-separated ENS name
    :raises InvalidName: if ``name`` has invalid syntax
    '''
    if not name:
        return name
    try:
        return idna.decode(name, uts46=True, std3_rules=True)
    except idna.IDNAError as exc:
        raise InvalidName("%s is an invalid name, because %s" % (name, exc)) from exc


def to_utc_datetime(timestamp):
    if timestamp:
        return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)
    else:
        return None
