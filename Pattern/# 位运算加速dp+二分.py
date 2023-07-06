# 位运算加速dp+二分
# LCP 65. 舒适的湿度

class Solution:
    def unSuitability(self, nums: list[int]) -> int:
        def check(mid: int) -> bool:
            mask = (1 << (mid + 1)) - 1
            dp = mask
            for num in nums:
                dp = ((dp << num) | (dp >> num)) & mask
            return dp != 0

        left, right = 0, max(nums) * 2  # 实际的上界为 max(nums)*2
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

作者：981377660LMT
链接：https://leetcode.cn/problems/3aqs1c/solution/python-by-981377660lmt-1ug9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。