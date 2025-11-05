# problem link-->> https://leetcode.com/problems/construct-k-palindrome-strings/description/


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        odd = 0
        count = Counter(s)
        for c , f in count.items():
            if f % 2 == 1:
                odd += 1

        return True if odd <= k else False
        
