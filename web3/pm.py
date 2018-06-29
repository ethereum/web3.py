from web3.module import (
    Module,
)

try:
    from ethpm import (
        Package,
    )
except ImportError as exc:
    raise Exception(
        "To use the (alpha) ethpm package, you must install it explicitly. "
        "Install with `pip install --upgrade ethpm`."
    ) from exc


# Package Management is currently still in alpha
# It is not automatically available on a web3 object.
# To use the `PM` module, attach it to your web3 object
# i.e. PM.attach(web3, 'pm')
class PM(Module):
    def get_package_from_manifest(self, manifest):
        pkg = Package(manifest)
        return pkg
