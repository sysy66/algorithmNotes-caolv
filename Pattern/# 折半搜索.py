# 折半搜索.py
# 805. 数组的均值分割

class Solution(object):
    def splitArraySameAverage(self, nums):
        A = nums
        N = len(A)
        S = sum(A)
        A = [z * N - S for z in A]

        if N == 1: return False

        #Want zero subset sum
        left = {A[0]}
        for i in range(1, N//2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in range(N//2, N-1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: return True

        sleft = sum(A[i] for i in range(N//2))
        sright = sum(A[i] for i in range(N//2, N))

        return any(-ha in right and (ha, -ha) != (sleft, sright) for ha in left)


# 作者：LeetCode
# 链接：https://leetcode.cn/problems/split-array-with-same-average/solution/shu-zu-de-jun-zhi-fen-ge-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。