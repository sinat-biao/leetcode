"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution(object): 
    def iteCombinations(self, dd, list_dig, k, str_now, all_combs):
        print(all_combs)
        if k >= len(list_dig):
            all_combs.append(str_now)
            return
        for i in dd[list_dig[k]]:
            self.iteCombinations(dd, list_dig, k+1, str_now + i, all_combs)
        
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 方法一：递归
        dd = {
            2:['a', 'b', 'c'],
            3:['d', 'e', 'f'],
            4:['g', 'h', 'i'],
            5:['j', 'k', 'l'],
            6:['m', 'n', 'o'],
            7:['p', 'q', 'r', 's'],
            8:['t', 'u', 'v'],
            9:['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        list_dig = list(int(l) for l in digits)
        print(list_dig)
        all_combinations = []
        self.iteCombinations(dd, list_dig, k=0, str_now='', all_combs=all_combinations)
        return all_combinations    


S = Solution()
digits = "23"
print(S.letterCombinations(digits))
digits = "2"
print(S.letterCombinations(digits))
digits = ""
print(S.letterCombinations(digits))
digits = "7"
print(S.letterCombinations(digits))