# 6927.合法分割的最小下标.py
# https://leetcode.cn/problems/minimum-index-of-a-valid-split/description/
# lang=python


# 解法：模拟

import heapq
from collections import Counter
from typing import List


class Solution:
	def minimumIndex(self, nums: List[int]) -> int:

		"""
		# 1.遍历列表找出最大频率的数值和频率
		dmt = -1  # dominant
		max_freq = 0
		cnt = Counter()
		for x in nums:
			cnt[x] += 1
			if cnt[x] > max_freq:
				max_freq = cnt[x]
				dmt = x
		"""

		# 2.调包~找出最大频率的数值和频率
		cnt = Counter(nums)
		max_freq, dmt = heapq.nlargest(1, [(v, k) for k, v in cnt.items()])[0]

		n = len(nums)
		c = 0
		for i, x in enumerate(nums):
			if x == dmt:
				c += 1
			if 2 * c > i + 1 and 2 * (max_freq - c) > n - i - 1:
				return i
		return -1


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[1, 2, 2, 2]))
	# 输出：2
	print(func(nums=[2, 1, 3, 1, 1, 1, 7, 1, 2, 1]))
	# 输出：4
	print(func(nums=[3, 3, 3, 3, 7, 2, 2]))
	# 输出：-1

	t_1 = time.time()
	print(t_1 - t_0)

