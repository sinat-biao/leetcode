"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 方法一：模拟乘法
    #     123
    #     456
    #     -----
    #     738
    #    615 
    #   492
        leijia = [[0]*(len(num1) + len(num2)) for i in range(len(num2))]
        print(leijia)
        for j in range(len(num2)-1, -1, -1):
            jinwei = 0
            local = len(leijia[0]) - 1 - (len(num2)-1 - j)
            for i in range(len(num1)-1, -1, -1):
                mul = int(num2[j]) * int(num1[i]) + jinwei
                jinwei = int(mul / 10)
                yushu = mul % 10
                # print(mul, jinwei, yushu)
                leijia[j][local] = yushu
                local -= 1
            if jinwei != 0:
                leijia[j][local] = jinwei
        print(leijia)
        # 对各位相乘结果进行累加
        result = [0] * len(leijia[0])
        local = len(result) - 1
        jinwei = 0
        for j in range(len(leijia[0])-1, -1, -1):
            sum_ = 0
            for i in range(len(leijia)):
                sum_ += leijia[i][j]
            sum_ += jinwei
            jinwei = int(sum_ / 10) 
            yushu = sum_ % 10
            # print(sum_, jinwei, yushu)
            result[local] = yushu
            local -= 1
        print(result)
        result_str = ''
        for i in range(len(result)):
            if i == 0 and result[i] == 0:
                result_str += ''
            else:
                result_str += str(result[i])
        return result_str


S = Solution()
num1 = '2'
num2 = '3'
print(S.multiply(num1, num2))
num1 = '123'
num2 = '456'
print(S.multiply(num1, num2))
num1 = '9'
num2 = '9'
print(S.multiply(num1, num2))