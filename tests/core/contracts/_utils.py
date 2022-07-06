import asyncio

from eth_utils.toolz import (
    identity,
)


def deploy(w3, Contract, apply_func=identity, args=None):
    args = args or []
    deploy_txn = Contract.constructor(*args).transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt["contractAddress"])
    contract = Contract(address=address)
    assert contract.address == address
    assert len(w3.eth.get_code(contract.address)) > 0
    return contract


async def async_deploy(async_web3, Contract, apply_func=identity, args=None):
    args = args or []
    deploy_txn = await Contract.constructor(*args).transact()
    deploy_receipt = await async_web3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt["contractAddress"])
    contract = Contract(address=address)
    assert contract.address == address
    assert len(await async_web3.eth.get_code(contract.address)) > 0
    return contract


def async_partial(f, *args, **kwargs):
    async def f2(*args2, **kwargs2):
        result = f(*args, *args2, **kwargs, **kwargs2)
        if asyncio.iscoroutinefunction(f):
            result = await result
        return result

    return f2
