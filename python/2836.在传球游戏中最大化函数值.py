# 2836.在传球游戏中最大化函数值
# https://leetcode.cn/problems/maximize-value-of-function-in-a-ball-passing-game/description/
# lang=python

# 解法:图论，带环链表
from collections import defaultdict, deque
from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        k += 1
        n = len(receiver)
        
        # 第一步找出图里的所有环，顺便计算从环上开始的最大值（用滑动窗口）
        ans = 0
        prefixs = defaultdict(list)
        vis = [0] * n
        loc = [0] * n
        for x in range(n):
            if vis[x]: continue
            seen = {}
            ls = list()
            while 1:
                vis[x] = 1
                seen[x] = len(ls)
                ls.append(x)
                x = receiver[x]
                if vis[x]:
                    if x not in seen: break
                    ls = ls[seen[x]:]
                    m = len(ls)
                    prefix = [0]
                    for idx, j in enumerate(ls):
                        prefixs[j] = prefix
                        loc[j] = idx
                    ls = ls + ls
                    for j in range(2 * m):
                        prefix.append(prefix[-1] + ls[j])
                    tmp1 = prefix[m] * (k // m)
                    r = k % m
                    if r:
                        tmp2 = cnt = sum(ls[:r])
                        for i in range(r, m + r):
                            cnt += ls[i] - ls[i - r]
                            tmp2 = max(tmp2, cnt)
                        tmp1 += tmp2
                    ans = max(ans, tmp1)
                    break
        
        # 第二部，从入度为0的点开始走，类似滑动窗口遍历每个点出发能得到结果，然后当然是取最大值~
        indegree = [0] * n
        for v in receiver:
            indegree[v] += 1
        
        for i in range(n):
            if indegree[i]: continue
            ptr = i
            q = deque()
            cnt = 0
            while ptr not in prefixs:
                q.append(ptr)
                cnt += ptr
                if len(q) == k:
                    ans = max(ans, cnt)
                    cnt -= q.popleft()
                ptr = receiver[ptr]
            prefix, idx = prefixs[ptr], loc[ptr]
            m = len(prefix) // 2
            kk = k - len(q)
            while q:
                ans = max(ans, cnt + prefix[idx + kk % m] - prefix[idx] + (kk // m) * prefix[m])
                cnt -= q.popleft()
                kk += 1
        
        return ans


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(receiver=[2, 0, 1], k=4))
    # 输出：6
    print(func(receiver=[1, 1, 1, 2, 3], k=3))
    # 输出：10
    print(func([3, 4, 1, 2, 2], 10))
    # 输出：27
    print(func([2, 1, 1], 4))
    # 输出：6
    print(func([2, 3, 3, 1], 15))
    # 输出：33
    print(func([1, 0, 1], 2))
    # 输出：3
    print(func([3, 2, 2, 1, 0], 2))
    # 输出：7
    
    t1 = time.time()
    print(t1 - t0)
