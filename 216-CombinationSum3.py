"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
"""
class Solution(object):
    def recursion(self, k, n, sub_arr, stack, target, nums):
        # print(stack, nums, target)
        if len(stack) < k - 1:
            for i in range(len(nums)):
                if nums[i] < target:
                    stack.append(nums[i])
                    self.recursion(k, n, sub_arr, stack, target-nums[i], nums[i+1:])
                    if len(stack) > 0:
                        stack.pop()
        if len(stack) == k - 1:
            for i in range(len(nums)):
                # print(target)
                if nums[i] == target:
                    stack.append(nums[i])
                    sub_arr.append([i for i in stack])
                    stack.pop()
        if len(stack) >= k:
            return
            
    def addone(self, state_nums):
        # 模拟二进制的加 1
        n = len(state_nums)
        if state_nums == [1] * n:
            return [0] * n
        else:
            k = n - 1
            # 从后向前搜索第一个不为 1 的位置
            while k > 0 and state_nums[k] != 0:
                k -= 1
            state_nums[k] = 1
            for j in range(k+1, n):
                state_nums[j] = 0
            return state_nums
            
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 方法一：暴力搜索
        
        # 方法二：递归（回溯）
        # nums = [i for i in range(1, 10)]
        # print(nums)
        # sub_arr = []
        # self.recursion(k, n, sub_arr, [], n, nums)
        # return sub_arr
    
        # 方法三：组合枚举法
        # 数组中每个元素只能有 2 个状态，出现（1）、不出现（0）。只需要以状态数组的方式让 k 个
        # 元素的状态为 1，然后计算这 k 个出现状态的数组元素之和，并判断是否满足 n 即可。
        nums = [i for i in range(1, 10)]
        state_nums = [0]*9
        print(nums, state_nums)
        sub_arr = []
        while True:
            sts = self.addone(state_nums)
            if sts == [0]*len(state_nums):
                return sub_arr
            # print(state_nums)
            sums = 0
            subs = []
            for i in range(len(state_nums)):
                if state_nums[i] == 1:
                    sums += nums[i]
                    subs.append(nums[i])
            if sums == n and len(subs) == k:
                sub_arr.append(subs)
        return sub_arr

        
S = Solution()
k, n = 3, 7
print(S.combinationSum3(k, n))  # [[1, 2, 4]]
k, n = 3, 9
print(S.combinationSum3(k, n))  # [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
k, n = 4, 1
print(S.combinationSum3(k, n))  # []
k, n = 3, 2
print(S.combinationSum3(k, n))  # []
k, n = 9, 45
print(S.combinationSum3(k, n))  # [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
k, n = 3, 28
print(S.combinationSum3(k, n))  # []