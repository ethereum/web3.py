import json
from pathlib import (
    Path,
)
import pytest

from eth_utils import (
    to_canonical_address,
)
from eth_utils.toolz import (
    assoc,
    assoc_in,
)

from ethpm import (
    ASSETS_DIR,
    Package,
)
from ethpm.backends.ipfs import (
    get_ipfs_backend,
)
from ethpm.exceptions import (
    EthPMValidationError,
    ManifestBuildingError,
)
from ethpm.tools import (
    get_ethpm_local_manifest,
    get_ethpm_spec_manifest,
)
from ethpm.tools.builder import (
    as_package,
    authors,
    build,
    build_dependency,
    contract_type,
    deployment,
    deployment_type,
    description,
    init_manifest,
    inline_source,
    keywords,
    license,
    links,
    manifest_version,
    normalize_contract_type,
    package_name,
    pin_source,
    source_inliner,
    source_pinner,
    validate,
    version,
    write_to_disk,
)
from web3.tools.pytest_ethereum.linker import (
    deploy,
    link,
    linker,
)

BASE_MANIFEST = {"name": "package", "manifest": "ethpm/3", "version": "1.0.0"}


@pytest.fixture
def owned_package(ethpm_spec_dir):
    manifest = get_ethpm_spec_manifest("owned", "v3.json")
    # source_id missing `./` prefix in ethpm-spec ("Owned.sol"/"./Owned.sol" though both are valid)
    source_obj = manifest['sources'].pop('Owned.sol')
    updated_manifest = assoc_in(manifest, ['sources', './Owned.sol'], source_obj)

    compiler = get_ethpm_local_manifest("owned", "output_v3.json")["contracts"]
    contracts_dir = ethpm_spec_dir / "examples" / "owned" / "contracts"
    return contracts_dir, updated_manifest, compiler


# todo validate no duplicate contracts in package


@pytest.fixture
def standard_token_package(ethpm_spec_dir):
    standard_token_dir = ethpm_spec_dir / "examples" / "standard-token"
    manifest = get_ethpm_spec_manifest("standard-token", "v3.json")
    compiler = get_ethpm_local_manifest("standard-token", "output_v3.json")["contracts"]
    contracts_dir = standard_token_dir / "contracts"
    return contracts_dir, manifest, compiler


@pytest.fixture
def registry_package():
    root = ASSETS_DIR / "registry"
    compiler = json.loads(Path(root / "solc_output.json").read_text())["contracts"]
    contracts_dir = root / "contracts"
    manifest = json.loads((root / "v3.json").read_text())
    return contracts_dir, manifest, compiler


@pytest.fixture
def manifest_dir(tmpdir):
    return Path(tmpdir.mkdir("sub"))


def test_builder_simple_with_package(w3):
    package = build(
        {},
        package_name("package"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        validate(),
        as_package(w3),
    )
    assert isinstance(package, Package)
    assert package.version == "1.0.0"


PRETTY_MANIFEST = """{
    "manifest": "ethpm/3",
    "name": "package",
    "version": "1.0.0"
}"""

MINIFIED_MANIFEST = (
    '{"manifest":"ethpm/3","name":"package","version":"1.0.0"}'
)

OWNED_CONTRACT = "// SPDX-License-Identifier: MIT\npragma solidity ^0.6.8;\n\ncontract Owned {\n    address owner;\n    \n    modifier onlyOwner { require(msg.sender == owner); _; }\n\n    constructor() public {\n        owner = msg.sender;\n    }\n}"  # noqa: E501


def test_builder_writes_manifest_to_disk(manifest_dir):
    build(
        {},
        package_name("package"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        validate(),
        write_to_disk(
            manifest_root_dir=manifest_dir, manifest_name="1.0.0.json", prettify=True
        ),
    )
    actual_manifest = (manifest_dir / "1.0.0.json").read_text()
    assert actual_manifest == PRETTY_MANIFEST


def test_builder_to_disk_uses_default_cwd(manifest_dir, monkeypatch):
    monkeypatch.chdir(manifest_dir)
    build(
        {},
        package_name("package"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        write_to_disk(),
        validate(),
    )
    actual_manifest = (manifest_dir / "1.0.0.json").read_text()
    assert actual_manifest == MINIFIED_MANIFEST


def test_to_disk_writes_minified_manifest_as_default(manifest_dir):
    build(
        {},
        package_name("package"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        write_to_disk(manifest_root_dir=manifest_dir, manifest_name="1.0.0.json"),
        validate(),
    )
    actual_manifest = (manifest_dir / "1.0.0.json").read_text()
    assert actual_manifest == MINIFIED_MANIFEST


def test_to_disk_uses_default_manifest_name(manifest_dir):
    build(
        {},
        package_name("package"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        write_to_disk(manifest_root_dir=manifest_dir),
        validate(),
    )
    actual_manifest = (manifest_dir / "1.0.0.json").read_text()
    assert actual_manifest == MINIFIED_MANIFEST


@pytest.mark.parametrize(
    "write_to_disk_fn",
    (
        write_to_disk(manifest_root_dir=Path("not/a/directory")),
        write_to_disk(manifest_name="invalid_name"),
    ),
)
def test_to_disk_with_invalid_args_raises_exception(manifest_dir, write_to_disk_fn):
    with pytest.raises(ManifestBuildingError):
        build(
            {},
            package_name("package"),
            manifest_version("ethpm/3"),
            version("1.0.0"),
            write_to_disk_fn,
        )


def test_builder_with_manifest_validation():
    with pytest.raises(EthPMValidationError, match="_invalid_package_name"):
        build(
            {},
            package_name("_invalid_package_name"),
            manifest_version("ethpm/3"),
            version("1.0.0"),
            validate(),
        )


@pytest.mark.parametrize(
    "fn,value",
    (
        (authors("some", "guy"), {"authors": ["some", "guy"]}),
        (license("MIT"), {"license": "MIT"}),
        (description("This is a package."), {"description": "This is a package."}),
        (keywords("awesome", "package"), {"keywords": ["awesome", "package"]}),
        (
            links(documentation="ipfs..", website="www"),
            {"links": {"documentation": "ipfs..", "website": "www"}},
        ),
    ),
)
def test_builder_with_simple_meta_fields(fn, value):
    manifest = build(BASE_MANIFEST, fn, validate())
    expected = assoc(BASE_MANIFEST, "meta", value)
    assert manifest == expected


def test_builder_simple_with_multi_meta_field():
    manifest = build(
        BASE_MANIFEST,
        authors("some", "guy"),
        license("MIT"),
        description("description"),
        keywords("awesome", "package"),
        links(website="www", repository="github"),
        validate(),
    )
    expected = assoc(
        BASE_MANIFEST,
        "meta",
        {
            "license": "MIT",
            "authors": ["some", "guy"],
            "description": "description",
            "keywords": ["awesome", "package"],
            "links": {"website": "www", "repository": "github"},
        },
    )
    assert manifest == expected


def test_builder_with_inline_source(owned_package, monkeypatch):
    root, _, compiler_output = owned_package

    monkeypatch.chdir(root)
    manifest = build(BASE_MANIFEST, inline_source("Owned", compiler_output), validate())

    expected = assoc(
        BASE_MANIFEST,
        "sources",
        {
            "./Owned.sol": {
                "content": OWNED_CONTRACT,
                "installPath": "./Owned.sol",
                "type": "solidity",
            }
        },
    )
    assert manifest == expected


def test_builder_with_source_inliner(owned_package, monkeypatch):
    root, _, compiler_output = owned_package

    monkeypatch.chdir(root)
    inliner = source_inliner(compiler_output)
    manifest = build(BASE_MANIFEST, inliner("Owned"), validate())
    expected = assoc(
        BASE_MANIFEST,
        "sources",
        {
            "./Owned.sol": {
                "content": OWNED_CONTRACT,
                "installPath": "./Owned.sol",
                "type": "solidity",
            }
        },
    )
    assert manifest == expected


def test_builder_with_inline_source_with_package_root_dir_arg(owned_package):
    root, _, compiler_output = owned_package

    manifest = build(
        BASE_MANIFEST,
        inline_source("Owned", compiler_output, package_root_dir=root),
        validate(),
    )
    expected = assoc(
        BASE_MANIFEST,
        "sources",
        {
            "./Owned.sol": {
                "content": OWNED_CONTRACT,
                "installPath": "./Owned.sol",
                "type": "solidity",
            }
        },
    )
    print(manifest)
    print('-')
    print(expected)
    assert manifest == expected


def test_builder_with_pin_source(owned_package, dummy_ipfs_backend):
    root, expected, compiler_output = owned_package
    ipfs_backend = get_ipfs_backend()

    manifest = build(
        {},
        package_name("owned"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        authors("Piper Merriam <pipermerriam@gmail.com>"),
        description(
            "Reusable contracts which implement a privileged 'owner' model for authorization."
        ),
        keywords("authorization"),
        license("MIT"),
        links(documentation="ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"),
        pin_source("Owned", compiler_output, ipfs_backend, root),
        validate(),
    )

    assert manifest == expected


def test_builder_with_pinner(owned_package, dummy_ipfs_backend):
    root, expected, compiler_output = owned_package
    ipfs_backend = get_ipfs_backend()
    pinner = source_pinner(compiler_output, ipfs_backend, root)
    manifest = build(
        {},
        package_name("owned"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        authors("Piper Merriam <pipermerriam@gmail.com>"),
        description(
            "Reusable contracts which implement a privileged 'owner' model for authorization."
        ),
        keywords("authorization"),
        license("MIT"),
        links(documentation="ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"),
        pinner("Owned"),
        validate(),
    )

    assert manifest == expected


def test_builder_with_init_manifest(owned_package, dummy_ipfs_backend):
    root, expected, compiler_output = owned_package
    ipfs_backend = get_ipfs_backend()

    manifest = build(
        init_manifest(package_name="owned", version="1.0.0"),
        authors("Piper Merriam <pipermerriam@gmail.com>"),
        description(
            "Reusable contracts which implement a privileged 'owner' model for authorization."
        ),
        keywords("authorization"),
        license("MIT"),
        links(documentation="ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"),
        pin_source("Owned", compiler_output, ipfs_backend, root),
        validate(),
    )

    assert manifest == expected


def test_builder_with_default_contract_types(owned_package):
    _, _, compiler_output = owned_package

    manifest = build(BASE_MANIFEST, contract_type("Owned", compiler_output), validate())

    contract_type_data = normalize_contract_type(compiler_output["Owned.sol"]["Owned"], "Owned.sol")
    compilers_data = contract_type_data.pop('compiler')
    compilers_data["contractTypes"] = ["Owned"]
    expected_with_contract_type = assoc(
        BASE_MANIFEST, "contractTypes", {"Owned": contract_type_data}
    )
    expected = assoc(expected_with_contract_type, "compilers", [compilers_data])
    assert manifest == expected


def test_builder_with_single_alias_kwarg(owned_package):
    _, _, compiler_output = owned_package

    manifest = build(
        BASE_MANIFEST,
        contract_type("Owned", compiler_output, alias="OwnedAlias"),
        validate(),
    )

    contract_type_data = normalize_contract_type(compiler_output["Owned.sol"]["Owned"], "Owned.sol")
    compilers_data = contract_type_data.pop('compiler')
    compilers_data["contractTypes"] = ["OwnedAlias"]
    expected_with_contract_type = assoc(
        BASE_MANIFEST,
        "contractTypes",
        {"OwnedAlias": assoc(contract_type_data, "contractType", "Owned")},
    )
    expected = assoc(expected_with_contract_type, "compilers", [compilers_data])
    assert manifest == expected


def test_builder_without_alias_and_with_select_contract_types(owned_package):
    _, _, compiler_output = owned_package

    manifest = build(
        BASE_MANIFEST, contract_type("Owned", compiler_output, abi=True, source_id=True), validate()
    )

    contract_type_data = normalize_contract_type(compiler_output["Owned.sol"]["Owned"], "Owned.sol")
    omitted_fields = ("deploymentBytecode", "userdoc", "devdoc", "compiler")
    selected_data = {
        k: v for k, v in contract_type_data.items() if k not in omitted_fields
    }
    expected = assoc(BASE_MANIFEST, "contractTypes", {"Owned": selected_data})
    assert manifest == expected


def test_builder_with_alias_and_select_contract_types(owned_package):
    _, _, compiler_output = owned_package

    manifest = build(
        BASE_MANIFEST,
        contract_type(
            "Owned",
            compiler_output,
            alias="OwnedAlias",
            abi=True,
            compiler=False,
            devdoc=True,
            userdoc=True,
            deployment_bytecode=True,
            runtime_bytecode=False,
            source_id=True,
        ),
        validate(),
    )

    contract_type_data = normalize_contract_type(compiler_output["Owned.sol"]["Owned"], "Owned.sol")
    contract_type_data.pop("compiler")
    expected = assoc(
        BASE_MANIFEST,
        "contractTypes",
        {"OwnedAlias": assoc(contract_type_data, "contractType", "Owned")},
    )
    assert manifest == expected


def test_builder_manages_duplicate_compilers(owned_package):
    _, _, compiler_output = owned_package

    manifest = build(
        BASE_MANIFEST,
        contract_type(
            "Owned",
            compiler_output,
            abi=True,
            compiler=True,
            source_id=True,
        ),
        contract_type(
            "Owned",
            compiler_output,
            alias="OwnedAlias",
            abi=True,
            compiler=True,
            source_id=True,
        ),
        validate(),
    )
    contract_type_data = normalize_contract_type(compiler_output["Owned.sol"]["Owned"], "Owned.sol")
    compiler_data = contract_type_data.pop("compiler")
    contract_type_data.pop('deploymentBytecode')
    contract_type_data.pop('devdoc')
    contract_type_data.pop('userdoc')
    compiler_data_with_contract_types = assoc(
        compiler_data, 'contractTypes', ['Owned', 'OwnedAlias']
    )
    expected_with_contract_types = assoc(
        BASE_MANIFEST,
        "contractTypes",
        {
            "Owned": assoc(contract_type_data, "contractType", "Owned"),
            "OwnedAlias": assoc(contract_type_data, "contractType", "Owned"),
        },
    )
    expected_with_contract_types['contractTypes']['Owned'].pop("contractType")
    expected = assoc(expected_with_contract_types, 'compilers', [compiler_data_with_contract_types])
    assert manifest == expected


def test_builder_raises_exception_if_selected_contract_type_missing_from_solc(
    owned_package
):
    _, _, compiler_output = owned_package
    with pytest.raises(ManifestBuildingError, match="runtimeBytecode not available"):
        build(
            BASE_MANIFEST,
            contract_type("Owned", compiler_output, abi=True, runtime_bytecode=True),
        )


def test_builder_with_standard_token_manifest(
    standard_token_package, dummy_ipfs_backend, monkeypatch
):
    root, expected_manifest, compiler_output = standard_token_package
    ipfs_backend = get_ipfs_backend()

    monkeypatch.chdir(root)
    manifest = build(
        {},
        package_name("standard-token"),
        manifest_version("ethpm/3"),
        version("1.0.0"),
        pin_source("StandardToken", compiler_output, ipfs_backend),
        pin_source("Token", compiler_output, ipfs_backend),
        contract_type("StandardToken", compiler_output, abi=True, devdoc=True, source_id=True),
        contract_type(
            "Token", compiler_output, abi=True, devdoc=True, userdoc=True, source_id=True
        ),
        validate(),
    )
    assert manifest == expected_manifest


def test_builder_with_link_references(
    registry_package, dummy_ipfs_backend, monkeypatch
):
    root, expected_manifest, compiler_output = registry_package
    monkeypatch.chdir(root)
    inliner = source_inliner(compiler_output)
    manifest = build(
        {},
        package_name("solidity-registry"),
        manifest_version("ethpm/3"),
        version("2.0.0"),
        inliner("Authorized"),
        inliner("IndexedOrderedSetLib"),
        inliner("PackageDB"),
        inliner("PackageRegistry"),
        inliner("PackageRegistryInterface"),
        inliner("ReleaseDB"),
        inliner("ReleaseValidator"),
        contract_type(
            "AuthorityInterface",
            compiler_output,
            abi=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "Authorized",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "AuthorizedInterface",
            compiler_output,
            abi=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "WhitelistAuthority",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "WhitelistAuthorityInterface",
            compiler_output,
            abi=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "IndexedOrderedSetLib",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "PackageDB",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "PackageRegistry",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "PackageRegistryInterface",
            compiler_output,
            abi=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "ReleaseDB",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        contract_type(
            "ReleaseValidator",
            compiler_output,
            abi=True,
            compiler=True,
            deployment_bytecode=True,
            runtime_bytecode=True,
            devdoc=True,
            source_id=True,
        ),
        validate(),
    )
    assert manifest == expected_manifest


def test_builder_deployment_simple(w3):
    expected = json.dumps(
        {
            "name": "package",
            "version": "1.0.0",
            "manifest": "ethpm/3",
            "deployments": {
                "blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef": {  # noqa: E501
                    "Owned": {
                        "contractType": "Owned",
                        "address": "0xd3CdA913deB6f67967B99D67aCDFa1712C293601",
                    }
                }
            },
        }
    )
    manifest = build(
        BASE_MANIFEST,
        deployment(
            block_uri="blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # noqa: E501
            contract_instance="Owned",
            contract_type="Owned",
            address=to_canonical_address("0xd3cda913deb6f67967b99d67acdfa1712c293601"),
        ),
        validate(),
    )
    assert manifest == json.loads(expected)


@pytest.fixture
def escrow_package(w3, deployer, ethpm_spec_dir):
    manifest = ethpm_spec_dir / "examples" / "escrow" / "v3.json"
    escrow_deployer = deployer(manifest)
    escrow_strategy = linker(
        deploy("SafeSendLib"),
        link("Escrow", "SafeSendLib"),
        deploy("Escrow", w3.eth.accounts[0]),
    )
    escrow_deployer.register_strategy("Escrow", escrow_strategy)
    escrow_package = escrow_deployer.deploy("Escrow")
    return escrow_package, w3


def test_builder_deployment_type_complex(escrow_package):
    escrow, w3 = escrow_package
    escrow_dep_type = deployment_type(
        contract_instance="Escrow",
        contract_type="Escrow",
        deployment_bytecode={
            "bytecode": "0x608060405234801561001057600080fd5b5060405160208061045383398101604081815291516002819055336000818152602081815285822084905583855294519294919390927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a3506103d2806100816000396000f3006080604052600436106100775763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663095ea7b3811461007c57806318160ddd146100b457806323b872dd146100db57806370a0823114610105578063a9059cbb14610126578063dd62ed3e1461014a575b600080fd5b34801561008857600080fd5b506100a0600160a060020a0360043516602435610171565b604080519115158252519081900360200190f35b3480156100c057600080fd5b506100c96101d8565b60408051918252519081900360200190f35b3480156100e757600080fd5b506100a0600160a060020a03600435811690602435166044356101de565b34801561011157600080fd5b506100c9600160a060020a03600435166102c9565b34801561013257600080fd5b506100a0600160a060020a03600435166024356102e4565b34801561015657600080fd5b506100c9600160a060020a036004358116906024351661037b565b336000818152600160209081526040808320600160a060020a038716808552908352818420869055815186815291519394909390927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925928290030190a35060015b92915050565b60025481565b600160a060020a03831660009081526020819052604081205482118015906102295750600160a060020a03841660009081526001602090815260408083203384529091529020548211155b80156102355750600082115b156102be57600160a060020a0380841660008181526020818152604080832080548801905593881680835284832080548890039055600182528483203384528252918490208054879003905583518681529351929391927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9281900390910190a35060016102c2565b5060005b9392505050565b600160a060020a031660009081526020819052604090205490565b3360009081526020819052604081205482118015906103035750600082115b15610373573360008181526020818152604080832080548790039055600160a060020a03871680845292819020805487019055805186815290519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a35060016101d2565b5060006101d2565b600160a060020a039182166000908152600160209081526040808320939094168252919091522054905600a165627a7a72305820cf9d6a3f751ca1e6b9bc2324e42633a4cde513d64c3e6cc32d6359629249e90200290000000000000000000000000000000000000000000000000000000000000001"  # noqa: E501
        },
        runtime_bytecode={
            "bytecode": "0x6080604052600436106100775763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663095ea7b3811461007c57806318160ddd146100b457806323b872dd146100db57806370a0823114610105578063a9059cbb14610126578063dd62ed3e1461014a575b600080fd5b34801561008857600080fd5b506100a0600160a060020a0360043516602435610171565b604080519115158252519081900360200190f35b3480156100c057600080fd5b506100c96101d8565b60408051918252519081900360200190f35b3480156100e757600080fd5b506100a0600160a060020a03600435811690602435166044356101de565b34801561011157600080fd5b506100c9600160a060020a03600435166102c9565b34801561013257600080fd5b506100a0600160a060020a03600435166024356102e4565b34801561015657600080fd5b506100c9600160a060020a036004358116906024351661037b565b336000818152600160209081526040808320600160a060020a038716808552908352818420869055815186815291519394909390927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925928290030190a35060015b92915050565b60025481565b600160a060020a03831660009081526020819052604081205482118015906102295750600160a060020a03841660009081526001602090815260408083203384529091529020548211155b80156102355750600082115b156102be57600160a060020a0380841660008181526020818152604080832080548801905593881680835284832080548890039055600182528483203384528252918490208054879003905583518681529351929391927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9281900390910190a35060016102c2565b5060005b9392505050565b600160a060020a031660009081526020819052604090205490565b3360009081526020819052604081205482118015906103035750600082115b15610373573360008181526020818152604080832080548790039055600160a060020a03871680845292819020805487019055805186815290519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a35060016101d2565b5060006101d2565b600160a060020a039182166000908152600160209081526040808320939094168252919091522054905600a165627a7a72305820cf9d6a3f751ca1e6b9bc2324e42633a4cde513d64c3e6cc32d6359629249e9020029"  # noqa: E501
        },
        compiler={
            "name": "solc",
            "version": "0.4.24+commit.e67f0147.Emscripten.clang",
            "settings": {"optimize": True},
        },
    )
    safesendlib_dep_type = deployment_type(
        contract_instance="SafeSendLib", contract_type="SafeSendLib"
    )
    manifest = build(
        {},
        package_name("escrow"),
        version("1.0.0"),
        manifest_version("ethpm/3"),
        escrow_dep_type(
            block_uri="blockchain://1111111111111111111111111111111111111111111111111111111111111111/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # noqa: E501
            address=escrow.deployments.get_instance("Escrow").address,
        ),
        # dep_type with block uri
        safesendlib_dep_type(
            block_uri="blockchain://1111111111111111111111111111111111111111111111111111111111111111/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # noqa: E501
            address=escrow.deployments.get_instance("SafeSendLib").address,
        ),
        # simple deployment
        deployment(
            block_uri="blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # noqa: E501
            contract_instance="Escrow",
            contract_type="Escrow",
            address=escrow.deployments.get_instance("Escrow").address,
        ),
        # simple deployment
        deployment(
            block_uri="blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",  # noqa: E501
            contract_instance="SafeSendLib",
            contract_type="SafeSendLib",
            address=escrow.deployments.get_instance("SafeSendLib").address,
        ),
        validate(),
    )
    assert len(manifest["deployments"].keys()) == 2
    assert len(list(manifest["deployments"].values())[0]) == 2
    assert len(list(manifest["deployments"].values())[1]) == 2


def test_builder_with_single_build_dependency():
    expected_build_dep = {
        "package": "ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"
    }
    expected = assoc_in(BASE_MANIFEST, ["buildDependencies"], expected_build_dep)
    actual = build(
        BASE_MANIFEST,
        build_dependency(
            "package", "ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"
        ),
        validate(),
    )
    assert actual == expected


def test_builder_with_multiple_build_dependencies():
    expected_build_deps = {
        "escrow": "ipfs://QmPDwMHk8e1aMEZg3iKsUiPSkhHkywpGB3KHKM52RtGrkv",
        "package": "ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW",
    }
    expected = assoc_in(BASE_MANIFEST, ["buildDependencies"], expected_build_deps)
    actual = build(
        BASE_MANIFEST,
        build_dependency(
            "package", "ipfs://QmUYcVzTfSwJoigggMxeo2g5STWAgJdisQsqcXHws7b1FW"
        ),
        build_dependency(
            "escrow", "ipfs://QmPDwMHk8e1aMEZg3iKsUiPSkhHkywpGB3KHKM52RtGrkv"
        ),
        validate(),
    )
    assert actual == expected


def test_builder_with_invalid_uri():
    with pytest.raises(
        EthPMValidationError, match="is not a supported content-addressed URI"
    ):
        build(
            {},
            package_name("package"),
            version("1.0.0"),
            manifest_version("ethpm/3"),
            build_dependency("package", "www.google.com"),
        )
