# problem link-->>> https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = {}
        def solve(i,j):
            if j-i+1 < 3:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            ans = float('inf')
            for m in range(i+1 , j):
                temp = values[i] * values[m] * values[j]
                ans = min(ans , solve(i , m) + temp + solve(m,j))
            dp[(i,j)] = ans
            return dp[(i,j)]
        return solve(0, len(values)-1)


        
