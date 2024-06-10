#problem link-->> https://leetcode.com/problems/matrix-diagonal-sum/description/


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
        for i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat)-1-i]
        return sum - ( mat[n//2][n//2]  if n%2 else 0 )
        
        
