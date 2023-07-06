"""zj-future04. 门店商品调配
通过的用户数160
尝试过的用户数470
用户总通过次数196
用户总提交次数1487
题目难度Hard
某连锁店开设了若干门店，门店间允许进行商品借调以应对暂时性的短缺。本月商品借调的情况记于数组 distributions，其中 distributions[i] = [from,to,num]，表示从 from 门店调配了 num 件商品给 to 门店。

若要使得每一个门店最终借出和借入的商品数量相同，请问至少还需要进行多少次商品调配。

 

注意：一次商品调配以三元组 [from, to, num] 表示，并有 from ≠ to 且 num > 0。"""
"""输入：distributions = [[0,1,5],[1,2,10],[2,0,5],[2,1,1]]
输出：1
解释：
商店 0 给商店 1 五件商品；
商店 1 给商店 2 十件商品；
商店 2 给商店 0 五件商品；
商店 2 给商店 1 一件商品。
此时商店 1 少了 4 件商品，商店 2 多了 4 件商品，

因此仅需一次商品调配，商店 2 给商店 1 四件商品，即可满足每个门店借出和借入商品数量相同：
商店 0 借出和借入的商品数量均为 5；
商店 1 借出和借入的商品数量均为 10；
商店 2 借出和借入的商品数量均为 10。"""
class Solution:
    def minTransfers(self, a: List[List[int]]) -> int:
        n = 12
        b = [0 for i in range(n)]
        for x, y, z in a:
            b[x] -= z
            b[y] += z
        f = [0 for i in range(1 << n)]
        for i in range(1 << n):
            s = 0
            for j in range(n):
                if i >> j & 1:
                    s += b[j]
            if s == 0:
                f[i] = 1
        f[0] = 0
        for i in range(1 << n):
            j = i
            while j > 0:
                f[i] = max(f[i], f[j] + f[i - j])
                j = (j - 1) & i
        return 12 - f[(1 << n) - 1]