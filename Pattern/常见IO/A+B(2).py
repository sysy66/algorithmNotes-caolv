# 输入第一行包括一个数据组数t(1 <= t <= 100)
# 接下来每行包括两个正整数a,b(1 <= a, b <= 1000)
"""
2
1 5
10 20
"""
##########################################
T = int(input())
testcases = list()
for _ in range(T):
    testcases.append(map(int, input().split()))
    
    
class Solution:
    def f(self, a, b):
        return a + b

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases:
    print(func(*args))
#######################################
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(a + b)
########################################
class Solution:
    def f(self, a, b):
        return a + b

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(func(a, b))
#######################################


