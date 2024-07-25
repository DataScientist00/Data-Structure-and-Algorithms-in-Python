#problem link--->> https://leetcode.com/problems/score-of-a-string/description/

class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            res +=(abs(ord(s[i])- abs(ord(s[i+1]))))
        return res


        
