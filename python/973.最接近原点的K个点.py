# 973.最接近原点的K个点.py
# https://leetcode.cn/problems/k-closest-points-to-origin/description/
# lang=python
from random import randint
from typing import List


# 解法:快速排序

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def randon_select(left: int, right: int, k: int) -> None:
            pivot_id = randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[pivot_id], points[right] = points[right], points[pivot_id]
            j = left
            for i in range(left, right):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot:
                    points[i], points[j] = points[j], points[i]
                    j += 1
            points[j], points[right] = points[right], points[j]
            if k < j - left + 1:
                randon_select(left, j - 1, k)
            elif k > j - left + 1:
                randon_select(j + 1, right, k - (j - left + 1))
        
        randon_select(0, len(points) - 1, k)
        return points[:k]


if __name__ == "__main__":
    import time
    
    t0 = time.time()
    
    s = Solution()
    func_name = dir(s)[-1]
    func = getattr(s, func_name)
    
    print(func(points=[[1, 3], [-2, 2]], k=1))
    # 输出：[[-2,2]]
    print(func(points=[[3, 3], [5, -1], [-2, 4]], k=2))
    # 输出：[[3,3],[-2,4]]
    
    t1 = time.time()
    print(t1 - t0)
