"""
Given two version numbers, version1 and version2, compare them.
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 方法一：分割比较
        v1_list = list(filter(None, version1.split('.')))
        v2_list = list(filter(None, version2.split('.')))
        print(v1_list, v2_list)
        for i in range(len(v1_list)):
            k = 0
            while k < len(v1_list[i])-1 and v1_list[i][k] == '0':
                k += 1
            v1_list[i] = v1_list[i][k:]
        for i in range(len(v2_list)):
            k = 0
            while k < len(v2_list[i])-1 and v2_list[i][k] == '0':
                k += 1
            v2_list[i] = v2_list[i][k:]
        print(v1_list, v2_list)
        v1_len = len(v1_list)
        v2_len = len(v2_list)
        # 如果最后一位是 0，没有意义，可以直接删掉
        i = v1_len-1
        while v1_list[i] == '0' and len(v1_list) > 1:
            v1_list.pop()
            i -= 1
        i = v2_len-1
        while v2_list[i] == '0' and len(v2_list) > 1:
            v2_list.pop()
            i -= 1
        print(v1_list, v2_list)
        v1_len = len(v1_list)
        v2_len = len(v2_list)
        k = 0
        while k < v1_len and k < v2_len:
            # print(k)
            if int(v1_list[k]) > int(v2_list[k]):
                return 1
            if int(v1_list[k]) < int(v2_list[k]):
                return -1
            k += 1
        if k < v1_len:
            return 1
        elif k < v2_len:
            return -1
        else:
            return 0            


S = Solution()
version1 = "1.01"
version2 = "1.001"
print(S.compareVersion(version1, version2))
version1 = "1.0"
version2 = "1.0.0"
print(S.compareVersion(version1, version2))
version1 = "0.1"
version2 = "1.1"
print(S.compareVersion(version1, version2))
version1 = "1.0.1"
version2 = "1"
print(S.compareVersion(version1, version2))
version1 = "7.5.2.4"
version2 = "7.5.3"
print(S.compareVersion(version1, version2))
version1 = "1"
version2 = "0"
print(S.compareVersion(version1, version2))