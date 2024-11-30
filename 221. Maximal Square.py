#problem link-->> https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        cache = {}
        def helper(r , c):
            if r >= row or c >= col:
                return 0
            if (r,c) not in cache:
                down = helper(r , c+1)
                right = helper(r+1 , c)
                diagonal = helper(r+1 , c+1)
                cache[(r,c)] = 0
                if matrix[r][c] == '1':
                    cache[(r,c)] = 1 + min(right,diagonal , down)
            return cache[(r,c)]
        helper(0,0)
        return max(cache.values()) ** 2
            
        
