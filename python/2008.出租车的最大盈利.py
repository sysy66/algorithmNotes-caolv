# 2008. 出租车的最大盈利
# https://leetcode.cn/problems/maximum-earnings-from-taxi/description/?envType=daily-question&envId=2023-12-08
# lang=python

# 解法:动态规划+二分
from bisect import bisect_right
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        a, b = [0], [0]
        for start, end, tip in rides:
            earn = end - start + tip
            i = bisect_right(a, start) - 1
            if end > a[-1]:
                a.append(end)
                b.append(max(earn + b[i], b[-1]))
            else:
                b[-1] = max(earn + b[i], b[-1])
        return b[-1]


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(n=5, rides=[[2, 5, 4], [1, 5, 1]]))
    # 输出：7
    print(func(n=20, rides=[[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]))
    # 输出：20
    print(func(n=10, rides=[[2, 3, 6], [8, 9, 8], [5, 9, 7], [8, 9, 1], [2, 9, 2], [9, 10, 6], [7, 10, 10],
                            [6, 7, 9], [4, 9, 7], [2, 3, 1]]))
    # 输出：33
    
    t1 = time.time()
    print(t1 - t0)
