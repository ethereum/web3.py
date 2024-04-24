from typing import (
    Any,
    Callable,
    Optional,
    Sequence,
    Tuple,
)

from eth_abi.abi import (
    ABICodec,
)
from eth_typing import (
    ABIFunction,
    HexStr,
    TypeStr,
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

from web3._utils.abi import (
    build_non_strict_registry,
    build_strict_registry,
    check_if_arguments_can_be_encoded,
    map_abi_data,
)
from web3._utils.encoding import (
    to_hex,
)
from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_bytes,
    abi_string_to_text,
)


def encode_abi(
    function_abi: ABIFunction,
    arguments: Sequence[Any] = None,
    data: Optional[HexStr] = None,
    is_async: Optional[bool] = False,
    resolver: Optional[Callable[..., Tuple[TypeStr, Any]]] = None,
    abi_codec: Optional[ABICodec] = None,
    strict: Optional[bool] = True,
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
    if abi_codec is None:
        registry = build_strict_registry()
        if not strict:
            registry = build_non_strict_registry()
        abi_codec = ABICodec(registry)

    try:
        argument_types = get_abi_input_types(function_abi)
    except ValueError:
        argument_types = []

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

    if not is_async and resolver is not None:
        normalizers.append(resolver)

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
