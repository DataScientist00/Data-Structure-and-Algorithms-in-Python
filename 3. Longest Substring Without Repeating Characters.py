#problem link--->>> https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res , lp = 0 , 0
        history = set()
        for rp  in range(len(s)):
            while s[rp] in history:
                history.remove(s[lp])
                lp += 1
            history.add(s[rp])
            res = max(res , rp-lp+1)
        return res

                


        
