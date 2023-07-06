# 分治0.py
# 300. 最长递增子序列

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        positions = list(range(n))
        positions.sort(key=lambda x:(nums.__getitem__(x), -x))
        dp = [1] * n

        # dac means DivideAndConquer
        def dac(l, r, positions):
            if l == r:
                return
            m = (l + r) >> 1
            left, right = [], []
            for pos in positions:
                if pos <= m:
                    left.append(pos)
                else:
                    right.append(pos)
            dac(l, m, left)
            #
            mx = 0
            for pos in positions:
                if pos <= m:
                    mx = max(mx, dp[pos])
                else:
                    dp[pos] = max(dp[pos], mx + 1)
            #
            dac(m + 1, r, right)

        dac(0, n - 1, positions)
        return max(dp)

        
################################################################
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        positions = list(range(n := len(nums)))
        positions.sort(key=lambda x: (nums.__getitem__(x), -x))

        self.dp = [1] * n
        self.DivideAndConquer(positions, 0, n - 1)
        return max(self.dp)

    def DivideAndConquer(self, nums: list[int], L: int, R: int) -> None:
        if L < R:
            mid = (L + R) >> 1
            left, right = self.Divide(nums, mid)
            self.DivideAndConquer(left, L, mid)
            self.Conquer(nums, mid)
            self.DivideAndConquer(right, mid + 1, R)

    def Divide(self, nums: list[int], mid: int) -> tuple:
        left, right = list(), list()
        for x in nums:
            if x <= mid:
                left.append(x)
            else:
                right.append(x)
        return left, right

    def Conquer(self, nums: list[int], mid: int) -> None:
        c = 0
        for x in nums:
            if x <= mid:
                c = max(c, self.dp[x])
            else:
                self.dp[x] = max(self.dp[x], c + 1)