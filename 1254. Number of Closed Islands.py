# problem link-->> https://leetcode.com/problems/number-of-closed-islands/description/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False  # Touches boundary → Not closed
            if (r, c) in visited or grid[r][c] == 1:
                return True  # Already visited or water → Still possibly closed
            
            visited.add((r, c))  # Mark as visited
            
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            return up and down and left and right  # Island is closed only if all directions are closed

        closed_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if dfs(r, c):  
                        closed_islands += 1  

        return closed_islands
        
