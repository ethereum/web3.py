from eth_utils import (
    keccak,
)
import rlp
from rlp.sedes import (
    Binary,
    big_endian_int,
)

from web3._utils.encoding import (
    pad_bytes,
    pad_hex,
)


def storage_position(map_key_hex, position_hex):
    '''
    https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_getstorageat
    Returns the patricia trie key (position) of a mapping's key.
    This helper function is used for formating arguments to eth_getStorageAt
    and eth_getProof.
    @param map_key_hex is the key stored in a map
    @param position_hex is the position where the mapping variable is defined
        in the contract
    '''
    key = pad_hex(map_key_hex, 256)[2:] + pad_hex(position_hex, 256)[2:]
    return keccak(bytes.fromhex(key)).hex()


nibble_to_number = {}
for i, c in enumerate('0123456789abcdef'):
    nibble_to_number[c] = i


class _Account(rlp.Serializable):
    fields = [
        ('nonce', big_endian_int),
        ('balance', big_endian_int),
        ('storage', Binary.fixed_length(32, allow_empty=True)),
        ('code_hash', Binary.fixed_length(32))
    ]


def verify_eth_getProof(proof, root):
    '''
    Verify that a proof returned by eth_getProof is valid for the given
    Patricia tree state root.
    @param proof is a proof returned by eth_getProof
    @param root is a Patricia tree state root returned by w3.eth.getBlock('latest').stateRoot
    '''
    acc = _Account(proof.nonce,
                   proof.balance,
                   proof.storageHash,
                   proof.codeHash)
    expected_value = rlp.encode(acc)
    addr = proof.address[2:]
    trie_key = keccak(bytes.fromhex(addr)).hex()
    account_proof = proof.accountProof
    if not _verify(root, trie_key, account_proof,
                   0, 0,
                   expected_value):
        return False
    for storage_proof in proof.storageProof:
        trie_key = keccak(pad_bytes(b'\x00', 32, storage_proof.key)).hex()
        root = proof.storageHash
        expected_value = rlp.encode(storage_proof.value)
        if not _verify(root, trie_key, storage_proof.proof,
                       0, 0,
                       expected_value):
            return False
    return True


def _verify(expected_root, key, proof, key_index, proof_index, expected_value):
    ''' Iterate the proof following the key.
        Return True if the value at the leaf is equal to the expected value.
        @param expected_root is the expected root of the current proof node.
        @param key is the key for which we are proving the value.
        @param proof is the proof the key nibbles as path.
        @param key_index keeps track of the index while stepping through
            the key nibbles.
        @param proof_index keeps track of the index while stepping through
            the proof nodes.
        @param expected_value is the key's value expected to be stored in
            the last node (leaf node) of the proof.
    '''
    node = proof[proof_index]
    if keccak(node) != expected_root:
        return False
    dec = rlp.decode(node)
    if len(dec) == 17:
        # branch node
        new_expected_root = dec[nibble_to_number[key[key_index]]]
        return _verify(new_expected_root, key, proof, key_index + 1, proof_index + 1,
                       expected_value)
    elif len(dec) == 2:
        # leaf or extension node
        # get prefix and optional nibble from the first byte
        (prefix, nibble) = dec[0][:1].hex()
        if prefix == '2':
            # even leaf node
            key_end = dec[0][1:].hex()
            if key_end == key[key_index:] and expected_value == dec[1]:
                return True
        elif prefix == '3':
            # odd leaf node
            key_end = nibble + dec[0][1:].hex()
            if key_end == key[key_index:] and expected_value == dec[1]:
                return True
        elif prefix == '0':
            # even extension node
            shared_nibbles = dec[0][1:].hex()
            extension_length = len(shared_nibbles)
            if shared_nibbles != key[key_index:key_index + extension_length]:
                return False
            new_expected_root = dec[1]
            return _verify(new_expected_root, key, proof,
                           key_index + extension_length, proof_index + 1,
                           expected_value)
        elif prefix == '1':
            # odd extension node
            shared_nibbles = nibble + dec[0][1:].hex()
            extension_length = len(shared_nibbles)
            if shared_nibbles != key[key_index:key_index + extension_length]:
                return False
            new_expected_root = dec[1]
            return _verify(new_expected_root, key, proof,
                           key_index + extension_length, proof_index + 1,
                           expected_value)
        else:
            # This should not be reached if the proof has the correct format
            assert False
    return False
