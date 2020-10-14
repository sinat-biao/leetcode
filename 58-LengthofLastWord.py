"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.
Note: A word is defined as a maximal substring consisting of non-space characters only.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：python 分割函数
        # 使用 split 会出现空字符串的问题，解决方式参见：
        # https://blog.csdn.net/life_journey/article/details/103254403?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
        # list_ = list(filter(None, s.split(' ')))
        # print(list_)
        # if len(list_) > 0:
        #     return len(list_[-1])
        # return 0
    
        # 方法二：双指针扫描
        # 使用两个指针 i，j，i 从头到尾扫描，遇到非空时，j 开始由此位置继续向后扫描，直到遇到下一个空格或到达数组末尾，
        # 然后每次 j 扫描停止，记录当前 j 的值。
        i = 0
        j = 0
        n = len(s)
        last_n_zero_count = j
        while i < n and j < n:
            if s[i] == " ":
                j = 0
                i += 1
            else:
                while i < n and j < n and s[i] != " ":
                    j += 1
                    i += 1
                last_n_zero_count = j
        return last_n_zero_count


S = Solution()
s = "Hello World"
print(S.lengthOfLastWord(s))
s = "a "
print(S.lengthOfLastWord(s))
s = "a"
print(S.lengthOfLastWord(s))
s = "b   a    "
print(S.lengthOfLastWord(s))