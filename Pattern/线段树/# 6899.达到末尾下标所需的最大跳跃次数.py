# 6899.达到末尾下标所需的最大跳跃次数.py
# https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/
# 线段树(动态开点+懒标记+区间最大值)


MAX_RANGE = int(1e9 + 7)


class SegmentTree:
	__slots__ = ("cnt", "lazy")

	def __init__(self) -> None:
		self.cnt = defaultdict(lambda: -1)
		self.lazy = defaultdict(lambda: -1)

	def query(self, L: int, R: int) -> int:
		return self.__query(L, R, -MAX_RANGE, MAX_RANGE, 1)

	def __query(self, L: int, R: int, l: int, r: int, o: int) -> int:
		if l == r:
			return self.cnt[o]
		self.__push_down(o)
		m = (l + r) >> 1
		res = -1
		if L <= m:
			res = max(res, self.__query(L, R, l, m, 2 * o))
		if R > m:
			res = max(res, self.__query(L, R, m + 1, r, 2 * o + 1))
		return res

	# 更新区间最值
	def update(self, L: int, R: int, delta: int) -> None:
		self.__update(L, R, -MAX_RANGE, MAX_RANGE, 1, delta)

	def __update(self, L: int, R: int, l: int, r: int, o: int, delta: int) -> None:
		if L <= l and r <= R:
			self.cnt[o] = max(self.cnt[o], delta)
			self.lazy[o] = max(self.lazy[o], delta)
			return
		self.__push_down(o)
		m = (l + r) >> 1
		if L <= m:
			self.__update(L, R, l, m, 2 * o, delta)
		if R > m:
			self.__update(L, R, m + 1, r, 2 * o + 1, delta)
		self.cnt[o] = max(self.cnt[2 * o], self.cnt[2 * o + 1])

	def __push_down(self, o):
		if self.lazy[o] != -1:
			self.cnt[2 * o] = max(self.cnt[2 * o], self.lazy[o])
			self.cnt[2 * o + 1] = max(self.cnt[2 * o + 1], self.lazy[o])
			self.lazy[2 * o] = max(self.lazy[2 * o], self.lazy[o])
			self.lazy[2 * o + 1] = max(self.lazy[2 * o + 1], self.lazy[o])
			self.lazy[o] = -1


class Solution:
	def maximumJumps(self, nums: List[int], target: int) -> int:
		n = len(nums)
		seg = SegmentTree()
		seg.update(nums[0], nums[0], 0)
		for i, x in enumerate(nums):
			if i == 0: continue
			y = seg.query(x - target, x + target)
			if i == n - 1:
				if y == -1:
					ans = -1
				else:
					ans = y + 1
			if y == -1: continue
			seg.update(x, x, y + 1)
		return ans

		