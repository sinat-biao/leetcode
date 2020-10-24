"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
"""
class Solution(object):
    def deserialize(self, s):
        n = len(s)
        stack = []
        # ni = NestedInteger()
        i = 0
        while i < n:
            if s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i] == ',':
                i += 1
            elif s[i] >= '0' and s[i] <= '9':
                start = i
                while i < n and s[i] >= '0' and s[i] <= '9':
                    i += 1
                stack.append(int(s[start:i]))
            elif s[i] == ']':
                list_ = []
                while len(stack) > 0 and stack[-1] != '[':
                    p = stack.pop()
                    list_.insert(0, p)
                stack.pop()
                i += 1
                stack.append(list_)
        print(stack)


S = Solution()
s = "324"
print(S.deserialize(s))
s = "[123,[456,[789]]]"
print(S.deserialize(s))
s = "[123,456,789]"
print(S.deserialize(s))
s = "[123,[456,789]]"
print(S.deserialize(s))