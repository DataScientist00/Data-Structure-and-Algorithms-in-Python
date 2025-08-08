# problem link-->> https://leetcode.com/problems/soup-servings/description/

class Solution:
    def soupServings(self, n: int) -> float:
        memo = {}
        prob = 0
        def dp(a  , b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            if (a,b) in memo:
                return memo[(a,b)]
            nonlocal prob
            prob = 0.25*(dp(a-4 , b-0) + dp(a-3 , b-1) + dp(a-2 , b-2) + dp(a-1 , b-3))
            memo[(a,b)] = prob
            return memo[(a,b)]
        if n > 5000:
            return 1.0
        n = ceil(n / 25)
        return dp(n,n)
        
