.. _Gas_Price:

Gas Price API
===============

For Ethereum transactions, gas price is a delicate property. For this reason, 
Web3 includes an API for configuring it.  

By default, Web3 will not include a ``gasPrice`` in the transaction as to relay 
this responsibility to the connected node. The Gas Price API allows you to 
define Web3's behaviour for populating the gas price. This is done using a 
"Gas Price Strategy" - a method which takes the Web3 object and a transaction 
dictionary and returns a gas price (denominated in wei). 

Retrieving gas price
--------------------

To retreive the gas price using the selected strategy simply call 
:meth:`~web3.eth.Eth.generateGasPrice` 

.. code-block:: python

    >>> Web3.eth.generateGasPrice()
    20000000000

Creating a gas price strategy
-------------------------------

A gas price strategy is implemented as a python method with the following 
signature:

.. code-block:: python

    def gas_price_strategy(web3, transaction_params=None):
    ...

The method must return a positive integer representing the gas price in wei.

To demonstrate, here is a rudimentary example of a gas price strategy that 
returns a higher gas price when the value of the transaction is higher than 
1 Ether.

.. code-block:: python

    from web3 import Web3
    
    def value_based_gas_price_strategy(web3, transaction_params):
        if transaction_params['value'] > Web3.toWei(1, 'ether'):
            return Web3.toWei(20, 'gwei')
        else:
            return Web3.toWei(5, 'gwei')

Selecting the gas price strategy
--------------------------------

The gas price strategy can be set by calling :meth:`~web3.eth.Eth.setGasPriceStrategy`.

.. code-block:: python

    from web3 import Web3
    
    def value_based_gas_price_strategy(web3, transaction_params):
        ...

    w3 = Web3(...)
    w3.eth.setGasPriceStrategy(value_based_gas_price_strategy)

Available gas price strategies
------------------------------

.. py:module:: web3.gas_strategies.rpc

.. py:method:: rpc_gas_price_strategy(web3, transaction_params=None)

    Makes a call to the `JSON-RPC eth_gasPrice 
    method <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gasprice>`_ which returns
    the gas price configured by the connected Ethereum node. 