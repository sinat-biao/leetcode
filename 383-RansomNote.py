"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 方法一：遍历搜索
        # 依次匹配 ransmNote 中的每个字符，每次匹配时搜索整个 magazine 字符串
        # magazine_list = list(magazine)
        # i = 0
        # n = len(ransomNote)
        # while i < n:
        #     if i < n and ransomNote[i] in magazine_list:
        #         # idx = magazine_list.index(ransomNote[i])
        #         magazine_list.remove(ransomNote[i])
        #         i += 1
        #     else:
        #         return False
        # return True
    
        # 方法二：字典计数法
        # 用一个长度为26的数组还记录 magazine 里字母出现的次数，
        # 然后再用 ransomNote去 验证这个数组是否包含了 ransomNote 所需要的所有字母（再来一个哈希表）。
        hashset_rans = {}
        # hashset_mag = {}
        for i in range(len(ransomNote)):
            if ransomNote[i] in hashset_rans:
                hashset_rans[ransomNote[i]] += 1
            else:
                hashset_rans[ransomNote[i]] = 1
        print(hashset_rans)
        for i in range(len(magazine)):
            if magazine[i] in hashset_rans:
                hashset_rans[magazine[i]] -= 1
        for val in hashset_rans.values():
            if val > 0:
                return False
        return True
            


S = Solution()
ransomNote = "a"
magazine = "b"
print(S.canConstruct(ransomNote, magazine))
ransomNote = "aa"
magazine = "ab"
print(S.canConstruct(ransomNote, magazine))
ransomNote = "aa"
magazine = "aab"
print(S.canConstruct(ransomNote, magazine))