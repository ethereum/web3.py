import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    List,
    Optional,
    Tuple,
    Type,
)

from eth_abi.exceptions import (
    DecodingError,
)
from eth_typing import (
    BlockNumber,
    ChecksumAddress,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    filter_by_type,
    get_abi_output_types,
    map_abi_data,
)
from web3._utils.async_transactions import (
    fill_transaction_defaults as async_fill_transaction_defaults,
)
from web3._utils.blocks import (
    is_hex_encoded_block_hash,
)
from web3._utils.contracts import (
    find_matching_fn_abi,
    prepare_transaction,
)
from web3._utils.normalizers import (
    BASE_RETURN_NORMALIZERS,
)
from web3._utils.transactions import (
    fill_transaction_defaults,
)
from web3.contract.base_contract import (
    BaseContractFunction,
)
from web3.exceptions import (
    BadFunctionCallOutput,
    BlockNumberOutofRange,
)
from web3.types import (  # noqa: F401
    ABI,
    ABIFunction,
    BlockIdentifier,
    CallOverride,
    FunctionIdentifier,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

ACCEPTABLE_EMPTY_STRINGS = ["0x", b"0x", "", b""]


def call_contract_function(
    w3: "Web3",
    address: ChecksumAddress,
    normalizers: Tuple[Callable[..., Any], ...],
    function_identifier: FunctionIdentifier,
    transaction: TxParams,
    block_id: Optional[BlockIdentifier] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    state_override: Optional[CallOverride] = None,
    ccip_read_enabled: Optional[bool] = None,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return_data = w3.eth.call(
        call_transaction,
        block_identifier=block_id,
        state_override=state_override,
        ccip_read_enabled=ccip_read_enabled,
    )

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(
            contract_abi, w3.codec, function_identifier, args, kwargs
        )

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = w3.codec.decode(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS
            and w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_identifier} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
            )
        raise BadFunctionCallOutput(msg) from e

    _normalizers = itertools.chain(
        BASE_RETURN_NORMALIZERS,
        normalizers,
    )
    normalized_data = map_abi_data(_normalizers, output_types, output_data)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


async def async_call_contract_function(
    async_w3: "Web3",
    address: ChecksumAddress,
    normalizers: Tuple[Callable[..., Any], ...],
    function_identifier: FunctionIdentifier,
    transaction: TxParams,
    block_id: Optional[BlockIdentifier] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    state_override: Optional[CallOverride] = None,
    ccip_read_enabled: Optional[bool] = None,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    Helper function for interacting with a contract function using the
    `eth_call` API.
    """
    call_transaction = prepare_transaction(
        address,
        async_w3,
        fn_identifier=function_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return_data = await async_w3.eth.call(  # type: ignore
        call_transaction,
        block_identifier=block_id,
        state_override=state_override,
        ccip_read_enabled=ccip_read_enabled,
    )

    if fn_abi is None:
        fn_abi = find_matching_fn_abi(
            contract_abi, async_w3.codec, function_identifier, args, kwargs
        )

    output_types = get_abi_output_types(fn_abi)

    try:
        output_data = async_w3.codec.decode(output_types, return_data)
    except DecodingError as e:
        # Provide a more helpful error message than the one provided by
        # eth-abi-utils
        is_missing_code_error = (
            return_data in ACCEPTABLE_EMPTY_STRINGS
            and await async_w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS  # type: ignore  # noqa: E501
        )
        if is_missing_code_error:
            msg = (
                "Could not transact with/call contract function, is contract "
                "deployed correctly and chain synced?"
            )
        else:
            msg = (
                f"Could not decode contract function call to {function_identifier} "
                f"with return data: {str(return_data)}, output_types: {output_types}"
            )
        raise BadFunctionCallOutput(msg) from e

    _normalizers = itertools.chain(
        BASE_RETURN_NORMALIZERS,
        normalizers,
    )
    normalized_data = map_abi_data(_normalizers, output_types, output_data)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


async def async_parse_block_identifier(
    w3: "Web3", block_identifier: BlockIdentifier
) -> BlockIdentifier:
    if block_identifier is None:
        return w3.eth.default_block
    if isinstance(block_identifier, int):
        return await async_parse_block_identifier_int(w3, block_identifier)
    elif block_identifier in ["latest", "earliest", "pending", "safe", "finalized"]:
        return block_identifier
    elif isinstance(block_identifier, bytes) or is_hex_encoded_block_hash(
        block_identifier
    ):
        requested_block = await w3.eth.get_block(block_identifier)  # type: ignore
        return requested_block["number"]
    else:
        raise BlockNumberOutofRange


async def async_parse_block_identifier_int(
    w3: "Web3", block_identifier_int: int
) -> BlockNumber:
    if block_identifier_int >= 0:
        block_num = block_identifier_int
    else:
        last_block = await w3.eth.get_block("latest")  # type: ignore
        last_block_num = last_block.number
        block_num = last_block_num + block_identifier_int + 1
        if block_num < 0:
            raise BlockNumberOutofRange
    return BlockNumber(block_num)


def transact_with_contract_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> HexBytes:
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = w3.eth.send_transaction(transact_transaction)
    return txn_hash


async def async_transact_with_contract_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> HexBytes:
    """
    Helper function for interacting with a contract function by sending a
    transaction.
    """
    transact_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = await w3.eth.send_transaction(transact_transaction)  # type: ignore
    return txn_hash


def estimate_gas_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    *args: Any,
    **kwargs: Any,
) -> int:
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimate_gas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return w3.eth.estimate_gas(estimate_transaction, block_identifier)


async def async_estimate_gas_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    *args: Any,
    **kwargs: Any,
) -> int:
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimate_gas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await w3.eth.estimate_gas(  # type: ignore
        estimate_transaction, block_identifier
    )


def build_transaction_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> TxParams:
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.build_transaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    prepared_transaction = fill_transaction_defaults(w3, prepared_transaction)

    return prepared_transaction


async def async_build_transaction_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    function_name: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    *args: Any,
    **kwargs: Any,
) -> TxParams:
    """Builds a dictionary with the fields required to make the given transaction

    Don't call this directly, instead use :meth:`Contract.build_transaction`
    on your contract instance.
    """
    prepared_transaction = prepare_transaction(
        address,
        w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await async_fill_transaction_defaults(w3, prepared_transaction)


def find_functions_by_identifier(
    contract_abi: ABI,
    w3: "Web3",
    address: ChecksumAddress,
    callable_check: Callable[..., Any],
    function_type: Type[BaseContractFunction],
) -> List[BaseContractFunction]:
    fns_abi = filter_by_type("function", contract_abi)
    return [
        function_type.factory(
            fn_abi["name"],
            w3=w3,
            contract_abi=contract_abi,
            address=address,
            function_identifier=fn_abi["name"],
            abi=fn_abi,
        )
        for fn_abi in fns_abi
        if callable_check(fn_abi)
    ]
