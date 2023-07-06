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
class Solution:
    def f(self, *arguments):
        return sum(arguments)


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)


while True:
    try:
        args = map(int, input().split())
        print(func(*args))
    except:
        break
#############################################
class Solution:
    def f(self, *arguments):
        return sum(arguments)


s = Solution()
func_name = dir(s)[-1]
func = getattr(s, func_name)


T = int(input())
for _ in range(T):
    args = map(int, input().split())
    print(func(*args))



