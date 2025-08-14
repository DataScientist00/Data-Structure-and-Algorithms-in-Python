# problem link-->> https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows , cols = len(rowSum) , len(colSum)
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            res[r][0] = rowSum[r]

        for c in range(cols):
            cur_col_sum = 0
            for r in range(rows):
                cur_col_sum += res[r][c]

            r = 0
            while cur_col_sum > colSum[c]:
                diff = cur_col_sum - colSum[c]
                to_remove = min(diff , res[r][c])
                res[r][c] -= to_remove
                res[r][c+1] += to_remove
                cur_col_sum -= to_remove
                r += 1
        return res
        
