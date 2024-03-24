//2858.可以到达每一个节点的最少边反转次数
//https://leetcode.cn/problems/minimum-edge-reversals-so-every-node-is-reachable/description/
//lang=golang
//
//解法:换根DP

package main

import "fmt"

func minEdgeReversals(n int, edges [][]int) []int {
    ret := make([]int, n)

    type pair struct { to, dis int }
    g := make([][]pair, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        g[u] = append(g[u], pair{v, 1})
        g[v] = append(g[v], pair{u, -1})
    }

    var dfs func(x, fa int)
    dfs = func(x, fa int) {
        for _, p := range g[x] {
            if p.to != fa {
                if p.dis < 0 {
                    ret[0]++
                }
                dfs(p.to, x)
            }
        }
    }
    dfs(0, -1)

    var reroot func(x, fa int)
    reroot = func(x, fa int) {
        for _, p := range g[x] {
            if p.to != fa {
                ret[p.to] = ret[x] + p.dis
                reroot(p.to, x)
            }
        }
    }
    reroot(0, -1)

    return ret
}

func main() {
	f := minEdgeReversals
	fmt.Println(f(4, [][]int{{2, 0}, {2, 1}, {1, 3}}))
	fmt.Println(f(3, [][]int{{1, 2}, {2, 0}}))
	// 输出：[1,1,0,2]
	// 输出：[2,0,1]
}
