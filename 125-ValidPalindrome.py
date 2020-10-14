"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution(object):
    def isalpha(self, c):
        if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
            return True
        else:
            return False
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 方法一：双指针
        # 使用两个指针 i，j，一个从左往右，一个从右往左，直到两者在中间回合。
        # 移动过程中跳过非数字+字母的字符，否则进行比较，然后两者均向中间移动一位。
        # s = s.lower()
        # print(s)
        # n = len(s)
        # i = 0
        # j = n - 1
        # while i < j:
        #     while i < j and not self.isalpha(s[i]):
        #         i += 1
        #     while i < j and not self.isalpha(s[j]):
        #         j -= 1
        #     if s[i] != s[j]:
        #         print(s[i], s[j], i, j)
        #         return False
        #     i += 1
        #     j -= 1
        # return True
    
        # 方法二：翻转字符
        # 首先对数组进行筛选，只保留字母和数字，然后翻转字符，比较前半部分是否一致
        n = len(s)
        s = s.lower()
        s_copy1 = []
        s_copy2 = []
        for i in range(n):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                s_copy1.append(s[i])
                s_copy2.insert(0, s[i])
        print(s_copy1)
        print(s_copy2)
        if len(s_copy1) == 0:
            return True
        mid = int(len(s_copy1) / 2)
        for i in range(mid+1):
            if s_copy1[i] != s_copy2[i]:
                return False
        return True
        

S = Solution()
s = "A man, a plan, a canal: Panama"
print(S.isPalindrome(s))
s = "race a car"
print(S.isPalindrome(s))
s = "0P"
print(S.isPalindrome(s))
s = " "
print(S.isPalindrome(s))