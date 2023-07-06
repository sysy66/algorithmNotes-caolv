lt, rt = -1, n
while lt + 1 < rt:
	mid = (lt + rt) // 2
	if nums[mid] <= target:
		lt = mid
	else:
		rt = mid
//rt的取值范围[0,n]闭区间