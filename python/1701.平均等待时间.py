# 1701.平均等待时间
# https://leetcode.cn/problems/average-waiting-time/description/
# lang=python

# 解法:按照题意模拟。按顺序遍历顾客，cur表示能够开始招待该顾客的时间，
# 当cur小于arrival时，从arrival开始做菜，否则从cur时刻开始做菜。

class Solution:
	def averageWaitingTime(self, customers: list[list[int]]) -> float:
		n = len(customers)
		tot = cur = 0
		for arrival, t in customers:
			if cur < arrival:
				cur = arrival
			cur += t
			tot += cur - arrival
		return tot / n


if __name__ == "__main__":
	import time

	t0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)
	print(func(customers=[[1, 2], [2, 5], [4, 3]]))
	# 输出：5.00000
	print(func(customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))
	# 输出：3.25000

	t1 = time.time()
	print(t1 - t0)
