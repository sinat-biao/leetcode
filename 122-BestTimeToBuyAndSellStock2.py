'''
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        # 方法一：递归求解（python 中超出时间限制）
        # return self.max_(prices)
    
        # 方法二：峰谷法
        # 仔细考虑发现，连续增长的几个点之间最大的利润是最高点减去最低点；
        # 而非连续增长点之间，最大利润就是若干个增长点之间的利润和；
        # max_pro = 0
        # vally = 0
        # peak = 0
        # i = 0
        # while i < len(prices) - 1:
        #     while i < len(prices) -1 and prices[i] >= prices[i+1]:
        #         i += 1
        #     vally = prices[i]
        #     while i < len(prices) - 1 and prices[i] <= prices[i+1]:
        #         i += 1
        #     peak = prices[i]
        #     max_pro += peak - vally
        # return max_pro
        
        # 方法三：峰谷法变种（一次遍历）
        # 观察发现，连续增长的点之间，所有点的连续差值之和刚好等于峰谷差值，例如 [1,2,3,4,5]中：(2-1) + (3-2) + (4-3) + (5-4) = 5-1
        # 利用这个特性，方法二中的峰谷法就不需要每次扫描子段的峰谷了。
        max_pro = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i + 1]:
                max_pro += prices[i+1] - prices[i]
        return max_pro
    
    def max_(self, prices):
        # print(prices)
        if len(prices) == 0:
            return 0
        max_m = 0
        for i in range(len(prices)):
            max_pro = 0
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    # print(max_pro)
                    # 注意体会递归的构造思路
                    profit = self.max_(prices[j+1:]) + prices[j] - prices[i]
                    if profit > max_pro:
                        max_pro = profit
            if max_pro > max_m:
                max_m = max_pro
        return max_m
    

S = Solution()
prices = [7,1,5,3,6,4]  # 7
print(S.maxProfit(prices))  
prices = [1,2,3,4,5]    # 4
print(S.maxProfit(prices))
prices = [7,6,4,3,1]    # 0
print(S.maxProfit(prices))  
prices = [3,3,5,0,0,3,1,4]  # 需要买入卖出三次：(5-3) + (3-0) + (4-1) = 8
print(S.maxProfit(prices))
prices = [3,2,6,5,0,3]  # 7
print(S.maxProfit(prices))
prices = [2,1,4,5,2,9,7]    # 11
print(S.maxProfit(prices))
prices = [0,1,3,5,7,9]    # 11
print(S.maxProfit(prices))
