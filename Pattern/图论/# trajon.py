# trajon


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ##构建图
        graph = dict()
        for i in range(n):
            graph[i] = dict()
        for s, v in connections:
            graph[s][v] = 1
            graph[v][s] = 1

        ##无向图中找桥

        low = [0 for i in range(n)]  # 设立最早时间戳
        dfn = [0 for i in range(n)]  # 设立当前时间戳
        res = []

        def dfs(node, pre, time):
            dfn[node] = time  # 初始化时间戳
            low[node] = time
            for nextnode in graph[node]:
                if nextnode != pre and dfn[nextnode] == 0:  # 如果该子节点不为父节点且为被访问过，即未被初始化时间戳
                    dfs(nextnode, node, time + 1)  # 递归子节点
                    if dfn[node] < low[nextnode]:  # 如果子节点最早时间戳仍大于当前节点的时间戳，
                                                   # 说明该子节点并没有回路返回跟早以前，那么他两构成一条唯一的路，找到桥
                        res.append([node, nextnode])
                    low[node] = min(low[node], low[nextnode])  # 更新当前节点的最早时间
                elif nextnode != pre and dfn[nextnode] != 0:  # 如果存在已访问的子节点，跟他比较更新自己的最小时间戳
                    low[node] = min(low[node], dfn[nextnode])

        dfs(0, -1, 1)
        return res

