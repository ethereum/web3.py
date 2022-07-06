from typing import (
    Any,
    Dict,
    ItemsView,
    List,
)

from eth_typing import (
    Address,
    HexStr,
)

from ethpm.validation.package import (
    validate_contract_name,
)
from web3._utils.compat import (
    TypedDict,
)
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
    ) -> None:
        self.deployment_data = deployment_data
        self.contract_instances = contract_instances

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

    def get_instance(self, contract_name: str) -> Contract:
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
                "Available deployments include: "
                f"{list(sorted(self.deployment_data.keys()))}."
            )


class DeploymentData(TypedDict):
    address: Address
    transaction: HexStr
    block: HexStr
    runtime_bytecode: Dict[str, Any]
    compiler: Dict[str, str]
    contractType: str
