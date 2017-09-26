
from web3.utils.encoding import (
    to_bytes,
)

CHAIN_ID_OFFSET = 35
V_OFFSET = 27


# watch here for updates to signature format: https://github.com/ethereum/EIPs/issues/191
def signature_wrapper(message, version=b'E'):
    assert isinstance(message, bytes)
    if version == b'E':
        preamble = b'\x19Ethereum Signed Message:\n'
        size = str(len(message)).encode('utf-8')
        return preamble + size + message
    else:
        raise NotImplementedError("Only the 'Ethereum Signed Message' preamble is supported")


def annotate_transaction_with_chain_id(transaction_parts, raw_v):
    '''
    Extends transaction with chain ID, according to EIP-155
    See details at https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md
    @return (transaction_parts, chain_id, v)
    '''
    assert len(transaction_parts) == 6
    (chain_id, v) = extract_chain_id(raw_v)
    if chain_id is None:
        chain_id_extension = []
    else:
        chain_id_extension = [to_bytes(chain_id), b'', b'']
    return (transaction_parts + chain_id_extension, chain_id, v)


def extract_chain_id(raw_v):
    '''
    Extracts chain ID, according to EIP-155
    @return (chain_id, v)
    '''
    above_id_offset = raw_v - CHAIN_ID_OFFSET
    if above_id_offset < 0:
        return (None, raw_v)
    else:
        (chain_id, v_bit) = divmod(above_id_offset, 2)
        return (chain_id, v_bit + V_OFFSET)
