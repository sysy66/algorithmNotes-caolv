# 2462.雇佣K位工人的总代价.py
# https://leetcode.cn/problems/total-cost-to-hire-k-workers/description/
# lang=python
from heapq import heapify, heapreplace
from random import randint
from typing import List


# 解法:堆+快速排序

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans, n = 0, len(costs)
        if n > 2 * candidates:
            pre = costs[:candidates]
            heapify(pre)
            suf = costs[-candidates:]
            heapify(suf)
            i, j = candidates, n - candidates - 1
            while k and i <= j:
                if pre[0] <= suf[0]:
                    ans += heapreplace(pre, costs[i])
                    i += 1
                else:
                    ans += heapreplace(suf, costs[j])
                    j -= 1
                k -= 1
            costs = pre + suf
        
        def random_select(left: int, right: int, k: int) -> None:
            pivot_id = randint(left, right)
            pivot = costs[pivot_id]
            costs[pivot_id], costs[right] = costs[right], costs[pivot_id]
            j = left
            for i in range(left, right):
                if costs[i] <= pivot:
                    costs[i], costs[j] = costs[j], costs[i]
                    j += 1
            costs[right], costs[j] = costs[j], costs[right]
            if k < j - left + 1:
                random_select(left, j - 1, k)
            elif k > j - left + 1:
                random_select(j + 1, right, k - (j - left + 1))
        
        if k:
            random_select(0, len(costs) - 1, k)
            ans += sum(costs[:k])
        return ans


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
    # 输出：11
    print(func(costs=[1, 2, 4, 1], k=3, candidates=3))
    # 输出：4
    print(func(costs=[31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58], k=11, candidates=2))
    # 输出：423
    
    t1 = time.time()
    print(t1 - t0)
