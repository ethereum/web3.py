import web3.utils.utils as utils

class Property(object):

    def __init__(self, options):
        self.name = options.get("name")
        self.getter = options.get("getter")
        self.setter = options.get("setter")
        self.inputFormatter = options.get("inputFormatter")
        self.outputFormatter = options.get("outputFormatter")
        self.requestManager = None

    def setRequestManager(self, rm):
        self.requestManager = rm

    def formatInput(self, arg):
        """
        Should be called to format input args of method
        """
        return self.inputFormatter(arg) if self.inputFormatter else arg

    def formatOutput(self, result):
        """
        Should be called to format output(result) of method
        """
        return self.outputFormatter(result) if result and self.outputFormatter else result

    def attachToObject(self, obj):
        names = self.name.split(".")
        name = names[0]
        if len(names) > 1:
            if not getattr(obj, names[0]):
                setattr(obj, names[0], object())
            obj = getattr(obj, names[0])
            name = names[1]
        setattr(obj, asyncGetterName(name), self.buildGet())

    def asyncGetterName(self, name):
        return "get" + name[0].upper() + name[1:]

    def buildGet():
        def get(*arguments):
            return self.formatOutput(self.requestManager.send(
                {
                "method": self.getter
                },
                *arguments
                ))
        return get

    def request():
        payload = {
            "method": self.getter,
            "params": [],
        }
        payload["format"] = self.formatOutput(self)
        return payload