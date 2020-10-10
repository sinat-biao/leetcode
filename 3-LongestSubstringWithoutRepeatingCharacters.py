"""
Given a string s, find the length of the longest substring without repeating characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 方法一：哈希表存储
        # 一次遍历，并将当前元素加入哈希表中，同时计数。
        # 一旦出现重复，清空哈希表，并重新开始上述过程，同时返回最大的计数值。
        # nums = 0
        # hashset = set()
        # count = 0
        # i = 0
        # j = i
        # while i < len(s):
        #     while j < len(s):
        #         if s[j] in hashset:
        #             hashset.clear()
        #             break
        #         else:
        #             hashset.add(s[j])
        #             count += 1
        #         j += 1
        #     i += 1
        #     j = i
        #     if count > nums:
        #         nums = count
        #     count = 0
        # return nums
    
        # 方法二：滑动窗口
        # 用一个 list 队列作为滑动窗口，每次出现重复元素，就从队首删除元素，知道队中不包含重复元素
        queue = list()
        nums = 0
        n = len(s)
        for i in range(n):
            if s[i] in queue:
                if nums < len(queue):
                    nums = len(queue)
                while len(queue) > 0:
                    out = queue.pop(0)
                    if out == s[i]:
                        queue.append(s[i])
                        break
            else:
                queue.append(s[i])
        if nums < len(queue):
            nums = len(queue)
        return nums
                    


S = Solution()
s = "abcabcbb"
print(S.lengthOfLongestSubstring(s))    # 3
s = "bbbbb"
print(S.lengthOfLongestSubstring(s))    # 1 
s = "pwwkew"
print(S.lengthOfLongestSubstring(s))    # 3
s = ""
print(S.lengthOfLongestSubstring(s))    # 0
s = " "
print(S.lengthOfLongestSubstring(s))    # 1
s = "dvdf"
print(S.lengthOfLongestSubstring(s))    # 3
s = "jbpnbwwd"
print(S.lengthOfLongestSubstring(s))    # 4

# s = " "
# print(len(s))
# print(s[0])