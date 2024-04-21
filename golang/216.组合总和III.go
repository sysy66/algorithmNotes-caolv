//216.组合总和III.go
//https://leetcode.cn/problems/combination-sum-iii/description/?envType=daily-question&envId=2024-04-21
//lang=golang
//
//解法:Gosper'sHack

package main

import (
	"fmt"
)

func combinationSum3(k int, n int) (ans [][]int) {
	for x := (1 << k) - 1; x < 1<<9; {

		var tmp []int
		cnt := 0
		for b := 0; b < 9; b++ {
			if x&(1<<b) > 0 {
				tmp = append(tmp, b+1)
				cnt += b + 1
			}
			if cnt > n {
				break
			}
		}
		if cnt == n {
			ans = append(ans, tmp)
		}

		lowbit := x & -x
		left := x + lowbit
		right := ((x ^ left) / lowbit) >> 2
		x = left | right

	}
	return ans
}

func main() {
	f := combinationSum3
	fmt.Println(f(3, 7))
	//输出: [[1,2,4]]
	fmt.Println(f(3, 9))
	//输出: [[1,2,6], [1,3,5], [2,3,4]]
	fmt.Println(f(4, 1))
	//输出: []
}
