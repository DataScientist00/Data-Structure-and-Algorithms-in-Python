#problem link-->> https://leetcode.com/problems/perfect-squares/description/



class Solution:
    def numSquares(self, n: int) -> int:
        memo = [n] * (n + 1)
        memo[0] = 0
        def dp(k):
            if memo[k] != n:
                return memo[k]
            min_count = float('inf')
            j = 1
            while j * j <= k:
                min_count = min(min_count, dp(k - j * j) + 1)
                j += 1
            memo[k] = min_count
            return memo[k]

        return dp(n)
