# 线段树(点值更新+区间最大值1.py
# 1964. 找出到每个位置为止最长的有效障碍赛跑路线

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
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        tmp = sorted(set(obstacles))
        v2i = {v: i for i, v in enumerate(tmp)}
        n = len(tmp)
        seg = SegmentTree(n)
        ans = [1] * len(obstacles)

        for i, ob in enumerate(obstacles):
            idx = v2i[ob]
            ans[i] = seg.query(0, idx) + 1
            seg.update(idx, ans[i])
        return ans

# 最长子序列的套路~

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        a = list()
        ans = list()

        for obstacle in obstacles:
            i = bisect_right(a, obstacle)
            if i < len(a):
                a[i] = obstacle
            else:
                a.append(obstacle)
            ans.append(i + 1)
        return ans


