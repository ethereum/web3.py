# coding=utf-8

import pytest

from eth_account.messages import (
    defunct_hash_message,
)
from eth_utils import (
    is_checksum_address,
)
from hexbytes import (
    HexBytes,
)

from web3 import (
    Account,
    Web3,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.utils.encoding import (
    to_bytes,
    to_hex,
)
from web3.utils.toolz import (
    dissoc,
)

# from https://github.com/ethereum/tests/blob/3930ca3a9a377107d5792b3e7202f79c688f1a67/BasicTests/txtest.json # noqa: 501
ETH_TEST_TRANSACTIONS = [
    {
        "chainId": None,
        "key": "c85ef7d79691fe79573b1a7064c19c1a9819ebdbd1faaab1a8ec92344438aaf4",
        "nonce": 0,
        "gasPrice": 1000000000000,
        "gas": 10000,
        "to": "0x13978aee95f38490e9769C39B2773Ed763d9cd5F",
        "value": 10000000000000000,
        "data": "",
        "unsigned": "eb8085e8d4a510008227109413978aee95f38490e9769c39b2773ed763d9cd5f872386f26fc1000080808080",  # noqa: 501
        "signed": "f86b8085e8d4a510008227109413978aee95f38490e9769c39b2773ed763d9cd5f872386f26fc10000801ba0eab47c1a49bf2fe5d40e01d313900e19ca485867d462fe06e139e3a536c6d4f4a014a569d327dcda4b29f74f93c0e9729d2f49ad726e703f9cd90dbb0fbf6649f1"  # noqa: 501
    },
    {
        "chainId": None,
        "key": "c87f65ff3f271bf5dc8643484f66b200109caffe4bf98c4cb393dc35740b28c0",
        "nonce": 0,
        "gasPrice": 1000000000000,
        "gas": 10000,
        "to": "",
        "value": 0,
        "data": "6025515b525b600a37f260003556601b596020356000355760015b525b54602052f260255860005b525b54602052f2",  # noqa: 501
        "unsigned": "f83f8085e8d4a510008227108080af6025515b525b600a37f260003556601b596020356000355760015b525b54602052f260255860005b525b54602052f2808080",  # noqa: 501
        "signed": "f87f8085e8d4a510008227108080af6025515b525b600a37f260003556601b596020356000355760015b525b54602052f260255860005b525b54602052f21ba05afed0244d0da90b67cf8979b0f246432a5112c0d31e8d5eedd2bc17b171c694a0bb1035c834677c2e1185b8dc90ca6d1fa585ab3d7ef23707e1a497a98e752d1b"  # noqa: 501
    }
]


@pytest.fixture
def PRIVATE_BYTES():
    return b'unicorns' * 4


@pytest.fixture
def PRIVATE_BYTES_ALT(PRIVATE_BYTES):
    return b'rainbows' * 4


@pytest.fixture
def web3js_key():
    return '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'


@pytest.fixture
def web3js_password():
    return 'test!'


@pytest.fixture(params=['instance', 'class'])
def acct(request, web3):
    if request.param == 'instance':
        return web3.eth.account
    elif request.param == 'class':
        return Account
    raise Exception('Unreachable!')


@pytest.fixture()
def w3():
    return Web3(EthereumTesterProvider())


def test_eth_account_create_variation(acct):
    account1 = acct.create()
    account2 = acct.create()
    assert account1 != account2


def test_eth_account_privateKeyToAccount_reproducible(acct, PRIVATE_BYTES):
    account1 = acct.privateKeyToAccount(PRIVATE_BYTES)
    account2 = acct.privateKeyToAccount(PRIVATE_BYTES)
    assert bytes(account1) == PRIVATE_BYTES
    assert bytes(account1) == bytes(account2)
    assert isinstance(str(account1), str)


def test_eth_account_privateKeyToAccount_diverge(acct, PRIVATE_BYTES, PRIVATE_BYTES_ALT):
    account1 = acct.privateKeyToAccount(PRIVATE_BYTES)
    account2 = acct.privateKeyToAccount(PRIVATE_BYTES_ALT)
    assert bytes(account2) == PRIVATE_BYTES_ALT
    assert bytes(account1) != bytes(account2)


def test_eth_account_privateKeyToAccount_seed_restrictions(acct):
    with pytest.raises(ValueError):
        acct.privateKeyToAccount(b'')
    with pytest.raises(ValueError):
        acct.privateKeyToAccount(b'\xff' * 31)
    with pytest.raises(ValueError):
        acct.privateKeyToAccount(b'\xff' * 33)


def test_eth_account_privateKeyToAccount_properties(acct, PRIVATE_BYTES):
    account = acct.privateKeyToAccount(PRIVATE_BYTES)
    assert callable(account.signHash)
    assert callable(account.signTransaction)
    assert is_checksum_address(account.address)
    assert account.address == '0xa79F6f349C853F9Ea0B29636779ae3Cb4E3BA729'
    assert account.privateKey == PRIVATE_BYTES


def test_eth_account_create_properties(acct):
    account = acct.create()
    assert callable(account.signHash)
    assert callable(account.signTransaction)
    assert is_checksum_address(account.address)
    assert isinstance(account.privateKey, bytes) and len(account.privateKey) == 32


def test_eth_account_recover_transaction_example(acct):
    raw_tx_hex = '0xf8640d843b9aca00830e57e0945b2063246f2191f18f2675cedb8b28102e957458018025a00c753084e5a8290219324c1a3a86d4064ded2d15979b1ea790734aaa2ceaafc1a0229ca4538106819fd3a5509dd383e8fe4b731c6870339556a5c06feb9cf330bb'  # noqa: E501
    from_account = acct.recoverTransaction(raw_tx_hex)
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'


def test_eth_account_recover_transaction_with_literal(acct):
    raw_tx = 0xf8640d843b9aca00830e57e0945b2063246f2191f18f2675cedb8b28102e957458018025a00c753084e5a8290219324c1a3a86d4064ded2d15979b1ea790734aaa2ceaafc1a0229ca4538106819fd3a5509dd383e8fe4b731c6870339556a5c06feb9cf330bb  # noqa: E501
    from_account = acct.recoverTransaction(raw_tx)
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'


def test_eth_account_recover_message(acct):
    v, r, s = (
        28,
        '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
        '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce',
    )
    message = "I♥SF"
    message_hash = defunct_hash_message(text=message)
    from_account = acct.recoverHash(message_hash, vrs=(v, r, s))
    assert from_account == '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'


@pytest.mark.parametrize(
    'signature_bytes',
    [
        # test signature bytes with standard v (0 in this case)
        b'\x0cu0\x84\xe5\xa8)\x02\x192L\x1a:\x86\xd4\x06M\xed-\x15\x97\x9b\x1e\xa7\x90sJ\xaa,\xea\xaf\xc1"\x9c\xa4S\x81\x06\x81\x9f\xd3\xa5P\x9d\xd3\x83\xe8\xfeKs\x1chp3\x95V\xa5\xc0o\xeb\x9c\xf30\xbb\x00',  # noqa: E501
        # test signature bytes with chain-naive v (27 in this case)
        b'\x0cu0\x84\xe5\xa8)\x02\x192L\x1a:\x86\xd4\x06M\xed-\x15\x97\x9b\x1e\xa7\x90sJ\xaa,\xea\xaf\xc1"\x9c\xa4S\x81\x06\x81\x9f\xd3\xa5P\x9d\xd3\x83\xe8\xfeKs\x1chp3\x95V\xa5\xc0o\xeb\x9c\xf30\xbb\x1b',  # noqa: E501
    ],
    ids=['test_sig_bytes_standard_v', 'test_sig_bytes_chain_naive_v']
)
def test_eth_account_recover_signature_bytes(acct, signature_bytes):
    msg_hash = b'\xbb\r\x8a\xba\x9f\xf7\xa1<N,s{i\x81\x86r\x83{\xba\x9f\xe2\x1d\xaa\xdd\xb3\xd6\x01\xda\x00\xb7)\xa1'  # noqa: E501
    from_account = acct.recoverHash(msg_hash, signature=signature_bytes)
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'


def test_eth_account_recover_vrs(acct):
    v, r, s = (
        27,
        5634810156301565519126305729385531885322755941350706789683031279718535704513,
        15655399131600894366408541311673616702363115109327707006109616887384920764603,
    )
    msg_hash = b'\xbb\r\x8a\xba\x9f\xf7\xa1<N,s{i\x81\x86r\x83{\xba\x9f\xe2\x1d\xaa\xdd\xb3\xd6\x01\xda\x00\xb7)\xa1'  # noqa: E501
    from_account = acct.recoverHash(msg_hash, vrs=(v, r, s))
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'

    from_account = acct.recoverHash(msg_hash, vrs=map(to_hex, (v, r, s)))
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'


def test_eth_account_recover_vrs_standard_v(acct):
    v, r, s = (
        0,
        5634810156301565519126305729385531885322755941350706789683031279718535704513,
        15655399131600894366408541311673616702363115109327707006109616887384920764603,
    )
    msg_hash = b'\xbb\r\x8a\xba\x9f\xf7\xa1<N,s{i\x81\x86r\x83{\xba\x9f\xe2\x1d\xaa\xdd\xb3\xd6\x01\xda\x00\xb7)\xa1'  # noqa: E501
    from_account = acct.recoverHash(msg_hash, vrs=(v, r, s))
    assert from_account == '0xFeC2079e80465cc8C687fFF9EE6386ca447aFec4'


@pytest.mark.parametrize(
    'message, key, expected_bytes, expected_hash, v, r, s, signature',
    (
        (
            'Some data',
            '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318',
            b'Some data',
            HexBytes('0x1da44b586eb0729ff70a73c326926f6ed5a25f5b056e7f47fbc6e58d86871655'),
            28,
            83713930994764734002432606962255364472443135907807238282514898577139886061053,
            43435997768575461196683613590576722655951133545204789519877940758262837256233,
            HexBytes('0xb91467e570a6466aa9e9876cbcd013baba02900b8979d43fe208a4a4f339f5fd6007e74cd82e037b800186422fc2da167c747ef045e5d18a5f5d4300f8e1a0291c'),  # noqa: E501
        ),
        (
            '10284',
            '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318',
            b'10284',
            HexBytes('0x0a162a5efbba02f38db3114531c8acba39fe676f09f7e471d93e8a06c471821c'),
            27,
            143748089818580655331728101695676826715814583506606354117109114714663470502,
            227853308212209543997879651656855994238138056366857653269155208245074180053,
            HexBytes('0x00515bc8fd32264e21ec0820e8c5123ed58c1195c9ea17cb018b1ad4073cc5a60080f5dcec397a5a8c523082bfa41771568903aa554ec06ba8475ca9050fb7d51b'),  # noqa: E501
        ),

    ),
    ids=['web3js_example', '31byte_r_and_s'],
)
def test_eth_account_sign(acct, message, key, expected_bytes, expected_hash, v, r, s, signature):
    message_hash = defunct_hash_message(text=message)
    assert message_hash == expected_hash

    signed = acct.signHash(message_hash, private_key=key)
    assert signed.messageHash == expected_hash
    assert signed.v == v
    assert signed.r == r
    assert signed.s == s
    assert signed.signature == signature

    account = acct.privateKeyToAccount(key)
    assert account.signHash(message_hash) == signed


@pytest.mark.parametrize(
    'txn, private_key, expected_raw_tx, tx_hash, r, s, v',
    (
        (
            {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 1000000000,
                'gas': 2000000,
                'gasPrice': 234567897654321,
                'nonce': 0,
                'chainId': 1
            },
            '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318',
            HexBytes('0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428'),  # noqa: E501
            HexBytes('0xd8f64a42b57be0d565f385378db2f6bf324ce14a594afc05de90436e9ce01f60'),
            4487286261793418179817841024889747115779324305375823110249149479905075174044,
            30785525769477805655994251009256770582792548537338581640010273753578382951464,
            37,
        ),
        (
            {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 0,
                'gas': 31853,
                'gasPrice': 0,
                'nonce': 0,
                'chainId': 1
            },
            '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318',
            HexBytes('0xf85d8080827c6d94f0109fc8df283027b6285cc889f5aa624eac1f558080269f22f17b38af35286ffbb0c6376c86ec91c20ecbad93f84913a0cc15e7580cd99f83d6e12e82e3544cb4439964d5087da78f74cefeec9a450b16ae179fd8fe20'),  # noqa: E501
            HexBytes('0xb0c5e2c6b29eeb0b9c1d63eaa8b0f93c02ead18ae01cb7fc795b0612d3e9d55a'),
            61739443115046231975538240097110168545680205678104352478922255527799426265,
            232940010090391255679819602567388136081614408698362277324138554019997613600,
            38,
        ),
    ),
    ids=['web3js_example', '31byte_r_and_s'],
)
def test_eth_account_sign_transaction(acct, txn, private_key, expected_raw_tx, tx_hash, r, s, v):
    signed = acct.signTransaction(txn, private_key)
    assert signed.r == r
    assert signed.s == s
    assert signed.v == v
    assert signed.rawTransaction == expected_raw_tx
    assert signed.hash == tx_hash

    account = acct.privateKeyToAccount(private_key)
    assert account.signTransaction(txn) == signed


@pytest.mark.parametrize(
    'transaction_info',
    ETH_TEST_TRANSACTIONS,
)
def test_eth_account_sign_transaction_from_eth_test(acct, transaction_info):
    expected_raw_txn = transaction_info['signed']
    key = transaction_info['key']

    transaction = dissoc(transaction_info, 'signed', 'key', 'unsigned')

    # validate r, in order to validate the transaction hash
    # There is some ambiguity about whether `r` will always be deterministically
    # generated from the transaction hash and private key, mostly due to code
    # author's ignorance. The example test fixtures and implementations seem to agree, so far.
    # See ecdsa_raw_sign() in /eth_keys/backends/native/ecdsa.py
    signed = acct.signTransaction(transaction, key)
    assert signed.r == Web3.toInt(hexstr=expected_raw_txn[-130:-66])

    # confirm that signed transaction can be recovered to the sender
    expected_sender = acct.privateKeyToAccount(key).address
    assert acct.recoverTransaction(signed.rawTransaction) == expected_sender


@pytest.mark.parametrize(
    'transaction',
    ETH_TEST_TRANSACTIONS,
)
def test_eth_account_recover_transaction_from_eth_test(acct, transaction):
    raw_txn = transaction['signed']
    key = transaction['key']
    expected_sender = acct.privateKeyToAccount(key).address
    assert acct.recoverTransaction(raw_txn) == expected_sender


def test_eth_account_encrypt(acct, web3js_key, web3js_password):
    encrypted = acct.encrypt(web3js_key, web3js_password)

    assert encrypted['address'] == '2c7536e3605d9c16a7a3d7b1898e529396a65c23'
    assert encrypted['version'] == 3

    decrypted_key = acct.decrypt(encrypted, web3js_password)

    assert decrypted_key == to_bytes(hexstr=web3js_key)


def test_eth_account_prepared_encrypt(acct, web3js_key, web3js_password):
    account = acct.privateKeyToAccount(web3js_key)
    encrypted = account.encrypt(web3js_password)

    assert encrypted['address'] == '2c7536e3605d9c16a7a3d7b1898e529396a65c23'
    assert encrypted['version'] == 3

    decrypted_key = acct.decrypt(encrypted, web3js_password)

    assert decrypted_key == to_bytes(hexstr=web3js_key)


@pytest.mark.xfail
@pytest.mark.parametrize(
    'expected_txn, raw_tx, expected_tx_hash, r, s, v',
    (
        (
            {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 1000000000,
                'gas': 2000000,
                'gasPrice': 234567897654321,
                'nonce': 0,
                'chainId': 1
            },
            HexBytes('0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428'),  # noqa: E501
            HexBytes('0xd8f64a42b57be0d565f385378db2f6bf324ce14a594afc05de90436e9ce01f60'),
            4487286261793418179817841024889747115779324305375823110249149479905075174044,
            30785525769477805655994251009256770582792548537338581640010273753578382951464,
            37,
        ),
        (
            {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 0,
                'gas': 31853,
                'gasPrice': 0,
                'nonce': 0,
                'chainId': 1
            },
            HexBytes('0xf85d8080827c6d94f0109fc8df283027b6285cc889f5aa624eac1f558080269f22f17b38af35286ffbb0c6376c86ec91c20ecbad93f84913a0cc15e7580cd99f83d6e12e82e3544cb4439964d5087da78f74cefeec9a450b16ae179fd8fe20'),  # noqa: E501
            HexBytes('0xb0c5e2c6b29eeb0b9c1d63eaa8b0f93c02ead18ae01cb7fc795b0612d3e9d55a'),
            61739443115046231975538240097110168545680205678104352478922255527799426265,
            232940010090391255679819602567388136081614408698362277324138554019997613600,
            38,
        ),
    ),
    ids=['web3js_example', '31byte_r_and_s'],
)
def test_eth_account_sign_and_send_EIP155_transaction_to_eth_tester(
        w3,
        expected_txn,
        raw_tx,
        expected_tx_hash,
        r, s, v):
    actual_tx_hash = w3.eth.sendRawTransaction(raw_tx)
    assert actual_tx_hash == expected_tx_hash
    actual_txn = w3.eth.getTransaction(actual_tx_hash)
    for key in ('to', 'nonce', 'gas', 'gasPrice', 'value', ):
        assert actual_txn[key] == expected_txn[key]
    assert actual_txn.r == r
    assert actual_txn.s == s
    assert actual_txn.v == v
