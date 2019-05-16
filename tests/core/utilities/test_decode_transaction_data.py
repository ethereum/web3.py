from web3._utils.contracts import (
    encode_transaction_data,
    decode_transaction_data,
)

from .test_abi import (
    TEST_FUNCTION_ABI,
    GET_ABI_INPUTS_OUTPUT,
)


def test_decode_transaction_data():
    fn_abi = TEST_FUNCTION_ABI
    args = GET_ABI_INPUTS_OUTPUT[1]
    data = encode_transaction_data(None, 'f', fn_abi=fn_abi, args=args)
    assert decode_transaction_data(TEST_FUNCTION_ABI, data) == args
