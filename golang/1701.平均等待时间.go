//1701.平均等待时间
//https://leetcode.cn/problems/average-waiting-time/description/
//lang=golang
//
//解法:按照题意模拟。按顺序遍历顾客，cur表示能够开始招待该顾客的时间，
//当cur小于arrival时，从arrival开始做菜，否则从cur时刻开始做菜。

package main

import "fmt"

func averageWaitingTime(customers [][]int) float64 {
	tot, cur := 0, 0
	for _, v := range customers {
		arrival, t := v[0], v[1]
		cur = max(cur, arrival) + t
		tot += cur - arrival
	}
	return float64(tot) / float64(len(customers))
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(averageWaitingTime([][]int{{1, 2}, {2, 5}, {4, 3}}))
	fmt.Println(averageWaitingTime([][]int{{5, 2}, {5, 4}, {10, 3}, {20, 1}}))
	// 输出：5.00000
	// 输出：3.25000
}
