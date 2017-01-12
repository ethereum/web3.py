import pytest

from web3.exceptions import ArgumentEncodeError


def test_bad_constructor_input_encoding(StringContract):
    """Deploying a contract with bad ABI signature should give a friendly exception."""

    with pytest.raises(ArgumentEncodeError):
        # web3.exceptions.ArgumentEncodeError: Cannot encode 1. argument of
        StringContract.deploy(args=[None])


