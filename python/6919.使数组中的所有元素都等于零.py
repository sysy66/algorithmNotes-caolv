# 6919.使数组中的所有元素都等于零.py
# https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/
# lang=python

# 解法1：滑动窗口
# 解法2：差分数组

# In[1]
from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i, cnt = 0, 0
        while i < n and nums[i] >= cnt:
            nums[i], cnt = nums[i] - cnt, nums[i]
            if i - k + 1 >= 0:
                cnt -= nums[i - k + 1]
            i += 1
        return i == n and cnt == 0


# In[2]
'''
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n - 1, 0, -1):
            nums[i] = nums[i] - nums[i - 1]

        for i in range(n):
            if nums[i] == 0: continue
            if i + k < n:
                nums[i + k] += nums[i]
            elif i + k > n:
                return False

        return True
'''

if __name__ == "__main__":
    import time

    t_0 = time.time()

    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)

    print(func(nums=[2, 2, 3, 1, 1, 0], k=3))
    # 输出：true
    print(func(nums=[1, 3, 1, 1], k=2))
    # 输出：false

    t_1 = time.time()
    print(t_1 - t_0)

