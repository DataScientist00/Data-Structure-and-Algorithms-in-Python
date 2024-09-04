#problem link-->> https://leetcode.com/problems/n-queens/description/


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        pos_diagonal ,neg_diagonal , cols = set() ,set() ,set()
        res = []
        def dfs(row):
            if row == n:
                temp = [''.join(board[i]) for i in range(n)]
                res.append(temp)
            for c in range(n):
                if c in cols or (row - c) in pos_diagonal or (row + c) in neg_diagonal:
                    continue
                cols.add(c)
                pos_diagonal.add(row - c)
                neg_diagonal.add(row + c)
                board[row][c] = 'Q'
                dfs(row + 1)
                cols.remove(c)
                pos_diagonal.remove(row - c)
                neg_diagonal.remove(row + c)
                board[row][c] = '.'

        dfs(0)
        return res

        

    

        




        
