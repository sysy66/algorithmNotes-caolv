# 100047.统计树中的合法路径数目.py
# https://leetcode.cn/problems/count-valid-paths-in-a-tree/description/
# lang=python

# 解法: 质数筛 + 深度优先搜索
from typing import List


MAX_RANGE = 10 ** 5 + 1
is_primes = [True] * MAX_RANGE
for i in range(2, MAX_RANGE):
    if is_primes[i]:
        for j in range(i * i, MAX_RANGE, i):
            is_primes[j] = False
is_primes[1] = False


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        grid = [[] for _ in range(n + 1)]
        for u, v in edges:
            grid[u].append(v)
            grid[v].append(u)
        
        ans = 0
        
        def dfs(x, fa):
            nonlocal ans
            a = 0 if is_primes[x] else 1
            b = a ^ 1
            for y in grid[x]:
                if y == fa: continue
                c, d = dfs(y, x)
                ans += a * d + b * c
                a += 0 if is_primes[x] else c
                b += c if is_primes[x] else d
            return a, b
        
        dfs(1, 0)
        return ans


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(n=5, edges=[[1, 2], [1, 3], [2, 4], [2, 5]]))
    # 输出：4
    print(func(n=6, edges=[[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]]))
    # 输出：6
    
    t1 = time.time()
    print(t1 - t0)
