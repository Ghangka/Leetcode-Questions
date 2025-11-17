# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 

# Runtime: O(n)
# Space: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]

        for price in prices:
            if price < min:
                min = price
            else:
                profit = max(profit, price - min)

        return profit