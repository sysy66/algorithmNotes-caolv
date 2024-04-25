//1916.统计为蚁群构筑房间的不同顺序.go
//https://leetcode.cn/problems/count-ways-to-build-rooms-in-an-ant-colony/description/
//lang=golang
//解法:乘法逆元+排列数

package main

import (
	"fmt"
)

const MOD = 1_000_000_007
const MX = 100_001

var fac, invFac [MX]int

func pow(b, e int) int {
	r := 1
	for ; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % MOD
		}
		b = b * b % MOD
	}
	return r
}

func init() {
	fac[0] = 1
	for i := 1; i < MX; i++ {
		fac[i] = fac[i-1] * i % MOD
	}
	invFac[MX-1] = pow(fac[MX-1], MOD-2)
	for i := MX - 2; i > -1; i-- {
		invFac[i] = invFac[i+1] * (i + 1) % MOD
	}
}

func waysToBuildRooms(prevRoom []int) int {
	n := len(prevRoom)
	f, cnt, inDeg := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		f[i]++
		cnt[i]++
		if i > 0 {
			inDeg[prevRoom[i]]++
		}
	}

	var q []int
	for i := 0; i < n; i++ {
		if inDeg[i] == 0 {
			q = append(q, i)
		}
	}

	for {
		u := q[0]
		q = q[1:]
		if u == 0 {
			break
		}
		v := prevRoom[u]
		f[v] = (f[v] * f[u]) % MOD * invFac[cnt[u]] % MOD
		cnt[v] += cnt[u]
		inDeg[v]--
		if inDeg[v] == 0 {
			q = append(q, v)
			f[v] = f[v] * fac[cnt[v]-1] % MOD
		}
	}
	return f[0]
}

func main() {
	f := waysToBuildRooms
	fmt.Println(f([]int{-1, 0, 1}))
	//输出: 1
	fmt.Println(f([]int{-1, 0, 0, 1, 2}))
	//输出: 6
}
