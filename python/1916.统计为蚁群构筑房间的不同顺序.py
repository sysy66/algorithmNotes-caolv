# 1916.统计为蚁群构筑房间的不同顺序.py
# https://leetcode.cn/problems/count-ways-to-build-rooms-in-an-ant-colony/description/
# lang=python
# 解法:乘法逆元+排列数
from collections import defaultdict, deque
from typing import List

MOD = 1_000_000_007
MX = 100_001

fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD
inv_fac = [0] * MX
inv_fac[-1] = pow(fac[-1], MOD - 2, MOD)
for i in range(MX - 2, -1, -1):
    inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD


# 自上而下
# class Solution:
#     def waysToBuildRooms(self, prevRoom: List[int]) -> int:
#         n = len(prevRoom)
#         g = defaultdict(list)
#         for i in range(1, n):
#             g[prevRoom[i]].append(i)
#
#         def dfs(x: int) -> (int, int):
#             ret, cnt = 1, 0
#             for y in g[x]:
#                 r, c = dfs(y)
#                 ret = ret * inv_fac[c] * r % MOD
#                 cnt += c
#             ret = ret * fac[cnt] % MOD
#             cnt += 1
#             return ret, cnt
#
#         return dfs(0)[0]


# 自下而上
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        f, cnt, in_degree = [1] * n, [1] * n, [0] * n
        
        for i in range(1, n):
            in_degree[prevRoom[i]] += 1
        
        q = deque(i for i, d in enumerate(in_degree) if d == 0)
        while True:
            u = q.popleft()
            if u == 0:
                break
            v = prevRoom[u]
            f[v] = f[v] * f[u] * inv_fac[cnt[u]] % MOD
            cnt[v] += cnt[u]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
                f[v] = f[v] * fac[cnt[v] - 1] % MOD
        return f[0]


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(prevRoom=[-1, 0, 1]))
    # 输出：1
    print(func(prevRoom=[-1, 0, 0, 1, 2]))
    # 输出：6
    t1 = time.time()
    print(t1 - t0)
