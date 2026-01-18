# problem link==>> https://leetcode.com/problems/number-complement/description/


class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)[2:]
        k = ''
        for i in a:
            if i == '0':
                k += '1'
            if i == '1':
                k += '0'
        return int(k,2)

        
