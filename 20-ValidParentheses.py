"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 方法一：栈匹配
        # 利用栈来存储匹配括号
        stack = list()
        n = len(s)
        for i in range(n):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != '(':
                    return False
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != '[':
                    return False
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != '{':
                    return False
        return True

S = Solution()
s = '()'
print(S.isValid(s))
s = "()[]{}"
print(S.isValid(s))
s = '(]'
print(S.isValid(s))
s = '([)]'
print(S.isValid(s))
s = '{[]}'
print(S.isValid(s))