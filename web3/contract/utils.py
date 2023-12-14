import itertools
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from eth_abi.exceptions import (
    DecodingError,
)
from eth_typing import (
    ChecksumAddress,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.abi import (
    filter_by_type,
    get_abi_output_types,
    map_abi_data,
    named_tree,
    recursive_dict_to_namedtuple,
)
from web3._utils.async_transactions import (
    async_fill_transaction_defaults,
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
from web3.exceptions import (
    BadFunctionCallOutput,
)
from web3.types import (
    ABI,
    ABIFunction,
    BlockIdentifier,
    CallOverride,
    FunctionIdentifier,
    TContractFn,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )

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
    decode_tuples: Optional[bool] = False,
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

    if decode_tuples:
        decoded = named_tree(fn_abi["outputs"], normalized_data)
        normalized_data = recursive_dict_to_namedtuple(decoded)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


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


def estimate_gas_for_function(
    address: ChecksumAddress,
    w3: "Web3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    state_override: Optional[CallOverride] = None,
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

    return w3.eth.estimate_gas(estimate_transaction, block_identifier, state_override)


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


def find_functions_by_identifier(
    contract_abi: ABI,
    w3: Union["Web3", "AsyncWeb3"],
    address: ChecksumAddress,
    callable_check: Callable[..., Any],
    function_type: Type[TContractFn],
) -> List[TContractFn]:
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


def get_function_by_identifier(
    fns: Sequence[TContractFn], identifier: str
) -> TContractFn:
    if len(fns) > 1:
        raise ValueError(
            f"Found multiple functions with matching {identifier}. " f"Found: {fns!r}"
        )
    elif len(fns) == 0:
        raise ValueError(f"Could not find any function with matching {identifier}")
    return fns[0]


# --- async --- #


async def async_call_contract_function(
    async_w3: "AsyncWeb3",
    address: ChecksumAddress,
    normalizers: Tuple[Callable[..., Any], ...],
    function_identifier: FunctionIdentifier,
    transaction: TxParams,
    block_id: Optional[BlockIdentifier] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    state_override: Optional[CallOverride] = None,
    ccip_read_enabled: Optional[bool] = None,
    decode_tuples: Optional[bool] = False,
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

    return_data = await async_w3.eth.call(
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
            and await async_w3.eth.get_code(address) in ACCEPTABLE_EMPTY_STRINGS
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

    if decode_tuples:
        decoded = named_tree(fn_abi["outputs"], normalized_data)
        normalized_data = recursive_dict_to_namedtuple(decoded)

    if len(normalized_data) == 1:
        return normalized_data[0]
    else:
        return normalized_data


async def async_transact_with_contract_function(
    address: ChecksumAddress,
    async_w3: "AsyncWeb3",
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
        async_w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        transaction=transaction,
        fn_abi=fn_abi,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    txn_hash = await async_w3.eth.send_transaction(transact_transaction)
    return txn_hash


async def async_estimate_gas_for_function(
    address: ChecksumAddress,
    async_w3: "AsyncWeb3",
    fn_identifier: Optional[FunctionIdentifier] = None,
    transaction: Optional[TxParams] = None,
    contract_abi: Optional[ABI] = None,
    fn_abi: Optional[ABIFunction] = None,
    block_identifier: Optional[BlockIdentifier] = None,
    state_override: Optional[CallOverride] = None,
    *args: Any,
    **kwargs: Any,
) -> int:
    """Estimates gas cost a function call would take.

    Don't call this directly, instead use :meth:`Contract.estimate_gas`
    on your contract instance.
    """
    estimate_transaction = prepare_transaction(
        address,
        async_w3,
        fn_identifier=fn_identifier,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await async_w3.eth.estimate_gas(
        estimate_transaction, block_identifier, state_override
    )


async def async_build_transaction_for_function(
    address: ChecksumAddress,
    async_w3: "AsyncWeb3",
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
        async_w3,
        fn_identifier=function_name,
        contract_abi=contract_abi,
        fn_abi=fn_abi,
        transaction=transaction,
        fn_args=args,
        fn_kwargs=kwargs,
    )

    return await async_fill_transaction_defaults(async_w3, prepared_transaction)
