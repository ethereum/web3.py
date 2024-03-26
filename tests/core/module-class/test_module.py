import pytest

from web3 import (
    EthereumTesterProvider,
    Web3,
)
from web3.method import (
    Method,
)


@pytest.fixture
def web3_with_external_modules(module1, module2, module3):
    return Web3(
        EthereumTesterProvider(),
        external_modules={
            "module1": module1,
            "module2": (
                module2,
                {
                    "submodule1": module3,
                },
            ),
        },
    )


def test_attach_methods_to_module(web3_with_external_modules):
    w3 = web3_with_external_modules

    w3.module1.attach_methods(
        {
            # set `property1` on `module1` with `eth_chainId` RPC endpoint
            "property1": Method("eth_chainId", is_property=True),
            # set `method1` on `module1` with `eth_getBalance` RPC endpoint
            "method1": Method("eth_getBalance"),
        }
    )

    assert w3.eth.chain_id == 131277322940537
    assert w3.module1.property1 == 131277322940537

    account = w3.eth.accounts[0]
    assert w3.eth.get_balance(account, "latest") == 1000000000000000000000000
    assert w3.module1.method1(account, "latest") == 1000000000000000000000000

    w3.module2.submodule1.attach_methods(
        {
            # set `method2` on `module2.submodule1` with `eth_blockNumber` RPC endpoint
            "method2": Method("eth_blockNumber", is_property=True)
        }
    )

    assert w3.eth.block_number == 0
    assert w3.module2.submodule1.method2 == 0

    w3.eth.attach_methods({"get_block2": Method("eth_getBlockByNumber")})

    assert w3.eth.get_block("latest")["number"] == 0
    assert w3.eth.get_block("pending")["number"] == 1

    assert w3.eth.get_block2("latest")["number"] == 0
    assert w3.eth.get_block2("pending")["number"] == 1


def test_attach_methods_with_mungers(web3_with_external_modules):
    w3 = web3_with_external_modules

    # `method1` uses `eth_getBlockByNumber` but makes use of unique mungers
    w3.module1.attach_methods(
        {
            "method1": Method(
                "eth_getBlockByNumber",
                mungers=[
                    lambda _method, block_id, full_transactions: (
                        block_id,
                        full_transactions,
                    ),
                    # take the user-provided `block_id` and subtract 1
                    lambda _method, block_id, full_transactions: (
                        block_id - 1,
                        full_transactions,
                    ),
                ],
            ),
        }
    )

    w3.provider.ethereum_tester.mine_block()
    assert w3.eth.get_block(0, False)["baseFeePerGas"] == 1000000000
    assert w3.eth.get_block(1, False)["baseFeePerGas"] == 875000000

    # Testing the mungers work:
    # `method1` also calls 'eth_getBlockByNumber' but subtracts 1
    # from the user-provided `block_id`
    # due to the second munger. So, `0` from above is a `1` here and `1` is `2`.
    assert w3.module1.method1(1, False)["baseFeePerGas"] == 1000000000
    assert w3.module1.method1(2, False)["baseFeePerGas"] == 875000000
