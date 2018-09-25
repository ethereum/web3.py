import pytest

from hypothesis import (
    given,
    settings,
    strategies as st,
)


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


def clear_chain_state(web3, snapshot):
    """Clear chain state
    Hypothesis doesn't allow function scoped fixtures to re-run between test runs
    so chain state needs to be explicitly cleared
    """
    web3.providers[0].ethereum_tester.revert_to_snapshot(snapshot)


@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=dynamic_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_dynamic_arguments(
        web3,
        wait_for_transaction,
        create_filter,
        emitter,
        api_style,
        tester_snapshot,
        vals):
    clear_chain_state(web3, tester_snapshot)

    if api_style == 'build_filter':
        filter_builder = emitter.events.LogDynamicArgs.build_filter()
        filter_builder.args['arg1'].match_single(vals['matching'])
        event_filter = filter_builder.deploy(web3)
    else:
        event_filter = create_filter(emitter, [
            'LogDynamicArgs', {
                'filter': {
                    'arg1': vals['matching']}}])

    txn_hashes = [
        emitter.functions.logDynamicArgs(
            arg0=vals['matching'], arg1=vals['matching']).transact(
                {'gasPrice': 1, 'gas': 400000, 'nonce': 0}),
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][0], arg1=vals['non_matching'][0]).transact(
                {'gasPrice': 1, 'gas': 400000, 'nonce': 1}),
    ]

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=fixed_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_fixed_arguments(
        web3,
        emitter,
        wait_for_transaction,
        create_filter,
        api_style,
        vals,
        tester_snapshot,
        request):
    clear_chain_state(web3, tester_snapshot)

    if api_style == 'build_filter':
        filter_builder = emitter.events.LogQuadrupleArg.build_filter()
        filter_builder.args['arg0'].match_single(vals['matching'][0])
        filter_builder.args['arg1'].match_single(vals['matching'][1])
        filter_builder.args['arg2'].match_single(vals['matching'][2])
        filter_builder.args['arg3'].match_single(vals['matching'][3])
        event_filter = filter_builder.deploy(web3)
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
        arg3=vals['matching'][3]).transact({'gasPrice': 1, 'gas': 100000, 'nonce': 0}))
    txn_hashes.append(emitter.functions.logQuadruple(
        which=5,
        arg0=vals['non_matching'][0],
        arg1=vals['non_matching'][1],
        arg2=vals['non_matching'][2],
        arg3=vals['non_matching'][3]).transact({'gasPrice': 1, 'gas': 100000, 'nonce': 1}))

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.parametrize('call_as_instance', (True, False))
@pytest.mark.parametrize('api_style', ('v4', 'build_filter'))
@given(vals=array_values())
@settings(max_examples=5, deadline=None)
def test_data_filters_with_list_arguments(
        web3,
        emitter,
        wait_for_transaction,
        call_as_instance,
        create_filter,
        api_style,
        vals,
        tester_snapshot,
        request):
    clear_chain_state(web3, tester_snapshot)

    matching, non_matching = vals

    if api_style == 'build_filter':
        filter_builder = emitter.events.LogListArgs.build_filter()
        filter_builder.args['arg1'].match_single(matching)
        event_filter = filter_builder.deploy(web3)

        txn_hashes = []
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=matching,
            arg1=matching).transact({'gasPrice': 1, 'nonce': 0}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=non_matching,
            arg1=non_matching).transact({'gasPrice': 1, 'nonce': 1}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=non_matching,
            arg1=matching).transact({'gasPrice': 1, 'nonce': 2}))
        txn_hashes.append(emitter.functions.logListArgs(
            arg0=matching,
            arg1=non_matching).transact({'gasPrice': 1, 'nonce': 3}))

        for txn_hash in txn_hashes:
            wait_for_transaction(web3, txn_hash)

        log_entries = event_filter.get_new_entries()
        assert len(log_entries) == 2
        assert log_entries[0]['transactionHash'] == txn_hashes[0]
        assert log_entries[1]['transactionHash'] == txn_hashes[2]
    else:
        with pytest.raises(TypeError):
            event_filter = create_filter(emitter, [
                'LogListArgs', {
                    'filter': {
                        'arg1': matching}}])
