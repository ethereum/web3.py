import pytest

from web3._utils.ens import (
    contract_ens_addresses,
    ens_addresses,
)
from web3.exceptions import (
    BadFunctionCallOutput,
    NameNotFound,
)


@pytest.fixture()
def math_addr(MathContract, address_conversion_func):
    w3 = MathContract.w3
    deploy_txn = MathContract.constructor().transact({"from": w3.eth.coinbase})
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    return address_conversion_func(deploy_receipt["contractAddress"])


def test_contract_with_unset_address(MathContract):
    with contract_ens_addresses(MathContract, []):
        with pytest.raises(NameNotFound):
            MathContract(address="unsetname.eth")


def test_contract_with_name_address(MathContract, math_addr):
    with contract_ens_addresses(MathContract, [("thedao.eth", math_addr)]):
        mc = MathContract(address="thedao.eth")
        caller = mc.w3.eth.coinbase
        assert mc.address == "thedao.eth"
        assert mc.functions.return13().call({"from": caller}) == 13


def test_contract_with_name_address_from_eth_contract(
    w3,
    MATH_ABI,
    MATH_CODE,
    MATH_RUNTIME,
    math_addr,
):
    with ens_addresses(w3, [("thedao.eth", math_addr)]):
        mc = w3.eth.contract(
            address="thedao.eth",
            abi=MATH_ABI,
            bytecode=MATH_CODE,
            bytecode_runtime=MATH_RUNTIME,
        )

        caller = mc.w3.eth.coinbase
        assert mc.address == "thedao.eth"
        assert mc.functions.return13().call({"from": caller}) == 13


def test_contract_with_name_address_changing(MathContract, math_addr):
    # Contract address is validated once on creation
    with contract_ens_addresses(MathContract, [("thedao.eth", math_addr)]):
        mc = MathContract(address="thedao.eth")

    caller = mc.w3.eth.coinbase
    assert mc.address == "thedao.eth"

    # what happens when name returns no address at all
    with contract_ens_addresses(mc, []):
        with pytest.raises(NameNotFound):
            mc.functions.return13().call({"from": caller})

    # what happens when name returns address to different contract
    with contract_ens_addresses(mc, [("thedao.eth", "0x" + "11" * 20)]):
        with pytest.raises(BadFunctionCallOutput):
            mc.functions.return13().call({"from": caller})

    # contract works again when name resolves correctly
    with contract_ens_addresses(mc, [("thedao.eth", math_addr)]):
        assert mc.functions.return13().call({"from": caller}) == 13
