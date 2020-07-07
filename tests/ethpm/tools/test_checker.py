import pytest

from ethpm.tools.checker import (
    WARNINGS,
    check_contract_types,
    check_manifest,
    check_meta,
    check_sources,
)


def test_checker_simple():
    warnings = check_manifest({})
    assert warnings == {
        "manifest": "Manifest missing a required 'manifest' field.",
        "name": "Manifest missing a suggested 'name' field",
        "version": "Manifest missing a suggested 'version' field.",
        "meta": "Manifest missing a suggested 'meta' field.",
        "sources": """Manifest is missing a sources field, which defines a source tree that """
        """should comprise the full source tree necessary to recompile the contracts """
        """contained in this release.""",
        "contractTypes": """Manifest does not contain any 'contractTypes'. Packages should """
        """only include contract types that can be found in the source files for this """
        """package. Packages should not include contract types from dependencies. """
        """Packages should not include abstract contracts in the contract types section """
        """of a release.""",
        "compilers": "Manifest is missing a suggested `compilers` field.",
    }


BASIC_MANIFEST = {
    "name": "package",
    "version": "1.0.0",
    "manifest": "ethpm/3",
}


@pytest.mark.parametrize(
    "manifest,expected",
    (
        ({}, {"meta": WARNINGS["meta_missing"]}),
        ({"meta": {}}, {"meta": WARNINGS["meta_missing"]}),
        (
            {"meta": {"x": "x"}},
            {
                "meta.authors": WARNINGS["authors_missing"],
                "meta.description": WARNINGS["description_missing"],
                "meta.links": WARNINGS["links_missing"],
                "meta.keywords": WARNINGS["keywords_missing"],
                "meta.license": WARNINGS["license_missing"],
            },
        ),
    ),
)
def test_check_meta(manifest, expected):
    warnings = check_meta(manifest, {})
    assert warnings == expected


@pytest.mark.parametrize(
    "manifest,expected",
    (
        # Sad paths
        ({}, {"sources": WARNINGS["sources_missing"]}),
        ({"sources": []}, {"sources": WARNINGS["sources_missing"]}),
        # Happy path
        ({"sources": {"links": "www.github.com"}}, {}),
    ),
)
def test_check_sources(manifest, expected):
    warnings = check_sources(manifest, {})
    assert warnings == expected


@pytest.mark.parametrize(
    "manifest,expected",
    (
        ({}, {"contractTypes": WARNINGS["contract_type_missing"]}),
        ({"contractTypes": {}}, {"contractTypes": WARNINGS["contract_type_missing"]}),
        (
            {"contractTypes": {"x": {"runtimeBytecode": {"invalid": "invalid"}}}},
            {
                "contractTypes": {
                    "x": {
                        "abi": WARNINGS["abi_missing"].format("x"),
                        "contractType": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("x"),
                        "deploymentBytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("x"),
                        "runtimeBytecode": WARNINGS[
                            "bytecode_subfield_missing"
                        ].format("x", "runtime"),
                        "devdoc": WARNINGS["devdoc_missing"].format("x"),
                        "userdoc": WARNINGS["userdoc_missing"].format("x"),
                    }
                }
            },
        ),
        (
            {
                "contractTypes": {
                    "x": {
                        "deploymentBytecode": [],
                        "runtimeBytecode": {"bytecode": []},
                    },
                    "y": {
                        "abi": [1],
                        "deploymentBytecode": [],
                        "runtimeBytecode": [],
                    },
                }
            },
            {
                "contractTypes": {
                    "x": {
                        "abi": WARNINGS["abi_missing"].format("x"),
                        "contractType": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("x"),
                        "deploymentBytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("x"),
                        "runtimeBytecode": WARNINGS[
                            "bytecode_subfield_missing"
                        ].format("x", "runtime"),
                        "devdoc": WARNINGS["devdoc_missing"].format("x"),
                        "userdoc": WARNINGS["userdoc_missing"].format("x"),
                    },
                    "y": {
                        "contractType": WARNINGS[
                            "contract_type_subfield_missing"
                        ].format("y"),
                        "deploymentBytecode": WARNINGS[
                            "deployment_bytecode_missing"
                        ].format("y"),
                        "runtimeBytecode": WARNINGS["runtime_bytecode_missing"].format(
                            "y"
                        ),
                        "devdoc": WARNINGS["devdoc_missing"].format("y"),
                        "userdoc": WARNINGS["userdoc_missing"].format("y"),
                    },
                }
            },
        ),
    ),
)
def test_check_contract_types(manifest, expected):
    warnings = check_contract_types(manifest, {})
    assert warnings == expected
