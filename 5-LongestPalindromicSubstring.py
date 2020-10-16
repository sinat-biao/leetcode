"""
Given a string s, return the longest palindromic substring in s.
"""
class Solution(object):
    def isPalindromic(self, subs):
        n = len(subs)
        mid = int(n / 2)
        for k in range(mid):
            if subs[k] != subs[n-k-1]:
                return False
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法一：遍历并判断每个子字符串（超时）
        # n = len(s)
        # if n == 0:
        #     return ''
        # ls = s[0]
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if self.isPalindromic(s[i:j+1]):
        #             if len(ls) < len(s[i:j+1]):
        #                 ls = s[i:j+1]
        # return ls
    
        # 方法二：双指针法
        # 用两个指针 i，j；i 从前往后依次遍历，每次遍历时，j 从后往前搜索，找到一个与 i 处值相同的元素后，判断此时 s[i:j+1] 是否为回文。
        # 同时在之后的比较中，判断 s[i:j+1] 的长度是否小于 ls 已有的长度，若小于，后面的无需再比较。
        # n = len(s)
        # ls = ''
        # for k in range(n):
        #     i = k
        #     j = n - 1 
        #     while j > i and j - i + 1 > len(ls):
        #         if s[j] == s[i]:
        #             if self.isPalindromic(s[i:j+1]):
        #                 if len(ls) < j - i + 1:
        #                     ls = s[i:j+1]
        #                     break
        #         j -= 1
        # if ls == '':
        #     if n != 0:
        #         ls = s[0]
        # return ls
    
        # 方法三：动态规划
        # 算法详见：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
        n = len(s)
        dp = [[-1]*n for k in range(n)]
        if n < 2:
            return s
        maxlen = 1
        begin = 0
        for i in range(n):
            dp[i][i] = 0
        for j in range(1, n):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == 1 and maxlen < j - i + 1:
                    maxlen = j - i + 1
                    begin = i
        return s[begin: begin + maxlen]
        
        # 方法四：中心扩散
        # 从一个中心扩散搜索最大的回文，此方法思路与双指针类似，只不过双指针是收缩而已。
            

S = Solution()
s = 'babad'
print(S.longestPalindrome(s))
s = 'cbbd'
print(S.longestPalindrome(s))
s = 'a'
print(S.longestPalindrome(s))
s = ''
print(S.longestPalindrome(s))
s = 'ac'
print(S.longestPalindrome(s))
s = 'bb'
print(S.longestPalindrome(s))
s = 'ccc'
print(S.longestPalindrome(s))