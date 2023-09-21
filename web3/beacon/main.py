from typing import (
    Any,
    Dict,
)

from eth_typing import (
    URI,
    HexStr,
)

from web3._utils.request import (
    get_response_from_get_request,
    json_make_get_request,
)
from web3.beacon.api_endpoints import (
    GET_ATTESTATIONS,
    GET_ATTESTER_SLASHINGS,
    GET_BEACON_HEADS,
    GET_BEACON_STATE,
    GET_BLINDED_BLOCKS,
    GET_BLOCK,
    GET_BLOCK_ATTESTATIONS,
    GET_BLOCK_HEADER,
    GET_BLOCK_HEADERS,
    GET_BLOCK_ROOT,
    GET_BLS_TO_EXECUTION_CHANGES,
    GET_DEPOSIT_CONTRACT,
    GET_EPOCH_COMMITTEES,
    GET_EPOCH_RANDAO,
    GET_EPOCH_SYNC_COMMITTEES,
    GET_FINALITY_CHECKPOINT,
    GET_FORK_DATA,
    GET_FORK_SCHEDULE,
    GET_GENESIS,
    GET_HASH_ROOT,
    GET_HEALTH,
    GET_LIGHT_CLIENT_BOOTSTRAP_STRUCTURE,
    GET_LIGHT_CLIENT_FINALITY_UPDATE,
    GET_LIGHT_CLIENT_OPTIMISTIC_UPDATE,
    GET_LIGHT_CLIENT_UPDATES,
    GET_NODE_IDENTITY,
    GET_PEER,
    GET_PEERS,
    GET_PROPOSER_SLASHINGS,
    GET_REWARDS,
    GET_SPEC,
    GET_SYNCING,
    GET_VALIDATOR,
    GET_VALIDATOR_BALANCES,
    GET_VALIDATORS,
    GET_VERSION,
    GET_VOLUNTARY_EXITS,
)


class Beacon:
    def __init__(
        self,
        base_url: str,
        request_timeout: float = 10.0,
    ) -> None:
        self.base_url = base_url
        self.request_timeout = request_timeout

    def _make_get_request(self, endpoint_url: str) -> Dict[str, Any]:
        uri = URI(self.base_url + endpoint_url)
        return json_make_get_request(uri, timeout=self.request_timeout)

    # [ BEACON endpoints ]

    # states

    def get_genesis(self) -> Dict[str, Any]:
        return self._make_get_request(GET_GENESIS)

    def get_hash_root(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_HASH_ROOT.format(state_id))

    def get_fork_data(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_FORK_DATA.format(state_id))

    def get_finality_checkpoint(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_FINALITY_CHECKPOINT.format(state_id))

    def get_validators(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_VALIDATORS.format(state_id))

    def get_validator(
        self, validator_id: str, state_id: str = "head"
    ) -> Dict[str, Any]:
        return self._make_get_request(GET_VALIDATOR.format(state_id, validator_id))

    def get_validator_balances(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_VALIDATOR_BALANCES.format(state_id))

    def get_epoch_committees(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_EPOCH_COMMITTEES.format(state_id))

    def get_epoch_sync_committees(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_EPOCH_SYNC_COMMITTEES.format(state_id))

    def get_epoch_randao(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_EPOCH_RANDAO.format(state_id))

    # headers

    def get_block_headers(self) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_HEADERS)

    def get_block_header(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_HEADER.format(block_id))

    # blocks

    def get_block(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK.format(block_id))

    def get_block_root(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_ROOT.format(block_id))

    def get_block_attestations(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_ATTESTATIONS.format(block_id))

    def get_blinded_blocks(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLINDED_BLOCKS.format(block_id))

    # rewards

    def get_rewards(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_REWARDS.format(block_id))

    # light client (untested but follows spec)

    def get_light_client_bootstrap_structure(
        self, block_root: HexStr
    ) -> Dict[str, Any]:
        return self._make_get_request(
            GET_LIGHT_CLIENT_BOOTSTRAP_STRUCTURE.format(block_root)
        )

    def get_light_client_updates(self) -> Dict[str, Any]:
        return self._make_get_request(GET_LIGHT_CLIENT_UPDATES)

    def get_light_client_finality_update(self) -> Dict[str, Any]:
        return self._make_get_request(GET_LIGHT_CLIENT_FINALITY_UPDATE)

    def get_light_client_optimistic_update(self) -> Dict[str, Any]:
        return self._make_get_request(GET_LIGHT_CLIENT_OPTIMISTIC_UPDATE)

    # pool

    def get_attestations(self) -> Dict[str, Any]:
        return self._make_get_request(GET_ATTESTATIONS)

    def get_attester_slashings(self) -> Dict[str, Any]:
        return self._make_get_request(GET_ATTESTER_SLASHINGS)

    def get_proposer_slashings(self) -> Dict[str, Any]:
        return self._make_get_request(GET_PROPOSER_SLASHINGS)

    def get_voluntary_exits(self) -> Dict[str, Any]:
        return self._make_get_request(GET_VOLUNTARY_EXITS)

    def get_bls_to_execution_changes(self) -> Dict[str, Any]:
        return self._make_get_request(GET_BLS_TO_EXECUTION_CHANGES)

    # [ CONFIG endpoints ]

    def get_fork_schedule(self) -> Dict[str, Any]:
        return self._make_get_request(GET_FORK_SCHEDULE)

    def get_spec(self) -> Dict[str, Any]:
        return self._make_get_request(GET_SPEC)

    def get_deposit_contract(self) -> Dict[str, Any]:
        return self._make_get_request(GET_DEPOSIT_CONTRACT)

    # [ DEBUG endpoints ]

    def get_beacon_state(self, state_id: str = "head") -> Dict[str, Any]:
        return self._make_get_request(GET_BEACON_STATE.format(state_id))

    def get_beacon_heads(self) -> Dict[str, Any]:
        return self._make_get_request(GET_BEACON_HEADS)

    # [ NODE endpoints ]

    def get_node_identity(self) -> Dict[str, Any]:
        return self._make_get_request(GET_NODE_IDENTITY)

    def get_peers(self) -> Dict[str, Any]:
        return self._make_get_request(GET_PEERS)

    def get_peer(self, peer_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_PEER.format(peer_id))

    def get_health(self) -> int:
        url = URI(self.base_url + GET_HEALTH)
        response = get_response_from_get_request(url)
        return response.status_code

    def get_version(self) -> Dict[str, Any]:
        return self._make_get_request(GET_VERSION)

    def get_syncing(self) -> Dict[str, Any]:
        return self._make_get_request(GET_SYNCING)
