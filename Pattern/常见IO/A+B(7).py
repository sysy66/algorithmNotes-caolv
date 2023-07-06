# 链接：https://ac.nowcoder.com/acm/contest/5652/G
# 来源：牛客网

# 输入数据有多组, 每行表示一组输入数据。

# 每行不定有n个整数，空格隔开。(1 <= n <= 100)。
"""
1 2 3
4 5
0 0 0 0 0
"""
#############################################
class Solution:
    def f(self, arguments):
        return sum(arguments)


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
        for arg in arguments:
            x += arg
        return x

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases:
    print(func(*args))
#############################################


