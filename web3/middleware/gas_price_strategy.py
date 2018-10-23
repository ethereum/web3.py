from web3._utils.toolz import (
    assoc,
)


def gas_price_strategy_middleware(make_request, web3):
    """
    Includes a gas price using the gas price strategy
    """
    async def middleware(method, params):
        if method == 'eth_sendTransaction':
            transaction = params[0]
            if 'gasPrice' not in transaction:
                generated_gas_price = await web3.eth.coro_generateGasPrice(transaction)
                if generated_gas_price is not None:
                    transaction = assoc(transaction, 'gasPrice', generated_gas_price)
                    return await make_request(method, [transaction])
        return await make_request(method, params)
    return middleware
