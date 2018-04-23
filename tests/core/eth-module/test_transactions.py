import pytest

from web3.exceptions import (
    ValidationError,
)
from web3.middleware.simulate_unmined_transaction import (
    unmined_receipt_simulator_middleware,
)


@pytest.mark.parametrize(
    'make_chain_id, expect_success',
    (
        (
            lambda web3: web3.net.chainId,
            True,
        ),
        pytest.param(
            lambda web3: 999999999999,
            False,
            marks=pytest.mark.xfail,
        ),
    ),
)
def test_send_transaction_with_valid_chain_id(web3, make_chain_id, expect_success):
    transaction = {
        'to': web3.eth.accounts[1],
        'chainId': make_chain_id(web3),
    }
    if expect_success:
        # just be happy that we didn't crash
        web3.eth.sendTransaction(transaction)
    else:
        with pytest.raises(ValidationError) as exc_info:
            web3.eth.sendTransaction(transaction)

        assert 'chain ID' in str(exc_info.value)


def test_unmined_transaction_wait_for_receipt(web3, extra_accounts):
    web3.middleware_stack.add(unmined_receipt_simulator_middleware)
    txn_hash = web3.eth.sendTransaction({
        'from': web3.eth.coinbase,
        'to': '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
        'value': 123457
    })
    assert web3.eth.getTransactionReceipt(txn_hash) is None

    txn_receipt = web3.eth.waitForTransactionReceipt(txn_hash)
    assert txn_receipt['transactionHash'] == txn_hash
    assert txn_receipt['blockHash'] is not None
