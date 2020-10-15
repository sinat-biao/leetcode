"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：哈希计数
        # 使用哈希表记录所有字母出现的次数，然后选择第一个次数为 1 的字符。
        # hashset_s = {}
        # for i in range(len(s)):
        #     if s[i] in hashset_s:
        #         hashset_s[s[i]] += 1
        #     else:
        #         hashset_s[s[i]] = 1
        # first_idx = len(s)
        # for key, val in hashset_s.items():
        #     if val == 1:
        #         idx = s.index(key)
        #         if idx < first_idx:
        #             first_idx = idx
        # if first_idx == len(s):
        #     return -1
        # else:
        #     return first_idx
        
        # 方法二：双指针搜索
        # 设定两个指针 i，j，i 依次向后搜索，每次 j 从 i+1 处向后搜索，查看是否有重复元素。
        # 若没有则返回 i，否则直到 i 到达末尾。
        reptchar = []
        n = len(s)
        for i in range(n):
            if s[i] in reptchar:
                continue
            for j in range(i+1, n):
                if s[j] == s[i]:
                    reptchar.append(s[i])
                    break
                if j == n-1 and s[j] != s[i]:
                    return i
            if i == n-1:
                if s[i] in reptchar:
                    return -1
                else:
                    return n-1
        return -1

S = Solution()
# s = "leetcode"
# print(S.firstUniqChar(s))
# s = "loveleetcode"
# print(S.firstUniqChar(s))
# s = "aab"
# print(S.firstUniqChar(s))
s = "aa"
print(S.firstUniqChar(s))