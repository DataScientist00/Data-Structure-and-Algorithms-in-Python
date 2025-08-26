# problem link-->> https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1 = len(grid)
        cols1 = len(grid[0])
        rows2 = 3 * rows1
        cols2 = 3 * cols1
        grid2 = [[0] * cols2 for _ in range(rows2)]

        for r in range(rows1):
            for c in range(cols1):
                r2 , c2 = r*3 , c*3
                if grid[r][c] == '/':
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == '\\':
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        
        def dfs(r ,c , visit):
            if 0 > r or r == rows2 or 0 > c or c == cols2 or (r,c) in visit or grid2[r][c] != 0:
                return
            directions = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]
            visit.add((r,c))
            for dr,dc in directions:
                dfs(dr , dc , visit)


        visit = set()
        ans = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r,c) not in visit:
                    dfs(r,c,visit)
                    ans += 1
        return ans



        
        
