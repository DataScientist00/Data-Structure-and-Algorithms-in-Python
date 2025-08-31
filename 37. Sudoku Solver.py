# problem link-->> https://leetcode.com/problems/sudoku-solver/description/


from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Pre-fill sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)
                else:
                    empties.append((i, j))

        def backtrack(idx=0):
            if idx == len(empties):
                return True  # solved

            i, j = empties[idx]
            b = (i // 3) * 3 + (j // 3)

            for d in map(str, range(1, 10)):
                if d not in rows[i] and d not in cols[j] and d not in boxes[b]:
                    # place number
                    board[i][j] = d
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[b].add(d)

                    if backtrack(idx + 1):
                        return True

                    # undo (backtrack)
                    board[i][j] = '.'
                    rows[i].remove(d)
                    cols[j].remove(d)
                    boxes[b].remove(d)

            return False

        backtrack()
