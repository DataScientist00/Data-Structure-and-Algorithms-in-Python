# problem link -- >> https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            rb = n & 1
            ans = ans << 1
            ans = ans | rb
            n = n >> 1
        return ans
        
