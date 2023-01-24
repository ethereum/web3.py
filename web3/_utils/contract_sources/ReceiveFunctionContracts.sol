pragma solidity >=0.6.0;


contract ReceiveFunctionContract {
    string text;

    fallback() external payable {
        text = 'fallback';
    }

    receive() external payable {
        text = 'receive';
    }

    function getText() public view returns (string memory) {
        return text;
    }

    function setText(string memory new_text) public returns (string memory) {
        return text = new_text;
    }
}

contract NoReceiveFunctionContract {
    string text;

    fallback() external {
        text = 'fallback';
    }

    function getText() public view returns (string memory) {
        return text;
    }

    function setText(string memory new_text) public returns (string memory) {
        return text = new_text;
    }
}
