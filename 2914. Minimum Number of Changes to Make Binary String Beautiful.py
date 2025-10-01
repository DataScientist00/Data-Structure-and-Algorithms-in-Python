# problem link-->> https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/description/


class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s):
            if s[i] == s[i+1]:
                i += 2
                continue
            ans += 1
            i += 2
        return ans


        
