import random,string

def test_shh_post(web3,skip_if_testrpc):
    skip_if_testrpc(web3)
    random_topic = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    assert web3.shh.post({"topics":[web3.fromAscii(random_topic)],"payload":web3.fromAscii("testing shh on web3.py")})
