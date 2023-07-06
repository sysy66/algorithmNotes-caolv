# 动态开点线段树
# 2276. 统计区间中的整数数目
# 节点自带范围~self.l, self,r

class CountIntervals:
    __slots__ = ("left", "right", 'l', 'r', "cnt")

    def __init__(self, l=1, r=int(1e9 + 7)):
        self.left = self.right = None
        self.l, self.r, self.cnt = l, r, 0

    def add(self, L: int, R: int) -> None:
        if self.cnt == self.r - self.l + 1: return
        if L <= self.l and self.r <= R:
            self.cnt = self.r - self.l + 1
            return
        m = (self.l + self.r) >> 1
        if not self.left:
            self.left = CountIntervals(self.l, m)
            self.right = CountIntervals(m + 1, self.r)
        if L <= m: self.left.add(L, R)
        if R > m: self.right.add(L, R)
        self.cnt = self.left.cnt + self.right.cnt

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

作者：endlesscheng
链接：https://leetcode.cn/problems/count-integers-in-intervals/solution/by-endlesscheng-clk2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。