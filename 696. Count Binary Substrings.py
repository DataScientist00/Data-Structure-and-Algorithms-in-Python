# problem link -- >> https://leetcode.com/problems/count-binary-substrings/description/


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 1
        prev= 0
        ans = 0
        curr = 1
        while i < len(s):
            if s[i-1] == s[i]:
                curr += 1
            else:
                ans += min(prev , curr)
                prev = curr
                curr = 1
            i += 1
        ans += min(prev , curr)
        return ans
            
        
