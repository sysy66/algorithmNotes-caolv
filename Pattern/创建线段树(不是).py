class RangeModule:

    def __init__(self):
        self.range = [0x3f3f3f3f]

    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect(self.range, left)
        j = bisect.bisect(self.range, right)
        if i & 1 and j & 1:
            if i == j:
                pass
            else:
                del self.range[i:j]
        elif i & 1 and not j & 1:
            self.range.insert(j, right)
            del self.range[i:j]
        elif not i & 1 and j & 1:
            self.range.insert(i, left)
            del self.range[i + 1:j + 1]
            if self.range.count(left) == 2:
                self.range.remove(left)
                self.range.remove(left)
        else:
            if i == j:
                self.range.insert(j, right)
                self.range.insert(i, left)
            else:
                self.range.insert(j, right)
                self.range.insert(i, left)
                del self.range[i + 1:j + 1]
        if self.range.count(right) == 2:
            self.range.remove(right)
            self.range.remove(right)
        if self.range.count(left) == 2:
            self.range.remove(left)
            self.range.remove(left)


    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect(self.range, left)
        j = bisect.bisect_left(self.range, right)
        if i & 1 and j & 1 and i == j:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect(self.range, left)
        j = bisect.bisect(self.range, right)
        if i & 1 and j & 1:
            if i == j:
                self.range.insert(j, right)
                self.range.insert(i, left)
            else:
                self.range.insert(j, right)
                self.range.insert(i, left)
                del self.range[i + 1:j + 1]
        elif i & 1 and not j & 1:
            self.range.insert(i, left)
            del self.range[i + 1:j + 1]
        elif not i & 1 and j & 1:
            self.range.insert(j, right)
            del self.range[i:j]
        else:
            if i == j:
                pass
            else:
                del self.range[i:j]
        if self.range.count(right) == 2:
            self.range.remove(right)
            self.range.remove(right)
        if self.range.count(left) == 2:
            self.range.remove(left)
            self.range.remove(left)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)