# problem link-->> https://leetcode.com/problems/minimum-length-of-string-after-operations/description/


class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for ch , cnt in count.items():
            if cnt % 2 == 0:
                res += 2
            else:
                res += 1
        return res
        
