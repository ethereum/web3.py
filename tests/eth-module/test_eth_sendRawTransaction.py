import rlp

from ethereum.transactions import Transaction
from ethereum.utils import privtoaddr

from testrpc.client.utils import (
    mk_random_privkey,
    encode_address,
    encode_data,
)


def test_eth_sendRawTransaction(web3, wait_for_transaction, extra_accounts):
    private_key = mk_random_privkey()
    address = encode_address(privtoaddr(private_key))

    funding_txn_hash = web3.eth.sendTransaction({
        "from": web3.eth.coinbase,
        "to": address,
        "value": 10000000000000000,
    })
    wait_for_transaction(web3, funding_txn_hash)

    # ethereum-tester-client doesn't quite implement the
    # `sendRawTransaction` correctly because of how the underlying tester
    # evm works.  It needs to know about the address for this to work.
    web3.personal.importRawKey(private_key, "password")
    web3.personal.unlockAccount(address, "password")

    initial_balance = web3.eth.getBalance(extra_accounts[1])

    tx = Transaction(
        web3.eth.getTransactionCount(address),
        web3.eth.gasPrice,
        100000,
        extra_accounts[1],
        1234,
        '',
    )
    tx.sign(private_key)

    raw_tx = rlp.encode(tx)
    raw_tx_hex = encode_data(raw_tx)

    txn_hash = web3.eth.sendRawTransaction(raw_tx_hex)
    wait_for_transaction(web3, txn_hash)
    txn_receipt = web3.eth.getTransactionReceipt(txn_hash)

    after_balance = web3.eth.getBalance(extra_accounts[1])

    assert after_balance - initial_balance == 1234
