"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
"""
class Solution(object):
    def isletter(self, c):
        if c >= 'a' and c <= 'z':
            return True
        else:
            return False
    
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 方法一：栈
        path_list = []
        n = len(path)
        i = 0
        while i < n:
            if path[i] == '/':
                path_list.append(path[i])
                i += 1
            else:
                start = i
                while i < n and path[i] != '/':
                    i += 1
                path_list.append(path[start:i])
            # elif path[i] == '.':
            #     if i+1 < n and path[i+1] == '.':
            #         path_list.append('..')
            #         i += 2
            #     else:
            #         path_list.append('.')
            #         i += 1
            # else:
            #     start = i
            #     while i < n and self.isletter(path[i]):
            #         i += 1
            #     path_list.append(path[start:i])
        print(path_list)
        stack = []
        for s in path_list:
            if s == '/' and len(stack) > 0 and stack[-1] == s:
                continue
            if s == '..':
                if len(stack) > 1:
                    stack.pop()
                    if len(stack) > 0:
                        stack.pop()
                continue
            if s == '.':
                continue
            stack.append(s)
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        print(stack)
        path_new = ''
        for s in stack:
            path_new += s
        return path_new              


S = Solution()
path = "/home/"
print(S.simplifyPath(path))
path = "/../"
print(S.simplifyPath(path))
path = "/home//foo/"
print(S.simplifyPath(path))
path = "/a/./b/../../c/"
print(S.simplifyPath(path))
path = "/a/../../b/../c//.//"
print(S.simplifyPath(path))
path = "/a//b////c/d//././/.."
print(S.simplifyPath(path))
path = "/.."
print(S.simplifyPath(path))
path = "/..."
print(S.simplifyPath(path))