#problem link-->> https://leetcode.com/problems/decode-ways/description/

#-------------------recursive-----------------
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(i):
            if i >= len(s):
                return 1
            if i in memo:
                return memo[i]
            if s[i] == '0':
                return 0
            res = dp(i+1)
            if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                res += dp(i+2)
            memo[i] = res
            return memo[i]
        return dp(0)

#---------------------bottom-up--------------------

def numDecodings(self, s: str) -> int:
        dp = {}
        dp[len(s)] = 1
        for i in range(len(s)-1 , -1 , -1):
            if s[i] == '0':
                dp[i] =  0
            else:
                dp[i] = dp[i+1]
                if i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    dp[i] += dp[i+2]
        return dp[0]
        
