"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""
class Solution(object):
    
    def recursion(self, candidates, new_target, list_sub, list_):
        if len(candidates) == 0 or min(candidates) > new_target:
            if len(list_sub) > 0:
                list_sub.pop()
            return
        else:
            for i in range(len(candidates)):
                if candidates[i] == new_target:
                    list_sub.append(candidates[i])
                    list_.append([j for j in list_sub])
                    list_sub.pop()
                    if len(list_sub) > 0:
                        list_sub.pop()
                    return
                else:
                    # 防止重复
                    if len(list_) != 0 and i < len(candidates) and candidates[i] == candidates[i-1]:
                        continue
                    list_sub.append(candidates[i])
                    self.recursion(candidates[i+1:], new_target-candidates[i], list_sub, list_)            
                if i < len(candidates) and candidates[i] == candidates[i-1]:
                    continue
                    
            if len(list_sub) > 0:
                list_sub.pop()
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 方法一：递归（回溯）
        list_ = []
        list_sub = []
        candidates.sort()
        print(candidates)
        self.recursion(candidates, target, list_sub, list_)
        return list_


S = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(S.combinationSum2(candidates, target))
candidates = [1,1]
target = 2
print(S.combinationSum2(candidates, target))
candidates = [10,1,2,7,6,1,5,1]
target = 8
print(S.combinationSum2(candidates, target))
candidates = [10,1,2,7,6,1,5,1,2,2,2]
target = 9
print(S.combinationSum2(candidates, target))