# problem link -- >> https://leetcode.com/problems/maximum-substrings-with-distinct-start/description/

class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set()
        ans = 0
        for c in s:
            if c not in seen:
                ans += 1
                
            seen.add(c)
        return ans
