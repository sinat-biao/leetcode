'''
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 方法一：直接加最后的数
        # count = len(digits) - 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
            else:
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
        
        # 方法二：类型转化 list -> int -> str -> list
        # count = 0
        # for i in digits:
        #     count = count * 10 + i
        # print(count)
        # count += 1
        # str_dig = str(count)
        # return [int(j) for j in str_dig]
        

S = Solution()
digits = [1,2,3]
print(S.plusOne(digits))
digits = [9,9,9]
print(S.plusOne(digits))
