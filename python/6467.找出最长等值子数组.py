# 6467.找出最长等值子数组
# https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/description/
# lang=python


# 解法: 动态规划
from bisect import bisect_left
from typing import List

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        idx = sorted(range(len(offers)), key=lambda x: offers[x][1])
        a = [0]
        ends = [-1]
        for i in idx:
            s, e, g = offers[i]
            a.append(a[-1])
            ends.append(e)
            j = bisect_left(ends, s) - 1
            a[-1] = max(a[-1], g + a[j])
        return a[-1]


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(n=5, offers=[[0, 0, 1], [0, 2, 2], [1, 3, 2]]))
    # 输出：3
    print(func(n=5, offers=[[0, 0, 1], [0, 2, 10], [1, 3, 2]]))
    # 输出：10
    
    t1 = time.time()
    print(t1 - t0)
