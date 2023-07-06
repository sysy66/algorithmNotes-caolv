# 树状数组
# 1409. 查询带键的排列

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
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        n = len(queries)
        bit = BIT(m + n)

        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = n + i
            bit.update(n + i, 1)

        ans = list()
        for i, query in enumerate(queries):
            cur = pos[query]
            bit.update(cur, -1)
            ans.append(bit.query(cur))
            cur = pos[query] = n - i
            bit.update(cur, 1)
        return ans


"""作者：LeetCode - Solution
链接：https: // leetcode.cn / problems / queries - on - a - permutation -
with-key / solution / cha - xun - dai - jian - de - pai - lie - by - leetcode - solution /
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""