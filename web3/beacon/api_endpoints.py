# [ BEACON endpoints ]

GET_GENESIS = "/eth/v1/beacon/genesis"
GET_HASH_ROOT = "/eth/v1/beacon/states/{0}/root"
GET_FORK_DATA = "/eth/v1/beacon/states/{0}/fork"
GET_FINALITY_CHECKPOINT = "/eth/v1/beacon/states/{0}/finality_checkpoints"
GET_VALIDATORS = "/eth/v1/beacon/states/{0}/validators"
GET_VALIDATOR = "/eth/v1/beacon/states/{0}/validators/{1}"
GET_VALIDATOR_BALANCES = "/eth/v1/beacon/states/{0}/validator_balances"
GET_EPOCH_COMMITTEES = "/eth/v1/beacon/states/{0}/committees"
GET_BLOCK_HEADERS = "/eth/v1/beacon/headers"
GET_BLOCK_HEADER = "/eth/v1/beacon/headers/{0}"
GET_BLOCK = "/eth/v2/beacon/blocks/{0}"
GET_BLOCK_ROOT = "/eth/v1/beacon/blocks/{0}/root"
GET_BLOCK_ATTESTATIONS = "/eth/v1/beacon/blocks/{0}/attestations"
GET_ATTESTATIONS = "/eth/v1/beacon/pool/attestations"
GET_ATTESTER_SLASHINGS = "/eth/v1/beacon/pool/attester_slashings"
GET_PROPOSER_SLASHINGS = "/eth/v1/beacon/pool/proposer_slashings"
GET_VOLUNTARY_EXITS = "/eth/v1/beacon/pool/voluntary_exits"

# [ CONFIG endpoints ]

GET_FORK_SCHEDULE = "/eth/v1/config/fork_schedule"
GET_SPEC = "/eth/v1/config/spec"
GET_DEPOSIT_CONTRACT = "/eth/v1/config/deposit_contract"

# [ DEBUG endpoints ]

GET_BEACON_STATE = "/eth/v1/debug/beacon/states/{0}"
GET_BEACON_HEADS = "/eth/v1/debug/beacon/heads"

# [ NODE endpoints ]

GET_NODE_IDENTITY = "/eth/v1/node/identity"
GET_PEERS = "/eth/v1/node/peers"
GET_PEER = "/eth/v1/node/peers/{0}"
GET_HEALTH = "/eth/v1/node/health"
GET_VERSION = "/eth/v1/node/version"
GET_SYNCING = "/eth/v1/node/syncing"
