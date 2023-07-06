# Tarjan(点双连通分量_标准模板).py
# LCP 54. 夺回据点

from typing import List
import time
from collections import deque

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        n = len(cost)
        g = [[] for _ in range(n)]
        for u, v in roads:
            g[u].append(v)
            g[v].append(u)

        clock = 0
        dfn = [0] * n
        low = [0] * n
        vis = [False] * n
        flag = [False] * n

        def tarjan(u, fa):
            nonlocal clock
            clock += 1
            child = 0
            vis[u] = True
            dfn[u] = low[u] = clock
            for v in g[u]:
                if not vis[v]:
                    child += 1
                    tarjan(v, u)
                    low[u] = min(low[u], low[v])
                    if fa != u and low[v] >= dfn[u] and not flag[u]:
                        flag[u] = True
                elif v != fa:
                    low[u] = min(low[u], dfn[v])
            if fa == u and child > 1 and not flag[u]:
                flag[u] = True

        # for i in range(n):
        #     if not vis[i]:
        #         tarjan(i, i)
        tarjan(0, 0)

        def bfs(x):
            ret = cost[x]
            cv = set()
            # cv means cut_vertex
            q = deque([x])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if flag[y]:
                        cv.add(y)
                    elif cost[y]:
                        ret = min(ret, cost[y])
                        cost[y] = 0
                        q.append(y)
            return ret if len(cv) < 2 else 0

        ans = list()
        for i in range(n):
            if not flag[i] and cost[i]:
                a = bfs(i)
                if a:
                    ans.append(a)

        return ans[0] if len(ans) == 1 else sum(ans) - max(ans)

# leetcode submit region end(Prohibit modification and deletion)

t_0 = time.time()

s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

print(func([11,5,4,11,7,11,6,7,16,7,15,6,7,10,4,14,18,6,3,18], [[0,1],[0,3],[0,5],[0,9],[0,14],[0,4],[0,16],[0,12],[0,8],[0,7],[1,2],[1,13],[1,7],[1,3],[1,16],[1,17],[1,10],[1,9],[2,8],[2,10],[2,9],[2,6],[2,13],[2,11],[2,16],[2,18],[2,3],[3,4],[3,7],[3,15],[3,16],[3,11],[4,6],[4,12],[4,19],[4,8],[4,5],[4,14],[4,7],[4,10],[5,13],[5,7],[5,19],[5,15],[5,16],[6,7],[6,15],[6,13],[6,14],[7,11],[7,16],[7,15],[7,14],[7,8],[8,17],[8,11],[8,13],[8,10],[9,11],[9,12],[9,19],[10,14],[10,11],[10,13],[10,15],[10,19],[11,14],[11,16],[11,17],[12,16],[12,18],[12,14],[13,15],[14,15],[14,16],[14,18],[14,17],[15,18],[15,16],[16,18],[16,17],[16,19],[17,19]]))
# 3
print(func(cost=[1, 2, 3, 4, 5, 6], roads=[[0, 1], [0, 2], [1, 3], [2, 3], [1, 2], [2, 4], [2, 5]]))
# 输出：6
print(func(cost=[3, 2, 1, 4], roads=[[0, 2], [2, 3], [3, 1]]))
# 输出：2
print(func([9, 2, 3, 4, 5, 6, 7], [[1, 2], [1, 3], [2, 3], [3, 6], [6, 0], [0, 3], [4, 2], [2, 5], [4, 5]]))
# 输出：5

t_1 = time.time()

print(t_1 - t_0)
