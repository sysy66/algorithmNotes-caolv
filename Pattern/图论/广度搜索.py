import collections

grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]

n = len(grid)

for i in range(n):
    for j in range(n):
        if grid[i][j]: que = collections.deque([(i, j, 0)]);vis = {(i, j)}

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
que1 = collections.deque([])

while que:
    x, y, dis = que.popleft()
    que1.append((x, y, dis))
    for t in range(4):
        i = x + dr[t]
        j = y + dc[t]
        if 0 <= i < n and 0 <= j < n and grid[i][j] and (i, j) not in vis:
            que.append((i, j, 0))
            vis.add((i, j))

while que1:
    x, y, dis = que1.popleft()
    for t in range(4):
        i = x + dr[t]
        j = y + dc[t]
        if 0 <= i < n and 0 <= j < n and grid[i][j] == 0 and (i, j) not in vis:
            que1.append((i, j, dis + 1))
            vis.add((i, j))
        if 0 <= i < n and 0 <= j < n and grid[i][j] and (i, j) not in vis:
            print(dis)

