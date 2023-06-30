from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Sequence,
    Union,
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
    abi_typed_params = abi_data_tree(abi_types_for_method, data)

    formatted_params = []
    for param in abi_typed_params:
        if param.abi_type == "address[]":
            # handle name conversion in an address list
            # Note: only supports single list atm, as is true the sync middleware
            # TODO: handle address[][], etc...
            formatted_data = await async_format_all_ens_names_to_address(
                async_web3,
                [param.abi_type[:-2]] * len(param.data),
                [subparam.data for subparam in param.data],
            )
        else:
            _abi_type, formatted_data = await async_abi_ens_resolver(
                async_web3,
                param.abi_type,
                param.data,
            )
        formatted_params.append(formatted_data)
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
        param_dict = params[0]
        fields = list(abi_types_for_method.keys() & param_dict.keys())
        formatted_params = await async_format_all_ens_names_to_address(
            async_web3,
            [abi_types_for_method[field] for field in fields],
            [param_dict[field] for field in fields],
        )
        formatted_dict = dict(zip(fields, formatted_params))
        return (formatted_dict,)
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
