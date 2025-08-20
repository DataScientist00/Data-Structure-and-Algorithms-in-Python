# problem link-->> https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        row ,col = len(matrix) , len(matrix[0])
        for r in range(row):
            res += matrix[r][0]
        for c in range(1,col):
            res += matrix[0][c]

        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c] == 1:
                    matrix[r][c] = 1 + min(matrix[r-1][c] , matrix[r][c-1], matrix[r-1][c-1])
                    res += matrix[r][c]
        return res


        
