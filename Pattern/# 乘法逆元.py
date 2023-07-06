# 乘法逆元
# 1916. 统计为蚁群构筑房间的不同顺序

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10**9 + 7
        
        n = len(prevRoom)
        # fac[i] 表示 i!
        # inv[i] 表示 i! 的乘法逆元
        fac, inv = [0] * n, [0] * n
        fac[0] = inv[0] = 1
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod
            # 使用费马小定理计算乘法逆元
            inv[i] = pow(fac[i], mod - 2, mod)
        
        # 构造树
        edges = defaultdict(list)
        for i in range(1, n):
            edges[prevRoom[i]].append(i)
        
        f, cnt = [0] * n, [0] * n
        
        def dfs(u: int) -> None:
            f[u] = 1
            for v in edges[u]:
                dfs(v)
                # 乘以左侧的 f[ch] 以及右侧分母中 cnt[ch] 的乘法逆元
                f[u] = f[u] * f[v] * inv[cnt[v]] % mod
                cnt[u] += cnt[v]
            # 乘以右侧分子中的 (cnt[i] - 1)!
            f[u] = f[u] * fac[cnt[u]] % mod
            cnt[u] += 1
        
        dfs(0)
        return f[0]