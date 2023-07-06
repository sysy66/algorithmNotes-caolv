# 动态开点线段树
# 715. Range 模块
# 不用Node的写法，功能：区域覆盖


MAX_RANGE = int(1e9 + 7)


class SegentTree:
    def __init__(self):
        self.val = defaultdict(bool)
        self.lazy = defaultdict(bool)

    def update(self, L: int, R: int, delta: bool):
        return self._update(L, R, 0, MAX_RANGE, 1, delta)

    def query(self, L: int, R: int):
        return self._query(L, R, 0, MAX_RANGE, 1)

    def _update(self, L: int, R: int, l: int, r: int, o: int, delta: bool):
        if L <= l and r <= R:
            self.val[o] = delta
            self.lazy[o] = True
            return
        self._pushdown(o)
        m = (l + r) >> 1
        if L <= m: self._update(L, R, l, m, 2 * o, delta)
        if R > m: self._update(L, R, m + 1, r, 2 * o + 1, delta)
        self._pushup(o)

    def _query(self, L: int, R: int, l: int, r: int, o: int):
        if L <= l and r <= R:
            return self.val[o]
        self._pushdown(o)
        m = (l + r) >> 1
        ret = True
        if L <= m: ret &= self._query(L, R, l, m, 2 * o)
        if R > m: ret &= self._query(L, R, m + 1, r, 2 * o + 1)
        return ret

    def _pushdown(self, o: int):
        if self.lazy[o]:
            self.lazy[2 * o] = self.lazy[2 * o + 1] = True
            self.val[2 * o] = self.val[2 * o + 1] = self.val[o]
            self.lazy[o] = False

    def _pushup(self, o: int):
        self.val[o] = self.val[2 * o] & self.val[2 * o + 1]


class RangeModule:
    def __init__(self):
        self.st = SegentTree()

    def addRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, False)