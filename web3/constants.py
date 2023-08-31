# Constants as Strings
ADDRESS_ZERO = "0x0000000000000000000000000000000000000000"
MAX_INT = "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
HASH_ZERO = "0x0000000000000000000000000000000000000000000000000000000000000000"

# Constants as Int
WEI_PER_ETHER = 1000000000000000000

# Grouped constants as Tuples
DYNAMIC_FEE_TXN_PARAMS = ("maxFeePerGas", "maxPriorityFeePerGas")

# JSON-RPC Response Validation Schema
# https://www.jsonrpc.org/specification#response_object
JSON_RPC_RESPONSE_SCHEMA = {
    "title": "JSON-RPC 2.0 Response Schema",
    "description": "A JSON-RPC 2.0 response message",
    "allOf": [
        {
            "type": "object",
            "properties": {
                "jsonrpc": {"type": "string", "enum": ["2.0"]},
                "id": {
                    "oneOf": [{"type": "string"}, {"type": "integer"}, {"type": "null"}]
                },
            },
            "required": ["jsonrpc", "id"],
        },
        {
            "oneOf": [
                {
                    "type": "object",
                    "properties": {"result": {}, "jsonrpc": {}, "id": {}},
                    "required": ["result"],
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "properties": {
                        "error": {
                            "type": "object",
                            "properties": {
                                "code": {"type": "integer"},
                                "message": {"type": ["string", "null"]},
                                "data": {
                                    "anyOf": [
                                        {"type": "string"},
                                        {"type": "number"},
                                        {"type": "boolean"},
                                        {"type": "null"},
                                        {"type": "object"},
                                        {"type": "array"},
                                    ]
                                },
                            },
                            "required": ["code", "message"],
                        },
                        "jsonrpc": {},
                        "id": {},
                    },
                    "required": ["error"],
                    "additionalProperties": False,
                },
            ]
        },
    ],
}
