# 输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。
"""
1 5
10 20
"""
######################################
testcases = list()
while True:
    try:
        testcases.append(map(int, input().split()))
    except:
        break

class Solution:
    def f(self, a, b):
        return a + b

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases:
    print(func(*args))
###############################################
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break