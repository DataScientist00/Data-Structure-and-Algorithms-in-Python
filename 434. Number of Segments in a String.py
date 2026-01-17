# problem link-->> https://leetcode.com/problems/number-of-segments-in-a-string/description/?cong=true


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        
