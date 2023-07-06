# Dijkstra 算法.py
# 1368. 使网格图至少有一条有效路径的最小代价

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [0] + [inf] * (m * n - 1)
        seen = set()
        q = [(0, 0, 0)]

        while q > 0:
            cur_dis, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            cur_pos = x * n + y
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_pos = nx * n + ny
                new_dis = cur_dis + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n and new_dis < dist[new_pos]:
                    dist[new_pos] = new_dis
                    heapq.heappush(q, (new_dis, nx, ny))
        
        return dist[m * n - 1]

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solution/shi-wang-ge-tu-zhi-shao-you-yi-tiao-you-xiao-lu-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        q = [(0, 0, 0)]

        while q:
            cur_dis, x, y = heapq.heappop(q)
            if (x, y) in seen:
                continue
            if x == m - 1 and y == n - 1:
                return cur_dis
            seen.add((x, y))
            for i, (nx, ny) in enumerate([(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]):
                new_dis = cur_dis + (1 if grid[x][y] != i + 1 else 0)
                if 0 <= nx < m and 0 <= ny < n:
                    heapq.heappush(q, (new_dis, nx, ny))
        