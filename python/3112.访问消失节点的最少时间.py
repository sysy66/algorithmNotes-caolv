# 3112.访问消失节点的最少时间.py
# https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/
# lang=python
from heapq import heappush, heappop
from typing import List


# 解法:Dijkstra

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        dis = [-1] * n
        dis[0] = 0
        h = [(0, 0)]
        
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, d in g[x]:
                if (dis[y] == -1 or dx + d < dis[y]) and dx + d < disappear[y]:
                    dis[y] = dx + d
                    heappush(h, (dx + d, y))
        
        return dis


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5]))
    # 输出：[0,-1,4]
    print(func(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 3, 5]))
    # 输出：[0,2,3]
    print(func(n=2, edges=[[0, 1, 1]], disappear=[1, 1]))
    # 输出：[0,-1]
    
    t1 = time.time()
    print(t1 - t0)
