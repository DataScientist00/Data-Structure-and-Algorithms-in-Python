#  problem link -->> https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        def top(mat , i ,j , dp):
            if i < 0 or j < 0 or i >=n or j >= n:
                return float('-inf')
            if j < n // 2:
                return float('-inf')
            if i == n-1 and j == n-1:
                return mat[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            down = mat[i][j] + top(mat , i+1 , j , dp)
            left = mat[i][j] + top(mat , i+1 , j-1 , dp)
            right = mat[i][j] + top(mat , i+1 , j+1 , dp)
            dp[i][j] = max(down , left , right)
            return dp[i][j]

        def bottom(mat , i , j , dp):
            if i < 0 or j < 0 or i >=n or j >= n:
                return float('-inf')
            if i < n // 2:
                return float('-inf')
            if i == n-1 and j == n-1:
                return mat[i][j]
            if dp[i][j] != -1:
                return dp[i][j]

            down = mat[i][j] + bottom(mat , i+1 , j+1 , dp)
            left = mat[i][j] + bottom(mat , i-1 , j+1 , dp)
            right = mat[i][j] + bottom(mat , i , j+1 , dp)
            dp[i][j] = max(down , left , right)
            return dp[i][j]

        diag = 0
        for i in range(n):
            diag += fruits[i][i]
            fruits[i][i] = 0
        dp = []
        for i in range(n+1):
            dp.append([-1]*(n+1))
        x = top(fruits , 0 , n-1 ,dp)

        dp = []
        for i in range(n+1):
            dp.append([-1]*(n+1))
        y = bottom(fruits ,n-1 , 0 , dp)
        return diag + x + y
        
