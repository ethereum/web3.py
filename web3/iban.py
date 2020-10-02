import functools
import re
from typing import (
    Any,
    Callable,
    Union,
)

from eth_typing import (
    Address,
    ChecksumAddress,
)
from eth_utils import (
    is_string,
    to_checksum_address,
)

from web3._utils.compat import (
    TypedDict,
)
from web3._utils.validation import (
    validate_address,
)

IbanOptions = TypedDict("IbanOptions", {
    "institution": str,
    "identifier": str,
})


def pad_left_hex(value: str, num_bytes: int) -> str:
    return value.rjust(num_bytes * 2, '0')


def iso13616Prepare(iban: str) -> str:
    """
    Prepare an IBAN for mod 97 computation by moving the first
    4 chars to the end and transforming the letters to numbers
    (A = 10, B = 11, ..., Z = 35), as specified in ISO13616.

    @method iso13616Prepare
    @param {String} iban the IBAN
    @returns {String} the prepared IBAN
    """
    A = ord("A")
    Z = ord("Z")

    iban = iban.upper()
    iban = iban[4:] + iban[:4]

    def charfunc(n: str) -> str:
        code = ord(n)
        if code >= A and code <= Z:
            return str(code - A + 10)
        else:
            return str(n)

    return "".join(map(charfunc, list(iban)))


def mod9710(iban: str) -> int:
    """
    Calculates the MOD 97 10 of the passed IBAN as specified in ISO7064.

    @method mod9710
    @param {String} iban
    @returns {Number}
    """
    remainder = iban
    block = None

    while len(remainder) > 2:
        block = remainder[:9]
        remainder = str(int(block) % 97) + remainder[len(block):]

    return int(remainder) % 97


def baseN(num: int, b: int, numerals: str = "0123456789abcdefghijklmnopqrstuvwxyz") -> str:
    """
    This prototype should be used to create
    an iban object from iban correct string

    @param {String} iban
    """
    return ((num == 0) and numerals[0]) or \
        (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


class IsValid:
    """
    Should be called to check if iban is correct

    Note: This is implemented as a descriptor so that it can be called as
          either an instance method.

    @method isValid
    @returns {Boolean} true if it is, otherwise false
    """
    def __get__(self, instance: 'Iban', owner: str) -> Callable[[str], bool]:
        if instance is None:
            return self.validate
        return functools.partial(self.validate, instance._iban)

    @staticmethod
    def validate(iban_address: Any) -> bool:
        if not is_string(iban_address):
            return False

        if re.match(r"^XE[0-9]{2}(ETH[0-9A-Z]{13}|[0-9A-Z]{30,31})$", iban_address) and \
                mod9710(iso13616Prepare(iban_address)) == 1:
            return True

        return False


class Iban:
    def __init__(self, iban: str) -> None:
        self._iban = iban

    @staticmethod
    def fromAddress(address: Union[Address, ChecksumAddress]) -> "Iban":
        """
        This method should be used to create
        an iban object from ethereum address

        @method fromAddress
        @param {String} address
        @return {Iban} the IBAN object
        """
        validate_address(address)
        address_as_integer = int(address, 16)
        address_as_base36 = baseN(address_as_integer, 36)
        padded = pad_left_hex(address_as_base36, 15)
        return Iban.fromBban(padded.upper())

    @staticmethod
    def fromBban(bban: str) -> "Iban":
        """
        Convert the passed BBAN to an IBAN for this country specification.
        Please note that <i>"generation of the IBAN shall be the exclusive
        responsibility of the bank/branch servicing the account"</i>.
        This method implements the preferred algorithm described in
        http://en.wikipedia.org/wiki/International_Bank_Account_Number#Generating_IBAN_check_digits

        @method fromBban
        @param {String} bban the BBAN to convert to IBAN
        @returns {Iban} the IBAN object
        """
        countryCode = "XE"

        remainder = mod9710(iso13616Prepare(countryCode + "00" + bban))
        checkDigit = ("0" + str(98 - remainder))[-2:]

        return Iban(countryCode + checkDigit + bban)

    @staticmethod
    def createIndirect(options: IbanOptions) -> "Iban":
        """
        Should be used to create IBAN object for given institution and identifier

        @method createIndirect
        @param {Object} options, required options are "institution" and "identifier"
        @return {Iban} the IBAN object
        """
        return Iban.fromBban("ETH" + options["institution"] + options["identifier"])

    isValid = IsValid()

    def isDirect(self) -> bool:
        """
        Should be called to check if iban number is direct

        @method isDirect
        @returns {Boolean} true if it is, otherwise false
        """
        return len(self._iban) in [34, 35]

    def isIndirect(self) -> bool:
        """
        Should be called to check if iban number if indirect

        @method isIndirect
        @returns {Boolean} true if it is, otherwise false
        """
        return len(self._iban) == 20

    def checksum(self) -> str:
        """
        Should be called to get iban checksum
        Uses the mod-97-10 checksumming protocol (ISO/IEC 7064:2003)

        @method checksum
        @returns {String} checksum
        """
        return self._iban[2:4]

    def institution(self) -> str:
        """
        Should be called to get institution identifier
        eg. XREG

        @method institution
        @returns {String} institution identifier
        """
        if self.isIndirect():
            return self._iban[7:11]
        else:
            return ""

    def client(self) -> str:
        """
        Should be called to get client identifier within institution
        eg. GAVOFYORK

        @method client
        @returns {String} client identifier
        """
        if self.isIndirect():
            return self._iban[11:]
        else:
            return ""

    def address(self) -> Union[str, ChecksumAddress]:
        """
        Should be called to get client direct address

        @method address
        @returns {String} client direct address
        """
        if self.isDirect():
            base36 = self._iban[4:]
            asInt = int(base36, 36)
            return to_checksum_address(pad_left_hex(baseN(asInt, 16), 20))

        return ""

    def toString(self) -> str:
        return self._iban
