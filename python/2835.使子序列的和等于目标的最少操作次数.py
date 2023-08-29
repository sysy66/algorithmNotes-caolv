# 2835.使子序列的和等于目标的最少操作次数.py
# https://leetcode.cn/problems/minimum-operations-to-form-subsequence-with-target-sum/description/
# lang=python

# 解法:贪心，由低到高逐位
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        
        a = [0] * 31
        for v in nums:
            a[v.bit_length() - 1] += 1
        b = [0] * 31
        while target:
            x = target & -target
            b[x.bit_length() - 1] += 1
            target &= target - 1
        
        ans = 0
        i = j = 0
        while 1:
            while j < 31 and b[j] == 0:
                j += 1
            if j == 31:
                return ans
            while i < j:
                a[i + 1] += a[i] // 2
                i += 1
            if a[i]:
                a[i] -= 1
            else:
                k = next(k for k in range(j + 1, 31) if a[k])
                a[k] -= 1
                ans += k - j
                for kk in range(j, k):
                    a[kk] += 1
            j += 1


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(nums=[1, 2, 8], target=7))
    # 输出：1
    print(func(nums=[1, 32, 1, 2], target=12))
    # 输出：2
    
    t1 = time.time()
    print(t1 - t0)
