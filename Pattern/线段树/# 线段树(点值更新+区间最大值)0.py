# 线段树(点值更新+区间最大值)0.py
# 1235. 规划兼职工作

class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.cnt = [0] * (2 << n.bit_length())

    def update(self, idx: int, delta: int) -> None:
        self.__update(1, 0, self.n - 1, idx, delta)

    def query(self, L: int, R: int) -> int:
        return self.__query(L, R, 1, 0, self.n - 1)

    def __update(self, o: int, l: int, r: int, idx: int, delta: int) -> int:
        if l == r:
            self.cnt[o] = delta
            return
        m = (l + r) >> 1
        if idx <= m: self.__update(2 * o, l, m, idx, delta)
        if idx > m: self.__update(2 * o + 1, m + 1, r, idx, delta)
        self.cnt[o] = max(self.cnt[2 * o], self.cnt[2 * o + 1])

    def __query(self, L: int, R: int, o: int, l: int, r: int) -> int:
        if L <= l and r <= R:
            return self.cnt[o]
        m = (l + r) >> 1
        ret = 0
        if L <= m: ret = max(ret, self.__query(L, R, 2 * o, l, m))
        if R > m: ret = max(ret, self.__query(L, R, 2 * o + 1, m + 1, r))
        return ret


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        v2i = {v: i for i, v in enumerate(sorted(set(startTime + endTime)))}
        startTime = [v2i[v] for v in startTime]
        endTime = [v2i[v] for v in endTime]
        sep = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        n = len(v2i)
        seg = SegmentTree(n)
        for s, e, p in sep:
            cur = max(seg.query(0, s) + p, seg.query(s + 1, e))
            seg.update(e, cur)
        return seg.query(0, n - 1)

# 二分做法

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # v2i = {v: i for i, v in enumerate(sorted(set(startTime + endTime)))}
        # startTime = [v2i[v] + 1 for v in startTime]
        # endTime = [v2i[v] + 1 for v in endTime]
        sep = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        a = [(0, 0)]
        for s, e, p in sep:
            i = bisect_left(a, (s + 1, )) - 1
            j = bisect_left(a, (e + 1, )) - 1
            cur = max(a[i][1] + p, a[j][1])
            bisect.insort(a, (e, cur))
        return a[-1][1]

