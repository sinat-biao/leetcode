"""
Given a roman numeral, convert it to an integer.
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：遍历搜索
        # 将所有罗马数字组合通过字典记录下来，然后遍历数组时，每次将当前元素和后一个元素组合起来，
        # 看其是否在字典中，若在字典中，取出对应值，然后后移 2 位继续遍历；若不在，则取出单个元素对应的值，
        # 然后后移 1 位继续遍历。
        # 定义所有的罗马字符串
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000,
                'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        n = len(s)
        sum_ = 0
        i = 0
        while i < n:
            if i + 1 < n:
                if s[i] + s[i+1] in dict.keys():
                    sum_ = sum_ + int(dict[s[i]+s[i+1]])
                    i += 2
                else:
                    sum_ += int(dict[s[i]])
                    i += 1
            else:
                sum_ += int(dict[s[i]])
                i += 1
        return sum_


S = Solution()
s = 'III'
print(S.romanToInt(s))
s = 'IV'
print(S.romanToInt(s))
s = 'IX'
print(S.romanToInt(s))
s = 'LVIII'
print(S.romanToInt(s))
s = 'MCMXCIV'
print(S.romanToInt(s))