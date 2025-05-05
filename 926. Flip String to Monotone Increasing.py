# problem link-->>> https://leetcode.com/problems/flip-string-to-monotone-increasing/description/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        cont1 = 0
        for n in s:
            if n == '1':
                cont1 += 1
            else:
                res = min(res+1 , cont1)
        return res
        
