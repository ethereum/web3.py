import hashlib
from pathlib import (
    Path,
)
from typing import (
    Dict,
)
from urllib import (
    parse,
)

from eth_utils import (
    to_text,
)
from google.protobuf.descriptor import (
    Descriptor,
)

from ethpm._utils.protobuf.ipfs_file_pb2 import (  # type: ignore
    Data,
    PBNode,
)

try:
    # `ipfshttpclient` backend is optional. This is only imported if the "web3[ipfs]"
    # install extra is installed
    from base58 import (
        b58encode,
    )
except ImportError:
    pass


def dummy_ipfs_pin(path: Path) -> Dict[str, str]:
    """
    Return IPFS data as if file was pinned to an actual node.
    """
    ipfs_return = {
        "Hash": generate_file_hash(path.read_bytes()),
        "Name": path.name,
        "Size": str(path.stat().st_size),
    }
    return ipfs_return


def create_ipfs_uri(ipfs_hash: str) -> str:
    return f"ipfs://{ipfs_hash}"


def extract_ipfs_path_from_uri(value: str) -> str:
    """
    Return the path from an IPFS URI.
    Path = IPFS hash & following path.
    """
    parse_result = parse.urlparse(value)

    if parse_result.netloc:
        if parse_result.path:
            return "".join((parse_result.netloc, parse_result.path.rstrip("/")))
        else:
            return parse_result.netloc
    else:
        return parse_result.path.strip("/")


def is_ipfs_uri(value: str) -> bool:
    """
    Return a bool indicating whether or not the value is a valid IPFS URI.
    """
    parse_result = parse.urlparse(value)
    if parse_result.scheme != "ipfs":
        return False
    if not parse_result.netloc and not parse_result.path:
        return False

    return True


#
# Generate IPFS hash
# Lifted from https://github.com/ethereum/populus/blob/feat%2Fv2/populus/utils/ipfs.py
#


SHA2_256 = b"\x12"
LENGTH_32 = b"\x20"


def multihash(value: bytes) -> bytes:
    data_hash = hashlib.sha256(value).digest()

    multihash_bytes = SHA2_256 + LENGTH_32 + data_hash
    return multihash_bytes


def serialize_bytes(file_bytes: bytes) -> Descriptor:
    file_size = len(file_bytes)

    data_protobuf = Data(
        Type=Data.DataType.Value("File"),
        Data=file_bytes,
        filesize=file_size,
    )
    data_protobuf_bytes = data_protobuf.SerializeToString()

    file_protobuf = PBNode(Links=[], Data=data_protobuf_bytes)

    return file_protobuf


def generate_file_hash(content_bytes: bytes) -> str:
    file_protobuf: Descriptor = serialize_bytes(content_bytes)
    # type ignored b/c SerializeToString is manually attached in ipfs_file_pb2.py
    file_protobuf_bytes = file_protobuf.SerializeToString()  # type: ignore
    file_multihash = multihash(file_protobuf_bytes)
    return to_text(b58encode(file_multihash))
