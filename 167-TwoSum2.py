'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法一：暴力法（此种方法在 python 中超出时间限制）
        # 两重循环暴力搜索
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
            
        # 方法二：两遍哈希
        # dict_ = {}
        # for i in range(len(numbers)):
        #     dict_[numbers[i]] = i
        # for i in range(len(numbers)):
        #     component = target - numbers[i]
        #     if dict_.get(component) != None:
        #         return [i+1, dict_[component]+1]
        
        # 方法三：一遍哈希
        # dict_ = {}
        # for i in range(len(numbers)):
        #     component = target - numbers[i]
        #     if dict_.get(component) != None:
        #         return [dict_[component]+1, i+1]
        #     else:
        #         dict_[numbers[i]] = i
                
        # 方法四：双指针
        # 由于此次数组有序，可以使用两个指针，分别从两边向中间移动，来进行匹配
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1
        

S = Solution()
numbers = [2,7,11,15]
target = 9
print(S.twoSum(numbers, target))