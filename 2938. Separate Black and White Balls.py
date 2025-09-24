# problem link-->> https://leetcode.com/problems/separate-black-and-white-balls/description/

class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        ans = 0
        for i,n in enumerate(s):
            if n == '0':
                ans += (i-l)
                l += 1
        return ans
        
