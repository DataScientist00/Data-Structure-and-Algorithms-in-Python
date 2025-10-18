
# problem link-->> https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = set()
        check_walls = set()
        check_guards = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r ,c , idx):
            if 0 <= r < m and 0 <= c < n and (r,c) not in check_walls and (r,c) not in check_guards:
                cells.add((r,c))
                new_r = r + directions[idx][0]
                new_c = c + directions[idx][1]
                dfs(new_r , new_c , idx)
            else:
                return

        for r ,c in walls:
            check_walls.add((r,c))
        for r,c in guards:
            check_guards.add((r,c))

        for r ,c in guards:
            dfs(r+1,c,0)
            dfs(r,c+1,1)
            dfs(r-1,c,2)
            dfs(r,c-1,3)

        return (m*n) - (len(cells) + len(guards) + len(walls))



        
