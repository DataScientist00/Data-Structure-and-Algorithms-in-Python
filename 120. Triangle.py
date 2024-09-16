#problem link-->> https://leetcode.com/problems/triangle/description/

#---------------------Recursion--------------------------
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(i,j,t):
            if t >= len(triangle):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = min((dp(i+1,j ,t+1) + triangle[i][j]) , (dp(i+1 , j+1,t+1)+ triangle[i][j]))
            return memo[(i,j)]
        return dp(0,0,0)
#---------------------Bottom-up Tabulation---------------------------
def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle)+1)
        for row in triangle[::-1]:
            for i , n in enumerate(row):
                dp[i] = n + min(dp[i] , dp[i+1])
        return dp[0]
        
