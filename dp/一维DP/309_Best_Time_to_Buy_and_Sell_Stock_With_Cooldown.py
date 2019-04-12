'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions 
as you like (ie, buy one and sell one share of the stock multiple times) with the following 
restrictions:

You may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

思路：可以用 state machine 来想象三种状态的转移：
        1) Rest state: We could keep staying rest, or buy stock and moving to the "Buy" state
        2) Buy  state: We could keep staying "Buy" state, in other words, doing nothing in that day
                       ,or sell stock and moving to the "Sell" state
        3) Sell state: We must take a rest in that day and move to "Rest" state

initial state:
    buy[0] = -prices[0]
    sell[0] = -float('inf')
    rest[0] = 0

transition function:
    buy[i] = max(buy[i-1], rest[i - 1] - prices[i])
    sell[i] = buy[i - 1] + prices[i]
    rest[i] = max(rest[i - 1], sell[i - 1])

Result: max(rest[-1], sell[-1])
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy = -prices[0] # After buying the stock in the first day
        rest = 0 # Taking a rest in the fist day, have no profit
        sell = -float('inf')
        for price in prices[1:]:
            buy, sell, rest = max(buy, rest - price), buy + price, max(rest, sell)
        return max(sell, rest)