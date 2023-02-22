from typing import (
    Any,
    Callable,
    Dict,
)

from eth_typing import (
    ContractName,
)

from ethpm import (
    Package,
)
from web3.tools.pytest_ethereum.exceptions import (
    DeployerError,
)
from web3.tools.pytest_ethereum.linker import (
    deploy,
    linker,
)


class Deployer:
    def __init__(self, package: Package) -> None:
        if not isinstance(package, Package):
            raise TypeError(
                f"Expected a Package object, instead received {type(package)}."
            )
        self.package = package
        self.strategies = {}  # type: Dict[str, Callable[[Package], Package]]

    def deploy(self, contract_type: ContractName, *args: Any, **kwargs: Any) -> Package:
        factory = self.package.get_contract_factory(contract_type)
        if contract_type in self.strategies:
            strategy = self.strategies[contract_type]
            return strategy(self.package)
        if factory.needs_bytecode_linking:
            raise DeployerError(
                "Unable to deploy an unlinked factory. "
                "Please register a strategy for this contract type."
            )
        strategy = linker(deploy(contract_type, *args, **kwargs))
        return strategy(self.package)

    def register_strategy(
        self, contract_type: ContractName, strategy: Callable[[Package], Package]
    ) -> None:
        self.strategies[contract_type] = strategy
