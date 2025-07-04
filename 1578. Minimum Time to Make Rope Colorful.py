# problem link-->> https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1,len(colors)):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l] 
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r

        return res
        
