#problem link->> https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/


class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        return int(s[0] + s[2]) + int(s[1] + s[3])
        
