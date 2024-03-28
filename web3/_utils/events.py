from abc import (
    ABC,
    abstractmethod,
)
from enum import (
    Enum,
)
from typing import (
    TYPE_CHECKING,
    Any,
    Collection,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

from eth_abi import (
    grammar,
)
from eth_abi.codec import (
    ABICodec,
)
from eth_typing import (
    ChecksumAddress,
    HexStr,
    Primitives,
    TypeStr,
)
from eth_utils import (
    event_abi_to_log_topic,
    is_list_like,
    keccak,
    to_bytes,
    to_dict,
    to_hex,
    to_tuple,
)
from eth_utils.curried import (
    apply_formatter_if,
)
from eth_utils.toolz import (
    complement,
    compose,
    cons,
    curry,
    valfilter,
)
from hexbytes import (
    HexBytes,
)

import web3
from web3._utils.abi import (
    get_normalized_abi_arg_type,
)
from web3._utils.encoding import (
    encode_single_packed,
    hexstr_if_str,
)
from web3.datastructures import (
    AttributeDict,
)
from web3.types import (
    ABIEvent,
    ABIEventParams,
    BlockIdentifier,
    EventData,
    FilterParams,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3._utils.filters import (  # noqa: F401
        AsyncLogFilter,
        LogFilter,
    )


def log_entry_data_to_bytes(
    log_entry_data: Union[Primitives, HexStr, str],
) -> HexBytes:
    return hexstr_if_str(to_bytes, log_entry_data)


def is_dynamic_sized_type(type_str: TypeStr) -> bool:
    abi_type = grammar.parse(type_str)
    return abi_type.is_dynamic


@to_tuple
def get_event_abi_types_for_decoding(
    event_inputs: Sequence[ABIEventParams],
) -> Iterable[TypeStr]:
    """
    Event logs use the `keccak(value)` for indexed inputs of type `bytes` or
    `string`.  Because of this we need to modify the types so that we can
    decode the log entries using the correct types.
    """
    for input_abi in event_inputs:
        if input_abi["indexed"] and is_dynamic_sized_type(input_abi["type"]):
            yield "bytes32"
        else:
            yield get_normalized_abi_arg_type(input_abi)


@to_tuple
def pop_singlets(seq: Sequence[Any]) -> Iterable[Any]:
    yield from (i[0] if is_list_like(i) and len(i) == 1 else i for i in seq)


@curry
def remove_trailing_from_seq(
    seq: Sequence[Any], remove_value: Optional[Any] = None
) -> Sequence[Any]:
    index = len(seq)
    while index > 0 and seq[index - 1] == remove_value:
        index -= 1
    return seq[:index]


_normalize_topic_list = compose(
    remove_trailing_from_seq(remove_value=None),
    pop_singlets,
)


def normalize_topic_list(topics: List[HexStr]) -> List[HexStr]:
    return _normalize_topic_list(topics)


def is_indexed(arg: Any) -> bool:
    if isinstance(arg, TopicArgumentFilter) is True:
        return True
    return False


is_not_indexed = complement(is_indexed)


class BaseEventFilterBuilder:
    formatter = None
    _fromBlock = None
    _toBlock = None
    _address = None
    _immutable = False

    def __init__(
        self,
        event_abi: ABIEvent,
        abi_codec: ABICodec,
        formatter: Optional[EventData] = None,
    ) -> None:
        self.event_abi = event_abi
        self.abi_codec = abi_codec
        self.formatter = formatter
        self.event_topic = initialize_event_topics(self.event_abi)
        self.args = AttributeDict(
            _build_argument_filters_from_event_abi(event_abi, abi_codec)
        )
        self._ordered_arg_names = tuple(arg["name"] for arg in event_abi["inputs"])

    @property
    def fromBlock(self) -> BlockIdentifier:
        return self._fromBlock

    @fromBlock.setter
    def fromBlock(self, value: BlockIdentifier) -> None:
        if self._fromBlock is None and not self._immutable:
            self._fromBlock = value
        else:
            raise ValueError(
                f"fromBlock is already set to {self._fromBlock!r}. "
                "Resetting filter parameters is not permitted"
            )

    @property
    def toBlock(self) -> BlockIdentifier:
        return self._toBlock

    @toBlock.setter
    def toBlock(self, value: BlockIdentifier) -> None:
        if self._toBlock is None and not self._immutable:
            self._toBlock = value
        else:
            raise ValueError(
                f"toBlock is already set to {self._toBlock!r}. "
                "Resetting filter parameters is not permitted"
            )

    @property
    def address(self) -> ChecksumAddress:
        return self._address

    @address.setter
    def address(self, value: ChecksumAddress) -> None:
        if self._address is None and not self._immutable:
            self._address = value
        else:
            raise ValueError(
                f"address is already set to {self.address!r}. "
                "Resetting filter parameters is not permitted"
            )

    @property
    def ordered_args(self) -> Tuple[Any, ...]:
        return tuple(map(self.args.__getitem__, self._ordered_arg_names))

    @property
    @to_tuple
    def indexed_args(self) -> Tuple[Any, ...]:
        return tuple(filter(is_indexed, self.ordered_args))

    @property
    @to_tuple
    def data_args(self) -> Tuple[Any, ...]:
        return tuple(filter(is_not_indexed, self.ordered_args))

    @property
    def topics(self) -> List[HexStr]:
        arg_topics = tuple(arg.match_values for arg in self.indexed_args)
        return normalize_topic_list(cons(to_hex(self.event_topic), arg_topics))

    @property
    def data_argument_values(self) -> Tuple[Any, ...]:
        if self.data_args is not None:
            return tuple(arg.match_values for arg in self.data_args)
        else:
            return (None,)

    @property
    def filter_params(self) -> FilterParams:
        params = {
            "topics": self.topics,
            "fromBlock": self.fromBlock,
            "toBlock": self.toBlock,
            "address": self.address,
        }
        return valfilter(lambda x: x is not None, params)


class EventFilterBuilder(BaseEventFilterBuilder):
    def deploy(self, w3: "Web3") -> "LogFilter":
        if not isinstance(w3, web3.Web3):
            raise ValueError(f"Invalid web3 argument: got: {w3!r}")

        for arg in AttributeDict.values(self.args):  # type: ignore[arg-type]
            arg._immutable = True  # type: ignore[attr-defined]
        self._immutable = True

        log_filter = cast("LogFilter", w3.eth.filter(self.filter_params))
        log_filter.filter_params = self.filter_params
        log_filter.set_data_filters(self.data_argument_values)
        log_filter.builder = self
        if self.formatter is not None:
            log_filter.log_entry_formatter = self.formatter
        return log_filter


class AsyncEventFilterBuilder(BaseEventFilterBuilder):
    async def deploy(self, async_w3: "AsyncWeb3") -> "AsyncLogFilter":
        if not isinstance(async_w3, web3.AsyncWeb3):
            raise ValueError(f"Invalid web3 argument: got: {async_w3!r}")

        for arg in AttributeDict.values(self.args):  # type: ignore[arg-type]
            arg._immutable = True  # type: ignore[attr-defined]
        self._immutable = True

        log_filter = await async_w3.eth.filter(self.filter_params)
        log_filter = cast("AsyncLogFilter", log_filter)
        log_filter.filter_params = self.filter_params
        log_filter.set_data_filters(self.data_argument_values)
        log_filter.builder = self
        if self.formatter is not None:
            log_filter.log_entry_formatter = self.formatter
        return log_filter


def initialize_event_topics(event_abi: ABIEvent) -> Union[bytes, List[Any]]:
    if event_abi["anonymous"] is False:
        # https://github.com/python/mypy/issues/4976
        return event_abi_to_log_topic(event_abi)  # type: ignore
    else:
        return list()


@to_dict
def _build_argument_filters_from_event_abi(
    event_abi: ABIEvent, abi_codec: ABICodec
) -> Iterable[Tuple[str, "BaseArgumentFilter"]]:
    for item in event_abi["inputs"]:
        key = item["name"]
        value: "BaseArgumentFilter"
        if item["indexed"] is True:
            value = TopicArgumentFilter(
                abi_codec=abi_codec, arg_type=get_normalized_abi_arg_type(item)
            )
        else:
            value = DataArgumentFilter(arg_type=get_normalized_abi_arg_type(item))
        yield key, value


array_to_tuple = apply_formatter_if(is_list_like, tuple)


@to_tuple
def _normalize_match_values(match_values: Collection[Any]) -> Iterable[Any]:
    for value in match_values:
        yield array_to_tuple(value)


class BaseArgumentFilter(ABC):
    _match_values: Tuple[Any, ...] = None
    _immutable = False

    def __init__(self, arg_type: TypeStr) -> None:
        self.arg_type = arg_type

    def match_single(self, value: Any) -> None:
        if self._immutable:
            raise ValueError("Setting values is forbidden after filter is deployed.")
        if self._match_values is None:
            self._match_values = _normalize_match_values((value,))
        else:
            raise ValueError("An argument match value/s has already been set.")

    def match_any(self, *values: Collection[Any]) -> None:
        if self._immutable:
            raise ValueError("Setting values is forbidden after filter is deployed.")
        if self._match_values is None:
            self._match_values = _normalize_match_values(values)
        else:
            raise ValueError("An argument match value/s has already been set.")

    @property
    @abstractmethod
    def match_values(self) -> None:
        pass


class DataArgumentFilter(BaseArgumentFilter):
    # type ignore b/c conflict with BaseArgumentFilter.match_values type
    @property
    def match_values(self) -> Tuple[TypeStr, Tuple[Any, ...]]:  # type: ignore
        return self.arg_type, self._match_values


class TopicArgumentFilter(BaseArgumentFilter):
    def __init__(self, arg_type: TypeStr, abi_codec: ABICodec) -> None:
        self.abi_codec = abi_codec
        self.arg_type = arg_type

    @to_tuple
    def _get_match_values(self) -> Iterable[HexStr]:
        yield from (self._encode(value) for value in self._match_values)

    # type ignore b/c conflict with BaseArgumentFilter.match_values type
    @property
    def match_values(self) -> Optional[Tuple[HexStr, ...]]:  # type: ignore
        if self._match_values is not None:
            return self._get_match_values()
        else:
            return None

    def _encode(self, value: Any) -> HexStr:
        if is_dynamic_sized_type(self.arg_type):
            return to_hex(keccak(encode_single_packed(self.arg_type, value)))
        else:
            return to_hex(self.abi_codec.encode([self.arg_type], [value]))


class EventLogErrorFlags(Enum):
    Discard = "discard"
    Ignore = "ignore"
    Strict = "strict"
    Warn = "warn"

    @classmethod
    def flag_options(self) -> List[str]:
        return [key.upper() for key in self.__members__.keys()]
