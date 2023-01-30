from eth_utils.toolz import (
    identity,
)


def deploy(w3, contract_factory, apply_func=identity, args=None):
    args = args or []
    deploy_txn = contract_factory.constructor(*args).transact()
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt["contractAddress"])
    contract = contract_factory(address=address)
    assert contract.address == address
    assert len(w3.eth.get_code(contract.address)) > 0
    return contract


async def async_deploy(async_web3, contract_factory, apply_func=identity, args=None):
    args = args or []
    deploy_txn = await contract_factory.constructor(*args).transact()
    deploy_receipt = await async_web3.eth.wait_for_transaction_receipt(deploy_txn)
    assert deploy_receipt is not None
    address = apply_func(deploy_receipt["contractAddress"])
    contract = contract_factory(address=address)
    assert contract.address == address
    assert len(await async_web3.eth.get_code(contract.address)) > 0
    return contract
