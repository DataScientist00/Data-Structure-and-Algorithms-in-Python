# problem link-->> https://leetcode.com/problems/extra-characters-in-a-string/description/


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s) : 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 1 + dfs(i+1) #not including case
            for j in range(i , len(s)):
                if s[i:j+1] in words:
                    res = min(res , dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)
        
