# much of this should live in web3/tools/ eventually

# sqlite db lives here?
# ORM models prob can copy pasta directly
# in memory instance before each test: https://github.com/ethereum/cthaeh/blob/master/tests/core/conftest.py
# (cleans up after each)
#   normalization needed on both sides; maybe simple middleware to do this, redirecting to sqlite
#   versions of this exist: https://github.com/ethereum/cthaeh/blob/master/cthaeh/rpc.py
#       #_log_to_rpc & #_rpc_request_to_filter_params

# import middleware/fixture.py to generate fixtures
# pull in factories? https://github.com/ethereum/cthaeh/blob/master/cthaeh/tools/factories.py
#  useful for generating test data ^

# input types forgiving, return strict. 
# todo: test filter middleware by fuzz testing against the other implementation

from web3 import Web3
from web3.providers.eth_tester import (
    EthereumTesterProvider,
)
from web3.middleware import construct_result_generator_middleware

from web3._utils.rpc_abi import RPC
from typing import (
    Dict,
    Iterable,
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
)
from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    ForeignKey,
    Index,
    Integer,
    LargeBinary,
    UniqueConstraint,
    orm,
)
from sqlalchemy.orm.exc import NoResultFound
from eth_typing import (
    Address,
    Hash32,
    HexAddress,
    HexStr,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

ZERO_HASH32 = Hash32(32 * b"\x00")

GENESIS_PARENT_HASH = ZERO_HASH32

import pytest
from sqlalchemy import create_engine


#####################
#    session.py
#####################
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker())




# else:

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


class BlockUncle(Base):
    query = Session.query_property()

    __tablename__ = "blockuncle"
    __table_args__ = (
        Index(
            "ix_blockuncle_idx_block_header_hash",
            "idx",
            "block_header_hash",
            unique=True,
        ),
        Index(
            "ix_block_header_hash_uncle_hash",
            "block_header_hash",
            "uncle_hash",
            unique=True,
        ),
    )

    idx = Column(Integer, nullable=False)

    block_header_hash = Column(
        LargeBinary(32), ForeignKey("block.header_hash"), primary_key=True
    )
    uncle_hash = Column(LargeBinary(32), ForeignKey("header.hash"), primary_key=True)

    block = relationship("Block")
    uncle = relationship("Header")


class Header(Base):
    query = Session.query_property()

    __tablename__ = "header"

    hash = Column(LargeBinary(32), primary_key=True)

    block = relationship("Block", uselist=False, back_populates="header")
    uncle_blocks = relationship(
        "Block", secondary="blockuncle", order_by=BlockUncle.idx
    )

    is_canonical = Column(Boolean, nullable=False)

    _parent_hash = Column(
        LargeBinary(32), ForeignKey("header.hash"), nullable=True, index=True
    )
    uncles_hash = Column(LargeBinary(32), nullable=False)
    coinbase = Column(LargeBinary(20), nullable=False)
    state_root = Column(LargeBinary(32), nullable=False)
    transaction_root = Column(LargeBinary(32), nullable=False)
    receipt_root = Column(LargeBinary(32), nullable=False)
    _bloom = Column(LargeBinary(1024), nullable=False)
    difficulty = Column(LargeBinary(32), nullable=False)
    block_number = Column(BigInteger, index=True, nullable=False)
    gas_limit = Column(BigInteger, nullable=False)
    gas_used = Column(BigInteger, nullable=False)
    timestamp = Column(Integer, nullable=False)
    extra_data = Column(LargeBinary, nullable=False)
    # mix_hash = Column(LargeBinary(32), nullable=False)
    nonce = Column(LargeBinary(8), nullable=False)

    children = relationship(
        "Header", backref=backref("parent", remote_side=[hash])
    )

    @property
    def parent_hash(self) -> Optional[Hash32]:
        if self._parent_hash is None:
            if self.block_number == 0:
                return GENESIS_PARENT_HASH
            else:
                return None
        else:
            return Hash32(self._parent_hash)

    @parent_hash.setter
    def parent_hash(self, value: Optional[Hash32]) -> None:
        if value == GENESIS_PARENT_HASH and self.block_number == 0:
            self._parent_hash = None
        else:
            self._parent_hash = value


class BlockTransaction(Base):
    query = Session.query_property()

    __tablename__ = "blocktransaction"
    __table_args__ = (
        Index(
            "ix_blocktransaction_idx_block_header_hash",
            "idx",
            "block_header_hash",
            unique=True,
        ),
        Index(
            "ix_block_header_hash_transaction_hash",
            "block_header_hash",
            "transaction_hash",
            unique=True,
        ),
    )
    idx = Column(Integer, nullable=False)

    block_header_hash = Column(
        LargeBinary(32), ForeignKey("block.header_hash"), primary_key=True
    )
    transaction_hash = Column(
        LargeBinary(32), ForeignKey("transaction.hash"), primary_key=True
    )

    block = relationship("Block")
    transaction = relationship("Transaction")


class Block(Base):
    query = Session.query_property()

    __tablename__ = "block"

    header_hash = Column(LargeBinary(32), ForeignKey("header.hash"), primary_key=True)
    header = relationship("Header", back_populates="block")

    uncles = relationship("Header", secondary="blockuncle", order_by=BlockUncle.idx)
    transactions = relationship(
        "Transaction", secondary="blocktransaction", order_by=BlockTransaction.idx
    )


class Transaction(Base):
    query = Session.query_property()

    __tablename__ = "transaction"

    hash = Column(LargeBinary(32), primary_key=True)

    block_header_hash = Column(
        LargeBinary(32), ForeignKey("block.header_hash"), nullable=True, index=True
    )
    block = relationship("Block")

    blocks = relationship(
        "Block", secondary="blocktransaction", order_by=BlockTransaction.idx
    )
    receipt = relationship("Receipt", uselist=False, back_populates="transaction")

    nonce = Column(BigInteger, nullable=False)
    gas_price = Column(BigInteger, nullable=False)
    gas = Column(BigInteger, nullable=False)
    to = Column(LargeBinary(20), nullable=True)
    value = Column(LargeBinary(32), nullable=False)
    data = Column(LargeBinary, nullable=False)
    v = Column(LargeBinary(32), nullable=False)
    r = Column(LargeBinary(32), nullable=False)
    s = Column(LargeBinary(32), nullable=False)

    sender = Column(LargeBinary(20), nullable=False)


class Receipt(Base):
    query = Session.query_property()

    __tablename__ = "receipt"

    transaction_hash = Column(
        LargeBinary(32), ForeignKey("transaction.hash"), primary_key=True
    )
    transaction = relationship("Transaction", back_populates="receipt")

    state_root = Column(LargeBinary(32), nullable=False)
    gas_used = Column(BigInteger, nullable=False)
    _bloom = Column(LargeBinary(1024), nullable=False)
    logs = relationship("Log", back_populates="receipt", order_by="Log.idx")

    @property
    def bloom(self) -> int:
        return big_endian_to_int(self._bloom)

    @bloom.setter
    def bloom(self, value: int) -> None:
        self._bloom = int_to_big_endian(value)


class LogTopic(Base):
    query = Session.query_property()

    __tablename__ = "logtopic"
    __table_args__ = (
        UniqueConstraint("idx", "log_id", name="ix_idx_log_id"),
        Index("ix_idx_topic_topic_log_id", "idx", "topic_topic", "log_id"),
    )
    id = Column(Integer, primary_key=True)

    idx = Column(Integer, nullable=False)

    topic_topic = Column(
        LargeBinary(32), ForeignKey("topic.topic"), index=True, nullable=False
    )
    log_id = Column(Integer, ForeignKey("log.id"), index=True, nullable=False)

    topic = relationship("Topic")
    log = relationship("Log")


class Log(Base):
    query = Session.query_property()

    __tablename__ = "log"
    __table_args__ = (
        UniqueConstraint("idx", "receipt_hash", name="ix_idx_receipt_hash"),
    )

    id = Column(Integer, primary_key=True)
    idx = Column(Integer, nullable=False)

    receipt_hash = Column(
        LargeBinary(32),
        ForeignKey("receipt.transaction_hash"),
        index=True,
        nullable=False,
    )
    receipt = relationship("Receipt", back_populates="logs")

    address = Column(LargeBinary(20), index=True, nullable=False)
    topics = relationship("Topic", secondary="logtopic", order_by=LogTopic.idx)
    data = Column(LargeBinary, nullable=False)

    def __repr__(self) -> str:
        return (
            f"Log("
            f"idx={self.idx!r}, "
            f"receipt_hash={self.receipt_hash!r}, "
            f"address={self.address!r}, "
            f"data={self.data!r}, "
            f"topics={self.topics!r}"
            f")"
        )

    def __str__(self) -> str:
        # TODO: use eth_utils.humanize_bytes once it is released
        if len(self.data) > 4:
            pretty_data = humanize_hash(Hash32(self.data))
        else:
            pretty_data = self.data.hex()

        if len(self.topics) == 0:
            pretty_topics = "(anonymous)"
        else:
            pretty_topics = "|".join(
                (
                    humanize_hash(Hash32(topic.topic))
                    for topic in self.topics
                )
            )

        return f"Log[#{self.idx} A={humanize_hash(self.address)} D={pretty_data}/T={pretty_topics}]" # noqa: E501


class Topic(Base):
    query = Session.query_property()

    __tablename__ = "topic"

    topic = Column(LargeBinary(32), primary_key=True)

    logs = relationship("Log", secondary="logtopic", order_by=LogTopic.idx)

    def __repr__(self) -> str:
        return f"Topic(topic={self.topic!r})"

    def __str__(self) -> str:
        return f"Topic[{humanize_hash(self.topic)}]"

# filters.py

import logging
from typing import Iterator, NamedTuple, Optional, Tuple, Union

from eth_typing import Address, BlockNumber, Hash32
from eth_utils import to_tuple
from sqlalchemy import and_, or_, orm
from sqlalchemy.orm import aliased
from sqlalchemy.sql import ClauseElement

BlockIdentifier = BlockNumber
# TODO: update to python3.8
# BlockIdentifier = Union[
#     Literal['latest'],
#     Literal['pending'],
#     Literal['earliest'],
#     BlockNumber,
# ]
TopicType = Union[None, Hash32, Tuple[Hash32, ...]]

logger = logging.getLogger("cthaeh.filter")


class FilterParams(NamedTuple):
    from_block: Optional[BlockIdentifier] = None
    to_block: Optional[BlockIdentifier] = None
    address: Union[None, Address, Tuple[Address, ...]] = None
    topics: Tuple[TopicType, ...] = ()


logtopic_0 = aliased(LogTopic)
logtopic_1 = aliased(LogTopic)
logtopic_2 = aliased(LogTopic)
logtopic_3 = aliased(LogTopic)

LOG_TOPIC_ALIASES = (logtopic_0, logtopic_1, logtopic_2, logtopic_3)


@to_tuple
def _construct_filters(params: FilterParams) -> Iterator[ClauseElement]:
    if isinstance(params.address, tuple):
        # TODO: or
        yield or_(*tuple(Log.address == address for address in params.address))
    elif isinstance(params.address, bytes):
        yield (Log.address == params.address)
    elif params.address is None:
        pass
    else:
        raise TypeError(f"Invalid address parameter: {params.address!r}")

    if isinstance(params.from_block, int):
        yield (Header.block_number >= params.from_block)
    elif params.from_block is None:
        pass
    else:
        raise TypeError(f"Invalid from_block parameter: {params.from_block!r}")

    if isinstance(params.to_block, int):
        yield (Header.block_number <= params.to_block)
    elif params.to_block is None:
        pass
    else:
        raise TypeError(f"Invalid to_block parameter: {params.to_block!r}")

    for idx, (topic, alias) in enumerate(zip(params.topics, LOG_TOPIC_ALIASES)):
        if isinstance(topic, bytes):
            yield and_(alias.idx == idx, alias.topic_topic == topic)
        elif isinstance(topic, tuple):
            yield or_(
                *(
                    and_(alias.idx == idx, alias.topic_topic == sub_topic)
                    for sub_topic in topic
                )
            )
        elif topic is None:
            pass
        else:
            raise TypeError(f"Unsupported topic at index {idx}: {topic!r}")


def filter_logs(session: orm.Session, params: FilterParams) -> Tuple[Log, ...]:
    orm_filters = _construct_filters(params)

    query = (
        session.query(Log)
        .join(Receipt, Log.receipt_hash == Receipt.transaction_hash)
        .join(Transaction, Receipt.transaction_hash == Transaction.hash)
        .join(Block, Transaction.block_header_hash == Block.header_hash)
        .join(Header, Block.header_hash == Header.hash)
        .outerjoin(logtopic_0, Log.id == logtopic_0.log_id)
        .outerjoin(logtopic_1, Log.id == logtopic_1.log_id)
        .outerjoin(logtopic_2, Log.id == logtopic_2.log_id)
        .outerjoin(logtopic_3, Log.id == logtopic_3.log_id)
        .filter(*orm_filters)
    )

    logger.debug("PARAMS: %s  QUERY: %s", params, query)

    return tuple(query.all())


#####################
#   rpc.py
#####################

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


#####################
#   factories.py
#####################
import factory
import secrets
from eth_typing import (
    Address,
    Hash32,
    HexAddress,
    HexStr,
)

def AddressFactory() -> Address:
    return Address(secrets.token_bytes(20))


def Hash32Factory() -> Hash32:
    return Hash32(secrets.token_bytes(32))


class HeaderFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Header
        sqlalchemy_session = Session
        rename = {"bloom": "_bloom"}

    hash = factory.LazyFunction(Hash32Factory)

    is_canonical = True

    _parent_hash = GENESIS_PARENT_HASH

    uncles_hash = factory.LazyFunction(Hash32Factory)
    coinbase = factory.LazyFunction(AddressFactory)

    state_root = factory.LazyFunction(Hash32Factory)
    transaction_root = factory.LazyFunction(Hash32Factory)
    receipt_root = factory.LazyFunction(Hash32Factory)

    bloom = b""

    difficulty = b"\x01"
    block_number = 0
    gas_limit = 3141592
    gas_used = 3141592
    timestamp = 0
    extra_data = b""
    # mix_hash = factory.LazyFunction(Hash32Factory)
    nonce = factory.LazyFunction(lambda: secrets.token_bytes(8))


class BlockFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Block
        sqlalchemy_session = Session

    header = factory.SubFactory(HeaderFactory)


class BlockUncleFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = BlockUncle
        sqlalchemy_session = Session

    block = factory.SubFactory(BlockFactory)
    uncle = factory.SubFactory(HeaderFactory)


class TransactionFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Transaction
        sqlalchemy_session = Session

    # TODO: Compute via RLP
    hash = factory.LazyFunction(Hash32Factory)

    block = factory.SubFactory(BlockFactory)

    nonce = 0
    gas_price = 1
    gas = 21000
    to = factory.LazyFunction(AddressFactory)
    value = b"\x00"
    data = b""
    v = b"\x00" * 32
    r = b"\x00" * 32
    s = b"\x00" * 32

    sender = factory.LazyFunction(AddressFactory)


class BlockTransactionFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = BlockTransaction
        sqlalchemy_session = Session

    block = factory.SubFactory(BlockFactory)
    transaction = factory.SubFactory(TransactionFactory)


class ReceiptFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Receipt
        sqlalchemy_session = Session
        rename = {"bloom": "_bloom"}

    transaction = factory.SubFactory(TransactionFactory)

    state_root = factory.LazyFunction(Hash32Factory)
    bloom = b""
    gas_used = 21000


class LogFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Log
        sqlalchemy_session = Session

    idx = 0
    receipt = factory.SubFactory(ReceiptFactory)

    address = factory.LazyFunction(AddressFactory)
    data = b""


class TopicFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = Topic
        sqlalchemy_session = Session

    topic = factory.LazyFunction(Hash32Factory)


class LogTopicFactory(factory.alchemy.SQLAlchemyModelFactory):  # type: ignore
    class Meta:
        model = LogTopic
        sqlalchemy_session = Session

    idx = 0

    topic = factory.SubFactory(TopicFactory)
    log = factory.SubFactory(LogFactory)

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
    # TODO: assert exception?

# Q's:
#   Where do local_filter_middleware tests get ran?
