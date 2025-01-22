#problem link-->> https://leetcode.com/problems/grid-game/description/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        prerow1 , prerow2 = grid[0].copy() , grid[1].copy()
        for i in range(1,N):
            prerow1[i] += prerow1[i-1]
            prerow2[i] += prerow2[i-1]
        res = float('inf')
        for i in range(N):
            top = prerow1[-1] - prerow1[i]
            bottom = prerow2[i-1] if i > 0 else 0
            secondrobot = max(top , bottom)
            res = min(res , secondrobot)
        return res
