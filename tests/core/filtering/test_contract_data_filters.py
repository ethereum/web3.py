import pytest

from hypothesis import (
    given,
    settings,
    strategies as st,
)

from web3 import Web3
from web3._utils.module_testing.emitter_contract import (
    CONTRACT_EMITTER_ABI,
    CONTRACT_EMITTER_CODE,
    CONTRACT_EMITTER_RUNTIME,
)
from web3.middleware import (
    local_filter_middleware,
)
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture(
    scope="module",
    params=[True, False],
    ids=["local_filter_middleware", "node_based_filter"])
def w3(request):
    use_filter_middleware = request.param
    provider = EthereumTesterProvider()
    w3 = Web3(provider)
    if use_filter_middleware:
        w3.middleware_onion.add(local_filter_middleware)
    return w3


@pytest.fixture(scope="module")
def EMITTER_CODE():
    return CONTRACT_EMITTER_CODE


@pytest.fixture(scope="module")
def EMITTER_RUNTIME():
    return CONTRACT_EMITTER_RUNTIME


@pytest.fixture(scope="module")
def EMITTER_ABI():
    return CONTRACT_EMITTER_ABI


@pytest.fixture(scope="module")
def EMITTER(EMITTER_CODE,
            EMITTER_RUNTIME,
            EMITTER_ABI):
    return {
        'bytecode': EMITTER_CODE,
        'bytecode_runtime': EMITTER_RUNTIME,
        'abi': EMITTER_ABI,
    }


@pytest.fixture(scope="module")
def Emitter(w3, EMITTER):
    return w3.eth.contract(**EMITTER)


@pytest.fixture(scope="module")
def emitter(w3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func):
    wait_for_block(w3)
    deploy_txn_hash = Emitter.constructor().transact({'gas': 10000000})
    deploy_receipt = wait_for_transaction(w3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = w3.eth.get_code(contract_address)
    assert bytecode == Emitter.bytecode_runtime
    _emitter = Emitter(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter


def not_empty_string(x):
    return x != ''


@st.composite
def dynamic_values(draw):
    non_matching_1 = draw(st.text().filter(not_empty_string))
    exclusions = (non_matching_1, '')
    matching_value = draw(st.text().filter(lambda x: x not in exclusions))
    return {
        "matching": matching_value,
        "non_matching": [
            non_matching_1,
        ]
    }


@st.composite
def fixed_values(draw):
    non_matching_1 = draw(st.integers(min_value=0))
    non_matching_2 = draw(st.integers(min_value=0))
    non_matching_3 = draw(st.integers(min_value=0))
    non_matching_4 = draw(st.integers(min_value=0))
    exclusions = (non_matching_1, non_matching_2, non_matching_3, non_matching_4)
    matching_values = draw(
        st.lists(
            elements=st.integers(
                min_value=0).filter(lambda x: x not in exclusions),
            min_size=4,
            max_size=4))
    return {
        "matching": matching_values,
        "non_matching": [
            non_matching_1,
            non_matching_2,
            non_matching_3,
            non_matching_4
        ]
    }


@st.composite
def array_values(draw):
    matching = draw(st.lists(elements=st.binary(min_size=2, max_size=2), min_size=1))
    non_matching = draw(
        st.lists(elements=st.binary(min_size=2, max_size=2)).filter(lambda x: x != matching))
    return (matching, non_matching)


@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=dynamic_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_dynamic_arguments(
        w3,
        wait_for_transaction,
        create_filter,
        emitter,
        api_style,
        vals):
    if api_style == 'build_filter':
        filter_builder = emitter.events.LogDynamicArgs.build_filter()
        filter_builder.args['arg1'].match_single(vals['matching'])
        event_filter = filter_builder.deploy(w3)
    else:
        event_filter = create_filter(emitter, [
            'LogDynamicArgs', {
                'filter': {
                    'arg1': vals['matching']}}])

    txn_hashes = [
        emitter.functions.logDynamicArgs(
            arg0=vals['matching'], arg1=vals['matching']).transact(
                {'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9, 'gas': 400000}),
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][0], arg1=vals['non_matching'][0]).transact(
                {'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9, 'gas': 400000}),
    ]

    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=fixed_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_fixed_arguments(
        w3,
        emitter,
        wait_for_transaction,
        create_filter,
        api_style,
        vals,
):
    if api_style == 'build_filter':
        filter_builder = emitter.events.LogQuadrupleArg.build_filter()
        filter_builder.args['arg0'].match_single(vals['matching'][0])
        filter_builder.args['arg1'].match_single(vals['matching'][1])
        filter_builder.args['arg2'].match_single(vals['matching'][2])
        filter_builder.args['arg3'].match_single(vals['matching'][3])
        event_filter = filter_builder.deploy(w3)
    else:
        event_filter = create_filter(emitter, [
            'LogQuadrupleArg', {
                'filter': {
                    'arg0': vals['matching'][0],
                    'arg1': vals['matching'][1],
                    'arg2': vals['matching'][2],
                    'arg3': vals['matching'][3]}}])

    txn_hashes = []
    txn_hashes.append(emitter.functions.logQuadruple(
        which=5,
        arg0=vals['matching'][0],
        arg1=vals['matching'][1],
        arg2=vals['matching'][2],
        arg3=vals['matching'][3]).transact({
            'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9, 'gas': 100000
        }))
    txn_hashes.append(emitter.functions.logQuadruple(
        which=5,
        arg0=vals['non_matching'][0],
        arg1=vals['non_matching'][1],
        arg2=vals['non_matching'][2],
        arg3=vals['non_matching'][3]).transact({
            'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9, 'gas': 100000
        }))

    for txn_hash in txn_hashes:
        wait_for_transaction(w3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.parametrize('call_as_instance', (True, False))
@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=array_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_list_arguments(
        w3,
        emitter,
        wait_for_transaction,
        call_as_instance,
        create_filter,
        api_style,
        vals,
):
    matching, non_matching = vals

    if api_style == 'build_filter':
        filter_builder = emitter.events.LogListArgs.build_filter()
        filter_builder.args['arg1'].match_single(matching)
        event_filter = filter_builder.deploy(w3)

        txn_hashes = []
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=matching,
            arg1=matching).transact({'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=non_matching,
            arg1=non_matching).transact({'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=non_matching,
            arg1=matching).transact({'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=matching,
            arg1=non_matching).transact({'maxFeePerGas': 10 ** 9, 'maxPriorityFeePerGas': 10 ** 9}))

        for txn_hash in txn_hashes:
            wait_for_transaction(w3, txn_hash)

        log_entries = event_filter.get_new_entries()
        assert len(log_entries) == 2
        assert log_entries[0]['transactionHash'] == txn_hashes[0]
        assert log_entries[1]['transactionHash'] == txn_hashes[2]
    else:
        with pytest.raises(TypeError):
            create_filter(emitter, [
                'LogListArgs', {
                    'filter': {
                        'arg1': matching}}])
