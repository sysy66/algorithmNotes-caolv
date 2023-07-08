# 6928. 黑格子的数目
# https://leetcode.cn/problems/number-of-black-blocks/
# lang=python

# 解法1：哈希

# In[1]
from typing import List
from collections import Counter


class Solution:
	def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
		ans = [0] * 5
		cnt = Counter()
		for x, y in coordinates:
			cnt[(x, y)] += 1
			cnt[(x - 1, y)] += 1
			cnt[(x, y - 1)] += 1
			cnt[(x - 1, y - 1)] += 1
		for (x, y), v in cnt.items():
			if y == -1 or y == n - 1 or x == m - 1 or x == -1: continue
			ans[v] += 1
		ans[0] = (m - 1) * (n - 1) - sum(ans)
		return ans


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(m=3, n=3, coordinates=[[0, 0]]))
	# 输出：[3,1,0,0,0]
	print(func(m=3, n=3, coordinates=[[0, 0], [1, 1], [0, 2]]))
	# 输出：[0,2,2,0,0]

	t_1 = time.time()
	print(t_1 - t_0)
