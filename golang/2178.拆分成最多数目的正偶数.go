// 2178. 拆分成最多数目的正偶数之和
// https://leetcode.cn/problems/maximum-split-of-positive-even-integers/description/
// lang=golang

// 解法:贪心

package main

import "fmt"

func maximumEvenSplit(finalSum int64) (res []int64) {
    if finalSum & 1 == 0 {
        for i := int64(2); i <= finalSum; i += 2 {
            res = append(res, i)
            finalSum -= i
        }
        res[len(res)-1] += finalSum
    }
    return
}

func main() {
    fmt.Println(maximumEvenSplit(12))
    fmt.Println(maximumEvenSplit(7))
    fmt.Println(maximumEvenSplit(28))
}
