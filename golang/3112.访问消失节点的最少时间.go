// 3112.访问消失节点的最少时间.go
// https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/description/
// lang=golang

// 解法:Dijkstra

package main

import (
	"container/heap"
	"fmt"
)

func minimumTime(n int, edges [][]int, disappear []int) []int {
	g := make([][][2]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], [2]int{v, w})
		g[v] = append(g[v], [2]int{u, w})
	}

	dis := make([]int, n)
	for i := 0; i < n; i++ {
		dis[i] = -1
	}

	dis[0] = 0
	h := hp{{}}

	for len(h) > 0 {
		p := heap.Pop(&h).(pair)
		dx, x := p.d, p.x
		if dx > dis[x] {
			continue
		}
		for _, e := range g[x] {
			y, d := e[0], e[1]
			nd := dx + d
			if (dis[y] == -1 || nd < dis[y]) && (nd < disappear[y]) {
				dis[y] = nd
				heap.Push(&h, pair{nd, y})
			}
		}
	}
	return dis
}

type pair struct{ d, x int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].d < h[j].d }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func main() {
	f := minimumTime
	fmt.Println(f(3, [][]int{[]int{0, 1, 2}, []int{1, 2, 1}, []int{0, 2, 4}}, []int{1, 1, 5}))
	// 输出：[0,-1,4]
}
