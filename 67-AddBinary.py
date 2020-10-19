"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 方法一：模拟进位运算，依次累加
        # n_a = len(a)
        # n_b = len(b)
        # n_min = min(n_a, n_b)
        # n_max = max(n_a, n_b)
        # if n_a > n_b:
        #     max_ab = a
        # else:
        #     max_ab = b
        # sum_ab = []
        # go = 0
        # for i in range(-1, -n_min-1, -1):
        #     if int(b[i]) + int(a[i]) + go == 0:
        #         sum_ab.insert(0, 0)
        #         go = 0
        #     elif int(b[i]) + int(a[i]) + go == 1:
        #         sum_ab.insert(0, 1)
        #         go = 0
        #     elif int(b[i]) + int(a[i]) + go == 2:
        #         sum_ab.insert(0, 0)
        #         go = 1
        #     else:
        #         # int(b[i]) + int(a[i]) + go == 3:
        #         sum_ab.insert(0, 1)
        #         go = 1
        # print(sum_ab)
        # for i in range(n_max-1-n_min, -1, -1):
        #     if int(max_ab[i]) + go == 0:
        #         sum_ab.insert(0, 0)
        #         go = 0
        #     elif int(max_ab[i]) + go == 1:
        #         sum_ab.insert(0, 1)
        #         go = 0
        #     elif int(max_ab[i]) + go == 2:
        #         sum_ab.insert(0, 0)
        #         go = 1
        #     else:
        #         # int(a[i]) + go == 3:
        #         sum_ab.insert(0, 1)
        #         go = 1
        # if go == 1:
        #     sum_ab.insert(0, 1)
        # print(sum_ab)
        # str_sum = ''
        # for i in range(len(sum_ab)):
        #     str_sum += str(sum_ab[i])
        # return str_sum
    
        # 方法二：转成十进制 -> 相加 -> 转成二进制
        tena = self.two2ten(a)
        tenb = self.two2ten(b)
        print(tena, tenb)
        addab = tena + tenb
        twoab = self.ten2two(addab)
        return twoab

    def two2ten(self, two):
        n = len(two)
        ten = 0
        i = n-1
        count = 0
        while i >= 0:
            ten += int(two[i]) * pow(2, count)
            count += 1
            i -= 1
        return ten
    
    def ten2two(self, ten):
        two = []
        while True:
            y = ten % 2
            t = int(ten / 2)
            if t == 0:
                two.insert(0, y)
                break
            else:
                two.insert(0,y)
                ten = t
        str_two = ''
        for i in two:
            str_two += str(i)
        return str_two
        
        

S = Solution()
a = "11"
b = "1"
print(S.addBinary(a, b))    # 100
a = "1010"
b = "1011"
print(S.addBinary(a, b))    # 10101
a = '1'
b = '111'
print(S.addBinary(a, b))    # 1000
a = "100"
b = "110010"
print(S.addBinary(a, b))    # 110110
