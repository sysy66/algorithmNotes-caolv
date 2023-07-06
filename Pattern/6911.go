// 6911. 不间断子数组
// https://leetcode.cn/problems/continuous-subarrays/description/

package main

import "fmt"

func max(a, b int) int {
	if b > a {
		return b
	}
	return a
}
func min(a, b int) int {
	if b < a {
		return b
	}
	return a
}

func continuousSubarrays(a []int) (ans int64) {
	cnt := map[int]int{}
	left := 0
	for right, x := range a {
		cnt[x]++
		for {
			mx, mn := x, x
			for k := range cnt {
				mx = max(mx, k)
				mn = min(mn, k)
			}
			if mx-mn <= 2 {
				break
			}
			y := a[left]
			if cnt[y]--; cnt[y] == 0 {
				delete(cnt, y)
			}
			left++
		}
		ans += int64(right - left + 1)
	}
	return
}

func main() {
	fmt.Println(continuousSubarrays([]int{5, 4, 2, 4}))
	// 8
	fmt.Println(continuousSubarrays([]int{1, 2, 3}))
	// 6
}

