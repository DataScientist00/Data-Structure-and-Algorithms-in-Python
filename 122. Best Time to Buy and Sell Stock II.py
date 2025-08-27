# problem link-->> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,flag):
            if i >= len(prices):
                return 0
            key = (i,flag)
            if key in memo:
                return memo[key]
            profit = 0
            buy = dont_buy = sell = hold = 0
            if flag:
                buy = - prices[i] + dp(i+1, not flag)
                dont_buy = dp(i+1 , flag)
                profit = max(buy, dont_buy)
            else:
                sell = prices[i] + dp(i+1 ,not flag)
                hold = dp(i+1 ,flag)
                profit = max(sell , hold)
            memo[key] = profit
            return memo[key]
        return dp(0,1)



        
        
