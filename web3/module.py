class Module:
    web3 = None

    def __init__(self, web3):
        self.web3 = web3

    @classmethod
    def attach(cls, target, module_name=None):
        if not module_name:
            module_name = cls.__name__.lower()

        if hasattr(target, module_name):
            raise AttributeError(
                "Cannot set {0} module named '{1}'.  The web3 object "
                "already has an attribute with that name".format(
                    target,
                    module_name,
                )
            )

        if isinstance(target, Module):
            web3 = target.web3
        else:
            web3 = target

        setattr(target, module_name, cls(web3))
