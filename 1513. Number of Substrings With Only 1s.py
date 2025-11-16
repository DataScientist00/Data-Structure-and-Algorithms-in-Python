# problem link-->> https://leetcode.com/problems/number-of-substrings-with-only-1s/description

class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        ans = 0
        for b in s:
            if b == '0':
                cnt = 0
            else:
                cnt += 1
                ans += cnt

        return ans % (10 ** 9 + 7)            
               
        
