//3170.删除星号以后字典序最小的字符串.go
//https://leetcode.cn/problems/lexicographically-minimum-string-after-removing-stars/description/
//lang=golang
//解法:优先队列

package main

import (
	"container/heap"
	"fmt"
)

func clearStars(s string) string {
	var t []rune
	var h hp
	delSet := map[int]int{}
	for _, c := range s {
		if c == '*' {
			delSet[heap.Pop(&h).(pair).idx] = 1
		} else {
			heap.Push(&h, pair{int(c), len(t)})
			t = append(t, c)
		}
	}
	j := 0
	for i, x := range t {
		if _, ok := delSet[i]; !ok {
			t[j] = x
			j++
		}
	}
	t = t[:j]
	return string(t)
}

type pair struct{ c, idx int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].c < h[j].c || h[i].c == h[j].c && h[i].idx > h[j].idx }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func main() {
	f := clearStars
	fmt.Println(f("aaba*"))
	//输出: "aab"
	fmt.Println(f("abc"))
	//输出: "abc"
}
