#problem link-->> https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and ((1 << 30) % n)== 0  #bitwise shift of largest possible number and then checking if mod is integer
        
