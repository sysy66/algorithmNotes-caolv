# 216.组合总和III.py
# https://leetcode.cn/problems/combination-sum-iii/description/?envType=daily-question&envId=2024-04-21
# lang=python3
#
# 解法:Gosper'sHack
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        x = (1 << k) - 1
        ans = list()
        
        while x < 1 << 9:
            
            tmp = list()
            cnt = 0
            for i in range(9):
                if x & (1 << i):
                    tmp.append(i + 1)
                    cnt += i + 1
                if cnt > n:
                    break
            if cnt == n:
                ans.append(tmp)
            
            lowbit = x & -x
            left = x + lowbit
            right = ((x ^ left) // lowbit) >> 2
            x = left | right
        
        return ans


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    print(func(3, 7))
    # 输出: [[1,2,4]]
    print(func(3, 9))
    # 输出: [[1,2,6], [1,3,5], [2,3,4]]
    print(func(4, 1))
    # 输出: []
    
    t1 = time.time()
    print(t1 - t0)
