
Extending Method
==========================

The JSON-RPC API can be extended to include methods that aren't included in web3 by default.

To extend the API, you will need to make a class that inherits from ModuleV2,
and you will need to use the Method class. Calls to Method go through these steps:

    1. Input munging - includes normalization, parameter checking, and early parameter
    formatting.  Basically, any processing on the input parameters that needs to happen before
    json_rpc_method string selection occurs.

        A note about mungers: The first (root) munger should reflect the desired
        api function arguments. In other words, if the api function wants to
        behave as: ``getBalance(account, block_identifier=None)``, the root munger
        should accept these same arguments, with the addition of the module as
        the first argument e.g.:

        .. code-block:: python

          def getBalance_root_munger(module, account, block_identifier=None):
              if block_identifier is None:
                  block_identifier = DEFAULT_BLOCK
              return module, [account, block_identifier]

        all mungers should return an argument list.

        If no munger is provided, a default munger expecting no method arguments
        will be used.

    2. Method Selection - The json_rpc_method argument can be method string or a
    function that returns a method string. If a callable is provided the processed
    method inputs are passed to the method selection function, and the returned
    method string is used.

    3. Request and Response Formatters Are Set - formatters are retrieved
    using the JSON-RPC method string, or custom formatters can be passed in.

    4. After the parameter processing from steps 1-3 the request is made using
    the calling function returned by the module attribute ``retrieve_caller_fn``
    and the reponse formatters are applied to the output.

This is perhaps best demonstrated through an example.
Let's say I wanted to add something like ``eth.getBalance``. I would make my class,
and make sure it inherits from ``ModuleV2``:

.. doctest::

    >>> from web3.method import Method
    >>> from web3.module import ModuleV2
    >>> from web3.auto.infura import w3

    >>> class Eth(ModuleV2):
    ...     def block_id_munger(self, account, block_identifier = None):
    ...         if block_identifier is None:
    ...             block_identifier = 'latest'
    ...         return (account, block_identifier)
    ...
    ...     getBalance = Method(
    ...         'eth_getBalance',
    ...         mungers=[block_id_munger],
    ...     )

    >>> balance = Eth(w3).getBalance('0x0000000000000000000000000000000000000000')


Note that the munger needs to accept all the parameters that the method uses.

I can also decide on what method to call based on
what parameters are passed in, like in the case of ``eth.getBlock``.
I pass in a method to the method_choice_depends_on_args argument.

.. doctest::

    >>> from web3.method import Method
    >>> from web3.module import ModuleV2
    >>> from web3.auto.infura import w3
    >>> from web3._utils.blocks import select_method_for_block_identifier

    >>> class Eth(ModuleV2):
    ...
    ...   def get_block_munger(self, block_identifier, full_transactions=False):
    ...       return (block_identifier, full_transactions)
    ...
    ...   getBlock = Method(
    ...      method_choice_depends_on_args=select_method_for_block_identifier(
    ...          if_predefined='eth_getBlockByNumber',
    ...          if_hash='eth_getBlockByHash',
    ...          if_number='eth_getBlockByNumber',
    ...      ),
    ...      mungers=[get_block_munger],
    ...   )

    >>> Eth(w3).getBlock(1)
    AttributeDict({'difficulty': 17171480576,
      'extraData': HexBytes('0x476574682f76312e302e302f6c696e75782f676f312e342e32'),
      'gasLimit': 5000,
      'gasUsed': 0,
      'hash': HexBytes('0x88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6'),
      'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
      'miner': '0x05a56E2D52c817161883f50c441c3228CFe54d9f',
      'mixHash': HexBytes('0x969b900de27b6ac6a67742365dd65f55a0526c41fd18e1b16f1a1215c2e66f59'),
      'nonce': HexBytes('0x539bd4979fef1ec4'),
      'number': 1,
      'parentHash': HexBytes('0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3'),
      'receiptsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'),
      'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
      'size': 537, 'stateRoot': HexBytes('0xd67e4d450343046425ae4271474353857ab860dbc0a1dde64b41b5cd3a532bf3'),
      'timestamp': 1438269988,
      'totalDifficulty': 34351349760,
      'transactions': [],
      'transactionsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'),
      'uncles': []})

We can also pass in custom request, response, and error handlers using ``Method``'s attributes
``request_formatters``, ``result_formatters``, and ``error_formatters``. In the example above,
the attribute dict formatter is being used as a default formatter. Passing in our own looks like:

.. doctest::

    >>> from web3.method import Method
    >>> from web3.module import ModuleV2
    >>> from web3.auto.infura import w3
    >>> from eth_utils.toolz import curry

    >>> class Eth(ModuleV2):
    ...     @curry
    ...     def make_response_nice(method_name, result):
    ...          if method_name == 'eth_getBalance':
    ...              print('Balance is: 8400238857870150803729 Wei')
    ...          else:
    ...              return result
    ...
    ...     def block_id_munger(self, account, block_identifier = None):
    ...         if block_identifier is None:
    ...             block_identifier = 'latest'
    ...         return (account, block_identifier)
    ...
    ...     getBalance = Method(
    ...         'eth_getBalance',
    ...         mungers=[block_id_munger],
    ...         result_formatters=make_response_nice
    ...     )

    >>> Eth(w3).getBalance('0x' + '00' * 20)
    Balance is: 8400238857870150803729 Wei
