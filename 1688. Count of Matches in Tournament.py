#problem link--->>> https://leetcode.com/problems/count-of-matches-in-tournament/description/


class Solution:
    def numberOfMatches(self, n: int) -> int:
        res =  0
        while n > 1:
            res = res + n // 2
            n = math.ceil(n/2)
        return res
                

        
