# problem link -- >> https://leetcode.com/problems/count-servers-that-communicate/description/


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        prerow = [0] * len(grid)
        precol = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    prerow[i] += 1
                    precol[j] += 1

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if prerow[i] >= 2 or precol[j] >= 2:
                        ans += 1
        return ans

                    
        
