# 6929.数组的最大美丽值.py
# https://leetcode.cn/problems/maximum-beauty-of-an-array-after-applying-operation/description/
# lang=python

# 解法：双指针的简单应用

from typing import List
from collections import Counter


class Solution:
	def maximumBeauty(self, nums: List[int], k: int) -> int:
		if k == 0:
			return max(Counter(nums).values())

		n = len(nums)
		nums.sort()

		"""
		ans = 1
		i = j = 0
		while j < n:
			while j < n and nums[j] - nums[i] <= 2 * k:
				j += 1
			ans = max(ans, j - i)
			i += 1
		return ans
		"""

		ans = 1
		i = j = 0
		while j < n:
			while nums[j] - nums[i] > 2 * k:
				i += 1
			ans = max(ans, j - i + 1)
			j += 1
		return ans


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[4, 6, 1, 2], k=2))
	# 输出：3
	print(func(nums=[1, 1, 1, 1], k=10))
	# 输出：4

	t_1 = time.time()
	print(t_1 - t_0)

