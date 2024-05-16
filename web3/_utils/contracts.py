from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

from eth_abi.codec import (
    ABICodec,
)
from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    ABI,
    ABIFunction,
    ABIFunctionInfo,
    ChecksumAddress,
    HexStr,
    TypeStr,
)
from eth_utils import (
    add_0x_prefix,
    encode_hex,
    is_binary_address,
    is_checksum_address,
    is_list_like,
    is_text,
)
from hexbytes import (
    HexBytes,
)

from web3.utils.abi import (
    get_abi_input_types,
    get_function_abi,
    get_function_info,
)
from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    get_fallback_func_abi,
    get_receive_func_abi,
    map_abi_data,
    named_tree,
)
from web3._utils.blocks import (
    is_hex_encoded_block_hash,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.function_identifiers import (
    FallbackFn,
    ReceiveFn,
)
from web3._utils.method_formatters import (
    to_integer_if_hex,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_ens_resolver,
    abi_string_to_text,
)
from web3.exceptions import (
    BlockNumberOutOfRange,
    MismatchedABI,
    Web3TypeError,
    Web3ValidationError,
    Web3ValueError,
)
from web3.types import (
    BlockIdentifier,
    BlockNumber,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def extract_argument_types(*args: Sequence[Any]) -> str:
    """
    Takes a list of arguments and returns a string representation of the argument types,
    appropriately collapsing `tuple` types into the respective nested types.
    """
    collapsed_args = []

    for arg in args:
        if is_list_like(arg):
            collapsed_nested = []
            for nested in arg:
                if is_list_like(nested):
                    collapsed_nested.append(f"({extract_argument_types(nested)})")
                else:
                    collapsed_nested.append(_get_argument_readable_type(nested))
            collapsed_args.append(",".join(collapsed_nested))
        else:
            collapsed_args.append(_get_argument_readable_type(arg))

    return ",".join(collapsed_args)


def encode_abi(
    w3: Union["AsyncWeb3", "Web3"],
    abi: ABIFunction,
    arguments: Sequence[Any],
    data: Optional[HexStr] = None,
) -> HexStr:
    try:
        argument_types = get_abi_input_types(abi)
    except ValueError:
        # fallback or receive functions do not have arguments
        # return encoded data without arguments
        return to_hex(HexBytes(data))

    if not check_if_arguments_can_be_encoded(abi, w3.codec, arguments, {}):
        raise Web3TypeError(
            "One or more arguments could not be encoded to the necessary "
            f"ABI type. Expected types are: {', '.join(argument_types)}"
        )

    normalizers = [
        abi_address_to_hex,
        abi_bytes_to_bytes,
        abi_string_to_text,
    ]
    if not w3.eth.is_async:
        normalizers.append(abi_ens_resolver(w3))

    normalized_arguments = map_abi_data(
        normalizers,
        argument_types,
        arguments,
    )
    encoded_arguments = w3.codec.encode(
        argument_types,
        normalized_arguments,
    )
    if data:
        return to_hex(HexBytes(data) + encoded_arguments)
    else:
        return encode_hex(encoded_arguments)


def prepare_transaction(
    address: ChecksumAddress,
    w3: Union["AsyncWeb3", "Web3"],
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    transaction: Optional[TxParams] = None,
    fn_args: Optional[Sequence[Any]] = None,
    fn_kwargs: Optional[Any] = None,
) -> TxParams:
    """
    :parameter `is_function_abi` is used to distinguish  function abi from contract abi
    Returns a dictionary of the transaction that could be used to call this
    TODO: make this a public API
    TODO: add new prepare_deploy_transaction API
    """
    if fn_abi is None:
        try:
            fn_abi = get_function_abi(
                contract_abi, fn_identifier, fn_args, fn_kwargs, abi_codec=w3.codec
            )
        except (MismatchedABI, TypeError):
            raise

    validate_payable(transaction, fn_abi)

    if transaction is None:
        prepared_transaction: TxParams = {}
    else:
        prepared_transaction = cast(TxParams, dict(**transaction))

    if "data" in prepared_transaction:
        raise Web3ValueError("Transaction parameter may not contain a 'data' key")

    if address:
        prepared_transaction.setdefault("to", address)

    prepared_transaction["data"] = encode_transaction_data(
        w3,
        fn_identifier,
        contract_abi,
        fn_abi,
        fn_args,
        fn_kwargs,
    )
    return prepared_transaction


def encode_transaction_data(
    w3: Union["AsyncWeb3", "Web3"],
    fn_identifier: Union[str, Type[FallbackFn], Type[ReceiveFn]],
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    args: Optional[Sequence[Any]] = None,
    kwargs: Optional[Any] = None,
) -> HexStr:
    if fn_identifier is FallbackFn:
        fn_abi, fn_selector, fn_arguments = get_fallback_function_info(
            contract_abi, fn_abi
        )
    elif fn_identifier is ReceiveFn:
        fn_abi, fn_selector, fn_arguments = get_receive_function_info(
            contract_abi, fn_abi
        )
    elif is_text(fn_identifier):
        function_info = get_function_info(
            contract_abi,
            fn_identifier,
            args,
            kwargs,
            w3.codec,
        )
    else:
        raise Web3TypeError("Unsupported function identifier")

    return add_0x_prefix(
        encode_abi(
            w3,
            abi=function_info["abi"],
            arguments=function_info["arguments"],
            data=function_info["selector"],
        )
    )


def decode_transaction_data(
    fn_abi: ABIFunction,
    data: HexStr,
    normalizers: Sequence[Callable[[TypeStr, Any], Tuple[TypeStr, Any]]] = None,
) -> Dict[str, Any]:
    data = HexBytes(data)

    try:
        argument_types = get_abi_input_types(fn_abi)
    except ValueError:
        # fallback or receive functions do not have arguments
        # proceed with decoding data without arguments
        argument_types = []
        pass

    abi_codec = ABICodec(default_registry)
    decoded = abi_codec.decode(argument_types, HexBytes(data[4:]))
    if normalizers:
        decoded = map_abi_data(normalizers, argument_types, decoded)
    return named_tree(fn_abi["inputs"], decoded)


def get_fallback_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> ABIFunctionInfo:
    if fn_abi is None:
        fn_abi = get_fallback_func_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return ABIFunctionInfo(
        abi=fn_abi,
        selector=fn_selector,
        arguments=fn_arguments,
    )


def get_receive_function_info(
    contract_abi: Optional[ABI] = None, fn_abi: Optional[ABIFunction] = None
) -> ABIFunctionInfo:
    if fn_abi is None:
        fn_abi = get_receive_func_abi(contract_abi)
    fn_selector = encode_hex(b"")
    fn_arguments: Tuple[Any, ...] = tuple()
    return ABIFunctionInfo(
        abi=fn_abi,
        selector=fn_selector,
        arguments=fn_arguments,
    )


def validate_payable(transaction: TxParams, abi: ABIFunction) -> None:
    """
    Raise Web3ValidationError if non-zero ether
    is sent to a non-payable function.
    """
    if "value" in transaction:
        if to_integer_if_hex(transaction["value"]) != 0:
            if (
                "payable" in abi
                and not abi["payable"]
                or "stateMutability" in abi
                and abi["stateMutability"] == "nonpayable"
            ):
                raise Web3ValidationError(
                    "Sending non-zero ether to a contract function "
                    "with payable=False. Please ensure that "
                    "transaction's value is 0."
                )


def _get_argument_readable_type(arg: Any) -> str:
    if is_checksum_address(arg) or is_binary_address(arg):
        return "address"

    return arg.__class__.__name__


def parse_block_identifier(
    w3: "Web3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return w3.eth.default_block
    if isinstance(block_identifier, int):
        return parse_block_identifier_int(w3, block_identifier)
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        return w3.eth.get_block(block_identifier)["number"]
    else:
        raise BlockNumberOutOfRange


def parse_block_identifier_int(w3: "Web3", block_identifier_int: int) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = w3.eth.get_block("latest")["number"]
        block_num = last_block + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutOfRange
    return BlockNumber(block_num)


async def async_parse_block_identifier(
    async_w3: "AsyncWeb3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return async_w3.eth.default_block
    if isinstance(block_identifier, int):
        return await async_parse_block_identifier_int(async_w3, block_identifier)
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        requested_block = await async_w3.eth.get_block(block_identifier)
        return requested_block["number"]
    else:
        raise BlockNumberOutOfRange


async def async_parse_block_identifier_int(
    async_w3: "AsyncWeb3", block_identifier_int: int
) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = await async_w3.eth.get_block("latest")
        last_block_num = last_block["number"]
        block_num = last_block_num + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutOfRange
    return BlockNumber(block_num)
