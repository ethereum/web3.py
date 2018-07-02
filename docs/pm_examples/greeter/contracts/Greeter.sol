pragma solidity ^0.4.24;

contract Greeter {
    bytes start = "Hello, ";
    bytes end = "!";

    string defaultResult = "Hello, Anonymous!";

    uint startLength = start.length;
    uint endLength = end.length;
    uint combinedLength = startLength + endLength;

    mapping (address => string) names;

    function setName(string _name) public {
        names[msg.sender] = _name;
    }

    function greet() public view returns (string) {
        bytes memory name = bytes(names[msg.sender]);
        uint nameLength = name.length;

        if(nameLength == 0) {
            return defaultResult;
        }

        bytes memory result = new bytes(combinedLength + nameLength);
        uint i;
        for(i = 0; i < startLength; i++) {
            result[i] = start[i];
        }
        uint j;
        for(j = 0; j < nameLength; j++) {
            result[i] = name[j];
            i++;
        }
        for(j = 0; j < endLength; j++) {
            result[i] = end[j];
            i++;
        }

        return string(result);
    }
}
