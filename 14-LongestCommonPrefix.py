"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 方法一：遍历比较
        common_prefix = ""
        if len(strs) == 0:
            return ""
        shortest_len = min([len(s) for s in strs])
        print(shortest_len)
        for i in range(shortest_len):
            char = strs[0][i]
            iscommon = True
            for s in strs:
                if s[i] != char:
                    iscommon = False
            if iscommon:
                common_prefix += char
            else:
                break
        return common_prefix


S = Solution()
strs = ["flower","flow","flight"]
print(S.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(S.longestCommonPrefix(strs))
strs = ["dog","dog3","dogert"]
print(S.longestCommonPrefix(strs))
strs = []
print(S.longestCommonPrefix(strs))
strs = ["cir","car"]
print(S.longestCommonPrefix(strs))