import random
import time
from lru import LRUCache

# ======== Параметри ========
N = 100_000
Q = 50_000
CACHE_CAPACITY = 1000

# ======== Дані ========
array = [random.randint(1, 100) for _ in range(N)]

# Генерація 50_000 випадкових запитів
queries = []
for _ in range(Q):
    if random.random() < 0.5:
        L = random.randint(0, N - 2)
        R = random.randint(L + 1, N)
        queries.append(("Range", L, R))
    else:
        i = random.randint(0, N - 1)
        v = random.randint(1, 100)
        queries.append(("Update", i, v))


# ======== Без кешу ========
def range_sum_no_cache(L, R):
    return sum(array[L:R])

def update_no_cache(index, value):
    array[index] = value

start_no_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_no_cache(query[1], query[2])
        # range by 2 times for see the time difference 
        # range_sum_no_cache(query[1], query[2])  
    else:
        update_no_cache(query[1], query[2])
end_no_cache = time.time()


# ======== З кешем ========
cache = LRUCache(capacity=CACHE_CAPACITY)

def range_sum_with_cache(L, R):
    key = (L, R)
    cached = cache.get(key)
    if cached != -1:
        return cached
    result = sum(array[L:R])
    cache.put(key, result)
    return result

def update_with_cache(index, value):
    array[index] = value
    cache.cache.clear()
    cache.list = cache.list.__class__()  # Очищення двозв’язного списку

start_cache = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_with_cache(query[1], query[2])
        # range by 2 times for see the time difference
        # range_sum_with_cache(query[1], query[2])    
    else:
        update_with_cache(query[1], query[2])
end_cache = time.time()


# ======== Результати ========
print(f"Час виконання без кешування: {end_no_cache - start_no_cache:.2f} секунд")
print(f"Час виконання з LRU-кешем: {end_cache - start_cache:.2f} секунд")
