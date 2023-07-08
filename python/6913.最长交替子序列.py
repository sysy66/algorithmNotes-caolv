# 6913.最长交替子序列
# https://leetcode.cn/problems/longest-alternating-subarray/
# lang=python

# 解法1：双指针
# 解法2：暴力

# In[1]
class Solution:
	def alternatingSubarray(self, nums: list[int]) -> int:
		n = len(nums)
		i = 0
		ans = -1
		while i < n - 1:
			if nums[i + 1] == nums[i] + 1:
				j = i
				while j + 1 < n and nums[j + 1] == nums[i + (j + 1 - i) % 2]:
					j += 1
				ans = max(ans, j - i + 1)
				i = j
			else:
				i += 1
		return ans


# In[2]
class Solution:
	def alternatingSubarray(self, nums: list[int]) -> int:
		n = len(nums)
		ans = -1
		for i in range(n - 1):
			if nums[i + 1] != nums[i] + 1: continue
			for j in range(i + 1, n):
				for k in range(i, j + 1):
					if nums[k] != nums[i + (k - i) % 2]:
						break
				else:
					ans = max(ans, j - i + 1)
		return ans


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[2, 3, 4, 3, 4]))
	# 输出：4
	print(func(nums=[4, 5, 6]))
	# 输出：2

	t_1 = time.time()
	print(t_1 - t_0)
