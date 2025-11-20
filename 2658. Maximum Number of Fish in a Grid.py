# problem link-->> https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def dfs(r , c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] and (r,c) not in visited:
                visited.add((r,c))
                temp = (grid[r][c] + dfs(r+1 , c)
                +dfs(r , c+1)
                +dfs(r-1,c)
                +dfs(r,c-1))
                return temp
            else:
                return 0
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res = max(res , dfs(i , j))
        return res
        
