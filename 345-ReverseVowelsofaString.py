"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法一：双指针
        i = 0
        j = len(s) - 1
        s = list(s)
        vowels = ['a', 'e', 'i' ,'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            while i < j and not s[i] in vowels:
                i += 1
            while i < j and not s[j] in vowels:
                j -= 1
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        str_ = ''
        for i in s:
            str_ += i
        return str_


S = Solution()
s = "hello"
print(S.reverseVowels(s))
s = "leetcode"
print(S.reverseVowels(s))
s = ""
print(S.reverseVowels(s))
s = "olate"
print(S.reverseVowels(s))
s = "aA"
print(S.reverseVowels(s))