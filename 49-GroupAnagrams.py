"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 方法一：哈希法
        # 将每个字符串都用哈希表存储一次，然后比较哈希表的值即可
        # hash_strs = {}
        # result = []
        # for str_ in strs:
        #     hash_ = {}
        #     for i in range(len(str_)):
        #         if str_[i] in hash_:
        #             hash_[str_[i]] += 1
        #         else:
        #             hash_[str_[i]] = 1
        #     hash_strs[str_] = hash_
        # print(hash_strs)
        # while len(strs) != 0:
        #     g = strs.pop()
        #     d = hash_strs[g]
        #     linshi = []
        #     linshi.append(g)
        #     strs_copy = [i for i in strs]
        #     for s in strs_copy:
        #         if hash_strs[s] == d:
        #             linshi.append(s)
        #             strs.remove(s)
        #     result.append(linshi)
        # return result
    
        # 方法二：状态表
        # 每个字符对应一个26为的状态表，出现的字符位置为1，比较状态表即可
        state_dict = {}
        for str_ in strs:
            state = [0] * 26
            for s in str_:
                state[ord(s)-ord('a')] += 1
            state_dict[str_] = state
        print(state_dict)
        result = []
        while len(strs) != 0:
            linshi = []
            g = strs.pop()
            linshi.append(g)
            strs_copy = [i for i in strs]
            for s in strs_copy:
                if state_dict[g] == state_dict[s]:
                    linshi.append(s)
                    strs.remove(s)
            result.append(linshi)
        return result
    
        # 方法三：硬编码(有误)
        # 为每个字符串提供一个硬编码
        # encode_dict = {}
        # result = []
        # for str_ in strs:
        #     code = 0
        #     for s in str_:
        #         code *= ord(s) - ord('a')
        #     encode_dict[str_] = code * len(str_)
        # print(encode_dict)
        # while len(strs) != 0:
        #     linshi = []
        #     g = strs.pop()
        #     linshi.append(g)
        #     strs_copy = [k for k in strs]
        #     for s in strs_copy:
        #         if encode_dict[s] == encode_dict[g]:
        #             linshi.append(s)
        #             strs.remove(s)
        #     result.append(linshi)
        # return result
                

S = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(S.groupAnagrams(strs))
strs = [""]
print(S.groupAnagrams(strs))
strs = ["a"]
print(S.groupAnagrams(strs))
strs = ["ddg","dg","ddd","ggg"]
print(S.groupAnagrams(strs))
strs = ["", ""]
print(S.groupAnagrams(strs))