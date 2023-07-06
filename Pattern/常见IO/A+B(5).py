# 输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
# 接下来t行, 每行一组数据。
# 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# 接下来n个正整数, 即需要求和的每个正整数。
"""
2
4 1 2 3 4
5 1 2 3 4 5
"""
#############################################
class Solution:
    def f(self, *arguments):
        return sum(arguments[1:])


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)


T = int(input())
for _ in range(T):
    args = map(int, input().split())
    print(func(*args))
##############################################
T = int(input())
testcases = list()
for _ in range(T):
    testcases.append(map(int, input().split()))

    
class Solution:
    def f(self, *arguments):
        x = 0
        for arg in arguments[1:]:
            x += arg
        return x

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases:
    print(func(*args))
#############################################

