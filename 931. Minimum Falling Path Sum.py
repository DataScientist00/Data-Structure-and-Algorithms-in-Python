# problem link-->> https://leetcode.com/problems/minimum-falling-path-sum/description/



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            for c in range(cols):
                top_left = matrix[r - 1][c - 1] if c - 1 >= 0 else float ('inf')
                top_above = matrix[r - 1][c]
                top_right = matrix[r - 1][c + 1] if c + 1 < cols else float('inf')

                matrix[r][c] = matrix[r][c] + min(top_left, top_above, top_right)
        return min(matrix[-1])

# ++++++++++++++ recursive +++++++++++++++++++++++++++
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         from typing import List

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         row = len(matrix)
#         col = len(matrix[0])
#         dp = {}

#         def dfs(r, c):
#             if c < 0 or c == col:
#                 return float('inf')
#             if r == row:
#                 return 0
#             if (r, c) in dp:
#                 return dp[(r, c)]

#             down_left = dfs(r + 1, c - 1)
#             down = dfs(r + 1, c)
#             down_right = dfs(r + 1, c + 1)

#             dp[(r, c)] = matrix[r][c] + min(down_left, down, down_right)
#             return dp[(r, c)]

#         ans = float('inf')
#         for a in range(col):
#             ans = min(ans, dfs(0, a))
#         return ans

        
