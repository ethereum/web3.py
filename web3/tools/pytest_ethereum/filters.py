import logging
from typing import Iterator, NamedTuple, Optional, Tuple, Union
from eth_typing import Address, BlockNumber, Hash32
from eth_utils import to_tuple
from sqlalchemy import and_, or_, orm
from sqlalchemy.orm import aliased
from sqlalchemy.sql import ClauseElement

from web3.tools.pytest_ethereum.models import (
    Block,
    Header,
    Log,
    LogTopic,
    Receipt,
    Transaction,
)

BlockIdentifier = BlockNumber
# TODO: update to python3.8
# BlockIdentifier = Union[
#     Literal['latest'],
#     Literal['pending'],
#     Literal['earliest'],
#     BlockNumber,
# ]
TopicType = Union[None, Hash32, Tuple[Hash32, ...]]


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
