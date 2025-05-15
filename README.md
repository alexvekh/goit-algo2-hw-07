# 📁 📁 Comparison of Execution Time for Array Queries Without Cache vs. LRU Cache
This script compares the performance of query operations (sum and update) with and without caching using LRU Cache.

        python lru_vs_nocache.py         # requires lru.py

⚙️ How does it work?

- Without caching: 50,000 random queries are computed from scratch.
- With LRU Cache: each result is stored in the cache. If the same query appears again, the result is fetched from the cache. However, updating one record clears the cache.

🧪 Execution Time Results
- Execution time without caching: 5.99 seconds
- Execution time with LRU cache: 5.81 seconds

📊 Explanation of Results
- Despite the expectation that caching would significantly improve performance, this did not happen.
- **Reason**: Since the queries involve the sum of values at random positions, the probability of the same pair appearing more than once is very low. In addition, frequent updates to the array invalidate the entire cache.
- **Recommendation**: To clearly see the benefit of LRU caching, try duplicating the queries – in this case, the execution time without cache doubles, while with cache it remains almost unchanged, as the repeated query is fetched directly from the cache.

# 📁 Comparison of LRU Cache vs. Splay Tree
This script compares the performance of computing Fibonacci numbers using:
- LRU Cache
- Splay Tree as a custom cache

        python lru_vs_splay.py         # requires splay_tree.py

🧪 Execution Time Results
- Execution time with LRU cache: 0.0004 seconds
- Execution time with Splay cache: 0.0002 seconds

📊 Explanation of Results

- Both caching methods show extremely fast execution, since all recursive calls to fib(k) are stored and reused.

- ✅ Splay Tree showed better performance (twice as fast as LRU Cache).

- Reason:
  - In a Splay Tree, the most recently accessed elements are automatically moved to the root (thanks to the splay operation). This makes access to frequently used items faster.
  - The LRU Cache also tracks access history, but it is based on a linked list structure, which may be slightly slower in some cases compared to tree-based access.