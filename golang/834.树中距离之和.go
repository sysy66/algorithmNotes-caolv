//834.树中距离之和
//https://leetcode.cn/problems/sum-of-distances-in-tree/description/
//lang=golang
//
//解法:换根DP

package main

import "fmt"

func sumOfDistancesInTree(n int, edges [][]int) []int {
    g := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        g[u] = append(g[u], v)
        g[v] = append(g[v], u)
    }

    ret := make([]int, n)
    size := make([]int, n)

    var dfs func(x, fa int)
    dfs = func(x, fa int) {
        size[x] = 1
        for _, y := range g[x] {
            if y != fa {
                dfs(y, x)
                ret[0] += size[y]
                size[x] += size[y]
            }
        }
    }
    dfs(0, -1)

    var reroot func(x, fa int)
    reroot = func(x, fa int) {
        for _, y := range g[x] {
            if y != fa {
                ret[y] = ret[x] + n - 2 * size[y]
                reroot(y, x)
            }
        }
    }
    reroot(0, -1)

    return ret
}

func main() {
	f := sumOfDistancesInTree
	fmt.Println(f(6, [][]int{{0,1}, {0,2}, {2,3},{2,4},{2,5}}))
	fmt.Println(f(1, [][]int{}))
	fmt.Println(f(2, [][]int{{1, 0}}))
	// 输出: [8,12,6,10,10,10]
	// 输出: [0]
	// 输出: [1,1]
}