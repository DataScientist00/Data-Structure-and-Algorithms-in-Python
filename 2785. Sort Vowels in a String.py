
# problem link-->> https://leetcode.com/problems/sort-vowels-in-a-string/description/


class Solution:
    def sortVowels(self, s: str) -> str:
        asc = {
            'A','E','I', 'O', 'U','a','e','i','o','u',            
        }
        tt = ''
        for i in s:
            if i in asc:
                tt += i
        tt = sorted(tt)
        tt= ''.join(tt)
        ans = ''
        j = 0
        for i in range(len(s)):
            if s[i] in asc:
                ans += tt[j]
                j += 1
            else:
                ans += s[i]
        return ans     
        
