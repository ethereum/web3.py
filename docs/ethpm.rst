.. _ethpm:

ethPM
=====

Overview
--------

This is a Python implementation of the `Ethereum Smart Contract
Packaging
Specification V3 <http://ethpm.github.io/ethpm-spec/v3-package-spec.html>`__,
driven by discussions in `ERC
190 <https://github.com/ethereum/EIPs/issues/190>`__, `ERC
1123 <https://github.com/ethereum/EIPs/issues/1123>`__, `ERC
1319 <https://github.com/ethereum/EIPs/issues/1319>`__.

``Py-EthPM`` is being built as a low-level library to help developers leverage the ethPM spec. Including ...

- Parse and validate packages.
- Construct and publish new packages.
- Provide access to contract factory classes.
- Provide access to all of a package's deployments.
- Validate package bytecode matches compilation output.
- Validate deployed bytecode matches compilation output.
- Access to package’s dependencies.
- Native integration with compilation metadata.

Package
-------

The ``Package`` object will function much like the ``Contract`` class
provided by ``web3``. Rather than instantiating the base class provided
by ``ethpm``, you will instead use a ``classmethod`` which generates a
new ``Package`` class for a given package.

``Package`` objects *must* be instantiated with a valid ``web3`` object.

.. doctest::

   >>> from ethpm import Package, get_ethpm_spec_dir
   >>> from web3 import Web3

   >>> w3 = Web3(Web3.EthereumTesterProvider())
   >>> ethpm_spec_dir = get_ethpm_spec_dir()
   >>> owned_manifest_path = ethpm_spec_dir / 'examples' / 'owned' / 'v3.json'
   >>> OwnedPackage = Package.from_file(owned_manifest_path, w3)
   >>> assert isinstance(OwnedPackage, Package)

For a closer look at how to interact with EthPM packages using web3, check out the
:ref:`examples page <ethpm_example>`.

Properties
~~~~~~~~~~

Each ``Package`` exposes the following properties.

.. autoclass:: ethpm.Package
   :members: name, version, manifest_version, uri, __repr__, contract_types, build_dependencies, deployments

.. py:attribute:: Package.w3

   The ``Web3`` instance currently set on this ``Package``. The deployments available on a package are automatically filtered to only contain those belonging to the currently set ``w3`` instance.

.. py:attribute:: Package.manifest

   The manifest dict used to instantiate a ``Package``.


Methods
~~~~~~~

Each ``Package`` exposes the following methods.

.. autoclass:: ethpm.Package
   :members: from_file, from_uri, update_w3, get_contract_factory, get_contract_instance


Validation
~~~~~~~~~~

The ``Package`` class currently verifies the following things.

-  Manifests used to instantiate a ``Package`` object conform to the `EthPM V3 Manifest Specification <https://github.com/ethpm/ethpm-spec/blob/master/spec/v3.spec.json>`__ and are tightly packed, with keys sorted alphabetically, and no trailing newline.


LinkableContract
----------------

`Py-EthPM` uses a custom subclass of ``Web3.contract.Contract`` to manage contract factories and instances which might require bytecode linking. To create a deployable contract factory, both the contract type's ``abi`` and ``deploymentBytecode`` must be available in the Package's manifest.

.. doctest::

   >>> from eth_utils import is_address
   >>> from web3 import Web3
   >>> from ethpm import Package, ASSETS_DIR

   >>> w3 = Web3(Web3.EthereumTesterProvider())
   >>> escrow_manifest_path = ASSETS_DIR / 'escrow' / 'with_bytecode_v3.json'

   >>> # Try to deploy from unlinked factory
   >>> EscrowPackage = Package.from_file(escrow_manifest_path, w3)
   >>> EscrowFactory = EscrowPackage.get_contract_factory("Escrow")
   >>> assert EscrowFactory.needs_bytecode_linking
   >>> escrow_instance = EscrowFactory.constructor(w3.eth.accounts[0]).transact()
   Traceback (most recent call last):
        ...
   ethpm.exceptions.BytecodeLinkingError: Contract cannot be deployed until its bytecode is linked.

   >>> # Deploy SafeSendLib
   >>> SafeSendFactory = EscrowPackage.get_contract_factory("SafeSendLib")
   >>> safe_send_tx_hash = SafeSendFactory.constructor().transact()
   >>> safe_send_tx_receipt = w3.eth.waitForTransactionReceipt(safe_send_tx_hash)

   >>> # Link Escrow factory to deployed SafeSendLib instance
   >>> LinkedEscrowFactory = EscrowFactory.link_bytecode({"SafeSendLib": safe_send_tx_receipt.contractAddress})
   >>> assert LinkedEscrowFactory.needs_bytecode_linking is False
   >>> escrow_tx_hash = LinkedEscrowFactory.constructor(w3.eth.accounts[0]).transact()
   >>> escrow_tx_receipt = w3.eth.waitForTransactionReceipt(escrow_tx_hash)
   >>> assert is_address(escrow_tx_receipt.contractAddress)


Properties
~~~~~~~~~~

.. py:attribute:: LinkableContract.unlinked_references

   A list of link reference data for the deployment bytecode, if present in the manifest data used to generate a ``LinkableContract`` factory. Deployment bytecode link reference data must be present in a manifest in order to generate a factory for a contract which requires bytecode linking.

.. py:attribute:: LinkableContract.linked_references

   A list of link reference data for the runtime bytecode, if present in the manifest data used to generate a ``LinkableContract`` factory. If you want to use the `web3` `Deployer` tool for a contract, then runtime bytecode link reference data must be present in a manifest.

.. py:attribute:: LinkableContract.needs_bytecode_linking

   A boolean attribute used to indicate whether a contract factory has unresolved link references, which must be resolved before a new contract instance can be deployed or instantiated at a given address.


Methods
~~~~~~~

.. py:classmethod:: LinkableContract.link_bytecode(attr_dict)

   This method returns a newly created contract factory with the applied link references defined in the ``attr_dict``. This method expects ``attr_dict`` to be of the type ``Dict[`contract_name`: `address`]`` for all link references that are unlinked.

URI Schemes and Backends
------------------------

BaseURIBackend
~~~~~~~~~~~~~~

``Py-EthPM`` uses the ``BaseURIBackend`` as the parent class for all of its URI backends. To write your own backend, it must implement the following methods.

.. py:method:: BaseURIBackend.can_resolve_uri(uri)

   Return a bool indicating whether or not this backend is capable of resolving the given URI to a manifest.
   A content-addressed URI pointing to valid manifest is said to be capable of "resolving".

.. py:method:: BaseURIBackend.can_translate_uri(uri)

   Return a bool indicating whether this backend class can translate the given URI to a corresponding content-addressed URI.
   A registry URI is said to be capable of "translating" if it points to another content-addressed URI in its respective on-chain registry.

.. py:method:: BaseURIBackend.fetch_uri_contents(uri)

   Fetch the contents stored at the provided uri, if an available backend is capable of resolving the URI. Validates that contents stored at uri match the content hash suffixing the uri.


IPFS
~~~~

``Py-EthPM`` has multiple backends available to fetch/pin files to IPFS. The desired backend can be set via the environment variable: ``ETHPM_IPFS_BACKEND_CLASS``.

- ``InfuraIPFSBackend`` (default)
    - `https://ipfs.infura.io`
- ``IPFSGatewayBackend`` (temporarily deprecated)
    - `https://ipfs.io/ipfs/`
- ``LocalIPFSBacked``
    - Connect to a local IPFS API gateway running on port 5001.
- ``DummyIPFSBackend``
    - Won't pin/fetch files to an actual IPFS node, but mocks out this behavior.

.. py:method:: BaseIPFSBackend.pin_assets(file_or_directory_path)

   Pin asset(s) found at the given path and returns the pinned asset data.


HTTPS
~~~~~

``Py-EthPM`` offers a backend to fetch files from Github, ``GithubOverHTTPSBackend``.

A valid content-addressed Github URI *must* conform to the following scheme, as described in `ERC1319 <https://github.com/ethereum/EIPs/issues/1319>`__, to be used with this backend.

.. code:: python

   https://api.github.com/repos/:owner/:repo/git/blobs/:file_sha


.. py:method:: create_content_addressed_github_uri(uri)

   This util function will return a content-addressed URI, as defined by Github's `blob <https://developer.github.com/v3/git/blobs/>`__ scheme. To generate a content-addressed URI for any manifest stored on github, this function requires accepts a Github API uri that follows the following scheme.

::

   https://api.github.com/repos/:owner/:repo/contents/:path/:to/manifest.json

.. doctest::

   >>> from ethpm.uri import create_content_addressed_github_uri

   >>> owned_github_api_uri = "https://api.github.com/repos/ethpm/ethpm-spec/contents/examples/owned/1.0.0.json"
   >>> content_addressed_uri = "https://api.github.com/repos/ethpm/ethpm-spec/git/blobs/8f9dc767d4c8b31fec4a08d9c0858d4f37b83180"

   >>> actual_blob_uri = create_content_addressed_github_uri(owned_github_api_uri)
   >>> assert actual_blob_uri == content_addressed_uri


Registry URIs
~~~~~~~~~~~~~

The URI to lookup a package from a registry should follow the following
format. (subject to change as the Registry Contract Standard makes it’s
way through the EIP process)

::

   scheme://address:chain_id/package_name@version

-  URI must be a string type
-  ``scheme``: (required) ``ethpm`` or ``erc1319``
-  ``address``: (required) Must be a valid ENS domain or a valid checksum address
   pointing towards a registry contract.
-  ``chain_id``: Chain ID of the chain on which the registry lives. Defaults to Mainnet. Supported chains include...

  - 1: Mainnet
  - 3: Ropsten
  - 4: Rinkeby
  - 5: Goerli
  - 42: Kovan

-  ``package-name``: Must conform to the package-name as specified in
   the
   `EthPM-Spec <http://ethpm-spec.readthedocs.io/en/latest/package-spec.html#package-name>`__.
-  ``version``: The URI escaped version string, *should* conform to the
   `semver <http://semver.org/>`__ version numbering specification.

Examples...

- ``ethpm://packages.zeppelinos.eth/owned@1.0.0``

- ``ethpm://0x808B53bF4D70A24bA5cb720D37A4835621A9df00:1/ethregistrar@1.0.0``

To specify a specific asset within a package, you can namespace the target asset.

- ``ethpm://maker.snakecharmers.eth:1/dai-dai@1.0.0/sources/token.sol``

- ``ethpm://maker.snakecharmers.eth:1/dai-dai@1.0.0/contractTypes/DSToken/abi``

- ``ethpm://maker.snakecharmers.eth:1/dai-dai@1.0.0/deployments/mainnet/dai``


Builder
-------

The manifest Builder is a tool designed to help construct custom manifests. The builder is still under active development, and can only handle simple use-cases for now.

To create a simple manifest
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For all manifests, the following ingredients are *required*.

.. code:: python

   build(
       {},
       package_name(str),
       version(str),
       manifest_version(str), ...,
   )
   # Or
   build(
       init_manifest(package_name: str, version: str, manifest_version: str="ethpm/3")
       ...,
   )


The builder (i.e. ``build()``) expects a dict as the first argument. This dict can be empty, or populated if you want to extend an existing manifest.

.. doctest::

   >>> from ethpm.tools.builder import *

   >>> expected_manifest = {
   ...   "name": "owned",
   ...   "version": "1.0.0",
   ...   "manifest": "ethpm/3"
   ... }
   >>> base_manifest = {"name": "owned"}
   >>> built_manifest = build(
   ...     {},
   ...     package_name("owned"),
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ... )
   >>> extended_manifest = build(
   ...     base_manifest,
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ... )
   >>> assert built_manifest == expected_manifest
   >>> assert extended_manifest == expected_manifest

With ``init_manifest()``, which populates "manifest" with "ethpm/3" (the only supported EthPM specification version), unless provided with an alternative "version".

.. doctest::

   >>> build(
   ...     init_manifest("owned", "1.0.0"),
   ... )
   {'name': 'owned', 'version': '1.0.0', 'manifest': 'ethpm/3'}



To return a ``Package``
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       as_package(w3: Web3),
   )

By default, the manifest builder returns a dict representing the manifest. To return a ``Package`` instance (instantiated with the generated manifest) from the builder, add the ``as_package()`` builder function with a valid ``web3`` instance to the end of the builder.

.. doctest::

   >>> from ethpm import Package
   >>> from web3 import Web3

   >>> w3 = Web3(Web3.EthereumTesterProvider())
   >>> built_package = build(
   ...     {},
   ...     package_name("owned"),
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ...     as_package(w3),
   ... )
   >>> assert isinstance(built_package, Package)


To validate a manifest
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       validate(),
   )

By default, the manifest builder does *not* perform any validation that the generated fields are correctly formatted. There are two ways to validate that the built manifest conforms to the EthPM V3 Specification.
    - Return a Package, which automatically runs validation.
    - Add the ``validate()`` function to the end of the manifest builder.

.. doctest::

   >>> valid_manifest = build(
   ...     {},
   ...     package_name("owned"),
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ...     validate(),
   ... )
   >>> assert valid_manifest == {"name": "owned", "manifest": "ethpm/3", "version": "1.0.0"}
   >>> invalid_manifest = build(
   ...     {},
   ...     package_name("_InvalidPkgName"),
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ...     validate(),
   ... )
   Traceback (most recent call last):
   ethpm.exceptions.EthPMValidationError: Manifest invalid for schema version 2. Reason: '_InvalidPkgName' does not match '^[a-z][-a-z0-9]{0,255}$'


To write a manifest to disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       write_to_disk(
           manifest_root_dir: Optional[Path],
           manifest_name: Optional[str],
           prettify: Optional[bool],
       ),
   )


Writes the active manifest to disk. Will not overwrite an existing manifest with the same name and root directory.

Defaults
- Writes manifest to current working directory (as returned by ``os.getcwd()``) unless a ``Path`` is provided as manifest_root_dir.
- Writes manifest with a filename of ``<version>.json`` unless desired manifest name (which must end in ".json") is provided as manifest_name.
- Writes the minified manifest version to disk unless prettify is set to True

.. doctest::

   >>> from pathlib import Path
   >>> import tempfile
   >>> p = Path(tempfile.mkdtemp("temp"))
   >>> build(
   ...     {},
   ...     package_name("owned"),
   ...     manifest_version("ethpm/3"),
   ...     version("1.0.0"),
   ...     write_to_disk(manifest_root_dir=p, manifest_name="manifest.json", prettify=True),
   ... )
   {'name': 'owned', 'manifest': 'ethpm/3', 'version': '1.0.0'}
   >>> with open(str(p / "manifest.json")) as f:
   ...     actual_manifest = f.read()
   >>> print(actual_manifest)
   {
        "manifest": "ethpm/3",
        "name": "owned",
        "version": "1.0.0"
   }


To pin a manifest to IPFS
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       pin_to_ipfs(
           backend: BaseIPFSBackend,
           prettify: Optional[bool],
       ),
   )

Pins the active manfiest to disk. Must be the concluding function in a builder set since it returns the IPFS pin data rather than returning the manifest for further processing.


To add meta fields
~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       description(str),
       license(str),
       authors(*args: str),
       keywords(*args: str),
       links(*kwargs: str),
       ...,
   )

.. doctest::

   >>> BASE_MANIFEST = {"name": "owned", "manifest": "ethpm/3", "version": "1.0.0"}
   >>> expected_manifest = {
   ...   "name": "owned",
   ...   "manifest": "ethpm/3",
   ...   "version": "1.0.0",
   ...   "meta": {
   ...     "authors": ["Satoshi", "Nakamoto"],
   ...     "description": "An awesome package.",
   ...     "keywords": ["auth"],
   ...     "license": "MIT",
   ...     "links": {
   ...       "documentation": "www.readthedocs.com/...",
   ...       "repo": "www.github.com/...",
   ...       "website": "www.website.com",
   ...     }
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     authors("Satoshi", "Nakamoto"),
   ...     description("An awesome package."),
   ...     keywords("auth"),
   ...     license("MIT"),
   ...     links(documentation="www.readthedocs.com/...", repo="www.github.com/...", website="www.website.com"),
   ... )
   >>> assert expected_manifest == built_manifest


Compiler Output
~~~~~~~~~~~~~~~

To build a more complex manifest for solidity contracts, it is required that you provide standard-json output from the solidity compiler. Or for a more convenient experience, use the `EthPM CLI <https://github.com/ethpm/ethpm-cli>`__.

Here is an example of how to compile the contracts and generate the standard-json output. More information can be found in the `Solidity Compiler <https://solidity.readthedocs.io/en/v0.4.24/using-the-compiler.html>`__ docs.

.. code:: sh

    solc --allow-paths <path-to-contract-directory> --standard-json < standard-json-input.json > owned_compiler_output.json

Sample standard-json-input.json

.. code:: json

    {
        "language": "Solidity",
        "sources": {
            "Contract.sol": {
                "urls": ["<path-to-contract>"]
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "evm.bytecode.object"]
                }
            }
        }
    }


The ``compiler_output`` as used in the following examples is the entire value of the ``contracts`` key of the solc output, which contains compilation data for all compiled contracts.


To add a source
~~~~~~~~~~~~~~~

.. code:: python

   # To inline a source
   build(
       ...,
       inline_source(
           contract_name: str,
           compiler_output: Dict[str, Any],
           package_root_dir: Optional[Path]
       ),
       ...,
   )
   # To pin a source
   build(
       ...,
       pin_source(
           contract_name: str,
           compiler_output: Dict[str, Any],
           ipfs_backend: BaseIPFSBackend,
           package_root_dir: Optional[Path]
       ),
       ...,
   )

There are two ways to include a contract source in your manifest.

Both strategies require that either . . .
    - The current working directory is set to the package root directory
      or
    - The package root directory is provided as an argument (``package_root_dir``)


To inline the source code directly in the manifest, use ``inline_source()`` or ``source_inliner()`` (to inline multiple sources from the same compiler_output), which requires the contract name and compiler output as args.

.. note::

   ``output_v3.json`` below is expected to be the standard-json output generated by the solidity compiler as described `here <https://solidity.readthedocs.io/en/v0.4.24/using-the-compiler.html>`_. The output must contain the ``abi`` and ``bytecode`` objects from compilation.

.. doctest::

   >>> import json
   >>> from ethpm import ASSETS_DIR, get_ethpm_spec_dir
   >>> ethpm_spec_dir = get_ethpm_spec_dir()
   >>> owned_dir = ethpm_spec_dir / "examples" / "owned" / "contracts"
   >>> compiler_output = json.loads((ASSETS_DIR / "owned" / "output_v3.json").read_text())['contracts']
   >>> expected_manifest = {
   ...   "name": "owned",
   ...   "version": "1.0.0",
   ...   "manifest": "ethpm/3",
   ...   "sources": {
   ...     "./Owned.sol": {
   ...       "content": """// SPDX-License-Identifier: MIT\npragma solidity ^0.6.8;\n\ncontract Owned """
   ...       """{\n    address owner;\n    \n    modifier onlyOwner { require(msg.sender == owner); _; }"""
   ...       """\n\n    constructor() public {\n        owner = msg.sender;\n    }\n}""",
   ...       "type": "solidity",
   ...       "installPath": "./Owned.sol"
   ...     }
   ...   }
   ... }
   >>> # With `inline_source()`
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     inline_source("Owned", compiler_output, package_root_dir=owned_dir),
   ... )
   >>> assert expected_manifest == built_manifest
   >>> # With `source_inliner()` for multiple sources from the same compiler output
   >>> inliner = source_inliner(compiler_output, package_root_dir=owned_dir)
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     inliner("Owned"),
   ...     # inliner("other_source"), etc...
   ... )
   >>> assert expected_manifest == built_manifest


To include the source as a content-addressed URI, ``Py-EthPM`` can pin your source via the Infura IPFS API. As well as the contract name and compiler output, this function requires that you provide the desired IPFS backend to pin the contract sources.

.. doctest::

   >>> import json
   >>> from ethpm import ASSETS_DIR, get_ethpm_spec_dir
   >>> from ethpm.backends.ipfs import get_ipfs_backend
   >>> ethpm_spec_dir = get_ethpm_spec_dir()
   >>> owned_dir = ethpm_spec_dir / "examples" / "owned" / "contracts"
   >>> compiler_output = json.loads((ASSETS_DIR / "owned" / "output_v3.json").read_text())['contracts']
   >>> ipfs_backend = get_ipfs_backend()
   >>> expected_manifest = {
   ...   "name": "owned",
   ...   "version": "1.0.0",
   ...   "manifest": "ethpm/3",
   ...   "sources": {
   ...     "./Owned.sol": {
   ...       "installPath": "./Owned.sol",
   ...       "type": "solidity",
   ...       "urls": ["ipfs://QmU8QUSt56ZoBDJgjjXvAZEPro9LmK1m2gjVG5Q4s9x29W"]
   ...     }
   ...   }
   ... }
   >>> # With `pin_source()`
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     pin_source("Owned", compiler_output, ipfs_backend, package_root_dir=owned_dir),
   ... )
   >>> assert expected_manifest == built_manifest
   >>> # With `source_pinner()` for multiple sources from the same compiler output
   >>> pinner = source_pinner(compiler_output, ipfs_backend, package_root_dir=owned_dir)
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     pinner("Owned"),
   ...     # pinner("other_source"), etc
   ... )
   >>> assert expected_manifest == built_manifest



To add a contract type
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       contract_type(
           contract_name: str,
           compiler_output: Dict[str, Any],
           alias: Optional[str],
           abi: Optional[bool],
           compiler: Optional[bool],
           contract_type: Optional[bool],
           deployment_bytecode: Optional[bool],
           devdoc: Optional[bool],
           userdoc: Optional[bool],
           source_id: Optional[bool],
           runtime_bytecode: Optional[bool]
       ),
       ...,
   )

The default behavior of the manifest builder's ``contract_type()`` function is to populate the manifest with all of the contract type data found in the ``compiler_output``.

.. doctest::

   >>> expected_manifest = {
   ...   'name': 'owned',
   ...   'manifest': 'ethpm/3',
   ...   'version': '1.0.0',
   ...   'compilers': [
   ...     {'name': 'solc', 'version': '0.6.8+commit.0bbfe453', 'settings': {'optimize': True}, 'contractTypes': ['Owned']}
   ...   ],
   ...   'contractTypes': {
   ...     'Owned': {
   ...       'abi': [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}],
   ...       'deploymentBytecode': {
   ...         'bytecode': '0x6080604052348015600f57600080fd5b50600080546001600160a01b03191633179055603f80602f6000396000f3fe6080604052600080fdfea26469706673582212208cbf6c3ccde7837026b3ec9660a0e95f1dbee0ce985f6879d7bc7e422519cc7564736f6c63430006080033'
   ...       },
   ...       'sourceId': 'Owned.sol',
   ...       'devdoc': {'methods': {}},
   ...       'userdoc': {'methods': {}}
   ...     }
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     contract_type("Owned", compiler_output)
   ... )
   >>> assert expected_manifest == built_manifest


To select only certain contract type data to be included in your manifest, provide the desired fields as ``True`` keyword arguments. The following fields can be specified for inclusion in the manifest . . .
    - ``abi``
    - ``compiler``
    - ``deployment_bytecode``
    - ``runtime_bytecode``
    - ``devdoc``
    - ``userdoc``
    - ``source_id``

.. doctest::

   >>> expected_manifest = {
   ...   'name': 'owned',
   ...   'manifest': 'ethpm/3',
   ...   'version': '1.0.0',
   ...   'contractTypes': {
   ...     'Owned': {
   ...       'abi': [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}],
   ...     }
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     contract_type("Owned", compiler_output, abi=True)
   ... )
   >>> assert expected_manifest == built_manifest

If you would like to alias your contract type, provide the desired alias as a kwarg. This will automatically include the original contract type in a ``contractType`` field. Unless specific contract type fields are provided as kwargs, ``contractType`` will stil default to including all availabe contract type data found in the compiler output.

.. doctest::

   >>> expected_manifest = {
   ...   'name': 'owned',
   ...   'manifest': 'ethpm/3',
   ...   'version': '1.0.0',
   ...   'contractTypes': {
   ...     'OwnedAlias': {
   ...       'abi': [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}],
   ...       'contractType': 'Owned'
   ...     }
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     contract_type("Owned", compiler_output, alias="OwnedAlias", abi=True)
   ... )
   >>> assert expected_manifest == built_manifest


To add a deployment
~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       deployment(
           block_uri,
           contract_instance,
           contract_type,
           address,
           transaction=None,
           block=None,
           deployment_bytecode=None,
           runtime_bytecode=None,
           compiler=None,
       ),
       ...,
   )

There are two strategies for adding a deployment to your manifest.

.. py:function:: deployment(block_uri, contract_instance, contract_type, address, transaction=None, block=None, deployment_bytecode=None, runtime_bytecode=None, compiler=None)

This is the simplest builder function for adding a deployment to a manifest. All arguments require keywords. This builder function requires a valid ``block_uri``, it's up to the user to be sure that multiple chain URIs representing the same blockchain are not included in the "deployments" object keys.

``runtime_bytecode``, ``deployment_bytecode`` and ``compiler`` must all be validly formatted dicts according to the `EthPM Spec <http://ethpm.github.io/ethpm-spec/package-spec.html#the-contract-instance-object>`__. If your contract has link dependencies, be sure to include them in the bytecode objects.


.. doctest::

   >>> expected_manifest = {
   ...   'name': 'owned',
   ...   'manifest': 'ethpm/3',
   ...   'version': '1.0.0',
   ...   'deployments': {
   ...     'blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef': {
   ...       'Owned': {
   ...         'contractType': 'Owned',
   ...         'address': '0x4F5B11C860B37B68De6d14FB7e7b5f18A9a1BD00',
   ...       }
   ...     }
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     deployment(
   ...         block_uri='blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
   ...         contract_instance='Owned',
   ...         contract_type='Owned',
   ...         address='0x4F5B11C860B37B68De6d14FB7e7b5f18A9a1BD00',
   ...     ),
   ... )
   >>> assert expected_manifest == built_manifest

.. py:function:: deployment_type(contract_instance, contract_type, deployment_bytecode=None, runtime_bytecode=None, compiler=None)

This builder function simplifies adding the same contract type deployment across multiple chains. It requires both a ``contract_instance`` and ``contract_type`` argument (in many cases these are the same, though ``contract_type`` *must* always match its correspondent in the manifest's "contract_types") and all arguments require keywords.

``runtime_bytecode``, ``deployment_bytecode`` and ``compiler`` must all be validly formatted dicts according to the `EthPM Spec <http://ethpm.github.io/ethpm-spec/package-spec.html#the-contract-instance-object>`__. If your contract has link dependencies, be sure to include them in the bytecode objects.

.. code:: python

   owned_type = deployment_type(contract_instance="Owned", contract_type="Owned")
   escrow_type = deployment_type(
       contract_instance = "Escrow",
       contract_type = "Escrow",
       deployment_bytecode = {
           "bytecode": "0x608060405234801561001057600080fd5b5060405160208061045383398101604081815291516002819055336000818152602081815285822084905583855294519294919390927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a3506103d2806100816000396000f3006080604052600436106100775763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663095ea7b3811461007c57806318160ddd146100b457806323b872dd146100db57806370a0823114610105578063a9059cbb14610126578063dd62ed3e1461014a575b600080fd5b34801561008857600080fd5b506100a0600160a060020a0360043516602435610171565b604080519115158252519081900360200190f35b3480156100c057600080fd5b506100c96101d8565b60408051918252519081900360200190f35b3480156100e757600080fd5b506100a0600160a060020a03600435811690602435166044356101de565b34801561011157600080fd5b506100c9600160a060020a03600435166102c9565b34801561013257600080fd5b506100a0600160a060020a03600435166024356102e4565b34801561015657600080fd5b506100c9600160a060020a036004358116906024351661037b565b336000818152600160209081526040808320600160a060020a038716808552908352818420869055815186815291519394909390927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925928290030190a35060015b92915050565b60025481565b600160a060020a03831660009081526020819052604081205482118015906102295750600160a060020a03841660009081526001602090815260408083203384529091529020548211155b80156102355750600082115b156102be57600160a060020a0380841660008181526020818152604080832080548801905593881680835284832080548890039055600182528483203384528252918490208054879003905583518681529351929391927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9281900390910190a35060016102c2565b5060005b9392505050565b600160a060020a031660009081526020819052604090205490565b3360009081526020819052604081205482118015906103035750600082115b15610373573360008181526020818152604080832080548790039055600160a060020a03871680845292819020805487019055805186815290519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a35060016101d2565b5060006101d2565b600160a060020a039182166000908152600160209081526040808320939094168252919091522054905600a165627a7a72305820cf9d6a3f751ca1e6b9bc2324e42633a4cde513d64c3e6cc32d6359629249e90200290000000000000000000000000000000000000000000000000000000000000001"
       },
       runtime_bytecode = {
           "bytecode": "0x6080604052600436106100775763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663095ea7b3811461007c57806318160ddd146100b457806323b872dd146100db57806370a0823114610105578063a9059cbb14610126578063dd62ed3e1461014a575b600080fd5b34801561008857600080fd5b506100a0600160a060020a0360043516602435610171565b604080519115158252519081900360200190f35b3480156100c057600080fd5b506100c96101d8565b60408051918252519081900360200190f35b3480156100e757600080fd5b506100a0600160a060020a03600435811690602435166044356101de565b34801561011157600080fd5b506100c9600160a060020a03600435166102c9565b34801561013257600080fd5b506100a0600160a060020a03600435166024356102e4565b34801561015657600080fd5b506100c9600160a060020a036004358116906024351661037b565b336000818152600160209081526040808320600160a060020a038716808552908352818420869055815186815291519394909390927f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925928290030190a35060015b92915050565b60025481565b600160a060020a03831660009081526020819052604081205482118015906102295750600160a060020a03841660009081526001602090815260408083203384529091529020548211155b80156102355750600082115b156102be57600160a060020a0380841660008181526020818152604080832080548801905593881680835284832080548890039055600182528483203384528252918490208054879003905583518681529351929391927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9281900390910190a35060016102c2565b5060005b9392505050565b600160a060020a031660009081526020819052604090205490565b3360009081526020819052604081205482118015906103035750600082115b15610373573360008181526020818152604080832080548790039055600160a060020a03871680845292819020805487019055805186815290519293927fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef929181900390910190a35060016101d2565b5060006101d2565b600160a060020a039182166000908152600160209081526040808320939094168252919091522054905600a165627a7a72305820cf9d6a3f751ca1e6b9bc2324e42633a4cde513d64c3e6cc32d6359629249e9020029"
       },
       compiler = {
           "name": "solc",
           "version": "0.4.24+commit.e67f0147.Emscripten.clang",
           "settings": {
               "optimize": True
           }
       }
   )
   manifest = build(
       package_name("escrow"),
       version("1.0.0"),
       manifest_version("ethpm/3"),
       owned_type(
           block_uri='blockchain://abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
           address=owned_testnet_address,
       ),
       owned_type(
           block_uri='blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
           address=owned_mainnet_address,
           transaction=owned_mainnet_transaction,
           block=owned_mainnet_block,
       ),
       escrow_type(
           block_uri='blockchain://abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
           address=escrow_testnet_address,
       ),
       escrow_type(
           block_uri='blockchain://1234567890123456789012345678901234567890123456789012345678901234/block/1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
           address=escrow_mainnet_address,
           transaction=escrow_mainnet_transaction,
       ),
   )

To add a build dependency
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   build(
       ...,
       build_dependency(
           package_name,
           uri,
       ),
       ...,
   )

.. py:function:: build_dependency(package_name, uri)

To add a build dependency to your manifest, just provide the package's name and a supported, content-addressed URI.

.. doctest::

   >>> expected_manifest = {
   ...   'name': 'owned',
   ...   'manifest': 'ethpm/3',
   ...   'version': '1.0.0',
   ...   'buildDependencies': {
   ...     'owned': 'ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW',
   ...   }
   ... }
   >>> built_manifest = build(
   ...     BASE_MANIFEST,
   ...     build_dependency('owned', 'ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW'),
   ... )
   >>> assert expected_manifest == built_manifest


Checker
-------

The manifest Checker is a tool designed to help validate manifests according to the natural language spec (link).

To validate a manifest
~~~~~~~~~~~~~~~~~~~~~~

.. doctest::

   >>> from ethpm.tools.checker import check_manifest

   >>> basic_manifest = {"name": "example", "version": "1.0.0", "manifest": "ethpm/3"}
   >>> check_manifest(basic_manifest)
   {'meta': "Manifest missing a suggested 'meta' field.", 'sources': 'Manifest is missing a sources field, which defines a source tree that should comprise the full source tree necessary to recompile the contracts contained in this release.', 'contractTypes': "Manifest does not contain any 'contractTypes'. Packages should only include contract types that can be found in the source files for this package. Packages should not include contract types from dependencies. Packages should not include abstract contracts in the contract types section of a release.", 'compilers': 'Manifest is missing a suggested `compilers` field.'}
