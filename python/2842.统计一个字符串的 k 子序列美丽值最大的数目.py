# 2842.统计一个字符串的 k 子序列美丽值最大的数目
# https://leetcode.cn/problems/count-k-subsequences-of-a-string-with-maximum-beauty/
# lang=python

# 解法:组合数学
import operator
from collections import Counter
from functools import reduce
from math import comb

MOD = 10 ** 9 + 7


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        a = sorted(Counter(s).values())
        n = len(a)
        
        if n < k:
            return 0
        elif n == k:
            return reduce(operator.mul, a) % MOD
        
        target = a[-k]
        i = j = n - k
        while j < n and a[j] == target:
            j += 1
        while i - 1 >= 0 and a[i - 1] == target:
            i -= 1
        return reduce(operator.mul, a[-k:]) * comb(j - i, j - n + k) % MOD


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(s="bcca", k=2))
    # 输出：4
    print(func(s="abbcd", k=4))
    # 输出：2
    t1 = time.time()
    print(t1 - t0)
