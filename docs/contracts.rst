.. _contracts:

Contracts
=========

.. py:module:: web3.contract

It is worth taking your time to understand all about contracts. To get started,
check out this example:

.. _contract_example:

Contract Deployment Example
----------------------------------------------

To run this example, you will need to install a few extra features:

- The sandbox node provided by eth-tester. You can install it with ``pip install -U web3[tester]``.
- The ``solc`` solidity compiler. See `Installing the Solidity Compiler
  <http://solidity.readthedocs.io/en/latest/installing-solidity.html#binary-packages>`_

.. code-block:: python

    >>> import json

    >>> from web3 import Web3
    >>> from solc import compile_standard

    # Solidity source code
    >>> compiled_sol = compile_standard({
    ...     "language": "Solidity",
    ...     "sources": {
    ...         "Greeter.sol": {
    ...             "content": '''
    ...                 pragma solidity ^0.5.0;
    ...
    ...                 contract Greeter {
    ...                   string public greeting;
    ...
    ...                   constructor() public {
    ...                       greeting = 'Hello';
    ...                   }
    ...
    ...                   function setGreeting(string memory _greeting) public {
    ...                       greeting = _greeting;
    ...                   }
    ...
    ...                   function greet() view public returns (string memory) {
    ...                       return greeting;
    ...                   }
    ...                 }
    ...               '''
    ...         }
    ...     },
    ...     "settings":
    ...         {
    ...             "outputSelection": {
    ...                 "*": {
    ...                     "*": [
    ...                         "metadata", "evm.bytecode"
    ...                         , "evm.bytecode.sourceMap"
    ...                     ]
    ...                 }
    ...             }
    ...         }
    ... })

    # web3.py instance
    >>> w3 = Web3(Web3.EthereumTesterProvider())

    # set pre-funded account as sender
    >>> w3.eth.defaultAccount = w3.eth.accounts[0]

    # get bytecode
    >>> bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']

    # get abi
    >>> abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']

    >>> Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Submit the transaction that deploys the contract
    >>> tx_hash = Greeter.constructor().transact()

    # Wait for the transaction to be mined, and get the transaction receipt
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    >>> greeter = w3.eth.contract(
    ...     address=tx_receipt.contractAddress,
    ...     abi=abi
    ... )

    >>> greeter.functions.greet().call()
    'Hello'

    >>> tx_hash = greeter.functions.setGreeting('Nihao').transact()
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    >>> greeter.functions.greet().call()
    'Nihao'


Contract Factories
------------------

These factories are not intended to be initialized directly.
Instead, create contract objects using the :meth:`w3.eth.contract() <web3.eth.Eth.contract>`
method. By default, the contract factory is :class:`Contract`. See the
example in :class:`ConciseContract` for specifying an alternate factory.

.. py:class:: Contract(address)

    Contract provides a default interface for deploying and interacting with
    Ethereum smart contracts.

    The address parameter can be a hex address or an ENS name, like ``mycontract.eth``.

.. py:class:: ConciseContract(Contract())

    .. warning:: Deprecated: This method is deprecated in favor of the :class:`~ContractCaller` API
      or the verbose syntax

    This variation of :class:`Contract` is designed for more succinct read access,
    without making write access more wordy. This comes at a cost of losing
    access to features like ``deploy()`` and properties like ``address``. It is
    recommended to use the classic ``Contract`` for those use cases.
    Just to be be clear, `ConciseContract` only exposes contract functions and all
    other `Contract` class methods and properties are not available with the `ConciseContract`
    API. This includes but is not limited to ``contract.address``, ``contract.abi``, and
    ``contract.deploy()``.

    Create this type of contract by passing a :py:class:`Contract` instance to
    :class:`ConciseContract`:


    .. code-block:: python

        >>> concise = ConciseContract(myContract)


    This variation invokes all methods as a call, so if the classic contract had a method like
    ``contract.functions.owner().call()``, you could call it with ``concise.owner()`` instead.

    For access to send a transaction or estimate gas, you can add a keyword argument like so:


    .. code-block:: python

        >>> concise.withdraw(amount, transact={'from': eth.accounts[1], 'gas': 100000, ...})

        >>>  # which is equivalent to this transaction in the classic contract:

        >>> contract.functions.withdraw(amount).transact({'from': eth.accounts[1], 'gas': 100000, ...})

.. py:class:: ImplicitContract(Contract())

   .. warning:: Deprecated: This method is deprecated in favor of the verbose syntax

   This variation mirrors :py:class:`ConciseContract`, but it invokes all methods as a
   transaction rather than a call, so if the classic contract had a method like
   ``contract.functions.owner.transact()``, you could call it with ``implicit.owner()`` instead.

    Create this type of contract by passing a :py:class:`Contract` instance to
    :class:`ImplicitContract`:


    .. code-block:: python

        >>> concise = ImplicitContract(myContract)


Properties
----------

Each Contract Factory exposes the following properties.


.. py:attribute:: Contract.address

    The hexadecimal encoded 20-byte address of the contract, or an ENS name.
    May be ``None`` if not provided during factory creation.


.. py:attribute:: Contract.abi

    The contract ABI array.


.. py:attribute:: Contract.bytecode

    The contract bytecode string.  May be ``None`` if not provided during
    factory creation.


.. py:attribute:: Contract.bytecode_runtime

    The runtime part of the contract bytecode string.  May be ``None`` if not
    provided during factory creation.

.. py:attribute:: Contract.functions

    This provides access to contract functions as attributes.  For example:
    ``myContract.functions.MyMethod()``.  The exposed contract functions are classes of the
    type :py:class:`ContractFunction`.

.. py:attribute:: Contract.events

    This provides access to contract events as attributes.  For example:
    ``myContract.events.MyEvent()``.  The exposed contract events are classes of the
    type :py:class:`ContractEvent`.

Methods
-------

Each Contract Factory exposes the following methods.

.. py:classmethod:: Contract.constructor(*args, **kwargs).transact(transaction=None)

    Construct and deploy a contract by sending a new public transaction.

    If provided ``transaction`` should be a dictionary conforming to the
    ``web3.eth.sendTransaction(transaction)`` method.  This value may not
    contain the keys ``data`` or ``to``.

    If the contract takes constructor parameters they should be provided as
    positional arguments or keyword arguments.

    If any of the arguments specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    deployment transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash for the deploy transaction.

    .. code-block:: python

        >>> deploy_txn = token_contract.constructor(web3.eth.coinbase, 12345).transact()
        >>> txn_receipt = web3.eth.getTransactionReceipt(deploy_txn)
        >>> txn_receipt['contractAddress']
        '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'

.. py:classmethod:: Contract.constructor(*args, **kwargs).estimateGas(transaction=None, block_identifier=None)

    Estimate gas for constructing and deploying the contract.

    This method behaves the same as the
    :py:meth:`Contract.constructor(*args, **kwargs).transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    The ``block_identifier`` parameter is passed directly to the call at the end portion
    of the function call.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    Returns the gas needed to deploy the contract.

    .. code-block:: python

        >>> token_contract.constructor(web3.eth.coinbase, 12345).estimateGas()
        12563

.. py:classmethod:: Contract.constructor(*args, **kwargs).buildTransaction(transaction=None)

    Construct the contract deploy transaction bytecode data.

    If the contract takes constructor parameters they should be provided as
    positional arguments or keyword arguments.

    If any of the ``args`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    Returns the transaction dictionary that you can pass to sendTransaction method.

    .. code-block:: python

        >>> transaction = {
        'gasPrice': w3.eth.gasPrice,
        'chainId': None
        }
        >>> contract_data = token_contract.constructor(web3.eth.coinbase, 12345).buildTransaction(transaction)
        >>> web3.eth.sendTransaction(contract_data)

.. _contract_createFilter:

.. py:classmethod:: Contract.events.your_event_name.createFilter(fromBlock=block, toBlock=block, \
                    argument_filters={"arg1": "value"}, topics=[])

    Creates a new event filter, an instance of :py:class:`web3.utils.filters.LogFilter`.

    - ``fromBlock`` is a mandatory field. Defines the starting block (exclusive) filter block range. It can be either the starting block number, or 'latest' for the last mined block, or 'pending' for unmined transactions. In the case of ``fromBlock``, 'latest' and 'pending' set the 'latest' or 'pending' block as a static value for the starting filter block.
    - ``toBlock`` optional. Defaults to 'latest'. Defines the ending block (inclusive) in the filter block range.  Special values 'latest' and 'pending' set a dynamic range that always includes the 'latest' or 'pending' blocks for the filter's upper block range.
    - ``address`` optional. Defaults to the contract address. The filter matches the event logs emanating from ``address``.
    - ``argument_filters``, optional. Expects a dictionary of argument names and values. When provided event logs are filtered for the event argument values. Event arguments can be both indexed or unindexed. Indexed values with be translated to their corresponding topic arguments. Unindexed arguments will be filtered using a regular expression.
    - ``topics`` optional, accepts the standard JSON-RPC topics argument.  See the JSON-RPC documentation for `eth_newFilter <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter>`_ more information on the ``topics`` parameters.

.. py:classmethod:: Contract.events.your_event_name.build_filter()

    Creates a EventFilterBuilder instance with the event abi, and the contract address if called from a deployed contract instance.  The EventFilterBuilder provides a convenient way to construct the filter parameters with value checking against the event abi. It allows for defining multiple match values or of single values through the match_any and match_single methods.

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.fromBlock = "latest"
        filter_builder.args.clientID.match_any(1, 2, 3, 4)
        filter_builder.args.region.match_single("UK")
        filter_instance = filter_builder.deploy()

    The ``deploy`` method returns a :py:class:`web3.utils.filters.LogFilter` instance from the filter parameters generated by the filter builder. Defining multiple match values for array arguments can be accomplished easily with the filter builder:

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.args.clientGroups.match_any((1, 3, 5,), (2, 3, 5), (1, 2, 3))

    The filter builder blocks already defined filter parameters from being changed.

    .. code-block:: python

        filter_builder = myContract.events.myEvent.build_filter()
        filter_builder.fromBlock = "latest"
        filter_builder.fromBlock = 0  # raises a ValueError


.. py:classmethod:: Contract.deploy(transaction=None, args=None)

    .. warning:: Deprecated: this method is deprecated in favor of
      :meth:`~Contract.constructor`, which provides more flexibility.

    Construct and send a transaction to deploy the contract.

    If provided ``transaction`` should be a dictionary conforming to the
    ``web3.eth.sendTransaction(transaction)`` method.  This value may not
    contain the keys ``data`` or ``to``.

    If the contract takes constructor arguments they should be provided as a
    list via the ``args`` parameter.

    If any of the ``args`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    deployment transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash for the deploy transaction.


.. py:classmethod:: Contract.encodeABI(fn_name, args=None, kwargs=None, data=None)

   Encodes the arguments using the Ethereum ABI for the contract function that
   matches the given ``fn_name`` and arguments ``args``. The ``data`` parameter
   defaults to the function selector.

   .. code-block:: python

      >>> contract.encodeABI(fn_name="register", args=["rainbows", 10])
      "0xea87152b0000000000000000000000000000000000000000000000000000000000000040000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000087261696e626f7773000000000000000000000000000000000000000000000000"

.. py:classmethod:: Contract.all_functions()

    Returns a list of all the functions present in a Contract where every function is
    an instance of :py:class:`ContractFunction`.

    .. code-block:: python

        >>> contract.all_functions()
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_signature(signature)

    Searches for a distinct function with matching signature. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises ``ValueError`` if no
    match is found.

    .. code-block:: python

        >>> contract.get_function_by_signature('identity(uint256,bool)')
        <Function identity(uint256,bool)>


.. py:classmethod:: Contract.find_functions_by_name(name)

    Searches for all function with matching name. Returns a list of matching functions
    where every function is an instance of :py:class:`ContractFunction`. Returns an empty
    list when no match is found.

    .. code-block:: python

        >>> contract.find_functions_by_name('identity')
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_name(name)

    Searches for a distinct function with matching name. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises ``ValueError`` if no
    match is found or if multiple matches are found.

    .. code-block:: python

        >>> contract.get_function_by_name('unique_name')
        <Function unique_name(uint256)>


.. py:classmethod:: Contract.get_function_by_selector(selector)

    Searches for a distinct function with matching selector.
    The selector can be a hexadecimal string, bytes or int.
    Returns an instance of :py:class:`ContractFunction` upon finding a match.
    Raises ``ValueError`` if no match is found.

    .. code-block:: python

        >>> contract.get_function_by_selector('0xac37eebb')
        <Function identity(uint256)'>
        >>> contract.get_function_by_selector(b'\xac7\xee\xbb')
        <Function identity(uint256)'>
        >>> contract.get_function_by_selector(0xac37eebb)
        <Function identity(uint256)'>


.. py:classmethod:: Contract.find_functions_by_args(*args)

    Searches for all function with matching args. Returns a list of matching functions
    where every function is an instance of :py:class:`ContractFunction`. Returns an empty
    list when no match is found.

    .. code-block:: python

        >>> contract.find_functions_by_args(1, True)
        [<Function identity(uint256,bool)>, <Function identity(int256,bool)>]


.. py:classmethod:: Contract.get_function_by_args(*args)

    Searches for a distinct function with matching args. Returns an instance of
    :py:class:`ContractFunction` upon finding a match. Raises ``ValueError`` if no
    match is found or if multiple matches are found.

    .. code-block:: python

        >>> contract.get_function_by_args(1)
        <Function unique_func_with_args(uint256)>


.. note::
    ``Contract`` methods ``all_functions``, ``get_function_by_signature``, ``find_functions_by_name``,
    ``get_function_by_name``, ``get_function_by_selector``, ``find_functions_by_args`` and
    ``get_function_by_args`` can only be used when abi is provided to the contract.


.. note::
    Web3.py rejects the initialization of contracts that have more than one function
    with the same selector or signature.
    eg. ``blockHashAddendsInexpansible(uint256)`` and ``blockHashAskewLimitary(uint256)`` have the
    same selector value equal to ``0x00000000``. A contract containing both of these functions
    will be rejected.


.. _ambiguous-contract-functions:

Invoke Ambiguous Contract Functions Example
-------------------------------------------

Below is an example of a contract that has multiple functions of the same name,
and the arguments are ambiguous.

.. code-block:: python

        >>> contract_source_code = """
        pragma solidity ^0.4.21;
        contract AmbiguousDuo {
          function identity(uint256 input, bool uselessFlag) returns (uint256) {
            return input;
          }
          function identity(int256 input, bool uselessFlag) returns (int256) {
            return input;
          }
        }
        """
        # fast forward all the steps of compiling and deploying the contract.
        >>> ambiguous_contract.functions.identity(1, True) # raises ValidationError

        >>> identity_func = ambiguous_contract.get_function_by_signature('identity(uint256,bool)')
        >>> identity_func(1, True)
        <Function identity(uint256,bool) bound to (1, True)>
        >>> identity_func(1, True).call()
        1


.. _enable-strict-byte-check:

Enabling Strict Checks for Bytes Types
--------------------------------------

By default, web3 is not very strict when it comes to hex and bytes values.
A bytes type will take a hex string, a bytestring, or a regular python
string that can be decoded as a hex.
Additionally, if an abi specifies a byte size, but the value that gets
passed in is less than the specified size, web3 will automatically pad the value.
For example, if an abi specifies a type of ``bytes4``, web3 will handle all of the following values:

.. list-table:: Valid byte and hex strings for a bytes4 type
   :widths: 25 75
   :header-rows: 1

   * - Input
     - Normalizes to
   * - ``''``
     - ``b'\x00\x00\x00\x00'``
   * - ``'0x'``
     - ``b'\x00\x00\x00\x00'``
   * - ``b''``
     - ``b'\x00\x00\x00\x00'``
   * - ``b'ab'``
     - ``b'ab\x00\x00'``
   * - ``'0xab'``
     - ``b'\xab\x00\x00\x00'``
   * - ``'1234'``
     - ``b'\x124\x00\x00'``
   * - ``'0x61626364'``
     - ``b'abcd'``
   * - ``'1234'``
     - ``b'1234'``


The following values will raise an error by default:

.. list-table:: Invalid byte and hex strings for a bytes4 type
   :widths: 25 75
   :header-rows: 1

   * - Input
     - Reason
   * - ``b'abcde'``
     - Bytestring with more than 4 bytes
   * - ``'0x6162636423'``
     - Hex string with more than 4 bytes
   * - ``2``
     - Wrong type
   * - ``'ah'``
     - String is not valid hex

However, you may want to be stricter with acceptable values for bytes types.
For this you can use the :meth:`w3.enable_strict_bytes_type_checking()` method,
which is available on the web3 instance. A web3 instance which has had this method
invoked will enforce a stricter set of rules on which values are accepted.

 - A Python string that is not prefixed with ``0x`` will throw an error.
 - A bytestring whose length not exactly the specified byte size
   will raise an error.

.. list-table:: Valid byte and hex strings for a strict bytes4 type
   :widths: 25 75
   :header-rows: 1

   * - Input
     - Normalizes to
   * - ``'0x'``
     - ``b'\x00\x00\x00\x00'``
   * - ``'0x61626364'``
     - ``b'abcd'``
   * - ``'1234'``
     - ``b'1234'``

.. list-table:: Invalid byte and hex strings with strict bytes4 type checking
   :widths: 25 75
   :header-rows: 1

   * - Input
     - Reason
   * - ``''``
     - Needs to be prefixed with a "0x" to be interpreted as an empty hex string
   * - ``'1234'``
     - Needs to either be a bytestring (b'1234') or be a hex value of the right size, prefixed with 0x (in this case: '0x31323334')
   * - ``b''``
     - Needs to have exactly 4 bytes
   * - ``b'ab'``
     - Needs to have exactly 4 bytes
   * - ``'0xab'``
     - Needs to have exactly 4 bytes
   * - ``'0x6162636464'``
     - Needs to have exactly 4 bytes


Taking the following contract code as an example:

.. testsetup:: arrayscontract

    from web3 import Web3
    w3 = Web3(Web3.EthereumTesterProvider())
    bytecode = "608060405234801561001057600080fd5b506040516106103803806106108339810180604052602081101561003357600080fd5b81019080805164010000000081111561004b57600080fd5b8281019050602081018481111561006157600080fd5b815185602082028301116401000000008211171561007e57600080fd5b5050929190505050806000908051906020019061009c9291906100a3565b505061019c565b82805482825590600052602060002090600f0160109004810192821561015a5791602002820160005b8382111561012a57835183826101000a81548161ffff02191690837e010000000000000000000000000000000000000000000000000000000000009004021790555092602001926002016020816001010492830192600103026100cc565b80156101585782816101000a81549061ffff021916905560020160208160010104928301926001030261012a565b505b509050610167919061016b565b5090565b61019991905b8082111561019557600081816101000a81549061ffff021916905550600101610171565b5090565b90565b610465806101ab6000396000f3fe608060405260043610610051576000357c0100000000000000000000000000000000000000000000000000000000900480633b3230ee14610056578063d7c8a410146100e7578063dfe3136814610153575b600080fd5b34801561006257600080fd5b5061008f6004803603602081101561007957600080fd5b8101908080359060200190929190505050610218565b60405180827dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff19167dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200191505060405180910390f35b3480156100f357600080fd5b506100fc61026c565b6040518080602001828103825283818151815260200191508051906020019060200280838360005b8381101561013f578082015181840152602081019050610124565b505050509050019250505060405180910390f35b34801561015f57600080fd5b506102166004803603602081101561017657600080fd5b810190808035906020019064010000000081111561019357600080fd5b8201836020820111156101a557600080fd5b803590602001918460208302840111640100000000831117156101c757600080fd5b919080806020026020016040519081016040528093929190818152602001838360200280828437600081840152601f19601f820116905080830192505050505050509192919290505050610326565b005b60008181548110151561022757fe5b9060005260206000209060109182820401919006600202915054906101000a90047e010000000000000000000000000000000000000000000000000000000000000281565b6060600080548060200260200160405190810160405280929190818152602001828054801561031c57602002820191906000526020600020906000905b82829054906101000a90047e01000000000000000000000000000000000000000000000000000000000000027dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1916815260200190600201906020826001010492830192600103820291508084116102a95790505b5050505050905090565b806000908051906020019061033c929190610340565b5050565b82805482825590600052602060002090600f016010900481019282156103f75791602002820160005b838211156103c757835183826101000a81548161ffff02191690837e01000000000000000000000000000000000000000000000000000000000000900402179055509260200192600201602081600101049283019260010302610369565b80156103f55782816101000a81549061ffff02191690556002016020816001010492830192600103026103c7565b505b5090506104049190610408565b5090565b61043691905b8082111561043257600081816101000a81549061ffff02191690555060010161040e565b5090565b9056fea165627a7a72305820a8f9f1f4815c1eedfb8df31298a5cd13b198895de878871328b5d96296b69b4e0029"
    abi = '''
      [
        {
          "constant": true,
          "inputs": [
            {
              "name": "",
              "type": "uint256"
            }
          ],
          "name": "bytes2Value",
          "outputs": [
            {
              "name": "",
              "type": "bytes2"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": true,
          "inputs": [],
          "name": "getBytes2Value",
          "outputs": [
            {
              "name": "",
              "type": "bytes2[]"
            }
          ],
          "payable": false,
          "stateMutability": "view",
          "type": "function"
        },
        {
          "constant": false,
          "inputs": [
            {
              "name": "_bytes2Value",
              "type": "bytes2[]"
            }
          ],
          "name": "setBytes2Value",
          "outputs": [],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "inputs": [
            {
              "name": "_bytes2Value",
              "type": "bytes2[]"
            }
          ],
          "payable": false,
          "stateMutability": "nonpayable",
          "type": "constructor"
        }
      ]
     '''.strip()

.. code-block:: python

    >>> #  pragma solidity >=0.4.22 <0.6.0;
    ...
    ... #   contract ArraysContract {
    ... #      bytes2[] public bytes2Value;

    ... #      constructor(bytes2[] memory _bytes2Value) public {
    ... #          bytes2Value = _bytes2Value;
    ... #      }

    ... #      function setBytes2Value(bytes2[] memory _bytes2Value) public {
    ... #          bytes2Value = _bytes2Value;
    ... #      }

    ... #      function getBytes2Value() public view returns (bytes2[] memory) {
    ... #          return bytes2Value;
    ... #      }
    ... #  }

    >>> # abi = "..."
    >>> # bytecode = "6080..."

.. doctest:: arrayscontract

    >>> ArraysContract = w3.eth.contract(abi=abi, bytecode=bytecode)

    >>> tx_hash = ArraysContract.constructor([b'b']).transact()
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    >>> array_contract = w3.eth.contract(
    ...     address=tx_receipt.contractAddress,
    ...     abi=abi
    ... )

    >>> array_contract.functions.getBytes2Value().call()
    [b'b\x00']
    >>> array_contract.functions.setBytes2Value([b'a']).transact({'gas': 420000, 'gasPrice': 21000})
    HexBytes('0x89f9b3a00651e406c568e85c1d2336c66b4ec40ba82c5e72726fbd072230a41c')
    >>> array_contract.functions.getBytes2Value().call()
    [b'a\x00']
    >>> w3.enable_strict_bytes_type_checking()
    >>> array_contract.functions.setBytes2Value([b'a']).transact()
    Traceback (most recent call last):
       ...
    ValidationError:
    Could not identify the intended function with name `setBytes2Value`


.. _contract-functions:

Contract Functions
------------------

.. py:class:: ContractFunction

The named functions exposed through the :py:attr:`Contract.functions` property are
of the ContractFunction type. This class is not to be used directly,
but instead through :py:attr:`Contract.functions`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        twentyone = myContract.functions.multiply7(3).call()

If you have the function name in a variable, you might prefer this alternative:

    .. code-block:: python

        func_to_call = 'multiply7'
        contract_func = myContract.functions[func_to_call]
        twentyone = contract_func(3).call()

:py:class:`ContractFunction` provides methods to interact with contract functions.
Positional and keyword arguments supplied to the contract function subclass
will be used to find the contract function by signature,
and forwarded to the contract function when applicable.

Methods
~~~~~~~~~~

.. py:method:: ContractFunction.transact(transaction)

    Execute the specified function by sending a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).transact(transaction)

    The first portion of the function call ``myMethod(*args, **kwargs)``
    selects the appropriate contract function based on the name and provided
    argument.  Arguments can be provided as positional arguments, keyword
    arguments, or a mix of the two.

    The end portion of this function call ``transact(transaction)`` takes a
    single parameter which should be a python dictionary conforming to
    the same format as the ``web3.eth.sendTransaction(transaction)`` method.
    This dictionary may not contain the keys ``data``.

    If any of the ``args`` or ``kwargs`` specified in the ABI are an ``address`` type, they
    will accept ENS names.

    If a ``gas`` value is not provided, then the ``gas`` value for the
    method transaction will be created using the ``web3.eth.estimateGas()``
    method.

    Returns the transaction hash.

    .. code-block:: python

        >>> token_contract.functions.transfer(web3.eth.accounts[1], 12345).transact()
        "0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd"


.. py:method:: ContractFunction.call(transaction, block_identifier='latest')

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).call(transaction)

    This method behaves the same as the :py:meth:`ContractFunction.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    Returns the return value of the executed function.

    .. code-block:: python

        >>> my_contract.functions.multiply7(3).call()
        21
        >>> token_contract.functions.myBalance().call({'from': web3.eth.coinbase})
        12345  # the token balance for `web3.eth.coinbase`
        >>> token_contract.functions.myBalance().call({'from': web3.eth.accounts[1]})
        54321  # the token balance for the account `web3.eth.accounts[1]`

    You can call the method at a historical block using ``block_identifier``. Some examples:

    .. code-block:: python

        # You can call your contract method at a block number:
        >>> token_contract.functions.myBalance().call(block_identifier=10)

        # or a number of blocks back from pending,
        # in this case, the block just before the latest block:
        >>> token_contract.functions.myBalance().call(block_identifier=-2)

        # or a block hash:
        >>> token_contract.functions.myBalance().call(block_identifier='0x4ff4a38b278ab49f7739d3a4ed4e12714386a9fdf72192f2e8f7da7822f10b4d')
        >>> token_contract.functions.myBalance().call(block_identifier=b'O\xf4\xa3\x8b\'\x8a\xb4\x9fw9\xd3\xa4\xedN\x12qC\x86\xa9\xfd\xf7!\x92\xf2\xe8\xf7\xdax"\xf1\x0bM')

        # Latest is the default, so this is redundant:
        >>> token_contract.functions.myBalance().call(block_identifier='latest')

        # You can check the state after your pending transactions (if supported by your node):
        >>> token_contract.functions.myBalance().call(block_identifier='pending')

.. py:method:: ContractFunction.estimateGas(transaction, block_identifier=None)

    Call a contract function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).estimateGas(transaction)

    This method behaves the same as the :py:meth:`ContractFunction.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    Returns the amount of gas consumed which can be used as a gas estimate for
    executing this transaction publicly.

    .. code-block:: python

        >>> my_contract.functions.multiply7(3).estimateGas()
        42650

    .. note::
        The parameter ``block_identifier`` is not enabled in geth nodes,
        hence passing a value of ``block_identifier`` when connected to a geth
        nodes would result in an error like:  ``ValueError: {'code': -32602, 'message': 'too many arguments, want at most 1'}``

.. py:method:: ContractFunction.buildTransaction(transaction)

    Builds a transaction dictionary based on the contract function call specified.

    Refer to the following invocation:

    .. code-block:: python

        myContract.functions.myMethod(*args, **kwargs).buildTransaction(transaction)

    This method behaves the same as the :py:meth:`Contract.transact` method,
    with transaction details being passed into the end portion of the
    function call, and function arguments being passed into the first portion.

    .. note::
        `nonce` is not returned as part of the transaction dictionary unless it is
        specified in the first portion of the function call:

        .. code-block:: python

            >>> math_contract.functions.increment(5).buildTransaction({'nonce': 10})

        You may use :meth:`~web3.eth.Eth.getTransactionCount` to get the current nonce
        for an account. Therefore a shortcut for producing a transaction dictionary with
        nonce included looks like:

        .. code-block:: python

            >>> math_contract.functions.increment(5).buildTransaction({'nonce': web3.eth.getTransactionCount('0xF5...')})

    Returns a transaction dictionary. This transaction dictionary can then be sent using
    :meth:`~web3.eth.Eth.sendTransaction`.

    Additionally, the dictionary may be used for offline transaction signing using
    :meth:`~web3.eth.account.Account.signTransaction`.

    .. code-block:: python

        >>> math_contract.functions.increment(5).buildTransaction({'gasPrice': 21000000000})
        {
            'to': '0x6Bc272FCFcf89C14cebFC57B8f1543F5137F97dE',
            'data': '0x7cf5dab00000000000000000000000000000000000000000000000000000000000000005',
            'value': 0,
            'gas': 43242,
            'gasPrice': 21000000000,
            'chainId': 1
        }

.. _fallback-function:

Fallback Function
~~~~~~~~~~~~~~~~~

    The Contract Factory also offers an API to interact with the fallback function, which supports four methods like
    normal functions:

.. py:method:: Contract.fallback.call(transaction)

    Call fallback function, executing the transaction locally using the
    ``eth_call`` API.  This will not create a new public transaction.

.. py:method:: Contract.fallback.estimateGas(transaction)

    Call fallback function and return the gas estimation.

.. py:method:: Contract.fallback.transact(transaction)

    Execute fallback function by sending a new public transaction.

.. py:method:: Contract.fallback.buildTransaction(transaction)

    Builds a transaction dictionary based on the contract fallback function call.

Events
------

.. py:class:: ContractEvents

The named events exposed through the :py:attr:`Contract.events` property are of the ContractEvents type. This class is not to be used directly, but instead through :py:attr:`Contract.events`.

For example:

    .. code-block:: python

        myContract = web3.eth.contract(address=contract_address, abi=contract_abi)
        tx_hash = myContract.functions.myFunction().transact()
        receipt = web3.eth.getTransactionReceipt(tx_hash)
        myContract.events.myEvent().processReceipt(receipt)

:py:class:`ContractEvent` provides methods to interact with contract events. Positional and keyword arguments supplied to the contract event subclass will be used to find the contract event by signature.

.. _processReceipt:

.. py:method:: ContractEvents.myEvent(*args, **kwargs).processReceipt(transaction_receipt, errors=WARN)

   Extracts the pertinent logs from a transaction receipt.

   If there are no errors, ``processReceipt`` returns a tuple of :ref:`Event Log Objects <event-log-object>`, emitted from the event (e.g. ``myEvent``),
   with decoded ouput.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> rich_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> rich_logs[0]['args']
       {'myArg': 12345}

   If there are errors, the logs will be handled differently depending on the flag that is passed in:

     - ``WARN`` (default) - logs a warning to the console for the log that has an error, and discards the log. Returns any logs that are able to be processed.
     - ``STRICT`` - stops all processing and raises the error encountered.
     - ``IGNORE`` - returns any raw logs that raised an error with an added "errors" field, along with any other logs were able to be processed.
     - ``DISCARD`` - silently discards any logs that have errors, and returns processed logs that don't have errors.

   An event log error flag needs to be imported from ``web3/logs.py``.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt)
       >>> processed_logs
       (
          AttributeDict({
              'args': AttributeDict({}),
              'event': 'myEvent',
              'logIndex': 0,
              'transactionIndex': 0,
              'transactionHash': HexBytes('0xfb95ccb6ab39e19821fb339dee33e7afe2545527725b61c64490a5613f8d11fa'),
              'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
              'blockHash': HexBytes('0xd74c3e8bdb19337987b987aee0fa48ed43f8f2318edfc84e3a8643e009592a68'),
              'blockNumber': 3
          })
       )


       # Or, if there were errors encountered during processing:
       >>> from web3.logs import STRICT, IGNORE, DISCARD, WARN
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt, errors=IGNORE)
       >>> processed_logs
       (
           AttributeDict({
               'type': 'mined',
               'logIndex': 0,
               'transactionIndex': 0,
               'transactionHash': HexBytes('0x01682095d5abb0270d11a31139b9a1f410b363c84add467004e728ec831bd529'),
               'blockHash': HexBytes('0x92abf9325a3959a911a2581e9ea36cba3060d8b293b50e5738ff959feb95258a'),
               'blockNumber': 5,
               'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
               'data': '0x0000000000000000000000000000000000000000000000000000000000003039',
               'topics': [
                   HexBytes('0xf70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb15')
               ],
               'errors': LogTopicError('Expected 1 log topics.  Got 0')})
          })
       )
       >>> processed_logs = contract.events.myEvent().processReceipt(tx_receipt, errors=DISCARD)
       >>> assert processed_logs == ()
       True

.. py:method:: ContractEvents.myEvent(*args, **kwargs).processLog(log)

   Similar to processReceipt_, but only processes one log at a time, instead of a whole transaction receipt.
   Will return a single :ref:`Event Log Object <event-log-object>` if there are no errors encountered during processing. If an error is encountered during processing, it will be raised.

   .. code-block:: python

       >>> tx_hash = contract.functions.myFunction(12345).transact({'to':contract_address})
       >>> tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
       >>> log_to_process = tx_receipt['logs'][0]
       >>> processed_log = contract.events.myEvent().processLog(log_to_process)
       >>> processed_log
       AttributeDict({
           'args': AttributeDict({}),
           'event': 'myEvent',
           'logIndex': 0,
           'transactionIndex': 0,
           'transactionHash': HexBytes('0xfb95ccb6ab39e19821fb339dee33e7afe2545527725b61c64490a5613f8d11fa'),
           'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
           'blockHash': HexBytes('0xd74c3e8bdb19337987b987aee0fa48ed43f8f2318edfc84e3a8643e009592a68'),
           'blockNumber': 3
       })


.. _event-log-object:

Event Log Object
~~~~~~~~~~~~~~~~

    The Event Log Object is a python dictionary with the following keys:

    * ``args``: Dictionary - The arguments coming from the event.
    * ``event``: String - The event name.
    * ``logIndex``: Number - integer of the log index position in the block.
    * ``transactionIndex``: Number - integer of the transactions index position
      log was created from.
    * ``transactionHash``: String, 32 Bytes - hash of the transactions this log
      was created from.
    * ``address``: String, 32 Bytes - address from which this log originated.
    * ``blockHash``: String, 32 Bytes - hash of the block where this log was
      in. null when it's pending.
    * ``blockNumber``: Number - the block number where this log was in. null
      when it's pending.

.. testsetup:: createFilter

    from web3 import Web3
    from hexbytes import HexBytes
    w3 = Web3(Web3.EthereumTesterProvider())
    bytecode = '6060604052341561000c57fe5b604051602080610acb833981016040528080519060200190919050505b620f42408114151561003b5760006000fd5b670de0b6b3a76400008102600281905550600254600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b505b610a27806100a46000396000f30060606040523615610097576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806306fdde0314610099578063095ea7b31461013257806318160ddd1461018957806323b872dd146101af578063313ce5671461022557806370a082311461025157806395d89b411461029b578063a9059cbb14610334578063dd62ed3e1461038b575bfe5b34156100a157fe5b6100a96103f4565b60405180806020018281038252838181518152602001915080519060200190808383600083146100f8575b8051825260208311156100f8576020820191506020810190506020830392506100d4565b505050905090810190601f1680156101245780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561013a57fe5b61016f600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061042e565b604051808215151515815260200191505060405180910390f35b341561019157fe5b610199610521565b6040518082815260200191505060405180910390f35b34156101b757fe5b61020b600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610527565b604051808215151515815260200191505060405180910390f35b341561022d57fe5b610235610791565b604051808260ff1660ff16815260200191505060405180910390f35b341561025957fe5b610285600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610796565b6040518082815260200191505060405180910390f35b34156102a357fe5b6102ab6107e0565b60405180806020018281038252838181518152602001915080519060200190808383600083146102fa575b8051825260208311156102fa576020820191506020810190506020830392506102d6565b505050905090810190601f1680156103265780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561033c57fe5b610371600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061081a565b604051808215151515815260200191505060405180910390f35b341561039357fe5b6103de600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610973565b6040518082815260200191505060405180910390f35b604060405190810160405280600981526020017f54657374546f6b656e000000000000000000000000000000000000000000000081525081565b600081600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a3600190505b92915050565b60025481565b600081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410806105f1575081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054105b156105fc5760006000fd5b81600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b9392505050565b601281565b6000600060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b919050565b604060405190810160405280600481526020017f544553540000000000000000000000000000000000000000000000000000000081525081565b600081600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410156108695760006000fd5b81600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b92915050565b6000600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b929150505600a165627a7a723058205071371ee2a4a1be3c96e77d939cdc26161a256fdd638efc08bd33dfc65d3b850029'
    ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"inputs":[{"name":"_totalSupply","type":"uint256"}],"payable":false,"type":"constructor","stateMutability":"nonpayable"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
    my_token_contract = w3.eth.contract(abi=ABI, bytecode=bytecode)
    alice, bob = w3.eth.accounts[0], w3.eth.accounts[1]
    assert alice == '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf', alice
    assert bob == '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF', bob
    tx_hash = my_token_contract.constructor(1000000).transact({'from': alice, 'gas': 899000, 'gasPrice': 320000})
    assert tx_hash == HexBytes('0x611aa2d5c3e51f08d0665c4529c5520ed32520d8a48ba2cf2aff3f2fce3f26e4'), tx_hash
    txn_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    assert txn_receipt['contractAddress'] == '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']
    contract = w3.eth.contract(contract_address, abi=ABI)
    total_supply = contract.functions.totalSupply().call()
    decimals = 10 ** 18
    assert total_supply == 1000000 * decimals, total_supply
    tx_hash = contract.functions.transfer(alice, 10).transact({'gas': 899000, 'gasPrice': 200000})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

.. doctest:: createFilter

     >>> transfer_filter = my_token_contract.events.Transfer.createFilter(fromBlock="0x0", argument_filters={'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf'})
     >>> transfer_filter.get_new_entries()
     [AttributeDict({'args': AttributeDict({'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'value': 10}),
      'event': 'Transfer',
      'logIndex': 0,
      'transactionIndex': 0,
      'transactionHash': HexBytes('0x0005643c2425552308b4a28814a4dedafb5d340a811b3d2b1c019b290ffd7410'),
      'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
      'blockHash': HexBytes('...'),
      'blockNumber': 2})]
     >>> transfer_filter.get_new_entries()
     []
     >>> tx_hash = contract.functions.transfer(alice, 10).transact({'gas': 899000, 'gasPrice': 200000})
     >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
     >>> transfer_filter.get_new_entries()
     [AttributeDict({'args': AttributeDict({'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'value': 10}),
      'event': 'Transfer',
      'logIndex': 0,
      'transactionIndex': 0,
      'transactionHash': HexBytes('0xea111a49b82b0a0729d49f9ad924d8f87405d01e3fa87463cf2903848aacf7d9'),
      'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
      'blockHash': HexBytes('...'),
      'blockNumber': 3})]
     >>> transfer_filter.get_all_entries()
     [AttributeDict({'args': AttributeDict({'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'value': 10}),
      'event': 'Transfer',
      'logIndex': 0,
      'transactionIndex': 0,
      'transactionHash': HexBytes('0x0005643c2425552308b4a28814a4dedafb5d340a811b3d2b1c019b290ffd7410'),
      'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
      'blockHash': HexBytes('...'),
      'blockNumber': 2}),
      AttributeDict({'args': AttributeDict({'from': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'to': '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf',
      'value': 10}),
      'event': 'Transfer',
      'logIndex': 0,
      'transactionIndex': 0,
      'transactionHash': HexBytes('0xea111a49b82b0a0729d49f9ad924d8f87405d01e3fa87463cf2903848aacf7d9'),
      'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b',
      'blockHash': HexBytes('...'),
      'blockNumber': 3})]

Utils
-----

.. py:classmethod:: Contract.decode_function_input(data)

    Decodes the transaction data used to invoke a smart contract function, and returns
    :py:class:`ContractFunction` and decoded parameters as :py:class:`dict`.

    .. code-block:: python

        >>> transaction = w3.eth.getTransaction('0x5798fbc45e3b63832abc4984b0f3574a13545f415dd672cd8540cd71f735db56')
        >>> transaction.input
        '0x612e45a3000000000000000000000000b656b2a9c3b2416437a811e07466ca712f5a5b5a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000000000000000093a80000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000116c6f6e656c792c20736f206c6f6e656c7900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        >>> contract.decode_function_input(transaction.input)
        (<Function newProposal(address,uint256,string,bytes,uint256,bool)>,
         {'_recipient': '0xB656b2a9c3b2416437A811e07466cA712F5a5b5a',
          '_amount': 0,
          '_description': b'lonely, so lonely',
          '_transactionData': b'',
          '_debatingPeriod': 604800,
          '_newCurator': True})

ContractCaller
--------------

.. py:class:: ContractCaller

The ``ContractCaller`` class provides an API to call functions in a contract. This class
is not to be used directly, but instead through ``Contract.caller``.

There are a number of different ways to invoke the ``ContractCaller``.

For example:

.. testsetup:: contractcaller

   import json
   from web3 import Web3
   w3 = Web3(Web3.EthereumTesterProvider())
   bytecode = "0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"
   ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"increased","type":"event"}]')
   contract = w3.eth.contract(abi=ABI, bytecode=bytecode)
   deploy_txn = contract.constructor().transact()
   deploy_receipt = w3.eth.waitForTransactionReceipt(deploy_txn)
   address = deploy_receipt.contractAddress

.. doctest:: contractcaller

   >>> myContract = w3.eth.contract(address=address, abi=ABI)
   >>> twentyone = myContract.caller.multiply7(3)
   >>> twentyone
   21

It can also be invoked using parentheses:

.. doctest:: contractcaller

   >>> twentyone = myContract.caller().multiply7(3)
   >>> twentyone
   21

And a transaction dictionary, with or without the ``transaction`` keyword.
You can also optionally include a block identifier. For example:

.. doctest:: contractcaller

   >>> from_address = w3.eth.accounts[1]
   >>> twentyone = myContract.caller({'from': from_address}).multiply7(3)
   >>> twentyone
   21
   >>> twentyone = myContract.caller(transaction={'from': from_address}).multiply7(3)
   >>> twentyone
   21
   >>> twentyone = myContract.caller(block_identifier='latest').multiply7(3)
   >>> twentyone
   21

Like :py:class:`ContractFunction`, :py:class:`ContractCaller`
provides methods to interact with contract functions.
Positional and keyword arguments supplied to the contract caller subclass
will be used to find the contract function by signature,
and forwarded to the contract function when applicable.
