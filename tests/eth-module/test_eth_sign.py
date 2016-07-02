from secp256k1 import PrivateKey
from rlp.utils import decode_hex

from ethereum.utils import privtoaddr

from eth_tester_client.utils import (
    mk_random_privkey,
    encode_address,
    encode_data,
    encode_32bytes,
    decode_hex,
)

from web3.web3.rpcprovider import TestRPCProvider


def test_eth_sign(web3):
    private_key_hex = b'0x5e95384d8050109aab08c1922d3c230739bc16976553c317e5d0b87b59371f2a'
    private_key = decode_hex(private_key)
    address = web3.personal.importRawKey(private_key, "password")
    web3.personal.unlockAccount(address, "password")

    data = '1234567890abcdefghijklmnopqrstuvwxyz'
    data_hash = web3.sha3(data)

    signed_data = web3.eth.sign(address, data_hash)

    assert False, "TODO"
    pk = PrivateKey(private_key)
    pk.public_key = pk.ecdsa_recover(
        rawhash,
        pk.ecdsa_recoverable_deserialize(
            zpad(utils.bytearray_to_bytestr(int_to_32bytearray(self.r)), 32) + zpad(utils.bytearray_to_bytestr(int_to_32bytearray(self.s)), 32),
            self.v - 27
        ),
        raw=True
    )
    pub = pk.serialize(compressed=False)
    assert expected == signed_data
