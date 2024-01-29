from abc import (
    ABC,
)
from typing import (
    TYPE_CHECKING,
    Any,
    cast,
)

from eth_utils.toolz import (
    assoc,
)

from web3.datastructures import (
    AttributeDict,
)
from web3.middleware.base import (
    Web3Middleware,
)

if TYPE_CHECKING:
    from web3 import (  # noqa: F401
        AsyncWeb3,
        Web3,
    )
    from web3.providers import (  # noqa: F401
        PersistentConnectionProvider,
    )
    from web3.types import (  # noqa: F401
        RPCEndpoint,
        RPCResponse,
    )


def _handle_async_response(response: "RPCResponse") -> "RPCResponse":
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


class AttributeDictMiddleware(Web3Middleware, ABC):
    """
    Converts any result which is a dictionary into an `AttributeDict`.

    Note: Accessing `AttributeDict` properties via attribute
        (e.g. my_attribute_dict.property1) will not preserve typing.
    """

    def response_processor(self, method: "RPCEndpoint", response: "RPCResponse") -> Any:
        if "result" in response:
            return assoc(
                response, "result", AttributeDict.recursive(response["result"])
            )
        else:
            return response

    # -- async -- #

    async def async_response_processor(
        self, method: "RPCEndpoint", response: "RPCResponse"
    ) -> Any:
        if self._w3.provider.has_persistent_connection:
            # asynchronous response processing
            provider = cast("PersistentConnectionProvider", self._w3.provider)
            provider._request_processor.append_middleware_response_processor(
                response, _handle_async_response
            )
            return response
        else:
            return _handle_async_response(response)


AttributeDictMiddleware = AttributeDictMiddleware
