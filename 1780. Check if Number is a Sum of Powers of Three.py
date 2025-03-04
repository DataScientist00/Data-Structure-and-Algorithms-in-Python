#problem link-->> https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i , summ):
            if summ == n:
                return True
            if (3 ** i) > n or summ > n:
                return False
            if backtrack(i+1 , summ + 3 ** i):
                return True
            return backtrack(i+1 , summ)

        return backtrack(0,0)
        
