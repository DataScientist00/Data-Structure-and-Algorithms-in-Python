
# problem link-->> https://leetcode.com/problems/magic-squares-in-grid/description/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        check = set()

        for r in range(rows - 2):
            for c in range(cols - 2):
                if (
                    grid[r][c]   + grid[r][c+1]   + grid[r][c+2]
                    == grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
                    == grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
                    == grid[r][c]   + grid[r+1][c]   + grid[r+2][c]
                    == grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
                    == grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
                    == grid[r][c]   + grid[r+1][c+1] + grid[r+2][c+2]
                    == grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]
                ):
                    check.update([
                        grid[r][c], grid[r][c+1], grid[r][c+2],
                        grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                        grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
                    ])

                    print('outside', check)

                    if check == set(range(1, 10)):
                        count += 1
                        print(check)

                    check.clear()

        return count
