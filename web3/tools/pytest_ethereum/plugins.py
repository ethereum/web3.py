import json
from pathlib import (
    Path,
)
import pytest
from typing import (
    Callable,
)

from ethpm import (
    Package,
)
from web3 import Web3
from web3.tools.pytest_ethereum.deployer import (
    Deployer,
)


@pytest.fixture
def deployer(w3: Web3) -> Callable[[Path], Deployer]:
    """
    Returns a `Deployer` instance composed from a `Package` instance
    generated from the manifest located at the provided `path` folder.
    """

    def _deployer(path: Path) -> Deployer:
        manifest = json.loads(path.read_text())
        package = Package(manifest, w3)
        return Deployer(package)

    return _deployer
