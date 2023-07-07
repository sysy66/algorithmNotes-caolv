# 二分查找的三种写法

# type:1
def f1(nums, target):
	n = len(nums)
	lt, rt = -1, n
	while lt + 1 < rt:
		mid = (lt + rt) // 2
		if nums[mid] <= target:
			lt = mid
		else:
			rt = mid
	return rt
	
# type:2
def f2(nums, target):
	n = len(nums)
	lt, rt = 0, n
	while lt + 1 <= rt:
		mid = (lt + rt) // 2
		if nums[mid] <= target:
			lt = mid + 1
		else:
			rt = mid
	return rt

# type:3
def f3(nums, target):
	n = len(nums)
	lt, rt = 0, n - 1
	while lt <= rt:
		mid = (lt + rt) // 2
		if nums[mid] <= target:
			lt = mid + 1
		else:
			rt = mid - 1
	return lt

print("start")
from bisect import bisect_right
nums = list(range(100))
for x in range(-100, 200):
	if not (bisect_right(nums, x) == f1(nums, x) == f2(nums, x) == f3(nums, x)):
		print(x)
print("end")
