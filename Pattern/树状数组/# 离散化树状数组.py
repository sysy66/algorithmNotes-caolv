# 离散化树状数组
# 剑指 Offer 51. 数组中的逆序对

class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.a[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x, dt):
        while x <= self.n:
            self.a[x] += dt
            x += BIT.lowbit(x)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 离散化
        v2i = {v: i for i, v in enumerate(sorted(set(nums)), 1)}
        # 树状数组统计逆序对
        bit = BIT(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            x = v2i[nums[i]]
            ans += bit.query(x - 1)
            bit.update(x, 1)
            
        return ans

"""作者：LeetCode-Solution
链接：https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        v2i = {v: i for i, v in enumerate(sorted(set(nums)), 1)}
        nums = [v2i[x] for x in nums[::-1]]
        a, ans = [0] * ((n := len(v2i)) + 1), 0

        for x in nums:
            x1, res = x, 0
            x -= 1
            while x: res, x = res + a[x], x - (x & -x)
            ans += res
            x = x1
            while x <= n: a[x], x = a[x] + 1, x + (x & -x)
        return ans