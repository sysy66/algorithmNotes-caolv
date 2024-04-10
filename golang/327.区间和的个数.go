// 327.区间和的个数.go
// https://leetcode.cn/problems/count-of-range-sum/description/
// lang=golang

// 解法: 力扣官方题解

package main

import "fmt"

func countRangeSum(nums []int, lower, upper int) int {
    var mergeCount func([]int) int
    mergeCount = func(arr []int) int {
        n := len(arr)
        if n <= 1 {
            return 0
        }

        n1 := append([]int(nil), arr[:n/2]...)
        n2 := append([]int(nil), arr[n/2:]...)
        cnt := mergeCount(n1) + mergeCount(n2) // 递归完毕后，n1 和 n2 均为有序

        // 统计下标对的数量
        l, r := 0, 0
        for _, v := range n1 {
            for l < len(n2) && n2[l]-v < lower {
                l++
            }
            for r < len(n2) && n2[r]-v <= upper {
                r++
            }
            cnt += r - l
        }

        // n1 和 n2 归并填入 arr
        p1, p2 := 0, 0
        for i := range arr {
            if p1 < len(n1) && (p2 == len(n2) || n1[p1] <= n2[p2]) {
                arr[i] = n1[p1]
                p1++
            } else {
                arr[i] = n2[p2]
                p2++
            }
        }
        return cnt
    }

    prefixSum := make([]int, len(nums)+1)
    for i, v := range nums {
        prefixSum[i+1] = prefixSum[i] + v
    }
    return mergeCount(prefixSum)
}

// 作者：力扣官方题解
// 链接：https://leetcode.cn/problems/count-of-range-sum/solutions/476038/qu-jian-he-de-ge-shu-by-leetcode-solution/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


func main() {
	f := countRangeSum
	fmt.Println(f([]int{-2, 5, -1}, -2, 2))
	fmt.Println(f([]int{0}, 0, 0))
	// 输出: 3
	// 输出: 1
}