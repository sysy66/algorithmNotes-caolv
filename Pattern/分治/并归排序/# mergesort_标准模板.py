# mergesort_标准模板
# 327. 区间和的个数

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.res = 0
        n = len(nums)
        prefixsum = [0 for _ in range(n + 1)]
        for i in range(n):
            prefixsum[i + 1] = prefixsum[i] + nums[i]

        self.mergesort(prefixsum, 0, len(prefixsum) - 1)
        return self.res

    def mergesort(self, nums: List[int], L: int, R: int) -> None:
        if L < R:
            mid = L + (R - L) // 2
            self.mergesort(nums, L, mid)
            self.mergesort(nums, mid + 1, R)
            self.merge(nums, L, mid, R)

    def merge(self, nums: List[int], L: int, mid: int, R: int) -> None:
        #########################################
        ## 套用标准的归并排序   本题需要单独计算的地方
        ii, jj, kk = L, mid + 1, mid + 1
        while ii <= mid:
            while jj <= R and nums[jj] - nums[ii] < self.lower:
                jj += 1
            while kk <= R and nums[kk] - nums[ii] <= self.upper:
                kk += 1
            self.res += (kk - jj)
            ii += 1
        #########################################
        i, j = L, mid + 1
        tmp = []
        while i <= mid and j <= R:
            if nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        if i <= mid:
            tmp += nums[i: mid + 1]
        if j <= R:
            tmp += nums[j: R + 1]
        """for i in range(len(tmp)):
                                    nums[L + i] = tmp[i]"""
        nums[L:R + 1] = tmp


"""作者：XingHe_XingHe
链接：https: // leetcode.cn / problems / count - of - range - sum / solution / cpython3 - 0
er - fen - 1
gui - bing - pai - xu - 2
shu - z - 9
dc4 /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""