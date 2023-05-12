from hexbytes import (
    HexBytes,
)

from web3.datastructures import (
    AttributeDict,
)


def test_eth_tester_apply_withdrawals(w3):
    w3.provider.ethereum_tester.backend.apply_withdrawals(
        [
            {
                "index": 2**64 - 1,
                "validator_index": 2**64 - 1,
                "address": b"\x01" * 20,
                "amount": 2**64 - 1,
            },
            {
                "index": 1,
                "validator_index": 1,
                "address": b"\x02" * 20,
                "amount": 1,
            },
        ]
    )
    latest_block = w3.eth.get_block("latest")

    # check that `withdrawals_root` (snakecase) is converted to
    # `withdrawalsRoot` (camelcase) in the eth-tester middleware
    assert hasattr(latest_block, "withdrawalsRoot")
    assert latest_block["withdrawalsRoot"] == HexBytes(
        "0xb495df754a123dffeb8c2c0daf3f575a82987e8ff32676fdf6362ed52f1aa3d3"
    )
    assert hasattr(latest_block, "withdrawals")
    assert latest_block["withdrawals"] == [
        AttributeDict(
            {
                "index": 2**64 - 1,
                # check that `validator_index` (snakecase) is converted to
                # `validatorIndex` (camelcase) in the eth-tester middleware
                "validatorIndex": 2**64 - 1,
                "address": f"0x{'01' * 20}",  # bytes -> hex
                "amount": 2**64 - 1,
            }
        ),
        AttributeDict(
            {
                "index": 1,
                "validatorIndex": 1,  # snakecase -> camelcase
                "address": f"0x{'02' * 20}",  # bytes -> hex
                "amount": 1,
            }
        ),
    ]
