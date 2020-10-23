"""
Implement a basic calculator to evaluate a simple expression string.
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：队列
        # n = len(s)
        # s_list = []
        # i = 0
        # while i < n:
        #     if s[i] == ' ':
        #         i += 1
        #     elif s[i] == '+' or s[i] == '-':
        #         s_list.append(s[i])
        #         i += 1
        #     elif s[i] >= '0' and s[i] <= '9':
        #         start = i
        #         i += 1
        #         while i < n and s[i] >= '0' and s[i] <= '9':
        #             i += 1
        #         s_list.append(int(s[start:i]))
        #     elif s[i] == '*' or s[i] == '/':
        #         sig = s[i]
        #         p1 = s_list.pop()
        #         i += 1
        #         while i < n and s[i] == ' ':
        #             i += 1
        #         start = i
        #         i += 1
        #         while i < n and s[i] >= '0' and s[i] <= '9':
        #             i += 1
        #         p2 = s[start:i]
        #         if sig == '*':
        #             s_list.append(int(p1) * int(p2))
        #         if sig == '/':
        #             s_list.append(int(int(p1) / int(p2)))
        # print(s_list)
        
        # # 出队
        # while len(s_list) > 2:
        #     p1 = s_list.pop(0)
        #     sig = s_list.pop(0)
        #     p2 = s_list.pop(0)
        #     if sig == '+':
        #         s_list.insert(0, p1 + p2)
        #     else:
        #         s_list.insert(0, p1 - p2)
        # return s_list[0]
    
        # 方法二：一遍扫描
        # 在扫描的时候跳过空格，同时将数字字符串转为 int 型存入 list 中。
        # 遇到运算符号，若是 +、-，需要判断后一个符号是否是 *、/，若是，则当前符号不运算直接加入 list；
        # 若不是，则当前的 +、- 可以直接运算，从 list 尾部取出一个元素与下一个数字元素进行运算后加入 list。
        n = len(s)
        s_list = []
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+' or s[i] == '-':
                sig = s[i]
                # 判断下个符号是否是 *、/
                i += 1
                start = i
                while s[i] == ' ':
                    i += 1
                while i < n and s[i] >= '0' and s[i] <= '9':
                    i += 1
                p2 = s[start:i]
                while i < n and s[i] == ' ':
                    i += 1
                if i < n and (s[i] == '*' or s[i] == '/'):
                    s_list.append(sig)
                    s_list.append(int(p2))
                else:
                    p1 = s_list.pop()
                    if sig == '+':
                        s_list.append(p1 + int(p2))
                    else:
                        s_list.append(p1 - int(p2))
            elif s[i] >= '0' and s[i] <= '9':
                start = i
                i += 1
                while i < n and s[i] >= '0' and s[i] <= '9':
                    i += 1
                s_list.append(int(s[start:i]))
            elif s[i] == '*' or s[i] == '/':
                sig = s[i]
                p1 = s_list.pop()
                i += 1
                while i < n and s[i] == ' ':
                    i += 1
                start = i
                i += 1
                while i < n and s[i] >= '0' and s[i] <= '9':
                    i += 1
                p2 = s[start:i]
                if sig == '*':
                    s_list.append(int(p1) * int(p2))
                if sig == '/':
                    s_list.append(int(int(p1) / int(p2)))
                while i<n and s[i] == ' ':
                    i += 1
                if i >= n or s[i] == '+' or s[i] == '-':
                    while len(s_list) > 2:
                        p1 = s_list.pop(0)
                        sig = s_list.pop(0)
                        p2 = s_list.pop(0)
                        if sig == '+':
                            s_list.insert(0, p1 + p2)
                        else:
                            s_list.insert(0, p1-p2)
        print(s_list)


S = Solution()
s = "3+2*2"
print(S.calculate(s))
s = " 3/2 "
print(S.calculate(s))
s = " 3+5 / 2 "
print(S.calculate(s))
s = "3+2*2"
print(S.calculate(s))
s = "42"
print(S.calculate(s))
s = '  99   '
print(S.calculate(s))
s = "0-2147483647"
print(S.calculate(s))
s = "1-1+1"
print(S.calculate(s))