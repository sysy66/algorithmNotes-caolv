# 树状数组简化版.py
# 2519. Count the Number of K-Big Indices


class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        has, ans, c, sm = [0] * ((n := len(nums))+1), 0, defaultdict(list), 0
        for i, v in enumerate(nums): c[v].append(i+1)
        for i in sorted(c):
            for x in c[i]:
                res = 0
                while x: res, x = res + has[x], x - (x & (-x))
                if sm - k >= res >= k: ans += 1
            for x in c[i]:
                while x <= n: has[x], x = has[x] + 1, x + (x & (-x))
            sm += len(c[i])
        return ans

作者：丁飞
链接：https://leetcode.cn/problems/count-the-number-of-k-big-indices/solutions/2036921/11-by-ding-fei-5-szk0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


a = [0] * (n + 1)
res, x = 0, _
while x: res, x = res + a[x], x - (x & -x)
while x <= n: a[x], x = a[x] + 1, x + (x & -x)
