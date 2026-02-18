# problem link -- >> https://leetcode.com/problems/binary-number-with-alternating-bits/description/



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = bin(n)
        last = 0
        for i in range(1,len(a)):
            if a[i-1] == a[i]:
                return False
        return True


        
