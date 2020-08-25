'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法一：队列
        # 将列表看作队列，队尾出，队首进
        # 时间复杂度：O(k)；空间复杂度：O(1)
        # for i in range(k):
        #     item = nums.pop()
        #     nums.insert(0, item)
        # return nums
    
        # 方法二：数组覆盖
        # 拷贝一个数组，然后每隔 k 个位置将拷贝数组对应位置的值覆盖到原数组上
        # 注意：python2 中没有 copy() 函数，所以需要使用下句复制
        # nums_copy = [i for i in nums]
        # k_ = len(nums) - k
        # for i in range(len(nums)):
        #     i_copy = (i + k_) % len(nums)
        #     nums[i] = nums_copy[i_copy]
        # return nums
    
        # 方法三：前移数据（这种方法在 python 中超出时间限制）
        # 将后 k 个元素依次移到最前面
        # while k > 0:
        #     nums = self.tofront(nums, len(nums)-1)
        #     k -= 1
        # return nums
    
        # 方法四：环状替换
        k = k % len(nums)
        count = 0
        for i in range(len(nums)):
            cu = i
            temp1 = nums[cu]
            while True:
                count += 1
                temp2 = nums[(cu+k)%len(nums)]
                nums[(cu+k)%len(nums)] = temp1
                cu = (cu + k) % len(nums)
                if cu == i:
                    break
                temp1 = temp2
            if not count < len(nums):
                print(i)
                break
        return nums
        
        
        # 方法五：反转替换
        # 这个方法基于这个事实：当我们旋转数组 k 次， k%n 个尾部元素会被移动到头部，剩下的元素会被向后移动。
        # 在这个方法中，我们首先将所有元素反转。然后反转前 k 个元素，再反转后面 n-k 个元素，就能得到想要的结果。
        # 当 k 大于 n 时，相当于将整个数组循环移动了 n，然后再移动 k-n。
        # nums.reverse()
        # print(nums)
        # # 【注意】：python 中的切片操作会创建出一个新的副本，在其上的改动不会影响原列表
        # nums[:k%len(nums)] = reversed(nums[:k%len(nums)])       # this work
        # # nums[:k].reverse()                # this doesn't work
        # nums[k%len(nums):] = reversed(nums[k%len(nums):])
        # return nums
        
    
        
    def tofront(self, nums, p):
        # 将 p 位置的元素移到最前面
        while p > 0:
            temp = nums[p]
            nums[p] = nums[p-1]
            nums[p-1] = temp
            p -= 1
        return nums
    
S = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(S.rotate(nums, k))
nums = [-1,-100,3,99]
k = 2
print(S.rotate(nums, k))
nums = [1, 2]
k = 3
print(S.rotate(nums, k))

# nums = [1,2,3,4,5,6,7]
# print(S.tofront(nums, 5))