# problem link-->> https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        def counts(n , target):
            if n ==0:
                return 1 if target == 0 else 0
            if (n , target) in dp:
                return dp[(n , target)]
            
            res = 0
            for i in range( 1 , k + 1):
                res = (res + counts(n - 1 , target - i)) % MOD
            dp[(n , target)] = res
            return res

        return counts(n , target)

        
