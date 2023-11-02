from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Optional,
    cast,
)

from eth_utils.toolz import (
    assoc,
)

from web3.datastructures import (
    AttributeDict,
)
from web3.types import (
    AsyncMiddlewareCoroutine,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        PersistentConnectionProvider,
    )


def attrdict_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], _w3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    Converts any result which is a dictionary into an `AttributeDict`.

    Note: Accessing `AttributeDict` properties via attribute
        (e.g. my_attribute_dict.property1) will not preserve typing.
    """

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        response = make_request(method, params)

        if "result" in response:
            return assoc(
                response, "result", AttributeDict.recursive(response["result"])
            )
        else:
            return response

    return middleware


# --- async --- #


async def async_attrdict_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], async_w3: "AsyncWeb3"
) -> AsyncMiddlewareCoroutine:
    """
    Converts any result which is a dictionary into an `AttributeDict`.

    Note: Accessing `AttributeDict` properties via attribute
        (e.g. my_attribute_dict.property1) will not preserve typing.
    """

    async def middleware(method: RPCEndpoint, params: Any) -> Optional[RPCResponse]:
        response = await make_request(method, params)
        if async_w3.provider.has_persistent_connection:
            # asynchronous response processing
            provider = cast("PersistentConnectionProvider", async_w3.provider)
            provider._request_processor.append_middleware_response_processor(
                response, _handle_async_response
            )
            return response
        else:
            return _handle_async_response(response)

    return middleware


def _handle_async_response(response: RPCResponse) -> RPCResponse:
    if "result" in response:
        return assoc(response, "result", AttributeDict.recursive(response["result"]))
    elif "params" in response and "result" in response["params"]:
        # this is a subscription response
        return assoc(
            response,
            "params",
            assoc(
                response["params"],
                "result",
                AttributeDict.recursive(response["params"]["result"]),
            ),
        )
    else:
        return response
