//2581.统计可能的树根数目
//https://leetcode.cn/problems/count-number-of-possible-root-nodes/description/
//lang=golang
//
//解法:换根DP

package main

import "fmt"

func rootCount(edges [][]int, guesses [][]int, k int) (ret int) {
    g := make([][]int, len(edges) + 1)
    for _, e := range edges {
        u, v := e[0], e[1]
        g[u] = append(g[u], v)
        g[v] = append(g[v], u)
    }

    type pair struct { x, y int }
    s := map[pair]int{}
    for _, e := range guesses {
        u, v := e[0], e[1]
        s[pair{u, v}] = 1
    }

    cnt := 0
    var dfs func(x, fa int)
    dfs = func(x, fa int) {
        for _, y := range g[x] {
            if y != fa {
                cnt += s[pair{x, y}]
                dfs(y, x)
            }
        }
    }
    dfs(0, -1)

    var reroot func(x, fa int)
    reroot = func(x, fa int) {
        if cnt >= k {
            ret++
        }
        for _, y := range g[x] {
            if y != fa {
                cnt -= s[pair{x, y}] - s[pair{y, x}]
                reroot(y, x)
                cnt += s[pair{x, y}] - s[pair{y, x}]
            }
        }
    }
    reroot(0, -1)
    return
}

func main() {
	f := rootCount
	fmt.Println(f([][]int{{0, 1}, {1,2}, {1,3}, {4,2}},[][]int{{1,3},{0,1},{1,0},{2,4}}, 3))
	fmt.Println(f([][]int{{0, 1}, {1,2}, {2,3}, {3,4}},[][]int{{1,0},{3,4},{2,1},{3,2}}, 1))
	// 	输出：3
	// 	输出：5
}