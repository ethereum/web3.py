
MATH_BYTECODE = (
    "606060405261022e806100126000396000f360606040523615610074576000357c01000000000000"
    "000000000000000000000000000000000000000000009004806316216f391461007657806361bc22"
    "1a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d5780"
    "63dcf537b11461014057610074565b005b610083600480505061016c565b60405180828152602001"
    "91505060405180910390f35b6100a6600480505061017f565b604051808281526020019150506040"
    "5180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191"
    "505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea"
    "565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b604051"
    "8082815260200191505060405180910390f35b610156600480803590602001909190505061021756"
    "5b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90"
    "565b60006000505481565b6000816000600082828250540192505081905550600060005054905080"
    "507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082"
    "815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090"
    "506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b600060078202"
    "90508050809050610229565b91905056"
)


MATH_ABI = [
    {
        "constant": False,
        "inputs": [],
        "name": "return13",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [],
        "name": "counter",
        "outputs": [
            {"name": "", "type": "uint256"},
        ],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "amt", "type": "uint256"},
        ],
        "name": "increment",
        "outputs": [
            {"name": "result", "type": "uint256"},
        ],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "int256"},
            {"name": "b", "type": "int256"},
        ],
        "name": "add",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [],
        "name": "increment",
        "outputs": [
            {"name": "", "type": "uint256"},
        ],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "a", "type": "int256"},
        ],
        "name": "multiply7",
        "outputs": [
            {"name": "result", "type": "int256"},
        ],
        "type": "function",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "value", "type": "uint256"},
        ],
        "name": "Increased",
        "type": "event",
    },
]

# The de-compiled math contract, for reference:
'''
contract Contract {
    function main() {
        memory[0x40:0x60] = 0x60;

        if (!msg.data.length) { stop(); }

        var var0 =
            msg.data[0x00:0x20] / 0x0100000000000000000000000000000000000000000000000000000000;

        if (var0 == 0x16216f39) {
            // Dispatch table entry for return13()
            var var1 = 0x0083;
            var1 = return13();
            var temp0 = memory[0x40:0x60];
            memory[temp0:temp0 + 0x20] = var1;
            var temp1 = memory[0x40:0x60];
            return memory[temp1:temp1 + (temp0 + 0x20) - temp1];
        } else if (var0 == 0x61bc221a) {
            // Dispatch table entry for counter()
            var1 = 0x00a6;
            var var2 = counter();
            var temp2 = memory[0x40:0x60];
            memory[temp2:temp2 + 0x20] = var2;
            var temp3 = memory[0x40:0x60];
            return memory[temp3:temp3 + (temp2 + 0x20) - temp3];
        } else if (var0 == 0x7cf5dab0) {
            // Dispatch table entry for increment(uint256)
            var1 = 0x00d2;
            var2 = msg.data[0x04:0x24];
            var1 = increment(var2);
            var temp4 = memory[0x40:0x60];
            memory[temp4:temp4 + 0x20] = var1;
            var temp5 = memory[0x40:0x60];
            return memory[temp5:temp5 + (temp4 + 0x20) - temp5];
        } else if (var0 == 0xa5f3c23b) {
            // Dispatch table entry for add(int256,int256)
            var1 = 0x0107;
            var2 = msg.data[0x04:0x24];
            var var3 = msg.data[0x24:0x44];
            var1 = add(var2, var3);
            var temp6 = memory[0x40:0x60];
            memory[temp6:temp6 + 0x20] = var1;
            var temp7 = memory[0x40:0x60];
            return memory[temp7:temp7 + (temp6 + 0x20) - temp7];
        } else if (var0 == 0xd09de08a) {
            // Dispatch table entry for increment()
            var1 = 0x012a;
            var1 = increment();
            var temp8 = memory[0x40:0x60];
            memory[temp8:temp8 + 0x20] = var1;
            var temp9 = memory[0x40:0x60];
            return memory[temp9:temp9 + (temp8 + 0x20) - temp9];
        } else if (var0 == 0xdcf537b1) {
            // Dispatch table entry for multiply7(int256)
            var1 = 0x0156;
            var2 = msg.data[0x04:0x24];
            var1 = multiply7(var2);
            var temp10 = memory[0x40:0x60];
            memory[temp10:temp10 + 0x20] = var1;
            var temp11 = memory[0x40:0x60];
            return memory[temp11:temp11 + (temp10 + 0x20) - temp11];
        } else { stop(); }
    }

    function return13() returns (var r0) {
        var var0 = 0x0d;
        return var0;
    }

    function counter() returns (var r0) { return storage[0x00]; }

    function increment(var arg0) returns (var r0) {
        storage[0x00] = storage[0x00] + arg0;
        var temp0 = memory[0x40:0x60];
        memory[temp0:temp0 + 0x20] = storage[0x00];
        var temp1 = memory[0x40:0x60];
        log(memory[temp1:temp1 + (temp0 + 0x20) - temp1],
            [0x3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5]);
        var var0 = storage[0x00];
        return var0;}

    function add(var arg0, var arg1) returns (var r0) {
        var var0 = arg0 + arg1;
        return var0;
    }

    function increment() returns (var r0) {
        var var0 = 0x00;
        var var1 = 0x020d;
        var var2 = 0x01;
        return increment(var2);
    }

    function multiply7(var arg0) returns (var r0) {
        var var0 = arg0 * 0x07;
        return var0;
    }
}
'''
