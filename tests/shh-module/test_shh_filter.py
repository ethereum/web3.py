import random,string,gevent

def test_shh_filter(web3,skip_if_testrpc):
    skip_if_testrpc(web3)
    topic = "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(10))
    recieved_messages = []
    shh_filter = web3.shh.filter({"topics":[web3.fromAscii(topic)]})
    shh_filter.watch(recieved_messages.append)
    gevent.sleep(1)
    
    payloads = []
    payloads.append("".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(20)))
    web3.shh.post({"topics":[web3.fromAscii(topic)],"payload":web3.fromAscii(payloads[len(payloads)-1])})
    gevent.sleep(1)
    
    payloads.append( "".join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(20))) 
    web3.shh.post({"topics":[web3.fromAscii(topic)],"payload":web3.fromAscii(payloads[len(payloads)-1])})
    gevent.sleep(1)

    for message in recieved_messages:
        assert web3.toAscii(message["payload"]) in payloads
