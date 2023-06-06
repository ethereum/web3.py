from pathlib import Path


ETHPM_DIR = Path(__file__).parent
ASSETS_DIR = ETHPM_DIR / "assets"


def get_ethpm_spec_dir() -> Path:
    ethpm_spec_dir = ETHPM_DIR / "ethpm-spec"
    v3_spec = ethpm_spec_dir / "spec" / "v3.spec.json"
    if not v3_spec.is_file():
        raise FileNotFoundError(
            "The ethpm-spec submodule is not available. "
            "Please import the submodule with `git submodule update --init`"
        )
    return ethpm_spec_dir


from .package import Package  # noqa: E402, F401
from .backends.registry import RegistryURI  # noqa: E402, F401
