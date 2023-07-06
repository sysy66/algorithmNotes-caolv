# 珂朵莉树(查询和更新和删除).py
# 715. Range 模块
# 半开区间 [left, right)

from sortedcontainers import SortedDict


class RangeModule:

    def __init__(self):
        self.d = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        i = self.d.bisect_left(left)
        while i < len(self.d) and self.d.values()[i] <= right:
            r, l = self.d.items()[i]
            left = min(left, l)  # 合并后的新区间，其左端点为所有被覆盖的区间的左端点的最小值
            right = max(right, r)  # 合并后的新区间，其右端点为所有被覆盖的区间的右端点的最大值
            self.d.popitem(i)
        self.d[right] = left

    def queryRange(self, left: int, right: int) -> bool:
        i = self.d.bisect_left(left)
        if i == len(self.d):
            return False
        r, l = self.d.items()[i]
        return l <= left and right <= r

    def removeRange(self, left: int, right: int) -> None:
        i = self.d.bisect_left(left)
        if i < len(self.d):
            r, l = self.d.items()[i]
            if l < left:
                self.d[left] = l
                i += 1
        while i < len(self.d) and self.d.values()[i] <= right:
            r, l = self.d.items()[i]
            if r > right:
                self.d[r] = right
                break
            else:
                self.d.popitem(i)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
