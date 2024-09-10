#problem link-->> https://leetcode.com/problems/coin-change-ii/description/

#------------------recursion---------------------------
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i , total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i >= len(coins):
                return 0
            if (i,total) in memo:
                return memo[(i , total)]
            memo[(i,total)] = (dp(i , total + coins[i]) + dp(i+1 , total))
            return memo[(i , total)]
        return dp(0,0)
#------------------bottom-up------------------------------
dp = [0] * (amount + 1)
        dp[0] = 1  
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]
        
        return dp[amount]
