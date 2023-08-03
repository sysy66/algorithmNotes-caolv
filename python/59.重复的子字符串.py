# 59.重复的子字符串
# https://leetcode.cn/problems/repeated-substring-pattern/description/
# lang=python

# 解法:官方题解方法三：KMP 算法

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def kmp(query: str, pattern: str) -> bool:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False

        return kmp(s + s, s)


# 作者：力扣官方题解
# 链接：https: // leetcode.cn / problems / repeated - substring - pattern / solutions / 386481 / zhong - fu - de - zi - zi - fu - chuan - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == "__main__":
    import time

    t0 = time.time()

    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(s="abab"))
    # 输出: true
    print(func(s="aba"))
    # 输出: false
    print(func(s="abcabcabcabc"))
    # 输出: true

    t1 = time.time()
    print(t1 - t0)
