import pytest

from web3.contract.utils import (
    get_function_info,
)


def get_contract_fn_abi(fn_name, args, kwargs, contract_abi):
    fn_abis_with_name = [abi for abi in contract_abi if abi["name"] == fn_name]

    # match function by args
    if len(args) > 0:
        for abi in fn_abis_with_name:
            if len(abi["inputs"]) == len(args):
                return abi

    # match function by kwargs
    if len(kwargs.keys()) > 0:
        for abi in fn_abis_with_name:
            inputs = [input["name"] for input in abi["inputs"]]
            if set(inputs) == kwargs.keys():
                return abi

    return fn_abis_with_name[0]


@pytest.mark.parametrize(
    "fn_name,args,kwargs,fn_selector,fn_arguments",
    [
        ("add", (1, 2), {}, "0xa5f3c23b", (1, 2)),
        ("counter", (), {}, "0x61bc221a", ()),
        ("incrementCounter", (), {}, "0x5b34b966", ()),
        ("incrementCounter", (), {"amount": 1}, "0x6abbb3b4", (1,)),
        ("incrementCounter", (1,), {}, "0x6abbb3b4", (1,)),
        ("multiply7", (100,), {}, "0xdcf537b1", (100,)),
        ("return13", (), {}, "0x16216f39", ()),
    ],
)
def test_get_function_info_for_math_contract(
    w3, math_contract_abi, fn_name, args, kwargs, fn_selector, fn_arguments
):
    fn_info_abi, fn_info_selector, fn_info_arguments = get_function_info(
        # fn_info = get_function_info(
        fn_name,
        w3.codec,
        contract_abi=math_contract_abi,
        args=args,
        kwargs=kwargs,
    )

    # Identify abi for fn_name from math_contract_abi
    fn_abi = get_contract_fn_abi(fn_name, args, kwargs, math_contract_abi)

    assert fn_info_abi == fn_abi
    assert fn_info_selector == fn_selector
    assert len(fn_info_arguments) == len(fn_arguments)
    assert fn_info_arguments == fn_arguments
