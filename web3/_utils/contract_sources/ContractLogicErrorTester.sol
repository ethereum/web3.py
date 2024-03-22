// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

contract MeasPub {
    address public publisher;
    string public description;
    uint public price_per_second; // wei per second

    mapping (address => uint) private balances;
    mapping (address => uint) private last_publish_block;
    mapping (uint => address) private subscriber_index;
    uint private subscriber_count;
    mapping (address => string) private subscriber_pubkey;

    event LogPublished(address indexed _subscriber, bytes _pwdenc, bytes _ipfsaddr, uint _cost);
    event LogDebug(string _msg);

    constructor() {
        publisher = msg.sender;
        price_per_second = 0; // Wei
    }

    function setPricePerSecond(uint _price) public {
        if (msg.sender == publisher) {
            price_per_second = _price;
        }
    }

    function publish(address _subscriber, bytes memory _pwdenc, bytes memory _ipfsaddr) public returns (bool covered) {
        if (msg.sender != publisher) {
            emit LogDebug("only publisher can publish");
            return false;
        }
        uint cost = (block.timestamp - last_publish_block[_subscriber]) * price_per_second;
        if (balances[_subscriber] < cost) {
            emit LogDebug("subscriber has insufficient funds");
            return false;
        }
        balances[_subscriber] -= cost;
        payable(publisher).transfer(cost);
        last_publish_block[_subscriber] = block.timestamp;
        emit LogPublished(_subscriber, _pwdenc, _ipfsaddr, cost);
        return true;
    }

    function getSubscriberCount() public view returns (uint count) {
        return subscriber_count;
    }

    function getSubscriber(uint _index) public view returns (address _subscriber, string memory _pubkey) {
        if (msg.sender != publisher) return (address(0), "");
        return (subscriber_index[_index], subscriber_pubkey[subscriber_index[_index]]);
    }

    function subscribe(string memory _pubkey) public payable returns (bool success) {
        if (last_publish_block[msg.sender] != 0) return false;
        last_publish_block[msg.sender] = block.timestamp;
        subscriber_index[subscriber_count] = msg.sender;
        subscriber_count += 1;
        subscriber_pubkey[msg.sender] = _pubkey;
        balances[msg.sender] += msg.value;
        emit LogDebug("new subscription successful");
        return true;
    }

    function kill() public {
        if (msg.sender == publisher) selfdestruct(payable(publisher));
    }
}
