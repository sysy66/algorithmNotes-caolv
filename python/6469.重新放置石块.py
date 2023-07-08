# 6469.重新放置石块
#
# lang=python

# 解法：逆序遍历

# In[1]
from typing import List


class Solution:
	def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
		_in, _out = set(), set()  # in记录会有石头最终到达的位置， out记录搬运过程中此处的石头在后续操作中会被搬走
		ft = list(zip(moveFrom, moveTo))
		for f, t in reversed(ft):
			if t not in _out:
				_in.add(t)
			_out.add(f)
		return sorted(_in | (set(nums) - _out))


if __name__ == "__main__":
	import time

	t_0 = time.time()

	s = Solution()
	func_name = dir(s)[-1]
	func = getattr(s, func_name)

	print(func(nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]))
	# 输出：[5,6,8,9]
	print(func(nums=[1, 1, 3, 3], moveFrom=[1, 3], moveTo=[2, 2]))
	# 输出：[2]

	t_1 = time.time()
	print(t_1 - t_0)
