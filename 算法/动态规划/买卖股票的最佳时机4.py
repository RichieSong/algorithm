# coding:utf-8
'''
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        有问题。。。。
        """
        n = len(prices)
        if n < 2: return 0

        pre_max_profit = [0 for i in range(n)]
        pro_max_profit = [0 for i in range(n)]
        max_profit = 0
        pre_min_price = prices[0]
        for i in range(1, n):
            pre_min_price = min(pre_min_price, prices[i])
            pre_max_profit[i] = max(pre_max_profit[i - 1], prices[i] - pre_min_price)
        pro_max_sell = prices[n - 1]
        for k in range(n - 2, -1, -1):
            pro_max_sell = max(pro_max_sell, prices[k])
            pro_max_profit[k] = max(pro_max_profit[k + 1], pro_max_sell - prices[k])
        for j in range(n):
            max_profit = max(max_profit, pre_max_profit[j]+pro_max_profit[j])
        return max_profit
