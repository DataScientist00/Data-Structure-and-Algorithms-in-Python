#problem link-->>  https://leetcode.com/problems/coin-change/description/

#------------ recursion----------------
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        coins.sort()
        def dp(total):
            if total == 0 :
                return 0
            if total in memo:
                return memo[total]
            minn = float('inf')
            for c in coins:
                amt = total - c
                if amt < 0 :
                    break
                minn = min(minn , 1 + dp(total - c))
            memo[total] = minn
            return memo[total]

        a = dp(amount)
        if a < float('inf'):
            return a
        else:
            return -1
#------------bottom-up-------------------

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        coins.sort()
        for i in range(1,amount+1):
            minn = float('inf')
            for c in coins:
                diff = i - c
                if diff < 0:
                    break
                minn = min(minn , 1 + dp[diff])
            dp[i] = minn
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1


        

        
