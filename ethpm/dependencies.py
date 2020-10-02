from typing import (
    Dict,
    List,
    Tuple,
)

from ethpm.validation.package import (
    validate_package_name,
)


class Dependencies:
    """
    Class to manage the `Package` instances of a Package's `buildDependencies`.
    """

    # ignoring Package type here and below to avoid a circular dependency
    def __init__(
        self, build_dependencies: Dict[str, "Package"]  # type: ignore  # noqa: F821
    ) -> None:
        self.build_dependencies = build_dependencies

    def __getitem__(self, key: str) -> "Package":  # type: ignore  # noqa: F821
        return self.build_dependencies.get(key)

    def __contains__(self, key: str) -> bool:
        return key in self.build_dependencies

    def _validate_name(self, name: str) -> None:
        validate_package_name(name)
        if name not in self.build_dependencies:
            raise KeyError(f"Package name: {name} not found in build dependencies.")

    def items(self) -> Tuple[Tuple[str, "Package"], ...]:  # type: ignore  # noqa: F821
        """
        Return an iterable containing package name and
        corresponding `Package` instance that are available.
        """
        item_dict = {
            name: self.build_dependencies.get(name) for name in self.build_dependencies
        }
        return tuple(item_dict.items())

    def values(self) -> List["Package"]:  # type: ignore  # noqa: F821
        """
        Return an iterable of the available `Package` instances.
        """
        values = [self.build_dependencies.get(name) for name in self.build_dependencies]
        return values

    def get_dependency_package(
        self, package_name: str
    ) -> "Package":  # type: ignore # noqa: F821
        """
        Return the dependency Package for a given package name.
        """
        self._validate_name(package_name)
        return self.build_dependencies.get(package_name)
