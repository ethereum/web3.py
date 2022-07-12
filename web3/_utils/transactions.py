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
from web3._utils.utility_methods import (
    all_in_dict,
    any_in_dict,
)
from web3.constants import (
    DYNAMIC_FEE_TXN_PARAMS,
)
from web3.types import (
    BlockIdentifier,
    TxData,
    TxParams,
    Wei,
    _Hash32,
)

TX_PARAM_LITERALS = Literal['type', 'from', 'to', 'gas', 'maxFeePerGas', 'maxPriorityFeePerGas',
                            'gasPrice', 'value', 'data', 'nonce', 'chainId', 'accessList']

VALID_TRANSACTION_PARAMS: List[TX_PARAM_LITERALS] = [
    'type',
    'from',
    'to',
    'gas',
    'accessList',
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
    'gasPrice': lambda web3, tx: web3.eth.generate_gas_price(tx),
    'maxFeePerGas': (
        lambda web3, tx:
        web3.eth.max_priority_fee + (2 * web3.eth.get_block('latest')['baseFeePerGas'])
    ),
    'maxPriorityFeePerGas': lambda web3, tx: web3.eth.max_priority_fee,
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
    strategy_based_gas_price = web3.eth.generate_gas_price(transaction)
    is_dynamic_fee_transaction = (
        strategy_based_gas_price is None
        and (
            'gasPrice' not in transaction  # default to dynamic fee transaction
            or any_in_dict(DYNAMIC_FEE_TXN_PARAMS, transaction)
        )
    )

    defaults = {}
    for key, default_getter in TRANSACTION_DEFAULTS.items():
        if key not in transaction:
            if (
                is_dynamic_fee_transaction and key == 'gasPrice'
                or not is_dynamic_fee_transaction and key in DYNAMIC_FEE_TXN_PARAMS
            ):
                # do not set default max fees if legacy txn or gas price if dynamic fee txn
                continue

            if callable(default_getter):
                if web3 is None:
                    raise ValueError("You must specify a '%s' value in the transaction" % key)
                default_val = default_getter(web3, transaction)
            else:
                default_val = default_getter

            defaults[key] = default_val
    return merge(defaults, transaction)


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
    # There is always a gasPrice now on eth_getTransaction call for pending transactions, including
    # dynamic fee transactions. For dynamic fee transactions, we need to pull the gasPrice value
    # back out of the extracted params if it is equal to the expected value (maxFeePerGas). If
    # we don't, the modified transaction will include a gasPrice as well as dynamic fee values in
    # the eth_sendTransaction call and cause a conflict.
    if all_in_dict(DYNAMIC_FEE_TXN_PARAMS, extracted_params):
        if extracted_params['gasPrice'] == extracted_params['maxFeePerGas']:
            extracted_params.pop('gasPrice')

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
    original_transaction: TxData,
    replacement_transaction: TxParams,
    gas_multiplier: float = 1.125
) -> TxParams:
    if original_transaction['blockHash'] is not None:
        raise ValueError(f'Supplied transaction with hash {original_transaction["hash"]!r} '
                         'has already been mined')
    if 'nonce' in replacement_transaction and (
        replacement_transaction['nonce'] != original_transaction['nonce']
    ):
        raise ValueError('Supplied nonce in new_transaction must match the pending transaction')

    if 'nonce' not in replacement_transaction:
        replacement_transaction = assoc(
            replacement_transaction, 'nonce', original_transaction['nonce']
        )

    if any_in_dict(DYNAMIC_FEE_TXN_PARAMS, replacement_transaction):
        # for now, the client decides if a dynamic fee txn can replace the existing txn or not
        pass

    elif 'gasPrice' in replacement_transaction and original_transaction['gasPrice'] is not None:
        if replacement_transaction['gasPrice'] <= original_transaction['gasPrice']:
            raise ValueError('Supplied gas price must exceed existing transaction gas price')

    else:
        generated_gas_price = web3.eth.generate_gas_price(replacement_transaction)
        minimum_gas_price = int(math.ceil(original_transaction['gasPrice'] * gas_multiplier))
        if generated_gas_price and generated_gas_price > minimum_gas_price:
            replacement_transaction = assoc(
                replacement_transaction, 'gasPrice', generated_gas_price
            )
        else:
            replacement_transaction = assoc(replacement_transaction, 'gasPrice', minimum_gas_price)

    return replacement_transaction


def replace_transaction(
    web3: "Web3", current_transaction: TxData, new_transaction: TxParams
) -> HexBytes:
    new_transaction = prepare_replacement_transaction(
        web3, current_transaction, new_transaction
    )
    return web3.eth.send_transaction(new_transaction)
