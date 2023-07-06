# 珂朵莉树(查询和更新).py
# LCP 32. 批量处理任务

from sortedcontainers import SortedDict


class OldDriveTree:
    def __init__(self):
        self.a = SortedDict()

    def query(self, left: int, right: int) -> int:
        a = self.a
        i = a.bisect_left(left)
        ret = 0
        while i < len(a) and a.values()[i] <= right:
            r, l = a.items()[i]
            ret += min(r, right) - max(l, left) + 1
            i += 1
        return ret

    def update(self, left: int, right: int) -> None:
        a = self.a
        i = a.bisect_left(left)
        while i < len(a) and a.values()[i] <= right:
            r, l = a.items()[i]
            left = min(left, l)
            right = max(right, r)
            a.popitem(i)
        a[right] = left


class Solution:
    def processTasks(self, tasks: list[list[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        odt = OldDriveTree()
        ans = 0
        for start, end, period in tasks:
            target = period - odt.query(start, end)
            if target <= 0: continue
            ans += target
            left, right = end - period + 2, end
            while left <= right:
                mid = (left + right) >> 1
                if end - mid + 1 - odt.query(mid, end) >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            odt.update(right, end)
        return ans

作者：少阴少阳
链接：https://leetcode.cn/problems/t3fKg1/solutions/2163863/python3tan-xin-pai-xu-ke-duo-li-shu-lao-u5xcx/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。