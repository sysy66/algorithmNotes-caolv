# 链接：https://ac.nowcoder.com/acm/contest/5652/H
# 来源：牛客网

# 输入描述:
# 输入有两行，第一行n

# 第二行是n个字符串，字符串之间用空格隔开
# 输出描述:
# 输出一行排序后的字符串，空格隔开，无结尾空格
"""
5
c d a bb e
"""
#############################################
n = int(input())
testcase = input().split()

class Solution:
    def f(self, s):
        s.sort()
        return ' '.join(s)

s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
print(func(testcase))
#############################################


