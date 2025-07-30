# problem link-->> https://leetcode.com/problems/sum-of-square-numbers/description/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            result = left * left + right * right
            if result < c:
                left += 1

            elif result > c:
                right -= 1

            else:
                return True
        return False
        
