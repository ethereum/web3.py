import requests


def make_post_request(endpoint_uri, data, *args, **kwargs):
    kwargs.setdefault('timeout', 10)
    response = requests.post(endpoint_uri, data=data, *args, **kwargs)
    response.raise_for_status()

    return response.content
