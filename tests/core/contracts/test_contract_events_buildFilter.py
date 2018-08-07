import json

CONTRACT_ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]')  # noqa: E501


def test_buildFilter(web3):
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    filter_builder = contract.events.Increased.buildFilter()
    filter_builder.args['value'].match_any(100, 200, 300)
    _filter = filter_builder.deploy(web3)
    assert _filter.filter_params == {
        'topics': (
            '0x3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5',)}
    assert _filter.data_filter_set == (('uint256', (100, 200, 300)),)
    filter_builder.args['value'].match_single(400)
    _filter2 = filter_builder.deploy(web3)
    assert _filter2.data_filter_set == (('uint256', (400,)),)
