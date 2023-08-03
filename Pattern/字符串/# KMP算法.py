# KMP算法.py
# 59. 重复的子字符串


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

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/repeated-substring-pattern/solution/zhong-fu-de-zi-zi-fu-chuan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

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
    i = 0
    res = []
    while i < n:
        while match != -1 and pattern[match + 1] != query[i]:
            match = fail[match]
        if pattern[match + 1] == query[i]:
            match += 1
            if match == m - 1:
                res.append(i - m + 1)
                i = i - m + 1
                match = -1
        i += 1
    return res  #query中，以res里的下标开头，长度为m的子字符串，为pattern

# 在 KMP 算法中，对于模式串，我们需要预处理出一个 fail 数组。
# 这个数组到底表示了什么？
# fail[i] 等于满足下述要求的 x 的最大值：s[0:i] 具有长度为 x+1 的完全相同的前缀和后缀。这也是 KMP 算法最重要的一部分。
