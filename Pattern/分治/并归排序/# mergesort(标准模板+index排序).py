# mergesort(标准模板+index排序)
# 315. 计算右侧小于当前元素的个数

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        positions = list(range(n := len(nums)))
        positions.sort(key=lambda x:(nums.__getitem__(x), x))
        
        self.ret = [0] * n
        self.mergesort(positions, 0, n - 1)
        return self.ret

    def mergesort(self, nums: list[int], L: int, R: int) -> None:
        if L < R:
            mid = (L + R) >> 1
            self.mergesort(nums, L, mid)
            self.mergesort(nums, mid + 1, R)
            self.merge(nums, L, mid, R)
    
    def merge(self, nums: list[int], L: int, mid: int, R: int) -> None:
        tmp = list()
        i, j = L, mid + 1
        while i <= mid and j <= R:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                self.ret[nums[j]] += mid + 1 - i
                j += 1
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        while j <= R:
            tmp.append(nums[j])
            self.ret[nums[j]] += mid + 1 - i
            j += 1
        nums[L: R + 1] = tmp


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        '''根据nums[*][0]进行排序，对应的index随之移动'''
        def mergeSort(nums, low, high):
            if low >= high:     # 递归终止
                return 0

            '''递归排序'''
            mid = low + (high-low)//2     
            mergeSort(nums, low, mid)           # 左半部分逆序对数目
            mergeSort(nums, mid+1, high)        # 右半部分逆序对数目

            '''nums[low, mid] 和 nums[mid+1, high] 已排序好'''
            tmp = []                            # 记录nums[low, high]排序结果
            left, right = low, mid+1
            while left<=mid and right<=high:
                if nums[left][0] <= nums[right][0]:         # 根据nums[*][0]进行排序
                    tmp.append(nums[left])
                    res[nums[left][1]] += right-(mid+1)     # 记录逆序对数目【对应坐标nums[*][1]处】
                    left += 1
                else:
                    tmp.append(nums[right])
                    right += 1
            
            '''左或右数组需遍历完（最多只有一个未遍历完）'''
            while left<=mid:
                tmp.append(nums[left])
                res[nums[left][1]] += right -(mid+1)    # 记录逆序对数目【对应坐标nums[*][1]处】
                left += 1

            while right<=high:
                tmp.append(nums[right])
                right += 1
            
            nums[low:high+1] = tmp


        '''主程序'''
        n = len(nums)
        res = [0] * n               # 存储结果
        nums = [(num, idx) for idx, num in enumerate(nums)] 
        # 每个数值附上其对应的索引：
        # 此时，nums[i][0]表示原来的数值，而nums[i][1]则表示原数值对应的索引（方便定位）

        mergeSort(nums, 0, n-1)     # 归并排序
        return res


