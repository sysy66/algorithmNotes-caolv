# 素数筛.py
# LCP 14. 切分数组
# 由于需要知道每个 nums[i]nums[i] 的所有质因子，我们需要一种方法将 nums[i]nums[i] 快速因子分解。我们用素数筛提前预处理 1到10^6的
# 任意数字 kk 的最小质因子in_prime_factor[k] 。获得 nums[i]nums[i] 所有质因子的方法为：
# 1. x=nums[i]
# 2. 获取min_prime_factor[x] 为 x 当前的最小质因子
# 3. x = x // min_prime_factor[x]
# 4. 如果 x=1，退出，否则回到步骤 2

max_num = 1000000
min_factor = [1] * (max_num + 1)
p = 2

# O(M loglog M)
while (p <= max_num):
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            break
        p += 1

class Solution:
    def splitArray(self, nums) -> int:
        f = {}
        n = len(nums)
        
        x = nums[0]
        INF = 100000000
        while True:
            if min_factor[x] == 1:
                f[x] = 1
                break
            
            f[min_factor[x]] = 1
            x //= min_factor[x]
        
        min_prev = 1
        for i in range(1, n):
            x = nums[i]
            
            min_cur = INF
            while True:
                if min_factor[x] == 1:
                    f[x] = min(f.get(x, INF), min_prev + 1)     
                    min_cur = min(min_cur, f[x])       
                    break
                
                f[min_factor[x]] = min(f.get(min_factor[x], INF), min_prev + 1)
                min_cur = min(min_cur, f[min_factor[x]])
                x //= min_factor[x]

            min_prev = min_cur

        return min_prev

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/qie-fen-shu-zu/solution/qie-fen-shu-zu-zhi-shu-shai-dp-by-leetcode-solutio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

############################################################################################################################################

maxnum = 10**6              #题目给的数据范围，自己判断的   预处理一下，后面直接使用
minprimefactor = [1 for _ in range(maxnum + 1)]     #每个数的最小质因子  是为了后面将这个数字质因数分解！！！！！
p = 2
while p <= maxnum:
    minprimefactor[p] = p                       #与官方解不同： 一个质数的最小质因子是它本身  官方解给的是1  不同之处是在函数中判断是否为一个质数的条件
    i = p
    while p*i <= maxnum:                        #从平方开始判断
        if minprimefactor[p*i] == 1:            #p的i倍
            minprimefactor[p*i] = p
        i += 1

    p += 1                                      #寻找下一个质数
    while p <= maxnum:
        if minprimefactor[p] == 1:              #如果是质数，break这个while，进入下一轮外while
            break
        else:
            p += 1
'''
for p in range(2, maxnum + 1):                  #埃氏筛   与官方解不同
    if minprimefactor[p] == 1:
        i = 1
        while p*i < maxnum + 1:
            if minprimefactor[p*i] == 1:
                minprimefactor[p*i] = p
            i += 1
'''                         #之所以要写在class Solution上面，是因为有几十个测试样例。在一个完整的函数中，上面这段预处理只需要执行1次（即使50个测试样例）
                            #若这段预处理写在class Solution里，每测试一个样例，就要执行1次，50个样例就执行50次，会TLE（超时）
class Solution:
    def splitArray(self, nums: List[int]) -> int:


        f = {}                      #因为从nums[0]是固定的 要求的是子数组的L和R，最大公约数大于1  只跟子数组的L和R有关
        n = len(nums)               #f是在当前这已有所有数字后面，再加上一个数字（质数），最少可以切分成多少个子数组
                                    #为什么是讨论在后面加一个“质数”  是因为题意要看的是 最大公约数>1，其实等价于 有至少一个相同的质因子  而每一个大于1的数都可以质因数分解
        x = nums[0]                 #所以我们就把后面加上的那个数字，分解成一个一个的质数，  以质数为目标进行讨论和dp
        INF = 10**8                                         #题目所给数据的范围自己定的

        while True:                                         #这个while是初试化！！！！！的过程  先把mums[0]弄明白  很关键
            if minprimefactor[x] == x:      #若x是个质数  最小质因子是它本身（这个地方与答案不同  因为答案是质数的最小质因子定为1了！！！！！！！！！！！！！！！！！）
                f[x] = 1                    #nums[0]就一个数字，最小分组就是1
                break                       #质数，也就没法质因数分解了         
            f[minprimefactor[x]] = 1        #如果在后面添上他的最小质因子  最少可以切分成1个分组    （比如， [12],若添加2 变成[12, 2]，有相同的质因子2，最大公约数>1）
            x //= minprimefactor[x]         #质因式分解     只要后面添加的都是它的质因子，都是最少可以切分成1个分组 (12 = 2*2*3  [12]添加3变成[12,3],有相同质因子3)
                                    #任何一个大于2的数字，都可以被质因式分解，即 x = 质数1 * 质数2 * 质数3 * ………………
        prevmin = 1                 #上一次最好的结果，就是只分成1个子数组  因为nums[0]就一个数字  也是一个值的初始化！！！！！
        for i in range(1, n):                               #nums[0]已经在初始化的时候处理过了  从nums[1]开始
            x = nums[i]

            curmin = INF
            while True:
                if minprimefactor[x] == x:    #如果x就是一个质数  最小质因子是它本身（这个地方与答案不同  因为答案是质数的最小质因子定为1了！！！！！！！！！！！！）
                    f[x] = min(f.get(x, INF), prevmin + 1)  #记忆中有x则直接读值，若没有则置INF  情形1：x跟之前某个数组组成一个子数组 情形2：x自己单独一个新子数组
                    curmin = min(curmin, f[x])              #更新curmin
                    break                                   #质数就不用质因数分解了
                f[minprimefactor[x]] = min(f.get(minprimefactor[x], INF), prevmin + 1)  #把x质因数分解  再比较  （比如12=2*2*3  比较了2，再比较3 看哪个更优，）
                #if minprimefactor[x] not in f:
                #    f[minprimefactor[x]] = prevmin + 1
                curmin = min(curmin, f[minprimefactor[x]])
                x //= minprimefactor[x]                     #质因数分解  过程就是比如 x=12  12 // 2 = 6判断     6 // 2 = 3判断    3 // 3 = 1判断  1判断完就break

            prevmin = curmin                                #更新参数，为下一轮做准备
        
        return prevmin

作者：XingHe_XingHe
链接：https://leetcode.cn/problems/qie-fen-shu-zu/solution/cpython3-zhi-shu-ai-shi-shai-bai-hua-shi-vihl/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。