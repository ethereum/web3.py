import aiohttp


async def make_post_request(endpoint_uri, data, *args, **kwargs):
    kwargs.setdefault('timeout', 10)
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.post(
                endpoint_uri,
                json=data,
                *args,
                **kwargs) as response:
            return await response.text()
