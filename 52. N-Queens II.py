#problems link-->> https://leetcode.com/problems/n-queens-ii/description/


class Solution:
    def totalNQueens(self, n: int) -> int:
        pos_diagonal ,neg_diagonal , cols = set() ,set() ,set()
        res = 0
        def dfs(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c in cols or (row - c) in pos_diagonal or (row + c) in neg_diagonal:
                    continue
                cols.add(c)
                pos_diagonal.add(row - c)
                neg_diagonal.add(row + c)
                dfs(row + 1)
                cols.remove(c)
                pos_diagonal.remove(row - c)
                neg_diagonal.remove(row + c)

        dfs(0)
        return res
