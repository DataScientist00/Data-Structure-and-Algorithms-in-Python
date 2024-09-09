#problem link-->> https://leetcode.com/problems/word-break/description/


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

        
