# 输入数据包括多组。
# 每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
# 接下来n个正整数,即需要求和的每个正整数。
"""
4 1 2 3 4
5 1 2 3 4 5
0
"""
#############################################
class Solution:
    def f(self, arguments):
        return sum(arguments[1:])


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

while True:
    args = list(map(int, input().split()))
    if args[0] == 0:
        break
    print(func(args))
##############################################
testcases = list()
while True:
    try:
        testcases.append(list(map(int, input().split())))
    except:
        break

class Solution:
    def f(self, arguments):
        x = 0
        for arg in arguments[1:]:
            x += arg
        return x

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases[:-1]:
    print(func(args))
#############################################

