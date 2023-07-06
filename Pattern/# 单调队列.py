# 单调队列
# 239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        st = deque()
        for i, num in enumerate(nums):
            while st and nums[st[-1]] <= num:
                st.pop()
            st.append(i)
            if i - st[0] == k:
                st.popleft()
            ans.append(nums[st[0]])
        return ans[k - 1:]