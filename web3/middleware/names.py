from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Sequence,
    Union,
)

from toolz import (
    merge,
)

from web3._utils.normalizers import (
    abi_ens_resolver,
    async_abi_ens_resolver,
)
from web3._utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)
from web3.types import (
    AsyncMiddlewareCoroutine,
    Middleware,
    RPCEndpoint,
)

from .._utils.abi import (
    abi_data_tree,
    async_data_tree_map,
    strip_abi_type,
)
from .._utils.formatters import (
    recursive_map,
)
from .formatting import (
    construct_formatting_middleware,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )


def name_to_address_middleware(w3: "Web3") -> Middleware:
    normalizers = [
        abi_ens_resolver(w3),
    ]
    return construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )


# -- async -- #


async def async_format_all_ens_names_to_address(
    async_web3: "AsyncWeb3",
    abi_types_for_method: Sequence[Any],
    data: Sequence[Any],
) -> Sequence[Any]:
    # provide a stepwise version of what the curried formatters do
    abi_typed_params = abi_data_tree(abi_types_for_method, data)
    formatted_data_tree = await async_data_tree_map(
        async_web3,
        async_abi_ens_resolver,
        abi_typed_params,
    )
    formatted_params = recursive_map(strip_abi_type, formatted_data_tree)
    return formatted_params


async def async_apply_ens_to_address_conversion(
    async_web3: "AsyncWeb3",
    params: Any,
    abi_types_for_method: Union[Sequence[str], Dict[str, str]],
) -> Any:
    if isinstance(abi_types_for_method, Sequence):
        formatted_params = await async_format_all_ens_names_to_address(
            async_web3, abi_types_for_method, params
        )
        return formatted_params

    elif isinstance(abi_types_for_method, dict):
        # first arg is a dict but other args may be preset
        # e.g. eth_call({...}, "latest")
        # this is similar to applying a dict formatter at index 0 of the args
        param_dict = params[0]
        fields = list(abi_types_for_method.keys() & param_dict.keys())
        formatted_params = await async_format_all_ens_names_to_address(
            async_web3,
            [abi_types_for_method[field] for field in fields],
            [param_dict[field] for field in fields],
        )
        formatted_dict = dict(zip(fields, formatted_params))
        formatted_params_dict = merge(param_dict, formatted_dict)
        return (formatted_params_dict, *params[1:])

    else:
        raise TypeError(
            f"ABI definitions must be a list or dictionary, "
            f"got {abi_types_for_method!r}"
        )


async def async_name_to_address_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any],
    async_w3: "AsyncWeb3",
) -> AsyncMiddlewareCoroutine:
    async def middleware(method: RPCEndpoint, params: Any) -> Any:
        abi_types_for_method = RPC_ABIS.get(method, None)
        if abi_types_for_method is not None:
            params = await async_apply_ens_to_address_conversion(
                async_w3,
                params,
                abi_types_for_method,
            )
        return await make_request(method, params)

    return middleware
