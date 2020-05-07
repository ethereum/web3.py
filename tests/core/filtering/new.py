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
    construct_log,
    serve_filter_from_db,
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
    result_generators = { RPC.eth_getLogs: functools.partial(serve_filter_from_db, session=session) }
    # do more methods need to be added here?
    #   getFilterLogs? getFilterChanges?
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

def test_get_logs_finds_exact_topic_match(session, w3):
    topic1 = Hash32Factory()
    topic2 = Hash32Factory()
    topic3 = Hash32Factory()
    topic4 = Hash32Factory()
    topic5 = Hash32Factory()
    construct_log(session, topics=(topic1, topic2, topic3, topic4, topic5))
    # TODO: assert exception for more than 4 topics?

# test all filter methods?
#   - createFilter:
#       event_filter = mycontract.events.myEvent.createFilter(fromBlock='latest', argument_filters={'arg1':10})
#   - w3.eth.filter({...filter criteria...}):
#       #get_all_entries()
#       #get_new_entries()
#       #format_entry()
#       #is_valid_entry()

# test that local_filter_middleware works as expected?

# Q's:
#   - Where do local_filter_middleware tests get run?
#   - Should this log architecture be a part of eth-tester in some way?
#   - This only applies to logs and not, for example, new blocks or pending txs?
#   - Should this result generator middleware get passed into all integration tests to support logs?
# todos:
#   - test filter middleware by fuzz testing against the other implementation
#   - noop web3 provider (when EthereumTesterProvider is overkill)
