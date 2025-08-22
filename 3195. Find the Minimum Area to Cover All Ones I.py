# problem link-->> https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minna , minnb = float('inf') , float('inf')
        maxxa , maxxb = float('-inf') , float('-inf')
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    minna = min(minna , r)
                    maxxa = max(maxxa , r)
                    minnb = min(minnb , c)
                    maxxb = max(maxxb , c)

        return ((maxxa - minna) + 1) * ((maxxb - minnb) + 1)


        
