# 取集合的所有子集.py
# 805. 数组的均值分割

"""
n = 3
i = (1 << n) - 1
j = i
while j > 0:
    print(bin(j))
    j = i & (j - 1)
"""

class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        i = (1 << n) - 1
        j = i & (i - 1)
        tot = sum(nums)
        while j > 0:
            a = list()
            for k in range(n):
                if j & (1 << k):
                    a.append(nums[k])

            if tot * len(a) == sum(a) * n:
                return True
            j = i & (j - 1)
        return False


