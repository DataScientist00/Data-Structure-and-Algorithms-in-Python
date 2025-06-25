# problem link-->> https://leetcode.com/problems/out-of-boundary-paths/description/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        dp = {}
        def dfs(i ,j , movesleft):
            if i < 0 or i == m or j <0 or j == n: return 1
            if movesleft == 0: return 0
            if (i , j , movesleft) in dp:
                return dp[(i , j , movesleft)]
            ans = 0
            for a , b in moves:
                ans = (ans + dfs(i + a , j + b , movesleft - 1)) % (10**9+7)
            dp[(i , j , movesleft)] = ans
                
            return ans
        return dfs(startRow , startColumn , maxMove)

        
