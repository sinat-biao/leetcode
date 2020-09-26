"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""
class Solution(object):
    def getsub(self, nums, subsets, detnums):
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            subsets.append(detnums + [nums[i]])
            # print(detnums, subsets)
            self.getsub(nums[i+1:], subsets, detnums + [nums[i]])
    
    def addone(self, a):
        # 加一
        n = len(a)
        if a == [1]*n:
            return [0]*n
        else:
            k = n - 1
            while k > 0 and a[k] != 0:
                k -= 1
            a[k] = 1
            for j in range(k+1, n):
                a[j] = 0
            return a
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 方法一：递归遍历
        # 每次从 nums 中取出一个元素，将其放入 detnums 中，并将当前 detnums（加入了新的 nums 中元素的）
        # 加入 subsets 中。对上述过程在每一个递归层次中依次选择不同的 nums 元素删除并执行递归即可。
        # 同时为了防止出现重复元素，可以考虑每次递归时，截断 nums，只取 nums 中删除的当前元素之后的值。
        # subsets = []
        # subsets.append([])  # 一开始只有空集
        # detnums = []
        # self.getsub(nums, subsets, detnums)
        # return subsets
    
        # 方法二：迭代法枚举子集（状态序列）
        # 记原序列中元素的总数为 n。原序列中的每个数字 $a_i$ 的状态可能有两种，即「在子集中」
        # 和「不在子集中」。我们用 1 表示「在子集中」，0 表示不在子集中，
        # 那么每一个子集可以对应一个长度为 n 的 0/1 序列，第 i 位表示 $a_i$ 是否在子集中。
        a = [0]*len(nums)
        a_end = [1]*len(nums)
        print(a, a_end)
        subsets = []
        while True:
            t = []
            for i in range(len(a)):
                if a[i] == 1:
                    t.append(nums[i])
            subsets.append(t)
            a = self.addone(a)
            if a == [0]*len(nums):
                break
        return subsets
            
            
        # 方法三：迭代
        # 这。。。。。。666
        # res = [[],]
        # for i in nums:
        #     res = res + [[i] + num for num in res]
        #     print(res)
        # return res
        
        # 方法四：利用 python 函数
        # itertools.combinations(iterable, r)
        # 可以创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序
        # import itertools
        # subsets = []
        # for i in range(len(nums)+1):
        #     subsets = subsets + list(itertools.combinations(nums, i))
        # return subsets
        
            


S = Solution()
nums = [1,2,3]
print(S.subsets(nums))
# a = [1,1,1]
# print(S.addone(a))