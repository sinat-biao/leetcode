"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
class Solution(object):
    def iterParenthesis(self, all_combs, k_l, k_r, n, str_now):
        print(all_combs)
        if k_r == n:
            all_combs.append(str_now)
            return
        if k_l == 0:
            self.iterParenthesis(all_combs, k_l+1, k_r, n, str_now+'(')
        else:
            if k_l == n:
                self.iterParenthesis(all_combs, k_l, k_r + 1, n, str_now+')')
            else:
                if k_l > k_r:
                    self.iterParenthesis(all_combs, k_l+1, k_r, n, str_now+'(')
                    self.iterParenthesis(all_combs, k_l, k_r + 1, n, str_now+')')
                else:
                    self.iterParenthesis(all_combs, k_l + 1, k_r, n, str_now + '(')
        
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 方法一：递归（回溯）
        all_combinations = []
        self.iterParenthesis(all_combinations, 0, 0, n, str_now='')
        return all_combinations


S = Solution()
n = 3
print(S.generateParenthesis(n))
n = 1
print(S.generateParenthesis(n))
        