from typing import (
    Any,
    Dict,
)

import requests

from web3.module import (
    Module,
)


class Beacon(Module):
    def __init__(
        self,
        base_url: str,
        session: requests.Session = requests.Session(),
    ) -> None:
        self.base_url = base_url
        self.session = session

    def _make_get_request(self, endpoint: str) -> Dict[str, Any]:
        url = self.base_url + endpoint
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    # [ BEACON endpoints ]

    def get_genesis(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/genesis"
        return self._make_get_request(endpoint)

    def get_hash_root(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/root"
        return self._make_get_request(endpoint)

    def get_fork_data(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/fork"
        return self._make_get_request(endpoint)

    def get_finality_checkpoint(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/finality_checkpoints"
        return self._make_get_request(endpoint)

    def get_validators(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/validators"
        return self._make_get_request(endpoint)

    def get_validator(
        self, validator_id: str, state_id: str = "head"
    ) -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/validators/{validator_id}"
        return self._make_get_request(endpoint)

    def get_validator_balances(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/validator_balances"
        return self._make_get_request(endpoint)

    def get_epoch_committees(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/states/{state_id}/committees"
        return self._make_get_request(endpoint)

    def get_block_headers(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/headers"
        return self._make_get_request(endpoint)

    def get_block_header(self, block_id: str) -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/headers/{block_id}"
        return self._make_get_request(endpoint)

    def get_block(self, block_id: str) -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/blocks/{block_id}"
        return self._make_get_request(endpoint)

    def get_block_root(self, block_id: str) -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/blocks/{block_id}/root"
        return self._make_get_request(endpoint)

    def get_block_attestations(self, block_id: str) -> Dict[str, Any]:
        endpoint = f"/eth/v1/beacon/blocks/{block_id}/attestations"
        return self._make_get_request(endpoint)

    def get_attestations(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/pool/attestations"
        return self._make_get_request(endpoint)

    def get_attester_slashings(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/pool/attester_slashings"
        return self._make_get_request(endpoint)

    def get_proposer_slashings(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/pool/proposer_slashings"
        return self._make_get_request(endpoint)

    def get_voluntary_exits(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/beacon/pool/voluntary_exits"
        return self._make_get_request(endpoint)

    # [ CONFIG endpoints ]

    def get_fork_schedule(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/config/fork_schedule"
        return self._make_get_request(endpoint)

    def get_spec(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/config/spec"
        return self._make_get_request(endpoint)

    def get_deposit_contract(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/config/deposit_contract"
        return self._make_get_request(endpoint)

    # [ DEBUG endpoints ]

    def get_beacon_state(self, state_id: str = "head") -> Dict[str, Any]:
        endpoint = f"/eth/v1/debug/beacon/states/{state_id}"
        return self._make_get_request(endpoint)

    def get_beacon_heads(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/debug/beacon/heads"
        return self._make_get_request(endpoint)

    # [ NODE endpoints ]

    def get_node_identity(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/node/identity"
        return self._make_get_request(endpoint)

    def get_peers(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/node/peers"
        return self._make_get_request(endpoint)

    def get_peer(self, peer_id: str) -> Dict[str, Any]:
        endpoint = f"/eth/v1/node/peers/{peer_id}"
        return self._make_get_request(endpoint)

    def get_health(self) -> int:
        endpoint = "/eth/v1/node/health"
        url = self.base_url + endpoint
        response = self.session.get(url)
        return response.status_code

    def get_version(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/node/version"
        return self._make_get_request(endpoint)

    def get_syncing(self) -> Dict[str, Any]:
        endpoint = "/eth/v1/node/syncing"
        return self._make_get_request(endpoint)
