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
    private_key = decode_hex(private_key_hex)
    address = web3.personal.importRawKey(private_key, "password")
    web3.personal.unlockAccount(address, "password")

    data = b'1234567890abcdefghijklmnopqrstuvwxyz'
    data_hash = web3.sha3(data)

    signature_hex = web3.eth.sign(address, data_hash)
    signature_bytes = decode_hex(signature_hex)

    assert False
    import ipdb; ipdb.set_trace()
    priv_key = PrivateKey(private_key, raw=True)
    pub_key = priv_key.pubkey
    signature = pub_key.ecdsa_deserialize_compact(signature_bytes)
    is_valid = pub_key.ecdsa_verify(
        msg=data,
        raw_sig=signature
    )

    assert expected == signed_data
