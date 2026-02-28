# problem link -- >> http://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        temp = ''
        for i in range(1,n+1):
            temp += bin(i)[2:]
        ans = int(temp , 2) % ((10 **9) + 7)
        return ans
        
