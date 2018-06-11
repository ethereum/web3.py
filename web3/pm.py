from typing import (
    Any,
    Dict,
)

from ethpm import Package

from web3.module import Module


class PM(Module):
    def get_package(self, manifest: Dict[str, Any]) -> Package:
        pkg = Package(manifest)
        return pkg
