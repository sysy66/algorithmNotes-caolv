# 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
"""
1 5
10 20
0 0
"""
##########################################
testcases = list()
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        testcases.append((a, b))

class Solution:
    def f(self, a, b):
        return a + b

    
s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for args in testcases:
    print(func(*args))
##############################################
class Solution:
    def f(self, a, b):
        return a + b


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        print(func(a, b))


