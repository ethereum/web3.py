import pytest

from secp256k1 import PrivateKey, PublicKey, ALL_FLAGS

from bitcoin import encode_pubkey

from ethereum.utils import privtoaddr

from eth_utils import (
    force_bytes,
    force_text,
    coerce_return_to_bytes,
    coerce_return_to_text,
    coerce_args_to_bytes,
    keccak,
    is_string,
    add_0x_prefix,
    encode_hex,
    decode_hex,
)


@coerce_return_to_bytes
def sha3(s):
    return encode_hex(keccak(s))


assert sha3(b'') == b'0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'


@coerce_args_to_bytes
@coerce_return_to_text
def extract_ecdsa_signer(msg_hash, signature):
    msg_hash_bytes = decode_hex(msg_hash) if msg_hash.startswith(b'0x') else msg_hash
    signature_bytes = decode_hex(signature) if signature.startswith(b'0x') else signature

    pk = PublicKey(flags=ALL_FLAGS)
    rec_id = signature_bytes[64]
    if is_string(rec_id):
        rec_id = ord(rec_id)
    pk.public_key = pk.ecdsa_recover(
        msg_hash_bytes,
        pk.ecdsa_recoverable_deserialize(
            signature_bytes[:64], rec_id,
        ),
        raw=True,
    )
    pk_serialized = pk.serialize(compressed=False)
    address = add_0x_prefix(sha3(encode_pubkey(pk_serialized, 'bin')[1:])[-40:])
    return address


def test_eth_sign(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    private_key_hex = '0x5e95384d8050109aab08c1922d3c230739bc16976553c317e5d0b87b59371f2a'
    private_key = decode_hex(private_key_hex)

    # This imports the private key into the running geth instance and unlocks
    # the account so that it can sign things.
    # `0xa5df35f30ba0ce878b1061ae086289adff3ba1e0`
    address = web3.personal.importRawKey(private_key, "password")
    web3.personal.unlockAccount(address, "password")

    assert add_0x_prefix(encode_hex(privtoaddr(private_key))) == add_0x_prefix(address)
    assert address == '0xa5df35f30ba0ce878b1061ae086289adff3ba1e0'

    # the data to be signed
    data = b'1234567890abcdefghijklmnopqrstuvwxyz'
    # the hash of the data `0x089c33d56ed10bd8b571a0f493cedb28db1ae0f40c6cd266243001528c06eab3`
    data_hash = web3.sha3(data, encoding=None)
    data_hash_bytes = decode_hex(data_hash)

    assert force_bytes(data_hash) == sha3(data)

    priv_key = PrivateKey(flags=ALL_FLAGS)
    priv_key.set_raw_privkey(private_key)

    # sanit check the extract_ecdsa_signer function works as expected.
    vector_sig = priv_key.ecdsa_sign_recoverable(data_hash_bytes, raw=True, digest=sha3_256)
    vector_sig_bytes, rec_id = priv_key.ecdsa_recoverable_serialize(vector_sig)
    vector_sig_bytes_full = vector_sig_bytes + force_bytes(chr(rec_id))
    vector_address = force_text(extract_ecdsa_signer(data_hash_bytes, vector_sig_bytes_full))

    assert vector_address == address

    # Now have geth sign some data.
    signature_hex = web3.eth.sign(address, data)
    signature_bytes = decode_hex(signature_hex)

    actual_signer = extract_ecdsa_signer(data_hash_bytes, signature_bytes)

    assert actual_signer == address

    # Verify the signature against the public key derived from the
    # original private key.  It fails.
    rec_id = signature_bytes[64]
    if is_string(rec_id):
        rec_id = ord(rec_id)
    recoverable_signature = priv_key.ecdsa_recoverable_deserialize(
        signature_bytes[:64],
        rec_id,
    )
    signature = priv_key.ecdsa_recoverable_convert(recoverable_signature)
    is_valid = priv_key.pubkey.ecdsa_verify(
        msg=data,
        raw_sig=signature,
        digest=sha3_256,
    )

    assert is_valid
