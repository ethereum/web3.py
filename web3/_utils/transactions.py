import math
from typing import (
    TYPE_CHECKING,
    List,
    Optional,
    cast,
)

from eth_typing import (
    ChecksumAddress,
)
from eth_utils.toolz import (
    assoc,
    curry,
    merge,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.compat import (
    Literal,
)
from web3._utils.threads import (
    Timeout,
)
from web3.exceptions import (
    TransactionNotFound,
)
from web3.types import (
    BlockIdentifier,
    TxData,
    TxParams,
    TxReceipt,
    Wei,
    _Hash32,
)

TX_PARAM_LITERALS = Literal['from', 'to', 'gas', 'maxFeePerGas', 'maxPriorityFeePerGas',
                            'gasPrice', 'value', 'data', 'nonce', 'chainId']

VALID_TRANSACTION_PARAMS: List[TX_PARAM_LITERALS] = [
    'from',
    'to',
    'gas',
    'maxFeePerGas',
    'maxPriorityFeePerGas',
    'gasPrice',
    'value',
    'data',
    'nonce',
    'chainId',
]

TRANSACTION_DEFAULTS = {
    'value': 0,
    'data': b'',
    'gas': lambda web3, tx: web3.eth.estimate_gas(tx),
    'gasPrice': lambda web3, tx: web3.eth.generate_gas_price(tx) or web3.eth.gas_price,
    'chainId': lambda web3, tx: web3.eth.chain_id,
}

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


@curry
def fill_nonce(web3: "Web3", transaction: TxParams) -> TxParams:
    if 'from' in transaction and 'nonce' not in transaction:
        return assoc(
            transaction,
            'nonce',
            web3.eth.get_transaction_count(
                cast(ChecksumAddress, transaction['from']),
                block_identifier='pending'))
    else:
        return transaction


@curry
def fill_transaction_defaults(web3: "Web3", transaction: TxParams) -> TxParams:
    """
    if web3 is None, fill as much as possible while offline
    """
    defaults = {}
    for key, default_getter in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            if callable(default_getter):
                if web3 is not None:
                    default_val = default_getter(web3, transaction)
                else:
                    raise ValueError("You must specify %s in the transaction" % key)
            else:
                default_val = default_getter
            defaults[key] = default_val
    return merge(defaults, transaction)


def wait_for_transaction_receipt(
    web3: "Web3", txn_hash: _Hash32, timeout: float, poll_latency: float
) -> TxReceipt:
    with Timeout(timeout) as _timeout:
        while True:
            try:
                txn_receipt = web3.eth.get_transaction_receipt(txn_hash)
            except TransactionNotFound:
                txn_receipt = None
            # FIXME: The check for a null `blockHash` is due to parity's
            # non-standard implementation of the JSON-RPC API and should
            # be removed once the formal spec for the JSON-RPC endpoints
            # has been finalized.
            if txn_receipt is not None and txn_receipt['blockHash'] is not None:
                break
            _timeout.sleep(poll_latency)
    return txn_receipt


def get_block_gas_limit(web3: "Web3", block_identifier: Optional[BlockIdentifier] = None) -> Wei:
    if block_identifier is None:
        block_identifier = web3.eth.block_number
    block = web3.eth.get_block(block_identifier)
    return block['gasLimit']


def get_buffered_gas_estimate(
    web3: "Web3", transaction: TxParams, gas_buffer: Wei = Wei(100000)
) -> Wei:
    gas_estimate_transaction = cast(TxParams, dict(**transaction))

    gas_estimate = web3.eth.estimate_gas(gas_estimate_transaction)

    gas_limit = get_block_gas_limit(web3)

    if gas_estimate > gas_limit:
        raise ValueError(
            "Contract does not appear to be deployable within the "
            "current network gas limits.  Estimated: {0}. Current gas "
            "limit: {1}".format(gas_estimate, gas_limit)
        )

    return Wei(min(gas_limit, gas_estimate + gas_buffer))


def get_required_transaction(web3: "Web3", transaction_hash: _Hash32) -> TxData:
    current_transaction = web3.eth.get_transaction(transaction_hash)
    if not current_transaction:
        raise ValueError(f'Supplied transaction with hash {transaction_hash!r} does not exist')
    return current_transaction


def extract_valid_transaction_params(transaction_params: TxData) -> TxParams:
    extracted_params = cast(TxParams, {
        key: transaction_params[key]
        for key in VALID_TRANSACTION_PARAMS
        if key in transaction_params
    })

    if extracted_params.get('data') is not None:
        if transaction_params.get('input') is not None:
            if extracted_params['data'] != transaction_params['input']:
                msg = 'failure to handle this transaction due to both "input: {}" and'
                msg += ' "data: {}" are populated. You need to resolve this conflict.'
                err_vals = (transaction_params['input'], extracted_params['data'])
                raise AttributeError(msg.format(*err_vals))
            else:
                return extracted_params
        else:
            return extracted_params
    elif extracted_params.get('data') is None:
        if transaction_params.get('input') is not None:
            return assoc(extracted_params, 'data', transaction_params['input'])
        else:
            return extracted_params
    else:
        raise Exception("Unreachable path: transaction's 'data' is either set or not set")


def assert_valid_transaction_params(transaction_params: TxParams) -> None:
    for param in transaction_params:
        if param not in VALID_TRANSACTION_PARAMS:
            raise ValueError('{} is not a valid transaction parameter'.format(param))


def prepare_replacement_transaction(
    web3: "Web3",
    current_transaction: TxData,
    new_transaction: TxParams,
    gas_multiplier: float = 1.125
) -> TxParams:
    if current_transaction['blockHash'] is not None:
        raise ValueError(f'Supplied transaction with hash {current_transaction["hash"]!r} '
                         'has already been mined')
    if 'nonce' in new_transaction and new_transaction['nonce'] != current_transaction['nonce']:
        raise ValueError('Supplied nonce in new_transaction must match the pending transaction')

    if 'nonce' not in new_transaction:
        new_transaction = assoc(new_transaction, 'nonce', current_transaction['nonce'])

    if 'maxFeePerGas' in new_transaction or 'maxPriorityFeePerGas' in new_transaction:
        # for now, the client decides if a 1559 txn can replace the existing txn or not
        pass

    elif 'gasPrice' in new_transaction and current_transaction['gasPrice'] is not None:
        if new_transaction['gasPrice'] <= current_transaction['gasPrice']:
            raise ValueError('Supplied gas price must exceed existing transaction gas price')

    else:
        generated_gas_price = web3.eth.generate_gas_price(new_transaction)
        minimum_gas_price = int(math.ceil(current_transaction['gasPrice'] * gas_multiplier))
        if generated_gas_price and generated_gas_price > minimum_gas_price:
            new_transaction = assoc(new_transaction, 'gasPrice', generated_gas_price)
        else:
            new_transaction = assoc(new_transaction, 'gasPrice', minimum_gas_price)

    return new_transaction


def replace_transaction(
    web3: "Web3", current_transaction: TxData, new_transaction: TxParams
) -> HexBytes:
    new_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction
    )
    return web3.eth.send_transaction(new_transaction)
