# 线段树(懒标记+区间值更新+区间最小值).py
# 1851. 包含每个查询的最小区间

class SegmentTree:
    __slots__ = ('n', "cnt", "lazy")
    
    def __init__(self, n: int) -> None:
        self.n = n
        self.cnt = [0x3f3f3f3f] * (2 << n.bit_length())
        self.lazy = [0x3f3f3f3f] * (2 << n.bit_length())

    # 查询点的最小值
    def query(self, P: int) -> int:
        return self.__query(P, 0, self.n - 1, 1)
    
    def __query(self, P: int, l: int, r: int, o: int) -> int:
        if l == r:
            return self.cnt[o]
        self.__push_down(o)
        m = (l + r) >> 1
        if P <= m:
            return self.__query(P, l, m, 2 * o)
        else:
            return self.__query(P, m + 1, r, 2 * o + 1)

    # 更新区间最小值
    def update(self, L: int, R: int, delta: int) -> None:
        self.__update(L, R, 0, self.n - 1, 1, delta)

    def __update(self, L: int, R: int, l: int, r: int, o: int, delta: int) -> None:
        if L <= l and r <= R:
            self.cnt[o] = min(self.cnt[o], delta)
            self.lazy[o] = min(self.lazy[o], delta)
            return
        self.__push_down(o)
        m = (l + r) >> 1
        if L <= m:
            self.__update(L, R, l, m, 2 * o, delta)
        if R > m:
            self.__update(L, R, m + 1, r, 2 * o + 1, delta)
        self.cnt[o] = min(self.cnt[2 * o], self.cnt[2 * o + 1])

    def __push_down(self, o):
        if self.lazy[o] != 0x3f3f3f3f:
            self.cnt[2 * o] = min(self.cnt[2 * o], self.lazy[o])
            self.cnt[2 * o + 1] = min(self.cnt[2 * o + 1], self.lazy[o])
            self.lazy[2 * o] = min(self.lazy[2 * o], self.lazy[o])
            self.lazy[2 * o + 1] = min(self.lazy[2 * o + 1], self.lazy[o])
            self.lazy[o] == 0x3f3f3f3f


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # 离散化
        points = set(queries)
        for s, e in intervals:
            points.add(s)
            points.add(e)
        v2i = {v: i for i, v in enumerate(sorted(points))}
        # 创建线段树
        seg = SegmentTree(len(points))
        for left, right in intervals:
            size = right - left + 1
            left = v2i[left]
            right = v2i[right]
            seg.update(left, right, size)
        # 单点查询
        ans = list()
        for q in queries:
            idx = v2i[q]
            sz = seg.query(idx)
            ans.append(sz if sz != 0x3f3f3f3f else -1)
        #
        return ans

