# 分治1.py
# 2407. 最长递增子序列 II

class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        n = len(nums)
        positions = list(range(n))
        positions.sort(key=lambda x:(nums.__getitem__(x), -x))
        dp = [1] * n

        def DivideAndConquer(l, r, positions):
            dac = DivideAndConquer
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
            que = deque()
            for pos in positions:
                if pos <= m:
                    while que and dp[pos] >= dp[que[-1]]:
                        que.pop()
                    que.append(pos)
                else:
                    while que and nums[que[0]] < nums[pos] - k:
                        que.popleft()
                    if que: dp[pos] = max(dp[pos], dp[que[0]] + 1)
            #
            dac(m + 1, r, right)

        DivideAndConquer(0, n - 1, positions)
        return max(dp)