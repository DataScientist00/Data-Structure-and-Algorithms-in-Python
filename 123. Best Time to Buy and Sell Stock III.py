# problem link -->> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,allowed_to_buy,t):
            if i >= len(prices):
                return 0
            if t >= 3:
                return 0
            key = (i,allowed_to_buy,t)
            if key in memo:
                return memo[key]
            if allowed_to_buy:
                buy = -prices[i]+dp(i+1 , False ,t+1)
                dont_buy = dp(i+1 , True , t)
                profit = max(buy , dont_buy)
            else:
                sell = prices[i]+dp(i+1 , True , t)
                dont_sell = dp(i+1 , False , t)
                profit = max(sell , dont_sell)
            memo[key] = profit
            return memo[key]

        return dp(0,True,0)
        
