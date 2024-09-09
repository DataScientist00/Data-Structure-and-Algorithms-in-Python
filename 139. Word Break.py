#problem link-->> https://leetcode.com/problems/word-break/description/

#----------Recursion-----------------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if len(s) == i:
                return True
            for j in wordDict:               
                if s[i:i + len(j)] == j:
                    memo[i] = dp(i + len(j))
                    if memo[i]:
                        return True
            return False
        return dp(0)
#------------bottom-up---------------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1 , -1 ,-1):
            for c in wordDict:
                if i + len(c) <= len(s) and s[i:i+len(c)] == c:
                    dp[i] = dp[i+len(c)]
                    if dp[i]:
                        break
        return dp[0]
                        

        

        

        
