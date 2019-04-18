'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

observation:
Buy:    prices[i]: min{prices[k], k <= i}
Sell:   prices[j]: max{prices[k], k >= j}

1） 我们可以选择到目前为止价格最低的股价进行买入，在未来某一天卖出，这样就符合到未来某一天的时候，
    那天的收益是最高的这么一个DP思想，就是当前最优

2）然后我们可以根据到目前为止收益的最高，到当天时的收益进行对比，也就是max(max_profit, prices[i] - min_price)
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        length = len(prices)
        for i in range(1, length):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit