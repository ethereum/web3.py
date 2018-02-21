import pytest

from web3.exceptions import (
    ValidationError,
)


@pytest.mark.parametrize(
    'make_chain_id, expect_success',
    (
        (
            lambda web3: web3.version.network,
            True,
        ),
        (
            lambda web3: int(web3.version.network),
            True,
        ),
        (
            lambda web3: int(web3.version.network) + 1,
            False,
        ),
        (
            lambda web3: str(int(web3.version.network) + 1),
            False,
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
