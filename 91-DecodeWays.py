"""
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""
class Solution(object):
    def iterDecoding(self, s, k, all_decode_list, decode_list):
        print(all_decode_list)
        n = len(s)
        if k >= n:
            all_decode_list.append([i for i in decode_list])
            return
        if s[k] == '0':
            return
        decode_list.append(s[k])
        self.iterDecoding(s, k+1, all_decode_list, decode_list)
        decode_list.pop()
        if k + 1 < n:
            decode_list.append(s[k:k+2])
            self.iterDecoding(s, k+2, all_decode_list, decode_list)
            decode_list.pop()
        
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：递归（超时）
        # all_decode_lists = []
        # self.iterDecoding(s, 0, all_decode_lists, [])
        # print(all_decode_lists)
        # count = 0
        # for li in all_decode_lists:
        #     isval = True
        #     for num in li:
        #         if int(num) >= 1 and int(num) <= 26:
        #             continue
        #         else:
        #             isval = False
        #     if isval:
        #         count += 1
        # return count
    
        # 方法二：递推
        # 3 位数共有 3 种不同的组合，后面每多一位，就会在原来的基础上判断组合形式，递推出新的组合形式
        # 存储截至目前位的所有组合形式，最后返回最后一位的组合数即可。
        # n = len(s)
        # dic = {}
        # for i in range(n):
        #     if i == 0 and s[i] == '0':
        #         dic[0] = []
        #     elif i == 0:
        #         dic[i] = []
        #         dic[i].append([s[i]])
        #     if i > 0:
        #         dic[i] = []
        #         for list_ in dic[i-1]:
        #             if s[i] != '0':
        #                 dic[i].append(list_ + [s[i]])
        #                 if int(list_[-1]) < 9 and int(list_[-1] + s[i]) <= 26:
        #                     dic[i].append(list_[:-1] + [list_[-1] + s[i]])
        #             else:
        #                 if int(list_[-1]) < 3:
        #                     dic[i].append(list_[:-1] + [list_[-1] + s[i]])
        # print(dic)
        # return len(dic[n-1])

        # 方法三：动态规划
        # 可以发现，在所有元素都只能取 1，2 的时候（即不管怎么组合都有意义的情况下），令 f[i] 代表截至第 i 个索引处时的组合数，
        # 则有 f[i] = f[i-2] + f[i-1]，因为此时可以将 s[i] 单独加在之前的所有组合上，共有 f[i-1] 个新组合；同时，
        # 将 s[i] 与 s[i-1] 结合组成 2 位数也是一种新组合，这种组合要求前一步的组合中最后一个元素是个位数，这种情况
        # 刚好和 f[i-2] 时的组合数一致（因为只看 f[i-2] 时的，相当于 i-1 时的那个元素还没有加上，其单独存在，作为个位数）。
        n = len(s)
        f = []
        for i in range(n):
            if i == 0 and s[i] == '0':
                return 0
            elif i == 0:
                f.append(1)
            if i == 1 and s[i] != '0':
                if int(s[i-1] + s[i]) <= 26:
                    f.append(2)
                else:
                    f.append(1)
            elif i == 1 and s[i] == '0':
                if int(s[i-1] + s[i]) > 26:
                    return 0
                else:
                    f.append(1)
            if i > 1:
                if s[i] == '0':
                    if s[i-1] == '0':
                        return 0
                    else:
                        if int(s[i-1] + s[i]) > 26:
                            return 0
                        else:
                            f.append(f[i-2])
                elif s[i-1] == '0':
                    f.append(f[i-1])
                else:
                    if int(s[i-1]+s[i]) <= 26:
                        f.append(f[i-1] + f[i-2])
                    else:
                        f.append(f[i-1])
        print(f)
        return f[-1]
    
                    
S = Solution()
s = '12'
print(S.numDecodings(s))
s = '226'
print(S.numDecodings(s))
s = '0'
print(S.numDecodings(s))
s = '1'
print(S.numDecodings(s))
s = '2101'
print(S.numDecodings(s))
s = "10"
print(S.numDecodings(s))
s = "27"
print(S.numDecodings(s))
s = "111111"
print(S.numDecodings(s))
s = "10010"
print(S.numDecodings(s))
s = "230"
print(S.numDecodings(s))
s = "301"
print(S.numDecodings(s))
# s = "111111111111111111111111111111111111111111111"
# print(S.numDecodings(s))