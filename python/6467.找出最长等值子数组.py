# 6467.找出最长等值子数组
# https://leetcode.cn/problems/find-the-longest-equal-subarray/description/
# lang=python


# 解法: 双端队列
from collections import defaultdict, deque
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cost = [0] * len(nums)
        v2i = {}
        gs = defaultdict(list)
        for i, x in enumerate(nums):
            if x not in v2i:
                v2i[x] = i - 1
            cost[i] = i - v2i[x] - 1
            v2i[x] = i
            gs[x].append(i)
        
        ans = 1
        for g in gs.values():
            if len(g) <= ans:
                continue
            q = deque()
            c = 0
            for i in g:
                q.append(i)
                c += cost[i]
                while c > k:
                    q.popleft()
                    j = q[0]
                    c -= cost[j]
                ans = max(ans, len(q))
        return ans


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(nums=[1, 3, 2, 3, 1, 3], k=3))
    # 输出：3
    print(func(nums=[1, 1, 2, 2, 1, 1], k=2))
    # 输出：4
    
    t1 = time.time()
    print(t1 - t0)
