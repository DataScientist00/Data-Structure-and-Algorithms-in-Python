#problem link-->> https://leetcode.com/problems/count-vowels-permutation/description/


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1,1,1,1,1]
        for _ in range(2,n+1):
            new_dp=[0] * 5
            new_dp[0] = (dp[1] + dp[2] + dp[4]) % MOD  
            new_dp[1] = (dp[0] + dp[2]) % MOD          
            new_dp[2] = (dp[1] + dp[3]) % MOD          
            new_dp[3] = dp[2] % MOD                    
            new_dp[4] = (dp[2] + dp[3]) % MOD
            dp = new_dp
        return sum(dp) % MOD   
        
