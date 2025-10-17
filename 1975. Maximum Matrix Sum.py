# problem link-->> https://leetcode.com/problems/maximum-matrix-sum/description/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        subtract_min = float('inf')
        total = 0
        odds = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                total += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    odds += 1
                subtract_min = min(subtract_min , abs(matrix[i][j]))

        if odds % 2 == 0:
            return total
        else:
            return total + (-2 * subtract_min) # Because we have added subtract_min while calculating total that's why -2 and not -1

        
