# _*_ coding:utf-8 _*_
# url:"https://leetcode.cn/problems/prime-in-diagonal/solutions/2216309/python3zhi-shu-shai-bian-li-by-musing-cl-aqpy/"


from typing import List


# 线性筛 欧拉筛
MX_RANGE = 4 * 10 ** 6 + 1
is_prime = [True] * MX_RANGE
primes = list()
for i in range(2, MX_RANGE):
    if is_prime[i]: primes.append(i)
    for p in primes:
        if i * p >= MX_RANGE: break
        is_prime[i * p] = False
        if i % p == 0: break
primes = set(primes)

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ret, n = 0, len(nums)
        for i in range(n):
            x = nums[i][i]
            if x in primes and x > ret: ret = x
            x = nums[i][n - 1 - i]
            if x in primes and x > ret: ret = x
        return ret


###################test#################
if __name__ == "__main__":
	import time
	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums = [[1,2,3],[5,6,7],[9,10,11]]))
	# 输出：11
	print(func(nums = [[1,2,3],[5,17,7],[9,11,10]]))
	# 输出：17

	t_1 = time.time()
	print(t_1 - t_0)

