# problem link-->> https://leetcode.com/problems/reverse-vowels-of-a-string/description/?cong=true


class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        s = list(s)
        t = set("aeiouAEIOU")
        while l < r:
            while l < r and  s[l] not in t:
                l += 1
            while l < r and s[r] not in t:
                r -= 1
            s[l] ,s[r] = s[r] , s[l]
            l += 1
            r -= 1
        return ''.join(s)
        
