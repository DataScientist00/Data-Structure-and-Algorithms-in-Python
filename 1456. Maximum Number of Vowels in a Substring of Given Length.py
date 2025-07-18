# problem link-->> https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = { 'a' , 'e' , 'i' ,'o' , 'u'}
        res , cnt , l = 0,0,0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r-l + 1 > k:
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res , cnt)
        return res
        
