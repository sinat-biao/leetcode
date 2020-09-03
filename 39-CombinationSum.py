"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""
class Solution(object):
    
    def recursionsearch(self, candidates, new_target, list_sub, list_):
        # 递归搜索函数
        # print(list_sub)
        if min(candidates) > new_target:
            # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            if len(list_sub) != 0:
                list_sub.pop()
            return
        else:
            for i in candidates:
                if i == new_target:
                    list_sub.append(i)
                    list_.append([j for j in list_sub])
                    # print(list_)
                    if len(list_sub) != 0:
                        list_sub.pop()
                    if len(list_sub) != 0:
                        list_sub.pop()
                    # print('------------------------')
                    return
                else:
                    # print('++++++++++++++++++++++++')
                    list_sub.append(i)
                    self.recursionsearch(candidates[candidates.index(i):], new_target-i, list_sub, list_)
            if len(list_sub) != 0:
                list_sub.pop()
                
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 方法一：递归
        # 用一个数组模拟栈，对 candidates 中的每一个元素，先取一个元素入栈，然后 target 减去当前元素的值得到 new_target，
        # 然后在 new_target 基础上再执行递归操作，直到遍历到等于 new_target 的元素，然后将当前栈状态作为一种解放入最终的 list 中，并同时弹出栈顶元素，继续遍历后面结果。
        # 若遍历到当前元素大于 new_target，说明此时栈积累的状态已经不满足解的条件了，将栈顶元素出栈，继续遍历后面结果。
        # 同时为了防止出现重复的栈状态（如 [2,2,3] 和 [2,3,2]），可以先对数组进行一次排序，然后每次递归时，取 candidates 中当前元素及之后的元素进行下轮递归。
        list_ = []
        list_sub = []
        candidates.sort()
        self.recursionsearch(candidates, target, list_sub, list_)
        return list_    
    

S = Solution()
# candidates = [2,3,6,7]
# target = 7
# print(S.combinationSum(candidates, target))
# candidates = [2,3,5]
# target = 8
# print(S.combinationSum(candidates, target))
candidates = [2]
target = 1
print(S.combinationSum(candidates, target))
candidates = [4,2,8]
target = 8
print(S.combinationSum(candidates, target))