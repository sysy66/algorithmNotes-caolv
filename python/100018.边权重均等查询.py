# 100018.边权重均等查询
# https://leetcode.cn/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/description/
# lang=python


# 解法:树上差分+找公共祖先+dfs
from collections import defaultdict
from typing import List


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        qs = [defaultdict(list) for _ in range(n)]
        for idx, (u, v) in enumerate(queries):
            qs[u][v].append(idx)
            qs[v][u].append(idx)
        
        grid = [[] for _ in range(n)]
        for u, v, w in edges:
            grid[u].append((v, w - 1))
            grid[v].append((u, w - 1))
        
        pa = list(range(n))
        # i to tuple
        i2t = dict()
        ans = [0] * len(queries)
        
        def dfs(x, fa, w):
            if fa == -1:
                i2t[0] = (0,) * 26
            else:
                t = list(i2t[fa])
                t[w] += 1
                i2t[x] = tuple(t)
            for y in qs[x]:
                if y in i2t:
                    z = y
                    while pa[z] != z:
                        z = pa[z]
                    tmp = tuple(i + j - 2 * k for i, j, k in zip(i2t[x], i2t[y], i2t[z]))
                    for idx in qs[x][y]:
                        ans[idx] = sum(tmp) - max(tmp)
            for zz, ww in grid[x]:
                if zz != fa:
                    dfs(zz, x, ww)
            pa[x] = fa
        
        dfs(0, -1, 0)
        return ans


if __name__ == "__main__":
    import time
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(n=7, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]],
               queries=[[0, 3], [3, 6], [2, 6], [0, 6]]))
    # 输出：[0,0,1,3]
    print(func(n=8, edges=[[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]],
               queries=[[4, 6], [0, 4], [6, 5], [7, 4]]))
    # 输出：[1,2,2,3]
    
    t1 = time.time()
    print(t1 - t0)
