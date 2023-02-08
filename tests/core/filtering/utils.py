from web3 import (
    Web3,
)
from web3.eth import (
    AsyncEth,
)
from web3.middleware import (
    async_local_filter_middleware,
    local_filter_middleware,
)
from web3.providers.eth_tester import (
    AsyncEthereumTesterProvider,
    EthereumTesterProvider,
)


def _w3_fixture_logic(request):
    use_filter_middleware = request.param
    provider = EthereumTesterProvider()
    w3 = Web3(provider)
    if use_filter_middleware:
        w3.middleware_onion.add(local_filter_middleware)
    return w3


def _emitter_fixture_logic(
    w3,
    emitter_contract_factory,
    wait_for_transaction,
    wait_for_block,
    address_conversion_func,
):
    wait_for_block(w3)
    deploy_txn_hash = emitter_contract_factory.constructor().transact({"gas": 10000000})
    deploy_receipt = wait_for_transaction(w3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt["contractAddress"])

    bytecode = w3.eth.get_code(contract_address)
    assert bytecode == emitter_contract_factory.bytecode_runtime
    _emitter = emitter_contract_factory(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter


# --- async --- #


def _async_w3_fixture_logic(request):
    use_filter_middleware = request.param
    provider = AsyncEthereumTesterProvider()
    async_w3 = Web3(provider, middlewares=[])

    if use_filter_middleware:
        async_w3.middleware_onion.add(async_local_filter_middleware)
    return async_w3


async def _async_emitter_fixture_logic(
    async_w3,
    async_emitter_contract_factory,
    async_wait_for_transaction,
    async_wait_for_block,
    address_conversion_func,
):
    await async_wait_for_block(async_w3)
    deploy_txn_hash = await async_emitter_contract_factory.constructor().transact(
        {"gas": 10000000}
    )
    deploy_receipt = await async_wait_for_transaction(async_w3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt["contractAddress"])

    bytecode = await async_w3.eth.get_code(contract_address)
    assert bytecode == async_emitter_contract_factory.bytecode_runtime
    _emitter = async_emitter_contract_factory(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter
