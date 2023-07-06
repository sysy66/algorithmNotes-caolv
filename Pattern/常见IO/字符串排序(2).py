# 多个测试用例，每个测试用例一行。

# 每行通过空格隔开，有n个字符，n＜100
"""
a c bb
f dddd
nowcoder
"""
#############################################
class Solution:
    def f(self, s):
        s.sort()
        return ' '.join(s)


testcases = list()
while True:
    try:
        testcases.append(input().split())
    except:
        break

s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)
for arg in testcases:
    print(func(arg))
#############################################
