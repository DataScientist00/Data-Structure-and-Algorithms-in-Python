#problem link--->> https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0:
            if (high-low)%2 == 0:
                return int(floor(((high-low)+1)/2)+1)
            else:
                return int(((high-low)+1)/2)
        else:
            return int(ceil((high-low)/2))


        
