#   Question: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
#       Tags: Array, Dynamic Programming
'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction(ie, buy one and sell one share of the stock), design
an algorithm to find the maximum profit.

eg1.
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

eg2.
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        lowest = prices[0]
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                if price - lowest > max_profit:
                    max_profit = price - lowest
        return max_profit

s = Solution()
print(s.maxProfit([7, 6, 4, 3, 1]))

