from typing import (
    Dict,
    ItemsView,
    List,
)

from ethpm.validation.package import (
    validate_contract_name,
)
from web3 import Web3
from web3.eth import (
    Contract,
)


class Deployments:
    """
    Deployment object to access instances of
    deployed contracts belonging to a package.
    """

    def __init__(
        self,
        deployment_data: Dict[str, Dict[str, str]],
        contract_instances: Dict[str, Contract],
        w3: Web3,
    ) -> None:
        self.deployment_data = deployment_data
        self.contract_instances = contract_instances
        self.w3 = w3

    def __getitem__(self, key: str) -> Dict[str, str]:
        return self.get(key)

    def __contains__(self, key: str) -> bool:
        return key in self.deployment_data

    def get(self, key: str) -> Dict[str, str]:
        self._validate_name_and_references(key)
        return self.deployment_data[key]

    def items(self) -> ItemsView[str, Dict[str, str]]:
        item_dict = {name: self.get(name) for name in self.deployment_data}
        return item_dict.items()

    def values(self) -> List[Dict[str, str]]:
        values = [self.get(name) for name in self.deployment_data]
        return values

    def get_instance(self, contract_name: str) -> None:
        """
        Fetches a contract instance belonging to deployment
        after validating contract name.
        """
        self._validate_name_and_references(contract_name)
        return self.contract_instances[contract_name]

    def _validate_name_and_references(self, name: str) -> None:
        validate_contract_name(name)
        if name not in self.deployment_data:
            raise KeyError(
                f"Contract deployment: {name} not found in deployment data. "
                f"Available deployments include: {list(sorted(self.deployment_data.keys()))}."
            )
