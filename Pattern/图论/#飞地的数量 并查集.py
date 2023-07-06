#飞地的数量 并查集

class UnionFind:
    def __init__(self, grid: List[List[int]]):
        m, n = len(grid), len(grid[0])
        self.parent = [0] * (m * n)
        self.rank = [0] * (m * n)
        self.onEdge = [False] * (m * n)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    self.parent[idx] = idx
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self.onEdge[idx] = True

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.onEdge[y] |= self.onEdge[x]
        else:
            self.parent[y] = x
            self.onEdge[x] |= self.onEdge[y]
            self.rank[x] += 1

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    idx = i * n + j
                    if j + 1 < n and grid[i][j + 1]:
                        uf.merge(idx, idx + 1)
                    if i + 1 < m and grid[i + 1][j]:
                        uf.merge(idx, idx + n)
        return sum(grid[i][j] and not uf.onEdge[uf.find(i * n + j)] for i in range(1, m - 1) for j in range(1, n - 1))

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/number-of-enclaves/solution/fei-di-de-shu-liang-by-leetcode-solution-nzs3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。