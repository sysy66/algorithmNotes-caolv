#线段树，离散化，注意懒标记
#218. 天际线问题

class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.cnt = [0] * (2 << n.bit_length())
        self.lazy = [0] * (2 << n.bit_length())

    def update(self, L: int, R: int, delta: int) -> None:
        self._update(L, R, 0, self.n - 1, 1, delta)

    def query(self, P: int) -> int:
        return self._query(P, 0, self.n - 1, 1)

    def _update(self, L: int, R: int, l: int, r: int, o: int, delta: int) -> None:
        if L <= l and r <= R:
            self.cnt[o] = max(self.cnt[o], delta)
            self.lazy[o] = max(self.lazy[o], delta)
            return
        self._pushdown(o)
        m = (l + r) >> 1
        if L <= m: self._update(L, R, l, m, 2 * o, delta)
        if R > m: self._update(L, R, m + 1, r, 2 * o + 1, delta)
        self._pushup(o)

    def _query(self, P: int, l: int, r: int, o: int) -> int:
        if l == P == r:
            return self.cnt[o]
        self._pushdown(o)
        m = (l + r) >> 1
        ret = 0
        if P <= m: ret = max(ret, self._query(P, l, m, 2 * o))
        if P > m: ret = max(ret, self._query(P, m + 1, r, 2 * o + 1))
        return ret

    def _pushdown(self, o: int) -> None:
        # 懒标记下放
        if self.lazy[o]:
            self.cnt[2 * o] = max(self.cnt[2 * o], self.lazy[o])
            self.cnt[2 * o + 1] = max(self.cnt[2 * o + 1], self.lazy[o])
            self.lazy[2 * o] = max(self.lazy[2 * o], self.lazy[o])
            self.lazy[2 * o + 1] = max(self.lazy[2 * o + 1], self.lazy[o])
            self.lazy[o] = 0

    def _pushup(self, o: int) -> None:
        self.cnt[o] = max(self.cnt[2 * o], self.cnt[2 * o + 1])


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # 端点去重
        points = set()
        for l, r, _ in buildings:
            points.add(l)
            points.add(r)
        points = sorted(points)
        v2i = {x:i for i, x in enumerate(points)}
        # 离散化更新线段树
        seg = SegmentTree(len(points))
        for l, r, height in buildings:
            seg.update(v2i[l], v2i[r] - 1, height)
        # 按照端点进行关键点查询
        ans = list()
        for p in points:
            height = seg.query(v2i[p])
            if ans and ans[-1][1] == height: continue
            ans.append([p, height])
        return ans