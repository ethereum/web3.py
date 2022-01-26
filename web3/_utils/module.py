from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Optional,
    Sequence,
    Union,
)

from web3.exceptions import (
    ValidationError,
)
from web3.module import (
    Module,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def attach_modules(
    parent_module: Union["Web3", "Module"],
    module_definitions: Dict[str, Any],
    w3: Optional[Union["Web3", "Module"]] = None
) -> None:
    for module_name, module_info in module_definitions.items():
        module_info_is_list_like = isinstance(module_info, Sequence)

        module_class = module_info[0] if module_info_is_list_like else module_info

        if hasattr(parent_module, module_name):
            raise AttributeError(
                f"Cannot set {parent_module} module named '{module_name}'.  The web3 object "
                "already has an attribute with that name"
            )

        if issubclass(module_class, Module):
            # If the `module_class` inherits from the `web3.module.Module` class, it has access to
            # caller functions internal to the web3.py library and sets up a proper codec. This
            # is likely important for all modules internal to the library.
            if w3 is None:
                setattr(parent_module, module_name, module_class(parent_module))
                w3 = parent_module
            else:
                setattr(parent_module, module_name, module_class(w3))
        else:
            # An external `module_class` need not inherit from the `web3.module.Module` class.
            setattr(parent_module, module_name, module_class)

        if module_info_is_list_like:
            if len(module_info) == 2:
                submodule_definitions = module_info[1]
                module = getattr(parent_module, module_name)
                attach_modules(module, submodule_definitions, w3)
            elif len(module_info) != 1:
                raise ValidationError("Module definitions can only have 1 or 2 elements.")
