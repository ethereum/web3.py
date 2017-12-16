.. _Gas_Pricing:

Gas Pricing API
===============

For Ethereum transactions, gas price is a delicate property. For this reason, 
Web3 includes an API for interacting with it.  

With Web3, the gas price included in a transaction (if not explicitly set) is 
determined by the selected "Gas Pricing Strategy". A gas pricing strategy is 
a method which takes the Web3 object and a transaction dictionary and returns 
a gas price (denominated in wei). 

Retrieving gas price
--------------------

To retreive the gas price using the selected strategy simply call 
:meth:`~overview.Web3.get_gas_price` 

.. code-block:: python

    >>> Web3.get_gas_price()
    20000000000

The default gas pricing strategy
--------------------------------

.. py:module:: web3.gas_strategies.rpc

.. py:method:: rpc_gas_pricing_strategy(web3, transaction_params=None)

    The default gas pricing strategy simply makes a call to the `JSON-RPC eth_gasPrice 
    method <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_gasprice>`_ which returns
    the gas price configured by the connected Ethereum node. 

Creating a gas pricing strategy
-------------------------------

A gas pricing strategy is implemented as a python method with the following 
signature:

.. code-block:: python

    def gas_pricing_strategy(web3, transaction_params=None):
    ...

The method must return a positive integer representing the gas price in wei.

To demonstrate, here is a rudimentary example of a gas pricing strategy that 
returns a higher gas price when the value of the transaction is higher than 
1 Ether.

.. code-block:: python

    from web3 import Web3
    
    def value_based_gas_pricing_strategy(web3, transaction_params):
        if transaction_params['value'] > Web3.toWei(1, 'ether'):
            return Web3.toWei(20, 'gwei')
        else:
            return Web3.toWei(5, 'gwei')

Selecting the gas pricing strategy
----------------------------------

The gas pricing strategy can be changed by setting :py:attr:`~Web3.gas_pricing_strategy`.

.. code-block:: python

    from web3 import Web3
    
    def value_based_gas_pricing_strategy(web3, transaction_params):
        ...

    w3 = Web3(...)
    w3.gas_pricing_strategy = value_based_gas_pricing_strategy