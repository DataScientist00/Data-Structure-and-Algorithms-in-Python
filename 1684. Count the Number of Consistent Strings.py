# problem link-->> https://leetcode.com/problems/count-the-number-of-consistent-strings/description/


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bitmask = 0
        for c in allowed:
            bit = 1 << ord(c) - ord('a')
            bitmask = bitmask | bit

        res = len(words)
        for w in words:
            for c in w:
                bit = 1 << ord(c) - ord('a')
                if bit & bitmask == 0:
                    res -= 1
                    break
        return res

        
