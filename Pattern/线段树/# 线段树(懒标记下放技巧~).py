# 线段树,懒标记技巧~
# 2569. 更新数组后处理求和查询


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.cnt = [0] * (2 << n.bit_length())
        self.lazy = [0] * (2 << n.bit_length())

    def update(self, L: int, R: int) -> None:
        self._update(L, R, 0, self.n - 1, 1)

    def query(self, L: int, R: int) -> int:
        return self._query(L, R, 0, self.n - 1, 1)

    def _update(self, L: int, R: int, l: int, r: int, o: int) -> None:
        if L <= l and r <= R:
            self.cnt[o] = r - l + 1 - self.cnt[o]
            self.lazy[o] ^= 1
            return
        self._pushdown(o, l, r)
        m = (l + r) >> 1
        if L <= m: self._update(L, R, l, m, 2 * o)
        if R > m: self._update(L, R, m + 1, r, 2 * o + 1)
        self._pushup(o)
    
    def _query(self, L: int, R: int, l: int, r: int, o: int) -> int:
        if L <= l and r <= R:
            return self.cnt[o]
        self._pushdown(o, l, r)
        m = (l + r) >> 1
        ret = 0
        if L <= m: ret += self._query(L, R, l, m, 2 * o)
        if R > m: ret += self._query(L, R, m + 1, r, 2 * o + 1)
        return ret

    def _pushdown(self, o: int, l: int, r: int) -> None:
        # 懒标记下放
        if self.lazy[o]:
            m = (l + r) >> 1
            self.cnt[2 * o] = m - l + 1 - self.cnt[2 * o]
            self.cnt[2 * o + 1] = r - m - self.cnt[2 * o + 1]
            self.lazy[2 * o] ^= 1
            self.lazy[2 * o + 1] ^= 1
            self.lazy[o] = 0

    def _pushup(self, o: int) -> None:
        self.cnt[o] = self.cnt[2 * o] + self.cnt[2 * o + 1]


class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        tot, n = sum(nums2), len(nums2)
        st = SegmentTree(n)
        ans = list()
        for i, x in enumerate(nums1):
            if x: st.update(i, i)
        for _type, l, r in queries:
            if _type == 3: ans.append(tot)
            elif _type == 2: tot += l * st.query(0, n - 1)
            else: st.update(l, r)
        return ans


作者：少阴少阳
链接：https://leetcode.cn/problems/handling-sum-queries-after-update/solutions/2119459/python3xian-duan-shu-lan-biao-ji-xia-fan-v7hv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。