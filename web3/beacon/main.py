from typing import (
    Any,
    Dict,
)

from eth_typing import (
    URI,
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
    GET_BLOCK,
    GET_BLOCK_ATTESTATIONS,
    GET_BLOCK_HEADER,
    GET_BLOCK_HEADERS,
    GET_BLOCK_ROOT,
    GET_DEPOSIT_CONTRACT,
    GET_EPOCH_COMMITTEES,
    GET_FINALITY_CHECKPOINT,
    GET_FORK_DATA,
    GET_FORK_SCHEDULE,
    GET_GENESIS,
    GET_HASH_ROOT,
    GET_HEALTH,
    GET_NODE_IDENTITY,
    GET_PEER,
    GET_PEERS,
    GET_PROPOSER_SLASHINGS,
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
    ) -> None:
        self.base_url = base_url

    def _make_get_request(self, endpoint_url: str) -> Dict[str, Any]:
        uri = URI(self.base_url + endpoint_url)
        return json_make_get_request(uri)

    # [ BEACON endpoints ]

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

    def get_block_headers(self) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_HEADERS)

    def get_block_header(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_HEADER.format(block_id))

    def get_block(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK.format(block_id))

    def get_block_root(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_ROOT.format(block_id))

    def get_block_attestations(self, block_id: str) -> Dict[str, Any]:
        return self._make_get_request(GET_BLOCK_ATTESTATIONS.format(block_id))

    def get_attestations(self) -> Dict[str, Any]:
        return self._make_get_request(GET_ATTESTATIONS)

    def get_attester_slashings(self) -> Dict[str, Any]:
        return self._make_get_request(GET_ATTESTER_SLASHINGS)

    def get_proposer_slashings(self) -> Dict[str, Any]:
        return self._make_get_request(GET_PROPOSER_SLASHINGS)

    def get_voluntary_exits(self) -> Dict[str, Any]:
        return self._make_get_request(GET_VOLUNTARY_EXITS)

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
