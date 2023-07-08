# 6923.将字符串分割为最少的美丽子字符串
#
# lang=python

# 解法1：动态规划

# In[1]
"""
ss = set()
x = 1
while len(bin(x)) - 2 <= 15:
	ss.add(bin(x)[2:])
	x *= 5
"""
from cmath import inf

ss = {'1001110001', '101', '11110100001001', '11001', '1111101', '110000110101', '1'}


class Solution:
	def minimumBeautifulSubstrings(self, s: str) -> int:
		n = len(s)
		dp = [[inf] * n for _ in range(n)]

		for i in range(n):
			if s[i] == "1":
				dp[i][i] = 1
		for j in range(1, n):
			for i in range(j - 1, -1, -1):
				if s[i:j + 1] in ss:
					dp[i][j] = 1
				else:
					dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))

		ans = dp[0][n - 1]
		return -1 if ans == inf else ans


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(s="1011"))
	# 输出：2
	print(func(s="111"))
	# 输出：3
	print(func(s="0"))
	# 输出：-1

	t_1 = time.time()
	print(t_1 - t_0)
