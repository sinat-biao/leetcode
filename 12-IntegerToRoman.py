"""
Given an integer, convert it to a roman numeral.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 方法一：枚举所有的情况
        # 题目要求 1 <= num <= 3999，那么，枚举这期间出现的每一阶进位的所有整数即可。
        # dd = {0:{0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'},
        #       1:{0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'},
        #       2:{0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'},
        #       3:{0:'', 1:'M', 2:'MM', 3:'MMM'}
        #       }
        # if num > 0 and num < 10:
        #     return dd[0][num]
        # elif num >= 10 and num < 100:
        #     shiwei = int(num / 10)
        #     gewei = num % 10
        #     return dd[1][shiwei] + dd[0][gewei]
        # elif num >= 100 and num < 1000:
        #     baiwei = int(num / 100)
        #     shiwei = int((num % 100) / 10)
        #     gewei = num % 100 % 10
        #     return dd[2][baiwei] + dd[1][shiwei] + dd[0][gewei]
        # else:
        #     qianwei = int(num / 1000)
        #     baiwei = int((num % 1000) / 100)
        #     shiwei = int(((num % 1000) % 100) / 10)
        #     gewei = num % 1000 % 100 % 10
        #     return dd[3][qianwei] + dd[2][baiwei] + dd[1][shiwei] + dd[0][gewei]

        # 方法二：贪心
        dd = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ds = ['M', 'CM', 'D','CD','C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        print(len(dd), len(ds))
        lomastr = ''
        for i in range(len(dd)):
            while dd[i] <= num:
                num -= dd[i]
                lomastr += ds[i]
        return lomastr

        

S = Solution()
num = 3
print(S.intToRoman(num))
num = 4
print(S.intToRoman(num))
num = 9
print(S.intToRoman(num))
num = 58
print(S.intToRoman(num))
num = 1994
print(S.intToRoman(num))
num = 10
print(S.intToRoman(num))
num = 100
print(S.intToRoman(num))
num = 101
print(S.intToRoman(num))