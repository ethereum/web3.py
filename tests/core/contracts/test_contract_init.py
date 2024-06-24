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
def math_addr(math_contract_factory, address_conversion_func):
    w3 = math_contract_factory.w3
    deploy_txn = math_contract_factory.constructor().transact(
        {"from": w3.eth.default_account}
    )
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    return address_conversion_func(deploy_receipt["contractAddress"])


def test_contract_with_unset_address(math_contract_factory):
    with contract_ens_addresses(math_contract_factory, []):
        with pytest.raises(NameNotFound):
            math_contract_factory(address="unsetname.eth")


def test_contract_with_name_address(math_contract_factory, math_addr):
    with contract_ens_addresses(math_contract_factory, [("thedao.eth", math_addr)]):
        mc = math_contract_factory(address="thedao.eth")
        caller = mc.w3.eth.default_account
        assert mc.address == "thedao.eth"
        assert mc.functions.return13().call({"from": caller}) == 13


def test_contract_with_name_address_from_eth_contract(
    w3,
    math_contract_abi,
    math_contract_bytecode,
    math_contract_runtime,
    math_addr,
):
    with ens_addresses(w3, [("thedao.eth", math_addr)]):
        mc = w3.eth.contract(
            address="thedao.eth",
            abi=math_contract_abi,
            bytecode=math_contract_bytecode,
            bytecode_runtime=math_contract_runtime,
        )

        assert mc.address == "thedao.eth"
        assert mc.functions.return13().call({"from": mc.w3.eth.default_account}) == 13


def test_contract_with_name_address_changing(math_contract_factory, math_addr):
    # Contract address is validated once on creation
    with contract_ens_addresses(math_contract_factory, [("thedao.eth", math_addr)]):
        mc = math_contract_factory(address="thedao.eth")

    caller = mc.w3.eth.default_account
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
