#problem link-->> https://leetcode.com/problems/count-sub-islands/description/


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row , col = len(grid1) , len(grid1[0])
        visit = set()

        def dfs(r,c):
            if (r < 0 or c < 0 or r == row or c== col or grid2[r][c] == 0 or
             (r,c) in visit):
                return True
            
            visit.add((r,c))
            res = True
            if grid1[r][c] == 0:
                res = False

            res = dfs(r-1 ,c) and res
            res = dfs(r+1 ,c) and res
            res = dfs(r ,c-1) and res
            res = dfs(r ,c+1) and res
            return res
        
        count = 0
        for r in range(row):
            for c in range(col):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    count += 1
        return count

