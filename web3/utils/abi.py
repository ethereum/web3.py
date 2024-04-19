from typing import (
    Any,
    List,
    Optional,
    Sequence,
    Union,
)

from eth_abi.abi import (
    ABICodec,
)

from eth_abi.registry import (
    registry as default_registry,
)
from eth_typing import (
    HexStr,
)

from web3.providers.rpc import (
    HTTPProvider,
)
from web3.providers import (
    BaseProvider,
)
from web3.types import (
    ABIEvent,
    ABIFunction,
)

from ens import (
    ENS,
)
from web3._utils.abi import (
    check_if_arguments_can_be_encoded,
    map_abi_data,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_ens_resolver,
    abi_string_to_text,
)

from eth_utils.abi import (
    get_abi_input_types,
)
from eth_utils.hexadecimal import (
    encode_hex,
)
from hexbytes import (
    HexBytes,
)


def get_abi_input_names(abi: Union[ABIFunction, ABIEvent]) -> List[str]:
    if "inputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["inputs"]]


def get_abi_output_names(abi: Union[ABIFunction]) -> List[str]:
    if "outputs" not in abi and abi["type"] == "fallback":
        return []
    return [arg["name"] for arg in abi["outputs"]]


def encode_abi(
    function_abi: ABIFunction,
    arguments: Sequence[Any] = None,
    data: Optional[HexStr] = None,
    is_async: Optional[bool] = False,
    provider: Optional[
        Any
    ] = None,  # TODO: Unable to use BaseProvider type here for some reason
    abi_codec: Optional[ABICodec] = None,
) -> HexStr:
    """
    Return encoded data from a function ABI and arguments.
    :param function_abi: Function ABI.
    :param type: `ABIFunction`
    :param data: Data to include in the encoded result.
    :param type: `HexStr`
    :param arguments: Arguments used for the transaction request.
    :param type: `Any`
    :param is_async: Enable async transaction encoder.
    :param type: `bool`
    :param provider: Provider instance to configure ENS for syncronous requests.
    :param type: `BaseProvider`
    :param abi_codec: Codec used for encoding and decoding. Default with
    `strict_bytes_type_checking` enabled.
    :param type: `ABICodec`
    :return: Encoded data for a transaction.
    :rtype: `HexStr`
    """
    if provider is None:
        provider = HTTPProvider()

    if abi_codec is None:
        abi_codec = ABICodec(default_registry)

    argument_types = get_abi_input_types(function_abi)

    if not check_if_arguments_can_be_encoded(function_abi, abi_codec, arguments, {}):
        raise TypeError(
            "One or more arguments could not be encoded to the necessary "
            f"ABI type. Expected types are: {', '.join(argument_types)}"
        )

    normalizers = [
        abi_address_to_hex,
        abi_bytes_to_bytes,
        abi_string_to_text,
    ]

    if not is_async:
        ens = ENS(provider)
        normalizers.append(abi_ens_resolver(ens=ens))

    normalized_arguments = map_abi_data(
        normalizers,
        argument_types,
        arguments,
    )
    encoded_arguments = abi_codec.encode(
        argument_types,
        normalized_arguments,
    )
    if data:
        return to_hex(HexBytes(data) + encoded_arguments)
    else:
        return encode_hex(encoded_arguments)
