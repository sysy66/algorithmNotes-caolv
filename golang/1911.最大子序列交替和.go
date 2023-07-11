//1911.最大子序列交替和.go
//https://leetcode.cn/problems/maximum-alternating-subsequence-sum/description/
//lang=golang
//
//解法:动态规划

package main

import "fmt"

func maxAlternatingSum(nums []int) int64 {
    var a, b int64 = 0, 0
    for _, y := range nums {
        x := int64(y)
        a = max(a, b - x)
        b = max(b, a + x)
    }
    return max(a, b)
}

func max(a, b int64) int64 {if a > b {return a}; return b}

func main() {
	fmt.Println(maxAlternatingSum([]int{4, 2, 5, 3}))
	fmt.Println(maxAlternatingSum([]int{5, 6, 7, 8}))
	fmt.Println(maxAlternatingSum([]int{6, 2, 1, 2, 4, 5}))
	//输出：7
	//输出：8
	//输出：10
}

