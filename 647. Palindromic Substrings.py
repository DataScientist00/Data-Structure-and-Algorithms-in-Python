#problem link-->> https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.ispali(s , i , i) #for odd size substring
            res += self.ispali(s , i , i+1) #for even size substring
        return res
    def ispali(self ,s, l , r):
        count = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
            
        
