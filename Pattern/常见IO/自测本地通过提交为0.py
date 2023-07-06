# 输入有多组测试用例，每组空格隔开两个整数
"""
1 1
"""
#############################################
class Solution:
    def f(self, a, b):
        return a + b


testcases = list()
while True:
    try:
        testcases.append(map(int, input().split()))
    except:
        break

s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for arg in testcases:
    print(func(*arg))
#############################################