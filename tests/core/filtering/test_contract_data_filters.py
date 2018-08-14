import pytest

from hypothesis import (
    given,
    strategies as st,
)


@st.composite
def dynamic_values(draw):
    matching_value = draw(st.text().filter(lambda x: x != ''))
    exclusions = (matching_value, '')
    non_matching_1 = draw(st.text().filter(lambda x: x not in exclusions))
    non_matching_2 = draw(st.text().filter(lambda x: x not in exclusions))
    non_matching_3 = draw(st.text().filter(lambda x: x not in exclusions))
    non_matching_4 = draw(st.text().filter(lambda x: x not in exclusions))
    return {
        "matching": matching_value,
        "non_matching": [
            non_matching_1,
            non_matching_2,
            non_matching_3,
            non_matching_4
        ]
    }


@st.composite
def fixed_values(draw):
    matching_values = draw(st.lists(elements=st.integers(min_value=0), min_size=4, max_size=4))
    non_matching_1 = draw(st.integers(min_value=0).filter(lambda x: x not in matching_values))
    non_matching_2 = draw(st.integers(min_value=0).filter(lambda x: x not in matching_values))
    non_matching_3 = draw(st.integers(min_value=0).filter(lambda x: x not in matching_values))
    non_matching_4 = draw(st.integers(min_value=0).filter(lambda x: x not in matching_values))
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
    matching = draw(st.lists(elements=st.binary(min_size=2, max_size=2)))
    non_matching = draw(
        st.lists(elements=st.binary(min_size=2, max_size=2)).filter(lambda x: x != matching))
    return (matching, non_matching)


@pytest.mark.xfail(reason="The regex based data filters do not work with dynamic sized types")
@pytest.mark.parametrize('call_as_instance', (True, False))
@given(vals=dynamic_values())
def test_data_filters_with_dynamic_arguments(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter,
        vals):

    if call_as_instance:
        event_filter = create_filter(emitter, [
            'LogDynamicArgs', {
                'filter': {
                    'arg1': vals['matching']}}])
    else:
        event_filter = create_filter(Emitter, [
            'LogDynamicArgs', {
                'filter': {
                    'arg1': vals['matching']}}])

    txn_hashes = []
    txn_hashes.append(
        emitter.functions.logDynamicArgs(
            arg0=vals['matching'], arg1=vals['matching']).transact())
    txn_hashes.append(
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][0], arg1=vals['non_matching'][0]).transact())
    txn_hashes.append(
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][1], arg1=vals['non_matching'][1]).transact())
    txn_hashes.append(
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][2], arg1=vals['non_matching'][2]).transact())
    txn_hashes.append(
        emitter.functions.logDynamicArgs(
            arg0=vals['non_matching'][3], arg1=vals['non_matching'][3]).transact())

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.parametrize('call_as_instance', (True, False))
@given(vals=fixed_values())
def test_data_filters_with_fixed_arguments(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter,
        vals):

    if call_as_instance:
        event_filter = create_filter(emitter, [
            'LogQuadrupleArg', {
                'filter': {
                    'arg0': vals['matching'][0],
                    'arg1': vals['matching'][1],
                    'arg2': vals['matching'][2],
                    'arg3': vals['matching'][3]}}])
    else:
        event_filter = create_filter(Emitter, [
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
        arg3=vals['matching'][3]).transact())
    txn_hashes.append(emitter.functions.logQuadruple(
        which=5,
        arg0=vals['non_matching'][0],
        arg1=vals['non_matching'][1],
        arg2=vals['non_matching'][2],
        arg3=vals['non_matching'][3]).transact())

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 1
    assert log_entries[0]['transactionHash'] == txn_hashes[0]


@pytest.mark.xfail(reason="The regex based data filters do not work with dynamic sized types")
@pytest.mark.parametrize('call_as_instance', (True, False))
@given(vals=array_values())
def test_data_filters_with_list_arguments(
        web3,
        emitter,
        Emitter,
        wait_for_transaction,
        emitter_event_ids,
        call_as_instance,
        create_filter,
        vals):

    matching, non_matching = vals

    if call_as_instance:
        event_filter = create_filter(emitter, [
            'LogListArgs', {
                'filter': {"arg1": matching}}])
    else:
        event_filter = create_filter(Emitter, [
            'LogListArgs', {
                'filter': {"arg1": matching}}])

    txn_hashes = []
    txn_hashes.append(emitter.functions.logListArgs(
        arg0=matching,
        arg1=matching).transact())
    txn_hashes.append(emitter.functions.logListArgs(
        arg0=non_matching,
        arg1=non_matching).transact())
    txn_hashes.append(emitter.functions.logListArgs(
        arg0=non_matching,
        arg1=matching).transact())
    txn_hashes.append(emitter.functions.logListArgs(
        arg0=matching,
        arg1=non_matching).transact())

    for txn_hash in txn_hashes:
        wait_for_transaction(web3, txn_hash)

    log_entries = event_filter.get_new_entries()
    assert len(log_entries) == 2
    assert log_entries[0]['transactionHash'] == txn_hashes[0]
    assert log_entries[1]['transactionHash'] == txn_hashes[3]
