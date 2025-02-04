#problem link-->> https://leetcode.com/problems/range-sum-query-2d-immutable/description/

class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.sumMatrix = []
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build the prefix sum matrix
        for r in range(rows):
            for c in range(cols):
                self.sumMatrix[r + 1][c + 1] = (matrix[r][c] 
                    + self.sumMatrix[r][c + 1] 
                    + self.sumMatrix[r + 1][c] 
                    - self.sumMatrix[r][c])

    def sumRegion(self, row1, col1, row2, col2):
        return (self.sumMatrix[row2 + 1][col2 + 1] 
                - self.sumMatrix[row1][col2 + 1] 
                - self.sumMatrix[row2 + 1][col1] 
                + self.sumMatrix[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
