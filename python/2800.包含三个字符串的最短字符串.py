# 2800.包含三个字符串的最短字符串.py
# https://leetcode.cn/problems/shortest-string-that-contains-three-strings/
# lang=python

# 解法: KMP 算法
from itertools import permutations


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:

        def kmp(query: str, pattern: str) -> str:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(n):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return query
            return query + pattern[match + 1:]

        def merge(s: str, t: str) -> str:
            return kmp(s, t)

        return min((merge(merge(a, b), c) for a, b, c in permutations((a, b, c))), key=lambda x: (len(x), x))


if __name__ == "__main__":
    import time

    t0 = time.time()

    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(a="abc", b="bca", c="aaa"))
    # 输出："aaabca"
    print(func(a="ab", b="ba", c="aba"))
    # 输出："aba"

    t1 = time.time()
    print(t1 - t0)
