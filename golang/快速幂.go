//快速幂.go

package main

import "fmt"

const MOD = int(1e9 + 7)

func pow(x, n int) int {
	//base 底数
	b := x
	//power 指数
	e := n
	//result 结果
	r := 1
	for e > 0 {
		if e&1 > 0 {
			r *= b
			r %= MOD
		}
		e >>= 1
		b *= b
		b %= MOD
	}
	return r
}

func main() {
	fmt.Println(pow(3, 4))
	//81
	fmt.Println(pow(107, 8))
	//678046174
}
