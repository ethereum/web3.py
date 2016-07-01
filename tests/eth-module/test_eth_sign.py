from rlp.utils import decode_hex

from ethereum.utils import privtoaddr

from eth_tester_client.utils import (
    mk_random_privkey,
    encode_address,
    encode_data,
    encode_32bytes,
)

from web3.web3.rpcprovider import TestRPCProvider


def test_eth_sign(web3):
    private_key = mk_random_privkey()
    address = web3.personal.importRawKey(private_key, "password")
    web3.personal.unlockAccount(address, "password")

    data = '1234567890abcdefghijklmnopqrstuvwxyz'

    signed_data = web3.eth.sign(address, data)

    # TODO: verify signature
    assert False, signed_data
