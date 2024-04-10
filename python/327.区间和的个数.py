# 327.区间和的个数.py
# https://leetcode.cn/problems/count-of-range-sum/description/
# lang=python
from itertools import accumulate
from typing import List


# 解法1: mergesort_模板

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
        # for i in range(len(tmp)):
        #     nums[L + i] = tmp[i]
        nums[L:R + 1] = tmp


# 作者：XingHe
# 链接：https://leetcode.cn/problems/count-of-range-sum/solutions/1256482/cpython3-0er-fen-1gui-bing-pai-xu-2shu-z-9dc4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

####################################################################################

# 解法2: 官解写法

class Solution1:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefixSum = list(accumulate(nums, initial=0))
        
        def mergeCount(arr: List[int]) -> int:
            n = len(arr)
            if n <= 1:
                return 0
            
            n1, n2 = arr[:n // 2], arr[n // 2:]
            cnt = mergeCount(n1) + mergeCount(n2)
            l, r = 0, 0
            for v in n1:
                while l < len(n2) and n2[l] < v + lower:
                    l += 1
                while r < len(n2) and n2[r] < v + upper + 1:
                    r += 1
                cnt += r - l
            
            p1, p2 = 0, 0
            for i in range(len(arr)):
                if p1 < len(n1) and (p2 == len(n2) or n1[p1] <= n2[p2]):
                    arr[i] = n1[p1]
                    p1 += 1
                else:
                    arr[i] = n2[p2]
                    p2 += 1
            return cnt
        
        return mergeCount(prefixSum)


if __name__ == "__main__":
    import time
    
    t_0 = time.time()
    
    s = Solution()
    # s = Solution1()
    func = getattr(s, "countRangeSum")
    print(func)
    
    print(func(nums=[-2, 5, -1], lower=-2, upper=2))
    # 输出：3
    print(func(nums=[0], lower=0, upper=0))
    # 输出：1
    
    t_1 = time.time()
    print(t_1 - t_0)
