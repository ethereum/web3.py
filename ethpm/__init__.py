from pathlib import Path


ETHPM_DIR = Path(__file__).parent
ASSETS_DIR = ETHPM_DIR / "assets"
SPEC_DIR: Path = ASSETS_DIR / "spec"
ETHPM_SPEC_DIR = ETHPM_DIR.parent / "ethpm-spec"

from .package import Package  # noqa: F401
from .backends.registry import RegistryURI  # noqa: F401
