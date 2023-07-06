# 状态压缩动态规划(5 个二进制位存储信息).py
# 1815. 得到新鲜甜甜圈的最多组数

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        kWidth = 5
        kWidthMask = (1 << kWidth) - 1

        cnt = Counter(x % batchSize for x in groups)

        start = 0
        for i in range(batchSize - 1, 0, -1):
            start = (start << kWidth) | cnt[i]

        @cache
        def dfs(mask: int) -> int:
            if mask == 0:
                return 0

            total = 0
            for i in range(1, batchSize):
                amount = ((mask >> ((i - 1) * kWidth)) & kWidthMask)
                total += i * amount

            best = 0
            for i in range(1, batchSize):
                amount = ((mask >> ((i - 1) * kWidth)) & kWidthMask)
                if amount > 0:
                    result = dfs(mask - (1 << ((i - 1) * kWidth)))
                    if (total - i) % batchSize == 0:
                        result += 1
                    best = max(best, result)

            return best

        ans = dfs(start) + cnt[0]
        dfs.cache_clear()
        return ans

"""作者：力扣官方题解
链接：https://leetcode.cn/problems/maximum-number-of-groups-getting-fresh-donuts/solutions/2071849/de-dao-xin-xian-tian-tian-quan-de-zui-du-pzra/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

# 按 313131 进制数来处理
class Solution:

    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:

        @cache

        def dfs(cur, rest):

            res = 0

            for i in range(1,batchSize):

                if rest // (31 ** i) % 31 > 0:

                    res = max(res, (cur==0) + dfs((cur+i)%batchSize, rest - 31 ** i))

            return res

        dfs.cache_clear()

        rest = [0] * batchSize

        for each in groups:

            rest[each % batchSize] += 1

        return rest[0] + dfs(0, sum(rest[i]*31**i for i in range(1,batchSize)))

作者：oldyan
链接：https://leetcode.cn/problems/maximum-number-of-groups-getting-fresh-donuts/solutions/698629/cji-yi-hua-sou-suo-by-oldyan-658o/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。