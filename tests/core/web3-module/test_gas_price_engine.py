from web3.utils.gas_price_engines import default_gas_price_engine


def test_default_gas_price_engine(web3):
    assert web3.gasPriceEngine == default_gas_price_engine


def test_default_gas_price_engine_returns_5_gwei(web3):
    assert web3.getGasPrice() == 5000000000
