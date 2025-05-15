# import sys
# sys.setrecursionlimit(2000)

from functools import lru_cache
from lru import LRUCache
from splay_tree import SplayCache
import time
import matplotlib.pyplot as plt
import timeit
from tabulate import tabulate


@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n-1) + fibonacci_lru(n-2)


def fibonacci_splay(n, tree):
    cached = tree.find(n)
    if cached is not None:
        return cached
    if n < 2:
        result = n
    else:
        result = fibonacci_splay(n-1, tree) + fibonacci_splay(n-2, tree)
    tree.insert(n, result)
    return result



def benchmark():
    ns = list(range(0, 951 , 50))
    results = []

    for n in ns:
        # Time LRU
        fibonacci_lru.cache_clear()
        lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=1)

        # Time Splay
        tree = SplayCache()
        splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=1)

        results.append((n, lru_time, splay_time))

    return results

# ====== Table and Plot ======

def display_results(results):
    headers = ["n", "LRU Cache Time (s)", "Splay Tree Time (s)"]
    table = [[n, f"{lru:.8f}", f"{splay:.8f}"] for n, lru, splay in results]
    print(tabulate(table, headers=headers, tablefmt="github"))

    # Plot
    x = [r[0] for r in results]
    y_lru = [r[1] for r in results]
    y_splay = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_lru, label="LRU Cache", marker='o')
    plt.plot(x, y_splay, label="Splay Tree", marker='s')
    plt.xlabel("n (Fibonacci number index)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Fibonacci Calculation Time: LRU Cache vs Splay Tree")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ====== Main ======

if __name__ == "__main__":
    results = benchmark()
    display_results(results)