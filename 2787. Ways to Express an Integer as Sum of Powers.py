# problem link-->> https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/


from functools import lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        memo = {}
        def dp(remaining , i):
            if (remaining , i) in memo:
                return memo[(remaining , i)]

            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if i > n:
                return 0
            power = i ** x
            if power > remaining:
                return 0
            take = dp(remaining - power , i +1)
            skip = dp(remaining , i + 1)
            memo[(remaining , i)] = (take + skip) % MOD
            return memo[(remaining , i)]

        return dp(n , 1)
