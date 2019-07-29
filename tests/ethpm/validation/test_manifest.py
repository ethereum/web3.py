import pytest

from ethpm import (
    ASSETS_DIR,
)
from ethpm.exceptions import (
    EthPMValidationError,
)
from ethpm.validation.manifest import (
    extract_contract_types_from_deployments,
    validate_manifest_against_schema,
    validate_manifest_deployments,
    validate_manifest_exists,
    validate_meta_object,
    validate_raw_manifest_format,
)
from ethpm.validation.package import (
    validate_manifest_version,
)


def test_validate_raw_manifest_configuration_validates_strict_manifests(
    all_strict_manifests
):
    assert validate_raw_manifest_format(all_strict_manifests) is None


def test_validate_raw_manifest_format_invalidates_pretty_manifests(
    all_pretty_manifests
):
    with pytest.raises(EthPMValidationError):
        validate_raw_manifest_format(all_pretty_manifests)


@pytest.mark.parametrize(
    "manifest",
    (
        # not alphabetical
        '{"x":"y","a":"b"}',
        # not UTF-8
        '{"\x80":"b","c":"d"}',
        # newlines
        '{"a":"b",\n"c":"d"}',
        '{"a":"b","c":"d"}\n',
        # whitespace
        '{"a":"b","c": "d"}',
    ),
)
def test_validate_raw_manifest_format_invalidates_invalid_manifests(tmpdir, manifest):
    p = tmpdir.mkdir("invalid").join("manifest.json")
    p.write(manifest)
    invalid_manifest = p.read()
    with pytest.raises(EthPMValidationError):
        validate_raw_manifest_format(invalid_manifest)


def test_validate_manifest_exists_validates():
    assert (
        validate_manifest_exists(ASSETS_DIR / "safe-math-lib" / "1.0.0.json")
        is None
    )


def test_validate_manifest_exists_invalidates():
    with pytest.raises(EthPMValidationError):
        validate_manifest_exists("DNE")


def test_validate_manifest_against_all_manifest_types(all_manifests):
    assert validate_manifest_against_schema(all_manifests) is None


def test_validate_manifest_invalidates(invalid_manifest):
    with pytest.raises(EthPMValidationError):
        validate_manifest_against_schema(invalid_manifest)


def test_validate_deployed_contracts_present_validates(
    manifest_with_conflicting_deployments
):
    with pytest.raises(EthPMValidationError):
        validate_manifest_deployments(manifest_with_conflicting_deployments)


def test_validate_deployments(safe_math_lib_package):
    validate = validate_manifest_deployments(safe_math_lib_package.manifest)
    assert validate is None


def test_validate_deployed_contracts_pr(manifest_with_no_deployments):
    validate = validate_manifest_deployments(manifest_with_no_deployments)
    assert validate is None


@pytest.mark.parametrize(
    "data,expected",
    (
        ({}, set()),
        ([{"some": {"contract_type": "one"}}], set(["one"])),
        (
            [{"some": {"contract_type": "one"}, "other": {"contract_type": "two"}}],
            set(["one", "two"]),
        ),
    ),
)
def test_extract_contract_types_from_deployments(data, expected):
    actual = extract_contract_types_from_deployments(data)
    assert actual == expected


@pytest.mark.parametrize("version", ("2"))
def test_validate_manifest_version_validates_version_two_string(version):
    validate = validate_manifest_version(version)
    assert validate is None


@pytest.mark.parametrize("version", (1, 2, "1" "3", b"3"))
def test_validate_manifest_version_invalidates_incorrect_versions(version):
    with pytest.raises(EthPMValidationError):
        validate_manifest_version(version)


@pytest.mark.parametrize(
    "meta,extra_fields",
    (
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "A Package that does things.",
                "keywords": ["ethpm", "package"],
                "links": {"documentation": "ipfs://Qm..."},
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "A Package that does things.",
                "keywords": ["ethpm", "package"],
                "links": {"documentation": "ipfs://Qm..."},
                "x-hash": "0x...",
            },
            True,
        ),
    ),
)
def test_validate_meta_object_validates(meta, extra_fields):
    result = validate_meta_object(meta, allow_extra_meta_fields=extra_fields)
    assert result is None


@pytest.mark.parametrize(
    "meta,extra_fields",
    (
        # With allow_extra_meta_fields=False
        ({"invalid": "field"}, False),
        ({"license": 123}, False),
        ({"license": "MIT", "authors": "auther@gmail.com"}, False),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": ["description", "of", "package"],
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": "singlekw",
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": ["ipfs://Qm"],
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": {"documentation": "ipfs://Qm"},
                "extra": "field",
            },
            False,
        ),
        (
            {
                "license": "MIT",
                "authors": ["author@gmail.com"],
                "description": "description",
                "keywords": ["auth", "package"],
                "links": {"documentation": "ipfs://Qm"},
                "x-hash": "0x",
            },
            False,
        ),
        # With allow_extra_meta_fields=True
        # Improperly formatted "x" field
        ({"license": "MIT", "extra": "field"}, True),
    ),
)
def test_validate_meta_object_invalidates(meta, extra_fields):
    with pytest.raises(EthPMValidationError):
        validate_meta_object(meta, allow_extra_meta_fields=extra_fields)
