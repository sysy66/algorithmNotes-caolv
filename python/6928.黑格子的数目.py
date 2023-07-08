# 6928. 黑格子的数目
# https://leetcode.cn/problems/number-of-black-blocks/
# lang=python

# 解法1：哈希

# In[1]
from typing import List
from collections import Counter


class Solution:
	def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
		coordinates.sort()
		coordinates.append([m, 0]) # 哨兵？
		ans = [0] * 5
		a, b = Counter(), Counter()
		cur = coordinates[0][0]
		for x, y in coordinates:
			if x != cur:
				if cur != 0:
					for k, v in a.items():
						if k == -1 or k == n - 1: continue
						ans[v] += 1
				if x == cur + 1:
					a, b = b, Counter()
				else:
					for k, v in b.items():
						if k == -1 or k == n - 1: continue
						ans[v] += 1
					a, b = Counter(), Counter()
				cur = x
			a[y - 1] += 1
			a[y] += 1
			b[y - 1] += 1
			b[y] += 1
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
