"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
"""
class Solution(object):
    def isnumber(self, c):
        if '0' <= c and c <= '9':
            return True
        else:
            return False
    
    def issign(self, c):
        if c == '-' or c == '+':
            return True
        else:
            return False
                
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：python 函数走起
        # s = s.strip()
        # n = len(s)
        # if len(s) == 0:
        #     return 0
        # str_ = ''
        # i = 0
        # if self.isnumber(s[0]) or self.issign(s[0]):
        #     str_ += s[0]
        #     i += 1
        #     while i < n and self.isnumber(s[i]):
        #         str_ += s[i]
        #         i += 1
        # else:
        #     return 0
        # if str_ == "+" or str_ == '-':
        #     return 0
        # int_str = int(str_)
        # if int_str > 2147483647:
        #     int_str = 2147483647        
        # if int_str < -2147483648:
        #     int_str = -2147483648
        # return int_str
    
        # 方法二：自动机（DFA）
        # 使用自动机记录每次状态转移的情况，并将状态转移表写入代码中
        automaton = Automaton()
        for c in s:
            automaton.get(c)
        num = int(automaton.sign) * automaton.ans
        print(num)
        if num > 2147483647:
            num = 2147483647
        if num < -2147483648:
            num = -2147483648
        return num
   
class Automaton:
    def __init__(self):
        self.state = 'start'     
        self.sign = 1
        self.ans = 0
        self.table = {
            'start':['start', 'signed', 'in_number', 'end'],
            'signed':['end', 'end', 'in_number', 'end'],
            'in_number':['end', 'end', 'in_number', 'end'],
            'end':['end', 'end', 'end', 'end']
        }
    
    def get_col(self, c):
        if c == ' ':
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c >= '0' and c <= '9':
            return 2
        else:
            return 3
    
    def get(self, c):
        # 获取下一个状态
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else '-1'
        

    
S = Solution()
str = '42'
print(S.myAtoi(str))
str = "   -42"
print(S.myAtoi(str))
str = "4193 with words"
print(S.myAtoi(str))
str = "words and 987"
print(S.myAtoi(str))
str = "-91283472332"
print(S.myAtoi(str))
str = "-9332 456 str"
print(S.myAtoi(str))
str = "+-12"
print(S.myAtoi(str))
str = "21474836460"
print(S.myAtoi(str))