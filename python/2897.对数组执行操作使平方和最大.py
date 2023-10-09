# 2897.对数组执行操作使平方和最大.py
# https://leetcode.cn/problems/apply-operations-on-array-to-maximize-sum-of-squares/description/
# lang=python

# 解法: 位运算 + 贪心
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        a = [0] * 30
        
        for x in nums:
            while x:
                lowbit = x & -x
                a[lowbit.bit_length() - 1] += 1
                x &= x - 1
        
        ans = 0
        for _ in range(k):
            v = 0
            for i in range(30):
                if a[i]:
                    v |= 1 << i
                    a[i] -= 1
            if v == 0:
                break
            ans += pow(v, 2, MOD)
            ans %= MOD
        return ans


if __name__ == "__main__":
    import time

    t0 = time.time()

    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func([96, 66, 60, 58, 32, 17, 63, 21, 30, 44, 15, 8, 98, 93], 2))
    # 输出: 32258
    print(func([2, 6, 5, 8], 2))
    # 输出: 261
    print(func([4, 5, 4, 7], 3))
    # 输出: 90

    t1 = time.time()
    print(t1 - t0)
