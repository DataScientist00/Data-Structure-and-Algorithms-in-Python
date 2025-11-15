# problem link-->> https://leetcode.com/problems/first-completely-painted-row-or-column/description/


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows , cols = len(mat) , len(mat[0])
        num_to_idx = {}
        for r in range(rows):
            for c in range(cols):
                num_to_idx[mat[r][c]] = (r,c)

        rows_check = [0] * rows
        cols_check = [0] * cols
        for i,n in enumerate(arr):
            r , c = num_to_idx[n]
            rows_check[r] += 1
            cols_check[c] += 1

            if rows_check[r] == cols or cols_check[c] == rows:
                return i
