#problem link-->> https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in memo:
                return memo[i]
            left = dp(i+1) 
            right = dp(i+2)
            memo[i] = left + right
            return memo[i]
        return dp(0)
        
