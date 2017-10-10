# flake8: noqa

ENS = [
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "resolver",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "owner",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "label",
        "type": "bytes32"
      },
      {
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "setSubnodeOwner",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "ttl",
        "type": "uint64"
      }
    ],
    "name": "setTTL",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "ttl",
    "outputs": [
      {
        "name": "",
        "type": "uint64"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "resolver",
        "type": "address"
      }
    ],
    "name": "setResolver",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "setOwner",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "label",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "NewOwner",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "resolver",
        "type": "address"
      }
    ],
    "name": "NewResolver",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "ttl",
        "type": "uint64"
      }
    ],
    "name": "NewTTL",
    "type": "event"
  }
]

AUCTION_REGISTRAR = [
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "releaseDeed",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "getAllowedTime",
    "outputs": [
      {
        "name": "timestamp",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "unhashedName",
        "type": "string"
      }
    ],
    "name": "invalidateName",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "hash",
        "type": "bytes32"
      },
      {
        "name": "owner",
        "type": "address"
      },
      {
        "name": "value",
        "type": "uint256"
      },
      {
        "name": "salt",
        "type": "bytes32"
      }
    ],
    "name": "shaBid",
    "outputs": [
      {
        "name": "sealedBid",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "bidder",
        "type": "address"
      },
      {
        "name": "seal",
        "type": "bytes32"
      }
    ],
    "name": "cancelBid",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "entries",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      },
      {
        "name": "",
        "type": "address"
      },
      {
        "name": "",
        "type": "uint256"
      },
      {
        "name": "",
        "type": "uint256"
      },
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "ens",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      },
      {
        "name": "_value",
        "type": "uint256"
      },
      {
        "name": "_salt",
        "type": "bytes32"
      }
    ],
    "name": "unsealBid",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "transferRegistrars",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "",
        "type": "address"
      },
      {
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "sealedBids",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "state",
    "outputs": [
      {
        "name": "",
        "type": "uint8"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      },
      {
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transfer",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      },
      {
        "name": "_timestamp",
        "type": "uint256"
      }
    ],
    "name": "isAllowed",
    "outputs": [
      {
        "name": "allowed",
        "type": "bool"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "finalizeAuction",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "registryStarted",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "launchLength",
    "outputs": [
      {
        "name": "",
        "type": "uint32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "sealedBid",
        "type": "bytes32"
      }
    ],
    "name": "newBid",
    "outputs": [],
    "payable": True,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "labels",
        "type": "bytes32[]"
      }
    ],
    "name": "eraseNode",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hashes",
        "type": "bytes32[]"
      }
    ],
    "name": "startAuctions",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "hash",
        "type": "bytes32"
      },
      {
        "name": "deed",
        "type": "address"
      },
      {
        "name": "registrationDate",
        "type": "uint256"
      }
    ],
    "name": "acceptRegistrarTransfer",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "_hash",
        "type": "bytes32"
      }
    ],
    "name": "startAuction",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "rootNode",
    "outputs": [
      {
        "name": "",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "hashes",
        "type": "bytes32[]"
      },
      {
        "name": "sealedBid",
        "type": "bytes32"
      }
    ],
    "name": "startAuctionsAndBid",
    "outputs": [],
    "payable": True,
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "_ens",
        "type": "address"
      },
      {
        "name": "_rootNode",
        "type": "bytes32"
      },
      {
        "name": "_startDate",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "registrationDate",
        "type": "uint256"
      }
    ],
    "name": "AuctionStarted",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "bidder",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "deposit",
        "type": "uint256"
      }
    ],
    "name": "NewBid",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "status",
        "type": "uint8"
      }
    ],
    "name": "BidRevealed",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "registrationDate",
        "type": "uint256"
      }
    ],
    "name": "HashRegistered",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "HashReleased",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "hash",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "name",
        "type": "string"
      },
      {
        "indexed": False,
        "name": "value",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "registrationDate",
        "type": "uint256"
      }
    ],
    "name": "HashInvalidated",
    "type": "event"
  }
]

DEED = [
  {
    "constant": True,
    "inputs": [],
    "name": "creationDate",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [],
    "name": "destroyDeed",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "setOwner",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "registrar",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "refundRatio",
        "type": "uint256"
      }
    ],
    "name": "closeDeed",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "newRegistrar",
        "type": "address"
      }
    ],
    "name": "setRegistrar",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "newValue",
        "type": "uint256"
      }
    ],
    "name": "setBalance",
    "outputs": [],
    "payable": True,
    "type": "function"
  },
  {
    "inputs": [],
    "type": "constructor"
  },
  {
    "payable": True,
    "type": "fallback"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": False,
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnerChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [],
    "name": "DeedClosed",
    "type": "event"
  }
]

FIFS_REGISTRAR = [
  {
    "constant": True,
    "inputs": [],
    "name": "ens",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "expiryTimes",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "subnode",
        "type": "bytes32"
      },
      {
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "register",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "rootNode",
    "outputs": [
      {
        "name": "",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "ensAddr",
        "type": "address"
      },
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "type": "constructor"
  }
]

RESOLVER = [
  {
    "constant": True,
    "inputs": [
      {
        "name": "interfaceID",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "contentTypes",
        "type": "uint256"
      }
    ],
    "name": "ABI",
    "outputs": [
      {
        "name": "contentType",
        "type": "uint256"
      },
      {
        "name": "data",
        "type": "bytes"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "x",
        "type": "bytes32"
      },
      {
        "name": "y",
        "type": "bytes32"
      }
    ],
    "name": "setPubkey",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "content",
    "outputs": [
      {
        "name": "ret",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "addr",
    "outputs": [
      {
        "name": "ret",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "contentType",
        "type": "uint256"
      },
      {
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "setABI",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "name",
    "outputs": [
      {
        "name": "ret",
        "type": "string"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "name",
        "type": "string"
      }
    ],
    "name": "setName",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "hash",
        "type": "bytes32"
      }
    ],
    "name": "setContent",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "name": "pubkey",
    "outputs": [
      {
        "name": "x",
        "type": "bytes32"
      },
      {
        "name": "y",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "node",
        "type": "bytes32"
      },
      {
        "name": "addr",
        "type": "address"
      }
    ],
    "name": "setAddr",
    "outputs": [],
    "payable": False,
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "ensAddr",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "constructor"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "a",
        "type": "address"
      }
    ],
    "name": "AddrChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "hash",
        "type": "bytes32"
      }
    ],
    "name": "ContentChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "name",
        "type": "string"
      }
    ],
    "name": "NameChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "contentType",
        "type": "uint256"
      }
    ],
    "name": "ABIChanged",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "name": "node",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "x",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "y",
        "type": "bytes32"
      }
    ],
    "name": "PubkeyChanged",
    "type": "event"
  }
]

REVERSE_REGISTRAR = [
  {
    "constant": False,
    "inputs": [
      {
        "name": "owner",
        "type": "address"
      },
      {
        "name": "resolver",
        "type": "address"
      }
    ],
    "name": "claimWithResolver",
    "outputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "claim",
    "outputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "ens",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [],
    "name": "defaultResolver",
    "outputs": [
      {
        "name": "",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "addr",
        "type": "address"
      }
    ],
    "name": "node",
    "outputs": [
      {
        "name": "ret",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "name",
        "type": "string"
      }
    ],
    "name": "setName",
    "outputs": [
      {
        "name": "node",
        "type": "bytes32"
      }
    ],
    "payable": False,
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "ensAddr",
        "type": "address"
      },
      {
        "name": "resolverAddr",
        "type": "address"
      }
    ],
    "payable": False,
    "type": "constructor"
  }
]
