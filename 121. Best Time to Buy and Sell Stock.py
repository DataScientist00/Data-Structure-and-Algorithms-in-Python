#problem link-->> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        profit , p = 0 , 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                profit = max(profit , p)
            else:
                l = r
            r += 1
        return profit


        
