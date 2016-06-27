from web3.utils import utils


class SolidityParam(object):

    def __init__(self, value="", offset=None):
        self.value = value
        self.offset = offset

    def dynamicPartLength(self):
        return len(self.dynamicPart()) // 2

    def withOffset(self, offset):
        return SolidityParam(self.value, offset)

    def combine(self, param):
        return SolidityParam(self.value + param.value)

    def isDynamic(self):
        return self.offset is not None

    def offsetAsBytes(self):
        if not self.isDynamic():
            return b""
        else:
            return utils.padLeft(utils.toTwosComplement(self.offset).toString(16), 64)  # toHex

    def staticPart(self):
        if not self.isDynamic():
            return self.value
        return self.offsetAsBytes()

    def dynamicPart(self):
        return self.value if self.isDynamic() else b""

    def encode(self):
        return self.staticPart() + self.dynamicPart()

    def encodeList(self, params):
        totalOffset = len(params) * 32

        def mapf(param):
            if not param.isDynamic():
                return param
            offset = totalOffset
            totalOffset += param.dynamicPartLength()  # NOQA
            return param.withOffset(offset)

        offsetParams = [mapf(p) for p in params]

        # Encode everything!
        result = b""
        for param in offsetParams:
            result += param.staticPart()
        for param in offsetParams:
            result += param.dynamicPart()

        return result
