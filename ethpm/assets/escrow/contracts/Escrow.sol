pragma solidity ^0.4.24;


import {SafeSendLib} from "./SafeSendLib.sol";


/// @title Contract for holding funds in escrow between two semi trusted parties.
/// @author Piper Merriam <pipermerriam@gmail.com>
contract Escrow {
    using SafeSendLib for address;

    address public sender;
    address public recipient;

    constructor(address _recipient) public payable {
        sender = msg.sender;
        recipient = _recipient;
    }

    /// @dev Releases the escrowed funds to the other party.
    /// @notice This will release the escrowed funds to the other party.
    function releaseFunds() public {
        if (msg.sender == sender) {
            recipient.sendOrThrow(address(this).balance);
        } else if (msg.sender == recipient) {
            sender.sendOrThrow(address(this).balance);
        } else {
            revert();
        }
    }
}
