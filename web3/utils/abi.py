# ABI call formatters


def transformToFullName(jsn):
    """
    Should be used to create full function/event name from json abi
    """
    if jsn["name"].find("(") != -1:
        return jsn["name"]

    typeName = ",".join([i["type"] for i in jsn["inputs"]])
    return jsn["name"] + "(" + typeName + ")"


def extractDisplayName(name):
    """
    Should be called to get display name of contract function
    """
    length = name.find("(")
    return name[:length] if length != -1 else name


def extractTypeName(name):
    """
    Returns overloaded part of function/event name
    """
    length = name.find("(")
    return name[length + 1:len(name) - 1].replace(" ", "") if length != -1 else ""
