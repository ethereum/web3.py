# [ BEACON endpoints ]
from typing import (
    Final,
)

GET_GENESIS: Final = "/eth/v1/beacon/genesis"

# states
GET_HASH_ROOT: Final = "/eth/v1/beacon/states/{0}/root"
GET_FORK_DATA: Final = "/eth/v1/beacon/states/{0}/fork"
GET_FINALITY_CHECKPOINT: Final = "/eth/v1/beacon/states/{0}/finality_checkpoints"
GET_VALIDATORS: Final = "/eth/v1/beacon/states/{0}/validators"
GET_VALIDATOR: Final = "/eth/v1/beacon/states/{0}/validators/{1}"
GET_VALIDATOR_BALANCES: Final = "/eth/v1/beacon/states/{0}/validator_balances"
GET_EPOCH_COMMITTEES: Final = "/eth/v1/beacon/states/{0}/committees"
GET_EPOCH_SYNC_COMMITTEES: Final = "/eth/v1/beacon/states/{0}/sync_committees"
GET_EPOCH_RANDAO: Final = "/eth/v1/beacon/states/{0}/randao"

# headers
GET_BLOCK_HEADERS: Final = "/eth/v1/beacon/headers"
GET_BLOCK_HEADER: Final = "/eth/v1/beacon/headers/{0}"

# blocks
GET_BLOCK: Final = "/eth/v2/beacon/blocks/{0}"
GET_BLOCK_ROOT: Final = "/eth/v1/beacon/blocks/{0}/root"
GET_BLOCK_ATTESTATIONS: Final = "/eth/v1/beacon/blocks/{0}/attestations"
GET_BLINDED_BLOCKS: Final = "/eth/v1/beacon/blinded_blocks/{0}"

# rewards
GET_REWARDS: Final = "/eth/v1/beacon/rewards/blocks/{0}"

# blobs
GET_BLOB_SIDECARS: Final = "/eth/v1/beacon/blob_sidecars/{0}"

# light client
GET_LIGHT_CLIENT_BOOTSTRAP_STRUCTURE: Final = "/eth/v1/beacon/light_client/bootstrap/{0}"
GET_LIGHT_CLIENT_UPDATES: Final = "/eth/v1/beacon/light_client/updates"
GET_LIGHT_CLIENT_FINALITY_UPDATE: Final = "/eth/v1/beacon/light_client/finality_update"
GET_LIGHT_CLIENT_OPTIMISTIC_UPDATE: Final = "/eth/v1/beacon/light_client/optimistic_update"

# pool
GET_ATTESTATIONS: Final = "/eth/v1/beacon/pool/attestations"
GET_ATTESTER_SLASHINGS: Final = "/eth/v1/beacon/pool/attester_slashings"
GET_PROPOSER_SLASHINGS: Final = "/eth/v1/beacon/pool/proposer_slashings"
GET_VOLUNTARY_EXITS: Final = "/eth/v1/beacon/pool/voluntary_exits"
GET_BLS_TO_EXECUTION_CHANGES: Final = "/eth/v1/beacon/pool/bls_to_execution_changes"


# [ CONFIG endpoints ]

GET_FORK_SCHEDULE: Final = "/eth/v1/config/fork_schedule"
GET_SPEC: Final = "/eth/v1/config/spec"
GET_DEPOSIT_CONTRACT: Final = "/eth/v1/config/deposit_contract"

# [ DEBUG endpoints ]

GET_BEACON_STATE: Final = "/eth/v1/debug/beacon/states/{0}"
GET_BEACON_HEADS: Final = "/eth/v1/debug/beacon/heads"

# [ NODE endpoints ]

GET_NODE_IDENTITY: Final = "/eth/v1/node/identity"
GET_PEERS: Final = "/eth/v1/node/peers"
GET_PEER: Final = "/eth/v1/node/peers/{0}"
GET_PEER_COUNT: Final = "/eth/v1/node/peer_count"
GET_HEALTH: Final = "/eth/v1/node/health"
GET_VERSION: Final = "/eth/v1/node/version"
GET_SYNCING: Final = "/eth/v1/node/syncing"

# [ VALIDATOR endpoints ]

GET_ATTESTER_DUTIES: Final = "/eth/v1/validator/duties/attester/{0}"
GET_BLOCK_PROPOSERS_DUTIES: Final = "/eth/v1/validator/duties/proposer/{0}"
GET_SYNC_COMMITTEE_DUTIES: Final = "/eth/v1/validator/duties/sync/{0}"

# [ REWARDS endpoints ]
GET_ATTESTATIONS_REWARDS: Final = "/eth/v1/beacon/rewards/attestations/{0}"
