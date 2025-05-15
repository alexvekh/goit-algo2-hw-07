from functools import lru_cache
from lru import LRUCache
from splay_tree import SplayCache
import time

#@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    cached = cache.get(n)
    if cached != -1:
        return cached
    result = fib(n - 1) + fib(n - 2)
    cache.put(n, result)
    return result


def fib(n):
    if n < 2:
        return n
    cached = splay.find(n)
    if cached != -1:
        return cached
    result = fib(n - 1) + fib(n - 2)
    splay.insert(n, result)
    return result



if __name__ == "__main__":
    
    cache = LRUCache(capacity=128)
    splay = SplayCache()

    start_lru = time.time()
    print(fib(35))
    end_lru = time.time()
    print(f"Час виконання з LRU-кешем: {end_lru - start_lru:.4f} секунд")

    start_splay = time.time()
    print(fib(35))
    end_splay = time.time()
    print(f"Час виконання з Splay-кешем: {end_splay - start_splay:.4f} секунд")
    