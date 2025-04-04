# problem link-->> https://leetcode.com/problems/number-of-enclaves/description/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0  # Mark visited
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Remove land connected to borders
        for r in range(rows):
            for c in [0, cols - 1]:
                if grid[r][c] == 1:
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows - 1]:
                if grid[r][c] == 1:
                    dfs(r, c)
        
        # Count remaining land cells
        return sum(grid[r][c] for r in range(rows) for c in range(cols))
        
