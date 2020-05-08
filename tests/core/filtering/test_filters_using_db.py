from eth_utils import to_canonical_address
import functools
import pytest
from sqlalchemy import create_engine

from web3 import Web3
from web3._utils.rpc_abi import RPC
from web3.middleware import construct_result_generator_middleware
from web3.providers.eth_tester import EthereumTesterProvider
from web3.tools.pytest_ethereum.factories import Hash32Factory
from web3.tools.pytest_ethereum.models import Base
from web3.tools.pytest_ethereum.normalizers import (
    add_new_filter,
    construct_log,
    get_all_logs_for_filter,
    get_new_logs_for_filter,
    serve_filter_from_db,
    uninstall_filter,
)
from web3.tools.pytest_ethereum.session import Session

@pytest.fixture(scope="session")
def engine():
    # PRO-TIP: Set `echo=True` for lots more SQL debug log output.
    return create_engine("sqlite:///:memory:", echo=False)


@pytest.fixture(scope="session")
def _schema(engine):
    Base.metadata.create_all(engine)


@pytest.fixture(scope="session")
def _Session(engine, _schema):
    Session.configure(bind=engine)
    return Session


@pytest.fixture
def session(_Session, _schema):
    session = Session()
    transaction = session.begin_nested()

    try:
        yield session
    finally:
        transaction.rollback()
        session.close()

@pytest.fixture
def w3(session):
    w3 = Web3(EthereumTesterProvider())
    filter_states = {}
    result_generators = {
        RPC.eth_getLogs: functools.partial(serve_filter_from_db, session=session),
        RPC.eth_newFilter: functools.partial(add_new_filter, session=session, filter_states=filter_states),
        RPC.eth_getFilterLogs: functools.partial(get_all_logs_for_filter, session=session, filter_states=filter_states),
        RPC.eth_getFilterChanges: functools.partial(get_new_logs_for_filter, session=session, filter_states=filter_states),
        RPC.eth_uninstallFilter: functools.partial(uninstall_filter, session=session, filter_states=filter_states),
    }
    middleware = construct_result_generator_middleware(result_generators)
    w3.middleware_onion.add(middleware)
    return w3

def test_empty_log(session, w3):
    construct_log(session)
    logs = w3.eth.getLogs({})
    assert len(logs) == 1

def test_get_logs_with_one_topic(session, w3):
    topic = Hash32Factory()
    log = construct_log(session, topics=(topic,))
    logs = w3.eth.getLogs({ 'topics': (topic,) })
    assert len(logs) == 1

def test_get_logs_finds_exact_topic_match(session, w3):
    topic1 = Hash32Factory()
    topic2 = Hash32Factory()
    topic3 = Hash32Factory()
    topic4 = Hash32Factory()
    construct_log(session, topics=(topic1, topic2, topic3, topic4))
    construct_log(session, topics=(topic1, topic2, topic3))
    construct_log(session, topics=(topic1, topic2))
    construct_log(session, topics=(topic1,))
    all_logs = w3.eth.getLogs({})
    assert len(all_logs) == 4
    logs = w3.eth.getLogs({ 'topics': (topic1,topic2) })
    assert len(logs) == 1

def test_create_filter_handles_none_args(session, w3, emitter):
    event_filter = w3.eth.filter({ "address": None, "fromBlock": None })
    all_logs = event_filter.get_all_entries()
    assert len(all_logs) == 0
    construct_log(session, address=to_canonical_address(emitter.address))
    new_logs = event_filter.get_new_entries()
    assert len(new_logs) == 1

@pytest.mark.skip("Known issue: getLogs should accept None values")
def test_get_logs_handles_none_args(session, w3, emitter):
    event_filter = w3.eth.getLogs({ "address": None, "fromBlock": None })
    all_logs = event_filter.get_all_entries()
    assert len(all_logs) == 0
    construct_log(session, address=to_canonical_address(emitter.address))
    new_logs = event_filter.get_new_entries()
    assert len(new_logs) == 1
