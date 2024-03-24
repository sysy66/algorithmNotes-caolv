//322.零钱兑换
//https://leetcode.cn/problems/coin-change/description/?envType=daily-question&envId=2024-03-24
//lang=golang
//
//解法:DP

package main

import (
	"fmt"
	"math"
	)

func coinChange(coins []int, n int) int {
    f := make([]int, n + 1)
    for i := 1; i < n + 1; i++ {
        f[i] = math.MaxInt / 2
    }

    for i := 1; i < n + 1; i++ {
        for _, c := range coins {
            if i - c < 0 { continue }
            f[i] = min(f[i], f[i - c] + 1)
        }
    }

    if f[n] == math.MaxInt / 2 {
        return -1
    }
    return f[n]
}

func main() {
	f := coinChange
	fmt.Println(f([]int{1, 2, 5}, 11))
	fmt.Println(f([]int{2}, 3))
	fmt.Println(f([]int{1}, 0))
// 	输出：3
// 	输出：-1
// 	输出：0
}