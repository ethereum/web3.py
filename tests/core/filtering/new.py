from typing import (
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Sequence,
    Tuple,
    TypedDict,
    Union,
)
from eth_utils import (
    big_endian_to_int,
    decode_hex,
    encode_hex,
    humanize_hash,
    int_to_big_endian,
    is_address,
    to_canonical_address,
    to_checksum_address,
    to_hex,
    to_int,
    to_tuple,
)
from eth_typing import (
    Address,
    BlockNumber,
    Hash32,
    HexAddress,
    HexStr,
)
import pytest
from sqlalchemy import create_engine, orm
from sqlalchemy.orm.exc import NoResultFound

from web3 import Web3
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.middleware import construct_result_generator_middleware
from web3._utils.rpc_abi import RPC
from web3.tools.pytest_ethereum.session import Session
from web3.tools.pytest_ethereum.models import (
    Base,
    Block,
    BlockTransaction,
    Header,
    Log,
    LogTopic,
    Receipt,
    Topic,
    Transaction,
)
from web3.tools.pytest_ethereum.factories import (
    AddressFactory,
    BlockTransactionFactory,
    Hash32Factory,
    HeaderFactory,
    LogFactory,
    LogTopicFactory,
)
from web3.tools.pytest_ethereum.filters import (
    FilterParams,
    filter_logs,
)

class RawFilterParams(TypedDict, total=False):
    fromBlock: Optional[HexStr]
    toBlock: Optional[HexStr]
    address: Union[None, HexAddress, List[HexAddress]]
    topics: List[Union[None, HexStr, List[HexStr]]]

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


# rpc.py

class RPCLog(TypedDict):
    logIndex: HexStr
    transactionIndex: HexStr
    transactionHash: HexStr
    blockHash: HexStr
    blockNumber: HexStr
    address: HexStr
    data: HexStr
    topics: List[HexStr]


@to_tuple
def _normalize_topics(
    raw_topics: List[Union[None, HexStr, List[HexStr]]],
) -> Iterable[Union[None, Hash32, Tuple[Hash32, ...]]]:
    for topic in raw_topics:
        if topic is None:
            yield None
        elif isinstance(topic, str):
            yield Hash32(decode_hex(topic))
        elif isinstance(topic, bytes):
            yield Hash32(topic)
        elif isinstance(topic, Sequence):
            yield tuple(Hash32(decode_hex(sub_topic)) for sub_topic in topic)
        else:
            raise TypeError(f"Unsupported topic: {topic!r}")


def _rpc_request_to_filter_params(raw_params: RawFilterParams) -> FilterParams:
    address: Union[None, Address, Tuple[Address, ...]]

    if "address" not in raw_params:
        address = None
    elif raw_params["address"] is None:
        address = None
    elif is_address(raw_params["address"]):
        address = to_canonical_address(raw_params["address"])  # type: ignore
    elif isinstance(raw_params["address"], list):
        address = tuple(
            to_canonical_address(sub_address) for sub_address in raw_params["address"]
        )
    else:
        raise TypeError(f"Unsupported address: {raw_params['address']!r}")

    topics: Tuple[Union[None, Hash32, Tuple[Hash32, ...]], ...]

    if "topics" not in raw_params:
        topics = ()
    elif raw_params["topics"] is None:
        topics = ()
    elif isinstance(raw_params["topics"], Sequence):
        topics = _normalize_topics(raw_params["topics"])
    else:
        raise TypeError(f"Unsupported topics: {raw_params['topics']!r}")

    from_block: Optional[BlockNumber]
    if "fromBlock" not in raw_params:
        from_block = None
    elif raw_params["fromBlock"] is None:
        from_block = None
    elif isinstance(raw_params["fromBlock"], str):
        from_block = BlockNumber(to_int(hexstr=raw_params["fromBlock"]))
    else:
        raise TypeError(f"Unsupported fromBlock: {raw_params['fromBlock']!r}")

    to_block: Optional[BlockNumber]
    if "toBlock" not in raw_params:
        to_block = None
    elif raw_params["toBlock"] is None:
        to_block = None
    elif isinstance(raw_params["toBlock"], str):
        to_block = BlockNumber(to_int(hexstr=raw_params["toBlock"]))
    else:
        raise TypeError(f"Unsupported toBlock: {raw_params['toBlock']!r}")

    return FilterParams(from_block, to_block, address, topics)


def _log_to_rpc_response(log: Log) -> RPCLog:
    transaction = log.receipt.transaction
    blocktransaction = BlockTransaction.query.filter(
        BlockTransaction.transaction_hash == transaction.hash,
        BlockTransaction.block_header_hash == transaction.block_header_hash,
    ).one()

    return RPCLog(
        logIndex=to_hex(log.idx),
        transactionIndex=to_hex(blocktransaction.idx),
        transactionHash=encode_hex(transaction.hash),
        blockHash=encode_hex(transaction.block.header_hash),
        blockNumber=to_hex(transaction.block.header.block_number),
        address=to_checksum_address(log.address),
        data=encode_hex(log.data),
        topics=[encode_hex(topic.topic) for topic in log.topics],
    )

@to_tuple
def get_or_create_topics(
    session: orm.Session, topics: Sequence[Hash32]
) -> Iterator[Topic]:
    cache: Dict[Hash32, Topic] = {}

    for topic in topics:
        if topic not in cache:
            try:
                cache[topic] = session.query(Topic).filter(Topic.topic == topic).one()
            except NoResultFound:
                cache[topic] = Topic(topic=topic)
                yield cache[topic]

# generate a log in the db with minimal boilerplate
# requires factories*
def construct_log(
    session: orm.Session,
    *,
    block_number: Optional[BlockNumber] = None,
    address: Optional[Address] = None,
    topics: Sequence[Hash32] = (),
    data: bytes = b"",
    is_canonical: bool = True,
) -> Log:
    if block_number is not None:
        try:
            header = (
                session.query(Header)  # type: ignore
                .filter(Header.is_canonical.is_(is_canonical))  # type: ignore
                .filter(Header.block_number == block_number)
                .one()
            )
        except NoResultFound:
            header = HeaderFactory(is_canonical=is_canonical, block_number=block_number)
    else:
        header = HeaderFactory(is_canonical=is_canonical)

    if address is None:
        address = AddressFactory()

    session.add(header)

    topic_objs = get_or_create_topics(session, topics)

    session.add_all(topic_objs)  # type: ignore

    if is_canonical:
        log = LogFactory(
            receipt__transaction__block__header=header, address=address, data=data
        )
        block_transaction = BlockTransactionFactory(
            idx=0,
            block=log.receipt.transaction.block,
            transaction=log.receipt.transaction,
        )
        session.add(block_transaction)
    else:
        log = LogFactory(receipt__transaction__block=None)
        block = BlockFactory(header=header)
        block_transaction = BlockTransactionFactory(
            idx=0, block=block, transaction=log.receipt.transaction
        )
        session.add_all((block, block_transaction))  # type: ignore

    log_topics = tuple(
        LogTopicFactory(idx=idx, log=log, topic=topic)
        for idx, topic in enumerate(topic_objs)
    )

    session.add(log)
    session.add_all(log_topics)  # type: ignore

    return log


def serve_filter_from_db(method, params, session):
    filter_params = _rpc_request_to_filter_params(params[0])
    logs = filter_logs(session, filter_params)
    return [_log_to_rpc_response(log) for log in logs]

@pytest.fixture
def w3(session):
    # todo: make a noop web3 provider for this type of testing
    w3 = Web3(EthereumTesterProvider())
    result_generators = { RPC.eth_getLogs: functools.partial(serve_filter_from_db, session=session) }
    # do more methods need to be added here?
    #   getFilterLogs? getFilterChanges?
    middleware = construct_result_generator_middleware(result_generators)
    w3.middleware_onion.add(middleware)
    return w3

import functools

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
