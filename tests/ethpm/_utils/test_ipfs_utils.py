from pathlib import (
    Path,
)
import pytest

from ethpm._utils.ipfs import (
    extract_ipfs_path_from_uri,
    generate_file_hash,
    is_ipfs_uri,
)


@pytest.mark.parametrize(
    "value,expected",
    (
        (
            "ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u",
        ),
        (
            "ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
        (
            "ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
        (
            "ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
        (
            "ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
        (
            "ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
        (
            "ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/",
            "QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme",
        ),
    ),
)
def test_extract_ipfs_path_from_uri(value, expected):
    actual = extract_ipfs_path_from_uri(value)
    assert actual == expected


@pytest.mark.parametrize(
    "value,expected",
    (
        ("ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u", True),
        ("ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/", True),
        ("ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/", True),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/", True),
        ("ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme", True),
        ("ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme", True),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme", True),
        ("ipfs:QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", True),
        ("ipfs:/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", True),
        ("ipfs://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", True),
        # malformed
        ("ipfs//QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", False),
        ("ipfs/QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", False),
        ("ipfsQmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme/", False),
        # HTTP
        ("http://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme", False),
        ("https://QmTKB75Y73zhNbD3Y73xeXGjYrZHmaXXNxoZqGCagu7r8u/readme", False),
        # No hash
        ("ipfs://", False),
    ),
)
def test_is_ipfs_uri(value, expected):
    actual = is_ipfs_uri(value)
    assert actual is expected


@pytest.mark.parametrize(
    "file_name,file_contents,expected",
    (
        ("test-1.txt", "piper\n", "QmUdxEGxvp71kqYLkA91mtNg9QRRSPBtA3UV6VuYhoP7DB"),
        (
            "test-2.txt",
            "pipermerriam\n",
            "QmXqrQR7EMePe9LCRUVrfkxYg5EHRNpcA1PZnN4AnbM9DW",
        ),
        (
            "test-3.txt",
            "this is a test file for ipfs hash generation\n",
            "QmYknNUKXWSaxfCWVgHd8uVCYHhzPerVCLvCCBedWtqbnv",
        ),
    ),
)
def test_generate_file_hash(tmpdir, file_name, file_contents, expected):
    p = tmpdir.mkdir("sub").join(file_name)
    p.write(file_contents)
    ipfs_multihash = generate_file_hash(Path(p).read_bytes())
    assert ipfs_multihash == expected
