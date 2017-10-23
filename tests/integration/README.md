For each integration test you need to define the following pytest fixtures.
They **must** all be *session* scoped.

* `web3`
* `empty_block`
* `block_with_txn`
* `math_contract`
* `unlocked_account`
* `funded_account_for_raw_txn`
* `math_contract_deploy_txn_hash`
* `mined_txn_hash`
* `emitter_contract`
* `block_with_txn_with_log`
* `txn_hash_with_log`

* `unlockable_account`
* `unlockable_account_pw`

The details for these fixtures are as follows.


### Fixture Details

#### `web3`

A Web3 instance configured to connect to the backend for the integration test.


#### `empty_block`

A block as returned by `web3.eth.getBlock` that has no transactions.


#### `block_with_txn`

A block as returned by `web3.eth.getBlock` that has a single transaction.


#### `math_contract`

An deployed Contract instance of the *Math* contract found in
`web3.utils.module_testing.math_contract`.


#### `unlocked_account`

The address of an account which is *unlocked*.


#### `funded_account_for_raw_txn`

An account which has not sent any transactions (nonce of 0) which has enough
ether for sending a single transaction.


#### `math_contract_deploy_txn_hash`

The transaction hash used to deploy the `math_contract`.


#### `mined_txn_hash`

The transaction hash of a transaction which has been mined.


#### `emitter_contract`

An deployed Contract instance of the *Emitter* contract found in
`web3.utils.module_testing.emitter_contract`.


#### `block_with_txn_with_log`

A block with a transaction with a single log entry.


#### `txn_hash_with_log`

The hash of a transaction which fires a single log entry.


#### `unlockable_account`

The address of an account that can be unlocked using the `unlockable_account_pw`


#### `unlockable_account_pw`

The password that can be used to unlock the `unlockable_account`
