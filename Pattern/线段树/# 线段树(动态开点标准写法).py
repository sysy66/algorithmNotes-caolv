# 动态开点线段树
# 715. Range 模块
# 标准写法，功能：区域覆盖


MAX_RANGE = int(1e9 + 7)
from typing import Optional


class Node:
    __slots__ = ("left", "right", "val", "lazy")

    def __init__(
            self,
            left: Optional["Node"] = None,
            right: Optional["Node"] = None,
            val=False,
            lazy=False
    ) -> None:
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy


class SegentTree:
    def __init__(self):
        self.root = Node()

    def update(self, L: int, R: int, delta: bool):
        return self._update(L, R, 0, MAX_RANGE, self.root, delta)

    def query(self, L: int, R: int):
        return self._query(L, R, 0, MAX_RANGE, self.root)

    def _update(self, L: int, R: int, l: int, r: int, node: Node, delta: bool):
        if L <= l and r <= R:
            node.val = delta
            node.lazy = True
            return
        self._pushdown(node)
        m = (l + r) >> 1
        if L <= m: self._update(L, R, l, m, node.left, delta)
        if R > m: self._update(L, R, m + 1, r, node.right, delta)
        self._pushup(node)

    def _query(self, L: int, R: int, l: int, r: int, node: Node):
        if L <= l and r <= R:
            return node.val
        self._pushdown(node)
        m = (l + r) >> 1
        ret = True
        if L <= m: ret &= self._query(L, R, l, m, node.left)
        if R > m: ret &= self._query(L, R, m + 1, r, node.right)
        return ret

    def _pushdown(self, node: Node):
        if not node.left: node.left = Node()
        if not node.right: node.right = Node()
        if node.lazy:
            node.left.lazy = node.right.lazy = True
            node.left.val = node.right.val = node.val
            node.lazy = False

    def _pushup(self, node: Node):
        node.val = node.left.val & node.right.val


class RangeModule:
    def __init__(self):
        self.st = SegentTree()

    def addRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, False)
        return res