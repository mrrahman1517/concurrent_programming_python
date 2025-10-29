import pytest
from day3_lru_cache_threadsafe import ThreadSafeLRU
import threading

def test_basic_put_get():
    cache = ThreadSafeLRU(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2

def test_eviction_policy():
    cache = ThreadSafeLRU(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)  # evicts 'a'
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3

def test_concurrent_access():
    cache = ThreadSafeLRU(capacity=5)

    def writer(start):
        for i in range(start, start + 100):
            cache.put(f"k{i}", i)

    threads = [threading.Thread(target=writer, args=(i * 100,)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # After all threads complete, ensure cache is still valid structure
    keys = list(cache.cache.keys())
    assert len(keys) <= cache.capacity
