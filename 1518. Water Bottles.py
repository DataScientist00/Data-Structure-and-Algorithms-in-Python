#problem link--->> https://leetcode.com/problems/water-bottles/description/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        res += numBottles
        leftover = 0
        while numBottles >= numExchange:
            leftover = floor(numBottles % numExchange)
            numBottles = floor(numBottles // numExchange)
            res += numBottles
            numBottles += leftover
        return res
        
