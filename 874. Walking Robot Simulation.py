# problem link -->> https://leetcode.com/problems/walking-robot-simulation/description/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y = 0,0
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        res = 0
        d = 0
        obs = {tuple(o) for o in obstacles}
        for c in commands:
            if c == -1:
                d = (d + 1)%4
            elif c == -2:
                d = (d - 1)%4
            else:
                dx , dy = dir[d]
                for i in range(c):
                    if (x + dx , y+dy) in obs:
                        break 
                    x , y = x + dx , y + dy
            res = max(res , x **2 + y ** 2)
        return res
        
