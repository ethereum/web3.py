import functools
import json
from pathlib import (
    Path,
)
import tempfile
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
)

from eth_typing import (
    URI,
    HexStr,
    Manifest,
)
from eth_utils import (
    add_0x_prefix,
    is_hex,
    is_string,
    to_bytes,
    to_checksum_address,
    to_dict,
    to_list,
)
from eth_utils.toolz import (
    assoc,
    assoc_in,
    concat,
    curry,
    pipe,
)

from ethpm import (
    Package,
)
from ethpm._utils.chains import (
    is_BIP122_block_uri,
)
from ethpm.backends.ipfs import (
    BaseIPFSBackend,
)
from ethpm.exceptions import (
    EthPMValidationError,
    ManifestBuildingError,
)
from ethpm.package import (
    format_manifest,
)
from ethpm.uri import (
    is_supported_content_addressed_uri,
)
from ethpm.validation.manifest import (
    validate_manifest_against_schema,
)
from ethpm.validation.package import (
    validate_package_name,
)
from web3._utils.validation import (
    validate_address,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def build(obj: Dict[str, Any], *fns: Callable[..., Any]) -> Dict[str, Any]:
    """
    Wrapper function to pipe manifest through build functions.
    Does not validate the manifest by default.
    """
    return pipe(obj, *fns)


#
# Required Fields
#


@curry
def package_name(name: str, manifest: Manifest) -> Manifest:
    """
    Return a copy of manifest with `name` set to "name".
    """
    return assoc(manifest, "name", name)


@curry
def manifest_version(manifest_version: str, manifest: Manifest) -> Manifest:
    """
    Return a copy of manifest with `manifest_version` set to "manifest".
    """
    return assoc(manifest, "manifest", manifest_version)


@curry
def version(version: str, manifest: Manifest) -> Manifest:
    """
    Return a copy of manifest with `version` set to "version".
    """
    return assoc(manifest, "version", version)


#
# Meta
#


def authors(*author_list: str) -> Manifest:
    """
    Return a copy of manifest with a list of author posargs set
    to "meta": {"authors": author_list}
    """
    return _authors(author_list)


@curry
@functools.wraps(authors)
def _authors(authors: Set[str], manifest: Manifest) -> Manifest:
    return assoc_in(manifest, ("meta", "authors"), list(authors))


@curry
def license(license: str, manifest: Manifest) -> Manifest:
    """
    Return a copy of manifest with `license` set to
    "meta": {"license": `license`}
    """
    return assoc_in(manifest, ("meta", "license"), license)


@curry
def description(description: str, manifest: Manifest) -> Manifest:
    """
    Return a copy of manifest with `description` set to
    "meta": {"descriptions": `description`}
    """
    return assoc_in(manifest, ("meta", "description"), description)


def keywords(*keyword_list: str) -> Manifest:
    """
    Return a copy of manifest with a list of keyword posargs set to
    "meta": {"keywords": keyword_list}
    """
    return _keywords(keyword_list)


@curry
@functools.wraps(keywords)
def _keywords(keywords: Set[str], manifest: Manifest) -> Manifest:
    return assoc_in(manifest, ("meta", "keywords"), list(keywords))


def links(**link_dict: str) -> Manifest:
    """
    Return a copy of manifest with a dict of link kwargs set to
    "meta": {"links": link_dict}
    """
    return _links(link_dict)


@curry
def _links(link_dict: Dict[str, str], manifest: Manifest) -> Manifest:
    return assoc_in(manifest, ("meta", "links"), link_dict)


#
# Sources
#


def get_names_and_paths(compiler_output: Dict[str, Any]) -> Dict[str, str]:
    """
    Return a mapping of contract name to relative path as defined in compiler output.
    """
    return {
        contract_name: make_path_relative(path)
        for path in compiler_output
        for contract_name in compiler_output[path].keys()
    }


def make_path_relative(path: str) -> str:
    """
    Returns the given path prefixed with "./" if the path
    is not already relative in the compiler output.
    """
    if "../" in path:
        raise ManifestBuildingError(
            f"Path: {path} appears to be outside of the virtual source tree. "
            "Please make sure all sources are within the virtual source tree "
            "root directory."
        )

    if path[:2] != "./":
        return f"./{path}"
    return path


def source_inliner(
    compiler_output: Dict[str, Any], package_root_dir: Optional[Path] = None
) -> Manifest:
    return _inline_sources(compiler_output, package_root_dir)


@curry
def _inline_sources(
    compiler_output: Dict[str, Any], package_root_dir: Optional[Path], name: str
) -> Manifest:
    return _inline_source(name, compiler_output, package_root_dir)


def inline_source(
    name: str, compiler_output: Dict[str, Any], package_root_dir: Optional[Path] = None
) -> Manifest:
    """
    Return a copy of manifest with added field to
    "sources": {relative_source_path: contract_source_data}.

    If `package_root_dir` is not provided, cwd is expected to resolve the relative
    path to the source as defined in the compiler output.
    """
    return _inline_source(name, compiler_output, package_root_dir)


@curry
def _inline_source(
    name: str,
    compiler_output: Dict[str, Any],
    package_root_dir: Optional[Path],
    manifest: Manifest,
) -> Manifest:
    names_and_paths = get_names_and_paths(compiler_output)
    cwd = Path.cwd()
    try:
        source_path = names_and_paths[name]
    except KeyError:
        raise ManifestBuildingError(
            f"Unable to inline source: {name}. "
            f"Available sources include: {list(sorted(names_and_paths.keys()))}."
        )

    if package_root_dir:
        if (package_root_dir / source_path).is_file():
            source_data = (package_root_dir / source_path).read_text()
        else:
            raise ManifestBuildingError(
                f"Contract source: {source_path} cannot be found in "
                f"provided package_root_dir: {package_root_dir}."
            )
    elif (cwd / source_path).is_file():
        source_data = (cwd / source_path).read_text()
    else:
        raise ManifestBuildingError(
            "Contract source cannot be resolved, please make sure that the working "
            "directory is set to the correct directory or provide `package_root_dir`."
        )

    # rstrip used here since Path.read_text() adds a newline to returned contents
    source_data_object = {
        "content": source_data.rstrip("\n"),
        "installPath": source_path,
        "type": "solidity",
    }
    return assoc_in(manifest, ["sources", source_path], source_data_object)


def source_pinner(
    compiler_output: Dict[str, Any],
    ipfs_backend: BaseIPFSBackend,
    package_root_dir: Optional[Path] = None,
) -> Manifest:
    return _pin_sources(compiler_output, ipfs_backend, package_root_dir)


@curry
def _pin_sources(
    compiler_output: Dict[str, Any],
    ipfs_backend: BaseIPFSBackend,
    package_root_dir: Optional[Path],
    name: str,
) -> Manifest:
    return _pin_source(name, compiler_output, ipfs_backend, package_root_dir)


def pin_source(
    name: str,
    compiler_output: Dict[str, Any],
    ipfs_backend: BaseIPFSBackend,
    package_root_dir: Optional[Path] = None,
) -> Manifest:
    """
    Pins source to IPFS and returns a copy of manifest with added field to
    "sources": {relative_source_path: IFPS URI}.

    If `package_root_dir` is not provided, cwd is expected to resolve the relative path
    to the source as defined in the compiler output.
    """
    return _pin_source(name, compiler_output, ipfs_backend, package_root_dir)


@curry
def _pin_source(
    name: str,
    compiler_output: Dict[str, Any],
    ipfs_backend: BaseIPFSBackend,
    package_root_dir: Optional[Path],
    manifest: Manifest,
) -> Manifest:
    names_and_paths = get_names_and_paths(compiler_output)
    try:
        source_path = names_and_paths[name]
    except KeyError:
        raise ManifestBuildingError(
            f"Unable to pin source: {name}. "
            f"Available sources include: {list(sorted(names_and_paths.keys()))}."
        )
    if package_root_dir:
        if not (package_root_dir / source_path).is_file():
            raise ManifestBuildingError(
                f"Unable to find and pin contract source: {source_path} "
                f"under specified package_root_dir: {package_root_dir}."
            )
        (ipfs_data,) = ipfs_backend.pin_assets(package_root_dir / source_path)
    else:
        cwd = Path.cwd()
        if not (cwd / source_path).is_file():
            raise ManifestBuildingError(
                f"Unable to find and pin contract source: {source_path} "
                f"current working directory: {cwd}."
            )
        (ipfs_data,) = ipfs_backend.pin_assets(cwd / source_path)

    source_data_object = {
        "urls": [f"ipfs://{ipfs_data['Hash']}"],
        "type": "solidity",
        "installPath": source_path,
    }
    return assoc_in(manifest, ["sources", source_path], source_data_object)


#
# Contract Types
#


def contract_type(
    name: str,
    compiler_output: Dict[str, Any],
    alias: Optional[str] = None,
    abi: Optional[bool] = False,
    compiler: Optional[bool] = False,
    contract_type: Optional[bool] = False,
    deployment_bytecode: Optional[bool] = False,
    devdoc: Optional[bool] = False,
    userdoc: Optional[bool] = False,
    source_id: Optional[bool] = False,
    runtime_bytecode: Optional[bool] = False,
) -> Manifest:
    """
    Returns a copy of manifest with added contract_data field as specified by kwargs.
    If no kwargs are present, all available contract_data found in the compiler output
    will be included.

    To include specific contract_data fields, add kwarg set to True (i.e. `abi=True`)
    To alias a contract_type, include a kwarg `alias` (i.e. `alias="OwnedAlias"`)
    If only an alias kwarg is provided, all available contract data will be included.
    Kwargs must match fields as defined in the EthPM Spec (except "alias") if user
    wants to include them in custom contract_type.
    """
    contract_type_fields = {
        "contractType": contract_type,
        "deploymentBytecode": deployment_bytecode,
        "runtimeBytecode": runtime_bytecode,
        "abi": abi,
        "compiler": compiler,
        "userdoc": userdoc,
        "devdoc": devdoc,
        "sourceId": source_id,
    }
    selected_fields = [k for k, v in contract_type_fields.items() if v]
    return _contract_type(name, compiler_output, alias, selected_fields)


@curry
def _contract_type(
    name: str,
    compiler_output: Dict[str, Any],
    alias: Optional[str],
    selected_fields: Optional[List[str]],
    manifest: Manifest,
) -> Manifest:
    contracts_by_name = normalize_compiler_output(compiler_output)
    try:
        all_type_data = contracts_by_name[name]
    except KeyError:
        raise ManifestBuildingError(
            f"Contract name: {name} not found in the provided compiler output."
        )
    if selected_fields:
        contract_type_data = filter_all_data_by_selected_fields(
            all_type_data, selected_fields
        )
    else:
        contract_type_data = all_type_data

    if "compiler" in contract_type_data:
        compiler_info = contract_type_data.pop("compiler")
        contract_type_ref = alias if alias else name
        manifest_with_compilers = add_compilers_to_manifest(
            compiler_info, contract_type_ref, manifest
        )
    else:
        manifest_with_compilers = manifest

    if alias:
        return assoc_in(
            manifest_with_compilers,
            ["contractTypes", alias],
            assoc(contract_type_data, "contractType", name),
        )
    return assoc_in(
        manifest_with_compilers, ["contractTypes", name], contract_type_data
    )


def add_compilers_to_manifest(
    compiler_info: Dict[str, Any], contract_type: str, manifest: Manifest
) -> Manifest:
    """
    Adds a compiler information object to a manifest's top-level `compilers`.
    """
    if "compilers" not in manifest:
        compiler_info["contractTypes"] = [contract_type]
        return assoc_in(manifest, ["compilers"], [compiler_info])

    updated_compiler_info = update_compilers_object(
        compiler_info, contract_type, manifest["compilers"]
    )
    return assoc_in(manifest, ["compilers"], updated_compiler_info)


@to_list
def update_compilers_object(
    new_compiler: Dict[str, Any],
    contract_type: str,
    previous_compilers: List[Dict[str, Any]],
) -> Iterable[Dict[str, Any]]:
    """
    Updates a manifest's top-level `compilers` with a new compiler information object.
    - If compiler version already exists, we just update the compiler's `contractTypes`
    """
    recorded_new_contract_type = False
    for compiler in previous_compilers:
        contract_types = compiler.pop("contractTypes")
        if contract_type in contract_types:
            raise ManifestBuildingError(
                f"Contract type: {contract_type} already referenced in `compilers`."
            )
        if compiler == new_compiler:
            contract_types.append(contract_type)
            recorded_new_contract_type = True
        compiler["contractTypes"] = contract_types
        yield compiler

    if not recorded_new_contract_type:
        new_compiler["contractTypes"] = [contract_type]
        yield new_compiler


@to_dict
def filter_all_data_by_selected_fields(
    all_type_data: Dict[str, Any], selected_fields: List[str]
) -> Iterable[Tuple[str, Any]]:
    """
    Raises exception if selected field data is not available in the contract type data
    automatically gathered by normalize_compiler_output. Otherwise, returns the data.
    """
    for field in selected_fields:
        if field in all_type_data:
            yield field, all_type_data[field]
        else:
            raise ManifestBuildingError(
                f"Selected field: {field} not available in data collected from "
                f"solc output: {list(sorted(all_type_data.keys()))}. Please make"
                "sure the relevant data is present in your solc output."
            )


def normalize_compiler_output(compiler_output: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return compiler output with normalized fields for each contract type,
    as specified in `normalize_contract_type`.
    """
    paths_and_names = [
        (path, contract_name)
        for path in compiler_output
        for contract_name in compiler_output[path].keys()
    ]
    paths, names = zip(*paths_and_names)
    if len(names) != len(set(names)):
        duplicates = {name for name in names if names.count(name) > 1}
        raise ManifestBuildingError(
            f"Duplicate contract types: {duplicates} were found in the compiler output."
        )
    return {
        name: normalize_contract_type(compiler_output[path][name], path)
        for path, name in paths_and_names
    }


@to_dict
def normalize_contract_type(
    contract_type_data: Dict[str, Any],
    source_id: str,
) -> Iterable[Tuple[str, Any]]:
    """
    Serialize contract_data found in compiler output to the defined fields.
    """
    yield "abi", contract_type_data["abi"]
    yield "sourceId", source_id
    if "evm" in contract_type_data:
        if "bytecode" in contract_type_data["evm"]:
            yield "deploymentBytecode", normalize_bytecode_object(
                contract_type_data["evm"]["bytecode"]
            )
        if "deployedBytecode" in contract_type_data["evm"]:
            yield "runtimeBytecode", normalize_bytecode_object(
                contract_type_data["evm"]["deployedBytecode"]
            )
    if "devdoc" in contract_type_data:
        yield "devdoc", contract_type_data["devdoc"]
    if "userdoc" in contract_type_data:
        yield "userdoc", contract_type_data["userdoc"]
    # make sure metadata isn't an empty string in solc output
    if "metadata" in contract_type_data and contract_type_data["metadata"]:
        yield "compiler", normalize_compiler_object(
            json.loads(contract_type_data["metadata"])
        )


@to_dict
def normalize_compiler_object(obj: Dict[str, Any]) -> Iterable[Tuple[str, Any]]:
    yield "name", "solc"
    yield "version", obj["compiler"]["version"]
    yield "settings", {"optimize": obj["settings"]["optimizer"]["enabled"]}


@to_dict
def normalize_bytecode_object(obj: Dict[str, Any]) -> Iterable[Tuple[str, Any]]:
    try:
        link_references = obj["linkReferences"]
    except KeyError:
        link_references = None
    try:
        bytecode = obj["object"]
    except KeyError:
        raise ManifestBuildingError(
            "'object' key not found in bytecode data from compiler output. "
            "Please make sure your solidity compiler output is valid."
        )
    if link_references:
        yield "linkReferences", process_link_references(link_references, bytecode)
        yield "bytecode", process_bytecode(link_references, bytecode)
    else:
        yield "bytecode", add_0x_prefix(bytecode)


def process_bytecode(link_refs: Dict[str, Any], bytecode: bytes) -> HexStr:
    """
    Replace link_refs in bytecode with 0's.
    """
    all_offsets = [y for x in link_refs.values() for y in x.values()]
    # Link ref validation.
    validate_link_ref_fns = (
        validate_link_ref(ref["start"] * 2, ref["length"] * 2)
        for ref in concat(all_offsets)
    )
    pipe(bytecode, *validate_link_ref_fns)
    # Convert link_refs in bytecode to 0's
    link_fns = (
        replace_link_ref_in_bytecode(ref["start"] * 2, ref["length"] * 2)
        for ref in concat(all_offsets)
    )
    processed_bytecode = pipe(bytecode, *link_fns)
    return add_0x_prefix(processed_bytecode)


@curry
def replace_link_ref_in_bytecode(offset: int, length: int, bytecode: str) -> str:
    new_bytes = (
        bytecode[:offset] + "0" * length + bytecode[offset + length :]  # noqa: E203
    )
    return new_bytes


# todo pull all bytecode linking/validating across py-ethpm into shared utils
@to_list
def process_link_references(
    link_refs: Dict[str, Any], bytecode: str
) -> Iterable[Dict[str, Any]]:
    for link_ref in link_refs.values():
        yield normalize_link_ref(link_ref, bytecode)


def normalize_link_ref(link_ref: Dict[str, Any], bytecode: str) -> Dict[str, Any]:
    name = list(link_ref.keys())[0]
    return {
        "name": name,
        "length": 20,
        "offsets": normalize_offsets(link_ref, bytecode),
    }


@to_list
def normalize_offsets(data: Dict[str, Any], bytecode: str) -> Iterable[List[int]]:
    for link_ref in data.values():
        for ref in link_ref:
            yield ref["start"]


@curry
def validate_link_ref(offset: int, length: int, bytecode: str) -> str:
    slot_length = offset + length
    slot = bytecode[offset:slot_length]
    if slot[:2] != "__" and slot[-2:] != "__":
        raise EthPMValidationError(
            f"Slot: {slot}, at offset: {offset} of length: {length} is not a valid "
            "link_ref that can be replaced."
        )
    return bytecode


#
# Deployments
#


def deployment_type(
    *,
    contract_instance: str,
    contract_type: str,
    deployment_bytecode: Dict[str, Any] = None,
    runtime_bytecode: Dict[str, Any] = None,
    compiler: Dict[str, Any] = None,
) -> Manifest:
    """
    Returns a callable that allows the user to add deployments of the same type
    across multiple chains.
    """
    return _deployment_type(
        contract_instance,
        contract_type,
        deployment_bytecode,
        runtime_bytecode,
        compiler,
    )


def deployment(
    *,
    block_uri: URI,
    contract_instance: str,
    contract_type: str,
    address: HexStr,
    transaction: HexStr = None,
    block: HexStr = None,
    deployment_bytecode: Dict[str, Any] = None,
    runtime_bytecode: Dict[str, Any] = None,
    compiler: Dict[str, Any] = None,
) -> Manifest:
    """
    Returns a manifest, with the newly included deployment. Requires a valid
    blockchain URI, however no validation is provided that this URI is unique
    amongst the other deployment URIs, so the user must take care that each
    blockchain URI represents a unique blockchain.
    """
    return _deployment(
        contract_instance,
        contract_type,
        deployment_bytecode,
        runtime_bytecode,
        compiler,
        block_uri,
        address,
        transaction,
        block,
    )


@curry
def _deployment_type(
    contract_instance: str,
    contract_type: str,
    deployment_bytecode: Dict[str, Any],
    runtime_bytecode: Dict[str, Any],
    compiler: Dict[str, Any],
    block_uri: URI,
    address: HexStr,
    tx: HexStr = None,
    block: HexStr = None,
    manifest: Manifest = None,
) -> Manifest:
    return _deployment(
        contract_instance,
        contract_type,
        deployment_bytecode,
        runtime_bytecode,
        compiler,
        block_uri,
        address,
        tx,
        block,
    )


@curry
def _deployment(
    contract_instance: str,
    contract_type: str,
    deployment_bytecode: Dict[str, Any],
    runtime_bytecode: Dict[str, Any],
    compiler: Dict[str, Any],
    block_uri: URI,
    address: HexStr,
    tx: HexStr,
    block: HexStr,
    manifest: Manifest,
) -> Manifest:
    validate_address(address)
    if not is_BIP122_block_uri(block_uri):
        raise ManifestBuildingError(f"{block_uri} is not a valid BIP122 URI.")

    if tx:
        if not is_string(tx) and not is_hex(tx):
            raise ManifestBuildingError(
                f"Transaction hash: {tx} is not a valid hexstring"
            )

    if block:
        if not is_string(block) and not is_hex(block):
            raise ManifestBuildingError(f"Block hash: {block} is not a valid hexstring")
    # todo: validate db, rb and compiler are properly formatted dicts
    deployment_data = _build_deployments_object(
        contract_type,
        deployment_bytecode,
        runtime_bytecode,
        compiler,
        address,
        tx,
        block,
        manifest,
    )
    return assoc_in(
        manifest, ["deployments", block_uri, contract_instance], deployment_data
    )


@to_dict
def _build_deployments_object(
    contract_type: str,
    deployment_bytecode: Dict[str, Any],
    runtime_bytecode: Dict[str, Any],
    compiler: Dict[str, Any],
    address: HexStr,
    tx: HexStr,
    block: HexStr,
    manifest: Dict[str, Any],
) -> Iterable[Tuple[str, Any]]:
    """
    Returns a dict with properly formatted deployment data.
    """
    yield "contractType", contract_type
    yield "address", to_checksum_address(address)
    if deployment_bytecode:
        yield "deploymentBytecode", deployment_bytecode
    if compiler:
        yield "compiler", compiler
    if tx:
        yield "transaction", tx
    if block:
        yield "block", block
    if runtime_bytecode:
        yield "runtimeBytecode", runtime_bytecode


#
# Build Dependencies
#


def build_dependency(package_name: str, uri: URI) -> Manifest:
    """
    Returns the manifest with injected build dependency.
    """
    return _build_dependency(package_name, uri)


@curry
def _build_dependency(package_name: str, uri: URI, manifest: Manifest) -> Manifest:
    validate_package_name(package_name)
    if not is_supported_content_addressed_uri(uri):
        raise EthPMValidationError(
            f"{uri} is not a supported content-addressed URI. "
            "Currently only IPFS and Github blob uris are supported."
        )
    return assoc_in(manifest, ("buildDependencies", package_name), uri)


#
# Helpers
#


@curry
def init_manifest(
    package_name: str, version: str, manifest_version: Optional[str] = "ethpm/3"
) -> Dict[str, Any]:
    """
    Returns an initial dict with the minimal required fields for a valid manifest.
    Should only be used as the first fn to be piped into a `build()` pipeline.
    """
    return {
        "name": package_name,
        "version": version,
        "manifest": manifest_version,
    }


#
# Formatting
#


@curry
def validate(manifest: Manifest) -> Manifest:
    """
    Return a validated manifest against the V2-specification schema.
    """
    validate_manifest_against_schema(manifest)
    return manifest


@curry
def as_package(w3: "Web3", manifest: Manifest) -> Package:
    """
    Return a Package object instantiated with the provided manifest and web3 instance.
    """
    return Package(manifest, w3)


def write_to_disk(
    manifest_root_dir: Optional[Path] = None,
    manifest_name: Optional[str] = None,
    prettify: Optional[bool] = False,
) -> Manifest:
    """
    Write the active manifest to disk
    Defaults
    - Writes manifest to cwd unless Path is provided as manifest_root_dir.
    - Writes manifest with a filename of Manifest[version].json unless a desired
    manifest name (which must end in json) is provided as manifest_name.
    - Writes the minified manifest version to disk unless prettify is set to True.
    """
    return _write_to_disk(manifest_root_dir, manifest_name, prettify)


@curry
def _write_to_disk(
    manifest_root_dir: Optional[Path],
    manifest_name: Optional[str],
    prettify: Optional[bool],
    manifest: Manifest,
) -> Manifest:
    if manifest_root_dir:
        if manifest_root_dir.is_dir():
            cwd = manifest_root_dir
        else:
            raise ManifestBuildingError(
                f"Manifest root directory: {manifest_root_dir} cannot be found, please "
                "provide a valid directory for writing the manifest to disk. "
                "(Path obj // leave manifest_root_dir blank to default to cwd)"
            )
    else:
        cwd = Path.cwd()

    if manifest_name:
        if not manifest_name.lower().endswith(".json"):
            raise ManifestBuildingError(
                f"Invalid manifest name: {manifest_name}. "
                "All manifest names must end in .json"
            )
        disk_manifest_name = manifest_name
    else:
        disk_manifest_name = manifest["version"] + ".json"

    contents = format_manifest(manifest, prettify=prettify)

    if (cwd / disk_manifest_name).is_file():
        raise ManifestBuildingError(
            f"Manifest: {disk_manifest_name} already exists in cwd: {cwd}"
        )
    (cwd / disk_manifest_name).write_text(contents)
    return manifest


@curry
def pin_to_ipfs(
    manifest: Manifest, *, backend: BaseIPFSBackend, prettify: Optional[bool] = False
) -> List[Dict[str, str]]:
    """
    Returns the IPFS pin data after pinning the manifest to the provided IPFS Backend.

    `pin_to_ipfs()` Should *always* be the last argument in a builder, as it will
    return the pin data and not the manifest.
    """
    contents = format_manifest(manifest, prettify=prettify)

    with tempfile.NamedTemporaryFile() as temp:
        temp.write(to_bytes(text=contents))
        temp.seek(0)
        return backend.pin_assets(Path(temp.name))
