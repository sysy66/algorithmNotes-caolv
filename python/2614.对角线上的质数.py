# 2614.对角线上的质数
# https://leetcode.cn/problems/prime-in-diagonal/solutions/2216309/python3zhi-shu-shai-bian-li-by-musing-cl-aqpy/
# lang=python

# 解法1:利用质数筛算出数据范围内的所有质数,再利用集合做到查询时间O(1);遍历对角线上的数,记录下最大的质数.
# 解法2：利用质数筛算出2000以内的所有质数;遍历对角线上的数,如果x不能被2000以内的某一质数整除,则x为质数,记录下最大的x为答案.
# PS:分别展示了欧拉筛(线性筛)和埃氏筛，用起来差别不大


# In[1]
from typing import List

# 埃氏筛
MX_RANGE = 4 * 10 ** 6 + 1
is_prime = [True] * MX_RANGE
primes = list()
for i in range(2, MX_RANGE):
	if is_prime[i]:
		primes.append(i)
		for j in range(i * i, MX_RANGE, i):
			is_prime[j] = False
primes = set(primes)


class Solution:
	def diagonalPrime(self, nums: List[List[int]]) -> int:
		ret, n = 0, len(nums)
		for i in range(n):
			for x in (nums[i][i], nums[i][n - 1 - i]):
				if x in primes and x > ret:
					ret = x
		return ret


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
	# 输出：11
	print(func(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
	# 输出：17

	t_1 = time.time()
	print(t_1 - t_0)


# In[2]
from typing import List

# 欧拉筛(线性筛)
MX_RANGE = 2001
is_prime = [True] * MX_RANGE
primes = list()
for i in range(2, MX_RANGE):
	if is_prime[i]: primes.append(i)
	for p in primes:
		if i * p >= MX_RANGE: break
		is_prime[i * p] = False
		if i % p == 0: break


class Solution:
	def diagonalPrime(self, nums: List[List[int]]) -> int:
		ret, n = 0, len(nums)
		for i in range(n):
			for x in (nums[i][i], nums[i][n - 1 - i]):
				if x <= ret: continue
				for p in primes:
					if x % p == 0 and x != p:
						break
				else:
					ret = max(ret, x)
		return ret if ret != 1 else 0


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[[1, 2, 3], [5, 6, 7], [9, 10, 11]]))
	# 输出：11
	print(func(nums=[[1, 2, 3], [5, 17, 7], [9, 11, 10]]))
	# 输出：17

	t_1 = time.time()
	print(t_1 - t_0)
