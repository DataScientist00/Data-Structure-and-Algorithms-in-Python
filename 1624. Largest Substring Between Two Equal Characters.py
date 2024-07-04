#problem link-->>>    https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mem = {}
        res = -1
        for i , c in enumerate(s):
            if c in mem:
                res = max(res, i- mem[c]-1)
            else:
                mem[c]=i
        return res

        
