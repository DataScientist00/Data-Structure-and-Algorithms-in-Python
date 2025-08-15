# problem link-->> https://leetcode.com/problems/power-of-four/description/


import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        p = math.ceil(math.sqrt(n))
        for i in range(p):
            if 4 ** i == n:
                return True
            if 4 ** i > n:
                return False
        return False
