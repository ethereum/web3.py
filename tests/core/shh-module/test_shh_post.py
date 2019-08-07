# def test_shh_post(web3, skip_if_testrpc):
#     skip_if_testrpc(web3)
#     assert 0
#     receiver_pub = web3.shh.getPublicKey(web3.shh.newKeyPair())
#     try:
#         response = web3.shh.post({
#             "topic": "0x12345678",
#             "powTarget": 2.5,
#             "powTime": 2,
#             "payload": web3.toHex(text="testing shh on web3.py"),
#             "pubKey": receiver_pub,
#         })
#     except ValueError:
#         # with pytest.raises(ValueError):
#         response = web3.shh.post({
#             "topic": "0x12345678",
#             "powTarget": 2.5,
#             "powTime": 2,
#             "payload": web3.toHex(text="testing shh on web3.py"),
#             "pubKey": receiver_pub,
#         })
#         assert False
#     else:
#         assert response is False
