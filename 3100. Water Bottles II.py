# problem link-->> https://leetcode.com/problems/water-bottles-ii/description/

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            ans += 1
            numBottles += 1
            numExchange += 1
        return ans
        
