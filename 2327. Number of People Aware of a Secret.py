# problem link -->>  https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n+1)
        dp[1] = 1
        for day in range(2,n+1):
            people_know = 0
            for j in range(day-forget+1,day-delay+1):
                if j > 0:
                    people_know = (people_know + dp[j])%MOD
            dp[day] = people_know

            
        res = 0
        for i in range(n-forget+1,n+1):
            if i > 0:
                res = (res + dp[i]) % MOD
        return res

        
