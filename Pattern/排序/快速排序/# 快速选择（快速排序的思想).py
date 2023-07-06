# 快速选择（快速排序的思想).py
# 973. 最接近原点的 K 个点

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def random_select(left, right, k):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[pivot_id], points[right] = points[right], points[pivot_id]
            j = left
            for i in range(left, right):
                if points[i][0] ** 2 + points[i][1] ** 2 <= pivot:
                    points[i], points[j] = points[j], points[i]
                    j += 1
            points[right], points[j] = points[j], points[right]
            if k < j - left + 1:
                random_select(left, j - 1, k)
            if k > j - left + 1:
                random_select(j + 1, right, k - (j - left + 1))
        
        n = len(points)
        random_select(0, n - 1, k)
        return points[:k]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def random_select(left: int, right: int, k: int):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if k < i - left + 1:
                random_select(left, i - 1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, k)
        return points[:k]

作者：力扣官方题解
链接：https://leetcode.cn/problems/k-closest-points-to-origin/solutions/477916/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。