# problem link-->> https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = n
        b = 0
        placevalue = 1
        while n > 1:
            step = 1
            if n%10 == 1:
                step = 2
            a = a - step*placevalue
            b = b + step*placevalue
            n = (n-step)//10

            placevalue *= 10
        return [a,b]
        

        
        
