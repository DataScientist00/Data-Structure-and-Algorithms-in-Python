# problem link-->> https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        v = Counter()
        c = Counter()
        res1 = 0
        res2 = 0
        for ch in s:
            if ch in vowels:
                v[ch] += 1
                res1 = max(res1 , v[ch])
            else:
                c[ch] += 1
                res2 = max(res2 , c[ch])
        return res1 + res2

        
