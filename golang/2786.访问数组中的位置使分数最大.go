//2786.访问数组中的位置使分数最大.go
//https://leetcode.cn/problems/visit-array-positions-to-maximize-score/description/
//lang=golang
//
//解法:动态规划

package main

import "fmt"

func maxScore(nums []int, x int) int64 {
        var nv int = 0
        var a = [2]int{0,0}
        for i := len(nums) - 1; i > -1; i-- {
            v := nums[i]
            nv = max(a[v & 1] + v, a[1 - v & 1] + v - x)
            a[v & 1] = max(a[v & 1], nv)
        }
        return int64(nv)
}

func max(a, b int) int {if a > b {return a}; return b}

func main() {
	fmt.Println(maxScore([]int{2,3,6,1,9,2}, 5))
	fmt.Println(maxScore([]int{2,4,6,8}, 3))
	//输出：13
	//输出：20
}

