from cytoolz.dicttoolz import (
    assoc,
)


def gas_price_middleware(make_request, web3):
    """
    Includes a gas price using the gas price strategy
    """
    def middleware(method, params):
        if method == 'eth_sendTransaction':
            transaction = params[0]
            generated_gas_price = web3.eth.generateGasPrice(transaction)
            if 'gasPrice' not in transaction and generated_gas_price:
                transaction = assoc(transaction, 'gasPrice', generated_gas_price)
                return make_request(method, [transaction])
        return make_request(method, params)
    return middleware
