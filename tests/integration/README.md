For each integration test you need to define the following pytest fixtures.
They **must** all be *session* scoped.

- `web3`
- `empty_block`
- `block_with_txn`
- `math_contract`
- `keyfile_account_address`
- `keyfile_account_pkey`
- `math_contract_deploy_txn_hash`
- `mined_txn_hash`
- `emitter_contract`
- `block_with_txn_with_log`
- `txn_hash_with_log`

The details for these fixtures are as follows.

### Fixture Details

#### `web3`

A Web3 instance configured to connect to the backend for the integration test.

#### `empty_block`

A block as returned by `web3.eth.get_block` that has no transactions.

#### `block_with_txn`

A block as returned by `web3.eth.get_block` that has a single transaction.

#### `math_contract`

An deployed Contract instance of the *Math* contract found in
`web3._utils.contract_sources.MathContract.sol`.

#### `keyfile_account_address`

The address of an account known and managed by the test fixture node.

#### `keyfile_account_pkey`

The private key of an account known and managed by the test fixture node.

#### `math_contract_deploy_txn_hash`

The transaction hash used to deploy the `math_contract`.

#### `mined_txn_hash`

The transaction hash of a transaction which has been mined.

#### `emitter_contract`

A deployed Contract instance of the *EmitterContract* contract found in
`web3._utils.contract_sources.EmitterContract.sol`.

#### `block_with_txn_with_log`

A block with a transaction with a single log entry.

#### `txn_hash_with_log`

The hash of a transaction which fires a single log entry.

# Updating Fixture ZIPs

**ONLY** trusted parties should be allowed to update zipped fixtures, since they pose an attack surface through which a third party could inject malicious code into the codebase.
