# 6912.构造最长非递减子数组.py
# https://leetcode.cn/problems/longest-non-decreasing-subarray-from-two-arrays/description/
# lang=python

# 解法1：动态规划

# In[1]
from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans, n = 0, len(nums1)

        pre = [0, 0]
        stp = [0, 0]
        for x, y in zip(nums1, nums2):
            u, v = 1, 1
            for i in range(2):
                if x >= pre[i]:
                    u = max(u, stp[i] + 1)
                if y >= pre[i]:
                    v = max(v, stp[i] + 1)
            pre = [x, y]
            stp = [u, v]
            ans = max(ans, u, v)

        return ans


if __name__ == "__main__":
    import time

    t_0 = time.time()

    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)

    print(func(nums1=[2, 3, 1], nums2=[1, 2, 1]))
    # 输出：2
    print(func(nums1=[1, 3, 2, 1], nums2=[2, 2, 3, 4]))
    # 输出：4
    print(func(nums1=[1, 1], nums2=[2, 2]))
    # 输出：2

    t_1 = time.time()
    print(t_1 - t_0)

