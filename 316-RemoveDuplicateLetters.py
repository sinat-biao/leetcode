"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
"""
class Solution(object):        
    def iterlist(self, result_list, s, k):
        if k == len(s):
            return
        result_linshi = []
        for i in range(len(result_list)):
            if result_list[i].find(s[k]) != -1:
                result_copy = result_list[i].replace(s[k], '')
                result_copy += s[k]
                result_linshi.append(result_copy)
            else:
                result_list[i] += s[k]
        result_list += result_linshi
        print(result_list)
        self.iterlist(result_list, s, k+1)
        
        
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法一：递归（超时）
        # 通过递归遍历所有的非重复组合
        # result_list = [s[0]]
        # self.iterlist(result_list, s, 1)
        # print(result_list)
        
        # 方法二：递归搜索所有的非重复组合（超时）
        # result_list = []
        # n = len(s)
        # for i in range(n):
        #     if i == 0:
        #         list_ = [s[i]]
        #         result_list.append(list_)
        #         continue
        #     result_list_copy = [rs for rs in result_list]
        #     for result in result_list_copy:
        #         if s[i] in result:
        #             # print(result)
        #             result_copy = [cc for cc in result]
        #             result_copy.remove(s[i])
        #             result_copy.append(s[i])
        #             result_list.append(result_copy)
        #         else:
        #             result.append(s[i])
        #     print(result_list)
        # print(result_list)
        # result_strs = []
        # for list_ in result_list:
        #     st = ''
        #     for c in list_:
        #         st += c
        #     result_strs.append(st)
        # print(result_strs)
        # result_strs.sort()
        # print(result_strs)
        # return result_strs[0]
        
        # 方法三：单调栈
        # 算法详见：https://leetcode-cn.com/problems/remove-duplicate-letters/solution/you-qian-ru-shen-dan-diao-zhan-si-lu-qu-chu-zhong-/
        stack = []
        # 维护一个计数器记录字符串中字符的数量
        # 因为输入为 ASCII 字符，大小 256 够用了
        count = [0] * 256
        for i in range(len(s)):
            count[ord(s[i])] += 1
        instack = [False] * 256
        for c in s:
            # 每遍历过一个字符，都将对应的计数减一
            count[ord(c)] -= 1
            if instack[ord(c)]:
                continue
            while len(stack) > 0 and stack[-1] > c:
                # 若之后不存在栈顶元素了，则停止 pop
                if count[ord(stack[-1])] == 0:
                    break
                # 若之后还有，则可以 pop
                instack[ord(stack.pop())] = False
            stack.append(c)
            instack[ord(c)] = True
        result = ''
        while len(stack) > 0:
            result += stack.pop(0)
        return result
                

                        
        

S = Solution()
s = "bcabc"
print(S.removeDuplicateLetters(s))
# s = "cbacdcbc"
# print(S.removeDuplicateLetters(s))
# s = "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"
# print(S.removeDuplicateLetters(s))
# s = s.replace('a', '')
# print(s)


# ss = ['adsf', 'poj']
# for c in ss:    # 这种遍历方式只是获取了 ss 中每个元素的一个副本，改动不会加到原来的元素上
#     print(c)
#     c += '-'
# print(ss)
# for i in range(len(ss)):
#     print(ss[i])
#     ss[i] += '-'
# print(ss)