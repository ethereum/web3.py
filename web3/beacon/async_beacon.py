from typing import (
    Any,
    Dict,
)

from eth_typing import (
    URI,
)

from web3._utils.request import (
    async_get_response_from_get_request,
    async_json_make_get_request,
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


class AsyncBeacon:
    is_async = True

    def __init__(
        self,
        base_url: str,
    ) -> None:
        self.base_url = base_url

    async def _async_make_get_request(self, endpoint_uri: str) -> Dict[str, Any]:
        uri = URI(self.base_url + endpoint_uri)
        return await async_json_make_get_request(uri)

    # [ BEACON endpoints ]

    async def get_genesis(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_GENESIS)

    async def get_hash_root(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(GET_HASH_ROOT.format(state_id))

    async def get_fork_data(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(GET_FORK_DATA.format(state_id))

    async def get_finality_checkpoint(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(
            GET_FINALITY_CHECKPOINT.format(state_id)
        )

    async def get_validators(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(GET_VALIDATORS.format(state_id))

    async def get_validator(
        self, validator_id: str, state_id: str = "head"
    ) -> Dict[str, Any]:
        return await self._async_make_get_request(
            GET_VALIDATOR.format(state_id, validator_id)
        )

    async def get_validator_balances(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(
            GET_VALIDATOR_BALANCES.format(state_id)
        )

    async def get_epoch_committees(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(GET_EPOCH_COMMITTEES.format(state_id))

    async def get_block_headers(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BLOCK_HEADERS)

    async def get_block_header(self, block_id: str) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BLOCK_HEADER.format(block_id))

    async def get_block(self, block_id: str) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BLOCK.format(block_id))

    async def get_block_root(self, block_id: str) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BLOCK_ROOT.format(block_id))

    async def get_block_attestations(self, block_id: str) -> Dict[str, Any]:
        return await self._async_make_get_request(
            GET_BLOCK_ATTESTATIONS.format(block_id)
        )

    async def get_attestations(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_ATTESTATIONS)

    async def get_attester_slashings(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_ATTESTER_SLASHINGS)

    async def get_proposer_slashings(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_PROPOSER_SLASHINGS)

    async def get_voluntary_exits(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_VOLUNTARY_EXITS)

    # [ CONFIG endpoints ]

    async def get_fork_schedule(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_FORK_SCHEDULE)

    async def get_spec(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_SPEC)

    async def get_deposit_contract(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_DEPOSIT_CONTRACT)

    # [ DEBUG endpoints ]

    async def get_beacon_state(self, state_id: str = "head") -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BEACON_STATE.format(state_id))

    async def get_beacon_heads(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_BEACON_HEADS)

    # [ NODE endpoints ]

    async def get_node_identity(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_NODE_IDENTITY)

    async def get_peers(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_PEERS)

    async def get_peer(self, peer_id: str) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_PEER.format(peer_id))

    async def get_health(self) -> int:
        url = URI(self.base_url + GET_HEALTH)
        response = await async_get_response_from_get_request(url)
        return response.status

    async def get_version(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_VERSION)

    async def get_syncing(self) -> Dict[str, Any]:
        return await self._async_make_get_request(GET_SYNCING)
