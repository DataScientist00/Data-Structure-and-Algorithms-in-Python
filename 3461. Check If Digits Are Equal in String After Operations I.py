# problem link-->> https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        temp = []
        i = 0
        while len(s) > 2:
            temp.append(str((int(s[i]) +  int(s[i+1])) % 10))
            i += 1
            if i == len(s)-1:
                s = ''.join(temp)
                temp = []
                i = 0
        return s[0] == s[1]
            
        
