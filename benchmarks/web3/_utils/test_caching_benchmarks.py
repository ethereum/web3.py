import asyncio

import pytest
from pytest_codspeed import BenchmarkFixture

import web3.utils.caching
import faster_web3.utils.caching


def run_100(func, *args, **kwargs):
    for _ in range(100):
        func(*args, **kwargs)


def insert_items(cls, size, keys, values):
    cache = cls(size=size)
    for k, v in zip(keys, values):
        cache.cache(k, v)


@pytest.mark.benchmark(group="SimpleCache-cache")
@pytest.mark.parametrize("size", [10, 100, 1000])
def test_web3_simplecache_cache(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size)))
    values = list(range(size))
    benchmark(run_100, insert_items, web3.utils.caching.SimpleCache, size, keys, values)


@pytest.mark.benchmark(group="SimpleCache-cache")
@pytest.mark.parametrize("size", [10, 100, 1000])
def test_faster_simplecache_cache(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size)))
    values = list(range(size))
    benchmark(run_100, insert_items, faster_web3.utils.caching.SimpleCache, size, keys, values)


def insert_and_evict(cls, size, keys, values):
    cache = faster_web3.utils.caching.SimpleCache(size=size)
    for k, v in zip(keys, values):
        cache.cache(k, v)


@pytest.mark.benchmark(group="SimpleCache-eviction")
@pytest.mark.parametrize("size", [10, 100])
def test_web3_simplecache_eviction(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size * 2)))
    values = list(range(size * 2))
    def insert_and_evict():
        cache = web3.utils.caching.SimpleCache(size=size)
        for k, v in zip(keys, values):
            cache.cache(k, v)
    benchmark(run_100, insert_and_evict, web3.utils.caching.SimpleCache, size, keys, values)


@pytest.mark.benchmark(group="SimpleCache-eviction")
@pytest.mark.parametrize("size", [10, 100])
def test_faster_simplecache_eviction(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size * 2)))
    values = list(range(size * 2))
    benchmark(run_100, insert_and_evict, faster_web3.utils.caching.SimpleCache, size, keys, values)


def retrieve_items(cache, keys):
    for k in keys:
        cache.get_cache_entry(k)


@pytest.mark.benchmark(group="SimpleCache-retrieval")
@pytest.mark.parametrize("size", [10, 100])
def test_web3_simplecache_retrieval(benchmark: BenchmarkFixture, size):
    cache = web3.utils.caching.SimpleCache(size=size)
    keys = list(map(str, range(size)))
    for k, v in zip(keys, range(size)):
        cache.cache(k, v)
    benchmark(run_100, retrieve_items, cache, keys)


@pytest.mark.benchmark(group="SimpleCache-retrieval")
@pytest.mark.parametrize("size", [10, 100])
def test_faster_simplecache_retrieval(benchmark: BenchmarkFixture, size):
    cache = faster_web3.utils.caching.SimpleCache(size=size)
    keys = list(map(str, range(size)))
    for k, v in zip(keys, range(size)):
        cache.cache(k, v)
    benchmark(run_100, retrieve_items, cache, keys)


def pop_items(cls, size, keys, values):
    cache = cls(size=size)
    for k, v in zip(keys, values):
        cache.cache(k, v)
    for k in keys:
        cache.pop(k)
            
@pytest.mark.benchmark(group="SimpleCache-pop")
@pytest.mark.parametrize("size", [10, 100])
def test_web3_simplecache_pop(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size)))
    values = list(range(size))
    benchmark(run_100, pop_items, web3.utils.caching.SimpleCache, size, keys, values)

@pytest.mark.benchmark(group="SimpleCache-pop")
@pytest.mark.parametrize("size", [10, 100])
def test_faster_simplecache_pop(benchmark: BenchmarkFixture, size):
    keys = list(map(str, range(size)))
    values = list(range(size))
    benchmark(run_100, pop_items, faster_web3.utils.caching.SimpleCache, size, keys, values)


async def popitem_many(cache, size, last):
    try:
        for _ in range(size):
            await cache.async_await_and_popitem(last=last, timeout=0.1)
    except asyncio.TimeoutError:
        return


@pytest.mark.benchmark(group="SimpleCache-async_await_and_popitem")
@pytest.mark.parametrize("size", [10, 100])
@pytest.mark.parametrize("last", [True, False])
def test_web3_simplecache_async_await_and_popitem(benchmark: BenchmarkFixture, size, last):
    cache = web3.utils.caching.SimpleCache(size=size)
    loop = asyncio.new_event_loop()
    for i in range(size * 10_000):
        cache.cache(str(i), i)
    @benchmark
    def run() -> None:
        loop.run_until_complete(popitem_many(cache, size, last))


@pytest.mark.benchmark(group="SimpleCache-async_await_and_popitem")
@pytest.mark.parametrize("size", [10, 100])
@pytest.mark.parametrize("last", [True, False])
def test_faster_simplecache_async_await_and_popitem(benchmark: BenchmarkFixture, size, last):
    cache = faster_web3.utils.caching.SimpleCache(size=size)
    loop = asyncio.new_event_loop()
    for i in range(size * 10_000):
        cache.cache(str(i), i)
    @benchmark
    def run() -> None:
        loop.run_until_complete(popitem_many(cache, size, last))
