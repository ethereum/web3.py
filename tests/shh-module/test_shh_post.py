def test_shh_post(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    random_topic = "testing"
    assert web3.shh.post({"topics":[web3.fromAscii(random_topic)], "payload":web3.fromAscii("testing shh on web3.py")})
