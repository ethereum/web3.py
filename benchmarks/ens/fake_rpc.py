FAKE_ENS_REGISTRY = "0x0000000000000000000000000000000000000002"
FAKE_RESOLVER = "0x0000000000000000000000000000000000000001"
FAKE_RESULT_ADDR = "0x314159265dD8dbb310642f98f50C066173C1259b"

def fake_json_rpc_response(request_data: dict):
    method = request_data.get("method")
    params = request_data.get("params", [])
    if method == "eth_call":
        call_data = params[0]
        to_addr = call_data.get("to", "").lower()
        if to_addr == FAKE_ENS_REGISTRY.lower():
            return {
                "jsonrpc": "2.0",
                "id": request_data["id"],
                "result": "0x" + "0" * 24 + FAKE_RESOLVER[2:]
            }
        elif to_addr == FAKE_RESOLVER.lower():
            return {
                "jsonrpc": "2.0",
                "id": request_data["id"],
                "result": "0x" + "0" * 24 + FAKE_RESULT_ADDR[2:]
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_data["id"],
                "result": "0x" + "0" * 40
            }
    elif method == "eth_getCode":
        addr = params[0].lower()
        if addr == FAKE_RESOLVER.lower():
            return {
                "jsonrpc": "2.0",
                "id": request_data["id"],
                "result": "0x6001600101"
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_data["id"],
                "result": "0x"
            }
    return {
        "jsonrpc": "2.0",
        "id": request_data["id"],
        "result": None
    }
