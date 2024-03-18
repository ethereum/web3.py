import pytest

from web3.exceptions import (
    Web3Exception,
)


def test_web3exception_with_user_message():
    with pytest.raises(Web3Exception) as exception:
        raise Web3Exception(user_message="This failed!")
    assert exception.type is Web3Exception
    assert exception.value.user_message == "This failed!"


def test_web3exception_with_kwargs():
    with pytest.raises(TypeError) as exception:
        raise Web3Exception(data={"message": "Unable to fulfill your request."})

    # For Python > 3.9, str exception includes 'Web3Exception.'
    expected = "__init__() got an unexpected keyword argument 'data'"
    actual = str(exception.value)
    assert exception.type is TypeError
    assert hasattr(exception.value, "data") is False
    assert expected in actual


def test_web3exception_with_args():
    with pytest.raises(Web3Exception) as exception:
        raise Web3Exception("failed")
    assert exception.type is Web3Exception
    assert exception.value.user_message is None
    assert exception.value.args[0] == "failed"
