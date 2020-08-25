'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 方法一：双指针法1（此种方法在 python 中超出时间限制）
        # i，j 两个指针，j 始终在 i 之后搜索最小值，遍历所有的可能性，最后返回最小的那一个
        # i = 0
        # j = i + 1
        # if len(prices) <= 1:
        #     return 0
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         new_pro = prices[j] - prices[i]
        #         if new_pro > max_profit:
        #             max_profit = new_pro
        # return max_profit

        # 方法二：双指针法2
        # 改进方法一，将其中的无用比较过程略去，j 每次直接定位到 i 后的 min 值
        # i = 0
        # j = i + 1
        # if len(prices) <= 1:
        #     return 0
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     max_ = max(prices[i+1:])
        #     if max_ - prices[i] > max_profit:
        #         max_profit = max_ - prices[i]
        # return max_profit
    
        # 方法三：一次遍历
        # 参考官方解答，一次扫描，遇到最小值更新最小值，同时计算最大利润，并更新当前的最大利润
        # 即：遍历一遍数组，计算每次 到当天为止 的最小股票价格和最大利润。
        max_pro = 0
        if len(prices) == 0:
            return 0
        min_num = max(prices)
        for i in range(len(prices)):
            if min_num > prices[i]:
                min_num = prices[i]
            else:
                if max_pro < prices[i] - min_num:
                    max_pro = prices[i] - min_num
        return max_pro
            
S = Solution()
prices = [7,1,5,3,6,4]
print(S.maxProfit(prices))
prices = []
print(S.maxProfit(prices))
prices = [2,4,1]
print(S.maxProfit(prices))