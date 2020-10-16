"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 方法一：二维数组保存
        # n = len(s)
        # if numRows == 1:
        #     l = n
        # else:
        #     l = int(n / (numRows*2-2) + 1) * (numRows - 1)
        # dd = [['0']* l for i in range(numRows)]
        # j = 0
        # k = 0
        # while k < n:
        #     # print(dd)
        #     for b in range(numRows):
        #         dd[b][j] = s[k]
        #         k += 1
        #         if k >= n:
        #             break
        #     j += 1
        #     if k >= n:
        #         break
        #     for b in range(numRows - 2, 0, -1):
        #         dd[b][j] = s[k]
        #         j += 1
        #         k += 1
        #         if k >= n:
        #             break
        #     if k >= n:
        #         break
        # # for d in dd:
        # #     print(d) 
        # str_ = ''        
        # for r in range(numRows):
        #     for low in range(l):
        #         if dd[r][low] != '0':
        #             str_ += dd[r][low]
        # return str_
    
        # 方法二：直接定位所有元素的位置
        # 第一行与最后一行元素每隔 (numRows - 1) * 2 - 1；
        # 第二行元素先隔 (numRows - 1) * 2 - 1，然后再隔 (numRows - (numRows - 1 - i) - 1) * 2 - 1 = i * 2 -1，依次重复。
        n = len(s)
        if numRows == 1:
            return s
        strs = ['' for i in range(numRows)]
        for i in range(numRows):
            c = i
            if i == 0:
                gap = (numRows-i-1)*2 - 1
                while c < n:
                    strs[i] += s[c]
                    c += gap + 1
            elif i > 0 and i < numRows - 1:
                gap1 = (numRows-i-1)*2 - 1
                # gap2 = (numRows - (numRows - 1 - i) - 1) * 2 - 1
                gap2 = i * 2 - 1
                g = 0
                while c < n:
                    strs[i] += s[c]
                    if g == 0:
                        c += gap1 + 1
                        g = 1
                    else:
                        c += gap2 + 1
                        g = 0
            else:
                gap = (numRows-1)*2 - 1
                while c < n:
                    strs[i] += s[c]
                    c += gap + 1
        print(strs)
        rt = ''
        for st in strs:
            rt += st
        return rt
            


S = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(S.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(S.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 5
print(S.convert(s, numRows))
s = "A"
numRows = 1
print(S.convert(s, numRows))
s = ""
numRows = 3
print(S.convert(s, numRows))