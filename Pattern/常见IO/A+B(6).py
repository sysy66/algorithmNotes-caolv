# 链接：https://ac.nowcoder.com/acm/contest/5652/F
# 来源：牛客网

# 输入数据有多组, 每行表示一组输入数据。
# 每行的第一个整数为整数的个数n(1 <= n <= 100)。
# 接下来n个正整数, 即需要求和的每个正整数。
"""
4 1 2 3 4
5 1 2 3 4 5
"""
#############################################
class Solution:
    def f(self, arguments):
        return sum(arguments[1:])


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

while True:
    try:
        args = list(map(int, input().split()))
        print(func(args))
    except:
        break
##############################################
testcases = list()
while True:
    try:
        testcases.append(map(int, input().split()))
    except:
        break

        
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


