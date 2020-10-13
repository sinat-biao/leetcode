"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 方法一：搜索遍历
        # n_s = len(haystack)
        # n_n = len(needle)
        # if n_n == 0:
        #     return 0
        # i = 0
        # j = 0
        # while i < n_s:
        #     if n_s - i < n_n:
        #         return -1
        #     if needle[j] == haystack[i]:
        #         j += 1
        #         while j < n_n:
        #             if needle[j] != haystack[i+j]:
        #                 break
        #             else:
        #                 j += 1
        #         if j == n_n:
        #             return i
        #         else:
        #             j = 0
        #     i += 1
        # return -1
    
        # 方法二：滚动哈希
        # 常数时间内生成哈希，并将其与 needle 数组的哈希值依次进行比较
        n = len(haystack)
        L = len(needle)
        if L > n:
            return -1
        # 计算 needle 和 haystack 的前 L 个元素的哈希值
        a = 26
        h = 0
        ref_h = 0
        modulus = pow(2, 31)
        for i in range(L):
            # ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
            # 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
            h = (h * a + ord(haystack[i]) - ord('a')) % modulus
            ref_h = (ref_h * a + ord(needle[i]) - ord('a')) % modulus
        if h == ref_h:
            return 0
        al = pow(a, L, modulus)
        # 循环计算后面的哈希值
        for i in range(1, n-L+1):
            h = (h * a - (ord(haystack[i-1]) - ord('a')) * al + ord(haystack[i+L-1])-ord('a')) % modulus
            if h == ref_h:
                return i
        return -1
            

S = Solution()
haystack = "hello"
needle = 'll'
print(S.strStr(haystack, needle))   # 2
haystack = "aaaaa"
needle = "bba"
print(S.strStr(haystack, needle))   # -1
haystack = ""
needle = ""
print(S.strStr(haystack, needle))   # 0
haystack = "hasssfsfsf"
needle = "sf"
print(S.strStr(haystack, needle))   # 4
haystack = "a"
needle = ""
print(S.strStr(haystack, needle))   # 0
haystack = "aaa"
needle = "aaaa"
print(S.strStr(haystack, needle))   # -1
            
