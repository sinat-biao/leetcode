"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法一：python 函数
        s_list = list(filter(None, s.split(' ')))   # filter的第一个参数为空的时候，会返回第二个参数中非空的值。
        print(s_list)
        s_list.reverse()
        print(s_list)
        result = ''
        for s_ in s_list:
            result += s_ + ' '
        return result[:-1]


S = Solution()
s = "the sky is blue "
print(S.reverseWords(s))
s = "  hello world  sy  "
print(S.reverseWords(s))
s = "a good   example"
print(S.reverseWords(s))
s = "  Bob    Loves  Alice   "
print(S.reverseWords(s))
s = "Alice does not even like bob"
print(S.reverseWords(s))