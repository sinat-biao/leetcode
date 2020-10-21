"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 方法一：插点
        # 在 1~n-1 这 n-1 个位置处插入三个点，然后判断形成的字符串是否合理即可
        n = len(s)
        if n > 12:
            return []
        d_list = []
        for i in range(1, n):
            for j in range(i+1, n):
                if i+3 < n and j > i + 3:
                    break
                for k in range(j+1, n):
                    if j+3 < n and k > j+3:
                        break
                    d_list.append([i, j, k])
        print(d_list)
        all_ip_add = []
        for i in d_list:
            s_list = list(s)
            s_list.insert(i[2], '.')
            s_list.insert(i[1], '.')
            s_list.insert(i[0], '.')
            all_ip_add.append(s_list)
        print(all_ip_add)
        all_ip_strs = []
        for ip in all_ip_add:
            i = 0
            sl = ''
            for i in ip:
                sl += i
            s_l = sl.split('.')
            isval = True
            for p in s_l:
                if len(p) > 1 and p[0] == '0':
                    isval = False
                elif int(p) > 255:
                    isval = False
            if isval:
                all_ip_strs.append(s_l[0] + '.' + s_l[1] + '.' + s_l[2] + '.' + s_l[3])
        # print(all_ip_strs)
        return all_ip_strs

        # 方法二：递归
        
        

S = Solution()
s = "25525511135"
print(S.restoreIpAddresses(s))
s = "0000"
print(S.restoreIpAddresses(s))
s = "1111"
print(S.restoreIpAddresses(s))
s = "010010"
print(S.restoreIpAddresses(s))
s = "101023"
print(S.restoreIpAddresses(s))