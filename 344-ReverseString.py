"""
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 方法一：双指针
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i] 
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return s

S = Solution()
s = ["h","e","l","l","o"]
print(S.reverseString(s))
s = ["H","a","n","n","a","h"]
print(S.reverseString(s))